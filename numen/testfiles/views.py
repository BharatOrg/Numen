from flask import render_template, request, abort, Response, redirect, g, session, jsonify, make_response
from functools import wraps
from werkzeug import secure_filename
from webapp import helpers
from webapp.helpers import *
import urllib
import time
import base64
import hashlib
import httplib
import re
from dateutil.relativedelta import relativedelta, SU
try: import simplejson as json
except ImportError: import json
import locale
import yaml
import os
import random
import datetime
from datetime import date, timedelta
import calendar
import pymssql
import sys, traceback
import pylibmc
import operator
import shutil
from StringIO import StringIO
import PIL
from PIL import Image
import string
from requests_ntlm import HttpNtlmAuth
import ldap

import tempfile

from webapp import app
from webapp.models import *

import xlrd

import requests

import pika
from gg_restclient import RestClient, GGException
from gg_dao import *
from gg_dao.legacy import LegacyOrder, LegacyInvoice, LegacyPurchaseOrder
from gg_utils import *

from passlib.apps import custom_app_context as pwd_context

import pdb
import dashboard

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
default_header = {'Content-Type':'application/json'}

rest_client = RestClient()

def check_browser():
    browser = request.user_agent.browser
    version = int(request.user_agent.version.split('.')[0])

    if browser and version:
        if (browser == 'msie' and version < 10):
            return True

def sort_user_list(l, r):
    v = cmp(l['user'].last_name, r['user'].last_name)
    if v != 0:
        return v
    return cmp(l['user'].first_name, r['user'].first_name)

# Custom Filters for html templates
def ssrs_url(params_dict, path):
    if not params_dict:
        return app.config['ssrs.base_url'].format(report_name=path)
    base_url = app.config['ssrs.param_url']

    url_params = urllib.urlencode([
                                   (key, x) for key, xs in params_dict.items()
                                   for x in ([xs] if isinstance(xs, str) or isinstance(xs, unicode) else xs)
                                   ])

    report_url = base_url.format(report_name=path, params=(url_params))

    return report_url

# Convert search service results to datatables arrays
def to_datatables(data):
    datatables = {"data" : []}
    for item in data['results']:
        # Merge flags and statuses for display
        display_statuses = item['flags']
        display_statuses.insert(0, item['status'])

        datatables["data"].append([item['id'],
                                    item['client'],
                                    display_statuses,
                                    item['sales_rep'],
                                    item['create_date'],
                                    item['type'],
                                    item['inhands'],
                                    item['purchase_orders']])
    return datatables;
# Environment filter names for filter functions
app.jinja_env.filters['ssrs_url'] = ssrs_url
app.jinja_env.filters['return_tracking_url'] = return_tracking_url
app.jinja_env.filters['prettify_currency'] = prettify_currency
app.jinja_env.filters['prettify_shipping'] = prettify_shipping
app.jinja_env.filters['prettify_date'] = prettify_date
app.jinja_env.filters['prettify_datehuman'] = prettify_datehuman
app.jinja_env.filters['prettify_dateweekhuman'] = prettify_dateweekhuman
app.jinja_env.filters['prettify_datetime'] = prettify_datetime
app.jinja_env.filters['prettify_phone'] = prettify_phone
app.jinja_env.filters['prettify_type'] = prettify_type
app.jinja_env.filters['prettify_status'] = prettify_status



@app.before_request
def validate_user():
    if request.path.startswith('/public') or request.path.startswith('/login'):
        return
    g.user = None

    if 'user' not in session:
        return

    try:
        g.user = User.objects.filter(User.id == session['user']).one()
        permissions = rest_client.get_permissions(session['user'], 'list')['permissions']
        g.permissions = Permissions(permissions)

    except Exception as e:
        traceback.print_exc()
        g.user = None

    if g.user != None:
        NumenAudit.record(g.user, request)

if app.config['MAINTENANCE']:
    @app.route('/')
    @app.route('/<path:path>')
    def maintenance(path=''):
        return render_template('maintenance.html')

else:
    @app.route('/')
    def index():
        return redirect(url_for('dashboard'))

    @login_required
    @app.route('/ReportServer/<path:ssrs_path>', methods=['GET','POST'])
    def ssrs_proxy(ssrs_path):

        print request.url
        url = app.config['ssrs_endpoint']+'ReportServer'.join(request.url.split('ReportServer')[1:])

        resp = None

        if request.method == 'GET':
            resp = requests.get(url,
                                auth = HttpNtlmAuth(app.config['ssrs_user'],
                                                    app.config['ssrs_pass']),
                                headers = request.headers)
        elif request.method == 'POST':
            resp = requests.post(url,
                                 data = request.form,
                                 auth = HttpNtlmAuth(app.config['ssrs_user'],
                                                     app.config['ssrs_pass']),
                                 headers = request.headers)

        svc_resp = make_response(resp.content)

        svc_resp.headers['content-type'] = resp.headers['content-type']

        print url
        print resp.headers['content-type']

        return svc_resp

    @app.route('/dashboard')
    @login_required
    def dashboard():

        # widget visibility/permission defaults
        divisions = g.user.divisions
        widget_permissions = []

        if g.permissions.have_permission('access_executive'):
            divisions = app.config['divisions']
            widget_permissions.append('access_executive')

        if g.permissions.have_permission('access_widget_sales'):
            widget_permissions.append('access_widget_sales')
        
        if g.permissions.have_permission('access_widget_fulfillment'):
            widget_permissions.append('access_widget_fulfillment')
        

        return render_template('index.html', divisions = json.dumps(divisions), widget_permissions = json.dumps(widget_permissions))


    @app.route('/admin/permissions')
    @login_required
    @requires_permission('access_admin')
    def permissions():
        users = list(User.objects)
        groups = rest_client.get_groups()['groups']
        return render_template('permissions.html', users = users, groups = groups)

    @app.route('/permissions', methods=['GET'])
    @login_required
    def get_all_permissions():
        permissions = rest_client.get_permissions()
        return jsonify(permissions)

    @app.route('/permissions/user/<user_id>', methods=['GET'])
    @login_required
    def get_permissions(user_id):
        user_permissions = rest_client.get_permissions(user_id)
        return jsonify(user_permissions)

    @app.route('/permissions/groups', methods=['GET', 'POST'])
    @login_required
    def get_create_groups():
        if request.method == 'GET':
            groups = rest_client.get_groups()
            return jsonify(groups)
        elif request.method == 'POST':
            resp = rest_client.create_group(json.dumps(request.json))
            return jsonify({'group' : resp})

    @app.route('/permissions/groups/<group_id>', methods=['GET', 'POST', 'DELETE'])
    @login_required
    def get_set_delete_group(group_id):
        if request.method == 'GET':
            group = rest_client.get_groups(group_id)
            return jsonify(group)
        elif request.method == 'POST':
            resp = rest_client.update_group(group_id, json.dumps(request.json))
            return jsonify(resp)
        elif request.method == 'DELETE':
            resp = rest_client.delete_group(group_id)
            return jsonify({'group' : resp})

    @app.route('/permissions/groups/user/<user_id>', methods=['GET', 'POST'])
    @login_required
    def get_set_groups(user_id):
        if request.method == 'GET':
            resp = rest_client.get_groups_for_user(user_id)
            return jsonify(resp)
        elif request.method == 'POST':
            resp = rest_client.update_groups_for_user(user_id, json.dumps(request.json))
            return jsonify(resp)

    @app.route('/admin/spoof_user/<user_id>', methods=['GET', 'POST'])
    @login_required
    @requires_permission('access_admin')
    def spoof_user(user_id):
        session['user'] = user_id
        return redirect(url_for('dashboard', error_msg='You are impersonating '+ session['user'] +'.'))

    @app.route('/shopify/set_fulfillment/<store_id>', methods=['GET'])
    @requires_permission('access_admin')
    @login_required
    def set_fulfillment(store_id):
        resp = rest_client.shopify_set_fulfillment(store_id)
        matched_skus = resp['matched_skus']
        unmatched_skus = resp['unmatched_skus']
        store = ShopifyStore.objects.filter(ShopifyStore.id==store_id).one()
        print jsonify(resp)
        return render_template('shopify_fulfillment_report.html', unmatched_skus=unmatched_skus, matched_skus=matched_skus, store=store)

    @app.route('/admin/shopify_admin')
    @requires_permission('access_admin')
    @login_required
    def shopify_admin():
        stores = ShopifyStore.objects

        return render_template('shopify_admin.html', stores=stores)

    @app.route('/admin/edit/shopify/<store_id>', methods=['GET','POST'])
    @requires_permission('access_admin')
    @login_required
    def edit_shopify_store(store_id):
        if request.method == 'GET':
            store = ShopifyStore.objects.filter(ShopifyStore.id==store_id).one()

            if not store:
                abort(404)

            return render_template('edit_shopify_store.html', store=store)

        if request.method == 'POST':

            store = ShopifyStore.objects.filter(ShopifyStore.id==store_id).one()

            store.client_id = request.form['client_id']

            if request.form['auto_set_fulfillment'] == 'True':
                store.auto_set_fulfillment = True
            else:
                store.auto_set_fulfillment = False

            if request.form['track_inventory'] == 'True':
                store.track_inventory = True
            else:
                store.track_inventory = False

            store.save()

            return redirect(url_for('shopify_admin'))

    @app.route('/admin/delete/shopify/<store_id>', methods=['GET'])
    @requires_permission('access_admin')
    @login_required
    def delete_shopify_store(store_id):
        store = ShopifyStore.objects.filter(ShopifyStore.id==store_id).one()
        if not store:
            return 404
        store.client_id = None
        store.save()
        return redirect(url_for('shopify_admin', success_msg='Client ID removed successfully'))

    @app.route('/admin/college_admin')
    @login_required
    @requires_permission('access_admin')
    def college_admin():
        stores = CollegeShirtStore.objects
        return render_template('college_admin.html', stores=stores)

    @app.route('/admin/edit/<store_id>', methods=['GET','POST'])
    @app.route('/admin/edit/', defaults={"store_id": None}, methods=['POST'])
    @login_required
    @requires_permission('access_admin')
    def edit_store(store_id):
        if request.method == 'GET':
            store = CollegeShirtStore.objects.filter(CollegeShirtStore.id==store_id).one()
            if not store:
                abort(404)
            return render_template('edit_store.html', store=store, contact=store.contact)
        else:
            if not store_id:
                #create a new store from post data
                store = CollegeShirtStore(
                    college=request.form['college'],
                    project=request.form['project'],
                    project_code=request.form['project_code'],
                    google_code=request.form['google_code'],
                    title=request.form['title'],
                    desc=request.form['desc'],
                    price=float(request.form['price']),
                    frats=request.form['frats'].split(',')
                    )
                store.contact = CollegeShirtContact(
                    name_line1=request.form['contact.name_line1'],
                    name_line2=request.form['contact.name_line2'],
                    addr_line1=request.form['contact.addr_line1'],
                    addr_line2=request.form['contact.addr_line2'],
                    city=request.form['contact.city'],
                    state=request.form['contact.state'],
                    zip=request.form['contact.zip']
                    )

                store.close_date = datetime.datetime.strptime(request.form['close_date'],
                                                              '%Y-%m-%d %H:%M')
                store.images.append(base64.b64encode(request.files['image'].read()))
                
                store.soc_rep=request.form['soc_rep']
                store.soc_email=request.form['soc_email']
                store.save()

            else:
                store = CollegeShirtStore.objects.filter(CollegeShirtStore.id==store_id).one()
                store.project_code=request.form['project_code']
                store.google_code=request.form['google_code']
                store.title=request.form['title']
                store.desc=request.form['desc']
                store.price=float(request.form['price'])
                store.frats=request.form['frats'].split(',')
                store.contact.name_line1=request.form['contact.name_line1']
                store.contact.name_line2=request.form['contact.name_line2']
                store.contact.addr_line1=request.form['contact.addr_line1']
                store.contact.addr_line2=request.form['contact.addr_line2']
                store.contact.city=request.form['contact.city']
                store.contact.state=request.form['contact.state']
                store.contact.zip=request.form['contact.zip']
                store.soc_rep=request.form['soc_rep']
                store.soc_email=request.form['soc_email']
                store.close_date = datetime.datetime.strptime(request.form['close_date'],
                                                              '%Y-%m-%d %H:%M')
                if 'image' in request.files and request.files['image'].filename:
                    store.images.append(base64.b64encode(request.files['image'].read()))
                print request.files
                store.save()

            return redirect(url_for('college_admin'))


    @app.route('/admin/add_image/<store_id>', methods=['POST'])
    @login_required
    @requires_permission('access_admin')
    def add_store_image(store_id):

        store = CollegeShirtStore.objects.filter(CollegeShirtStore.id==store_id).one()
        store.project_code=request.form['project_code']
        store.google_code=request.form['google_code']
        store.title=request.form['title']
        store.desc=request.form['desc']
        store.price=float(request.form['price'])
        store.frats=request.form['frats'].split(',')
        store.contact.name_line1=request.form['contact.name_line1']
        store.contact.name_line2=request.form['contact.name_line2']
        store.contact.addr_line1=request.form['contact.addr_line1']
        store.contact.addr_line2=request.form['contact.addr_line2']
        store.contact.city=request.form['contact.city']
        store.contact.state=request.form['contact.state']
        store.contact.zip=request.form['contact.zip']
        store.soc_rep=request.form['soc_rep']
        store.soc_email=request.form['soc_email']
        store.close_date = datetime.datetime.strptime(request.form['close_date'],
                                                      '%Y-%m-%d %H:%M')
        if 'image' in request.files and request.files['image'].filename:
            store.images.append(base64.b64encode(request.files['image'].read()))
        store.save()
        return jsonify({'images': store.images})

    @app.route('/admin/new_store')
    @login_required
    @requires_permission('access_admin')
    def new_store():
        return render_template('edit_store.html', store=None, contact=None)

    @app.route('/admin/delete_store/<store_id>', methods=['GET'])
    @login_required
    @requires_permission('access_admin')
    def delete_store(store_id):
        store = CollegeShirtStore.objects.filter(CollegeShirtStore.id==store_id).one()
        if not store:
            return 404
        store.archived = True
        store.save()
        return redirect(url_for('college_admin', success_msg='Store deleted successfully'))

    @app.route('/admin/delete_image/<store_id>/<int:image>', methods=['GET'])
    @login_required
    @requires_permission('access_admin')
    def delete_image(store_id, image):
        store = CollegeShirtStore.objects.filter(CollegeShirtStore.id==store_id).one()
        if not store:
            return 404

        pos = image - 1
        del store.images[pos]
        store.save()
        return redirect(url_for('edit_store', store_id=store_id))

    @app.route('/report_data', methods=['POST'])
    @login_required
    def report_data():
        try:
            print "The /report_data endpoint has been called."
            report_name = request.form['report_name']
            print report_name
            params = {}
            for key, value in request.form.items():
               params[key] = value


            if 'from_date' in request.form:
                params["from_date"] = datetime.datetime.strptime(request.form["from_date"], '%m/%d/%Y').strftime('%Y-%m-%d')
            if 'to_date' in request.form:
                params["to_date"] = datetime.datetime.strptime(request.form["to_date"], '%m/%d/%Y').strftime('%Y-%m-%d')

            if 'sales_codes' in request.form:
                params['sales_codes'] = request.form.getlist('sales_codes')

            report_data = rest_client.exec_report(json.dumps(params), report_name, 'json')

            print "The full report data hase been collected."
            json_data = json.loads(report_data["payload"])

            headers = json_data["headers"]
            columns = [{"title": hval} for hval in headers]

            json_data["report_name"] = report_data["report_name"]
            json_data["columns"] = columns
            json_data["params"] = report_data["params"]
            print "The payload and other data have been collected!"

            return jsonify(json_data)
        except:
            traceback.print_exc()
            return jsonify({"error_message":"The Report has failed. Please try again."}), 500


    @app.errorhandler(500)
    def serverError(error):
        header = 'Something Broke '
        icon = 'fa-bomb'
        mssg = 'Our server experienced a problem.'
        return render_template('error_template.html', header=header, icon=icon, mssg=mssg), 500

    @app.errorhandler(404)
    def pageNotFound(error):
        header = 'Oops, Bad Link '
        icon = 'fa-chain-broken'
        mssg = "Sorry, that page can't be found."
        return render_template('error_template.html', header=header, icon=icon, mssg=mssg), 404

    @app.errorhandler(403)
    def pageNotFound(error):
        header = 'Forbidden '
        icon = 'fa-exclamation-triangle'
        mssg = "You don't have the permission to access this page."
        return render_template('error_template.html', header=header, icon=icon, mssg=mssg), 403


    @app.route('/admin/feed', methods=['GET','POST'])
    @login_required
    def admin_feed():
        data = []
        error_msg = None
        user = None

        if request.method == "POST":
            audit_data = NumenAudit.objects.filter(NumenAudit.user_id == request.form['user_id'])

            for datum in audit_data:
                data += [{
                         'create_time': datum.create_time.strftime('%m/%d/%Y %H:%M:%S.%f'),
                         'endpoint': datum.endpoint,
                         'method': datum.method,
                         'params': pickle.loads(datum.params),
                         'id': datum.id,
                         'user_id': datum.user_id
                         }]
                user = datum.user_id
            if not data:
                error_msg="This user has no activity for the last 90 days"

        return render_template('feed.html', users=User.objects.sort('+last_name'), data=data, error_msg=error_msg, user=user)

    @app.route('/tools/warehouse/pack_scan', methods=['GET','POST'])
    @login_required
    @requires_permission('access_warehouse_packslip')
    def pack_scan():
        success_msg = None
        error_msg = None

        if request.method == "POST":
            try:

                session['packslip_printer'] = request.form['pick_printer']

                rest_client.print_packslip(request.form["scan"], request.form["pick_printer"])
                success_msg = "Scan Success"
            except:
                traceback.print_exc()
                error_msg = "Scan Failed"

        return render_template('pack_scan.html', success_msg=success_msg, error_msg=error_msg, printers=PackslipPrinter.objects, selected_printer=session['packslip_printer'] if 'packslip_printer' in session else None)

    @app.route('/tools/warehouse/edit_printer/<samba_path>', methods=['GET','POST'])
    @app.route('/tools/warehouse/edit_printer/', defaults={"samba_path": None}, methods=['POST'])
    @login_required
    @requires_permission('access_warehouse_packslip')
    def edit_printer(samba_path):
        if request.method == 'GET':
            printer = PackslipPrinter.objects.filter(PackslipPrinter.samba_path==samba_path).one()
            return render_template('edit_printer.html', printer=printer)
        else:
            if not samba_path:

                printer = PackslipPrinter(
                                  name=request.form['name'],
                                  samba_path=request.form['samba_path'])

                printer.save()

            else:
                printer = PackslipPrinter.objects.filter(PackslipPrinter.samba_path==samba_path).one()
                printer.name=request.form['name']
                printer.samba_path=request.form['samba_path']

                printer.save()
            return redirect(url_for('pack_scan'))

    @app.route('/tools/warehouse/new_printer')
    @login_required
    @requires_permission('access_warehouse_packslip')
    def new_printer():
        return render_template('edit_printer.html', printer=None)


    @app.route('/tools/warehouse/delete_printer/<samba_path>', methods=['GET'])
    @login_required
    @requires_permission('access_warehouse_packslip')
    def delete_printer(samba_path):
        printer = PackslipPrinter.objects.filter(PackslipPrinter.samba_path==samba_path).one()

        printer.delete()
        return redirect(url_for('pack_scan', success_msg='Printer Deleted'))

    @app.route('/orders/edit', methods=['PUT'])
    @login_required
    @requires_permission('update_fulfillment')
    def order_edit():
        order = json.dumps(request.json)
        try:
            rest_client.update_order(order, request.json['id'])
        except:
            return jsonify({"msg":"Could not update the order."}), 500
        else:
            return jsonify({"msg":"Order saved."})

    @app.route('/orders/resubmit', methods=['PUT'])
    @login_required
    @requires_permission('update_fulfillment')
    def order_resubmit():
        order = json.dumps(request.json)
        try:
            rest_client.update_order(order, request.json['id'])
        except:
            return jsonify({"msg":"Could not update the order."}), 500
        else:
            try:
                rest_client.resubmit_order(order, request.json['id'])
            except:
                return jsonify({"msg":"Order could not be resubmitted."}), 500
            else:
                return jsonify({"msg":"Order saved and resubmitted."})

    @app.route('/orders/wmsdelete', methods=['PUT'])
    @login_required
    @requires_permission('delete_fulfillment')
    def order_wmsdelete():

        # Customer is required for ESB logic
        payload = {
            'status' : 'suspended',
            'customer' : request.json['customer']
            }
        try:
            # Method does not yet exist - stub
            rest_client.delete_wms_order(request.json['id'])
        except:
            return jsonify({"msg":"Could not delete the order from WMS."}), 500

        try:
            rest_client.update_order(json.dumps(payload), request.json['id'])
        except:
            return jsonify({"msg":"Order could not be updated within Numen."}), 500

        return jsonify({"msg":"Order deleted from WMS and updated in Numen."})


    @app.route('/orders/search', methods=['GET', 'POST'])
    @login_required
    @requires_permission('read_orders','read_fulfillment')
    def order_search():
        RESULT_LIMIT = 6000
        if request.method == 'GET':
            users = []

            if g.permissions.have_permission('query_division'):
                users = [user for user in User.objects.filter(User.accpac_ids != [])
                                if any([ True for div in g.user.divisions
                                        if div in user.divisions ])]
                if g.permissions.have_permission('read_orders_all'):
                    users = User.objects.filter(User.accpac_ids != [])


            return render_template('order_search.html', users=users)
        else:
            data = None
            error_msg = None
            try:
                end_date = request.form['end_date']
                start_date = request.form['start_date']
                if request.form['end_date']:
                    end_date = int(time.mktime(datetime.datetime.strptime(request.form['end_date'], "%m/%d/%Y").timetuple()))
                if request.form['start_date']:
                    start_date = int(time.mktime(datetime.datetime.strptime(request.form['start_date'], "%m/%d/%Y").timetuple()))

                permissions = {"wms" : False, "accpac" : {"allow" : False, "codes" : []}}

                if g.permissions.have_permission('read_fulfillment'):
                    permissions['wms'] = True

                if g.permissions.have_permission('read_orders_all'):
                    permissions['accpac']['allow'] = True
                    if request.form.getlist('sales_rep'):
                        permissions['accpac']['codes'] = request.form.getlist('sales_rep')
                elif g.permissions.have_permission('query_division'):
                    permissions['accpac']['allow'] = True
                    for division in g.user.divisions:
                        [permissions['accpac']['codes'].extend(user.accpac_ids) for user in User.objects.filter(User.divisions == division)]
                    permissions['accpac']['codes'] = list(set(permissions['accpac']['codes']))
                    if request.form.getlist('sales_rep'):
                        permissions['accpac']['codes'] = request.form.getlist('sales_rep')
                else:
                    if g.user.accpac_ids:
                        permissions['accpac']['allow'] = True
                        permissions['accpac']['codes'] = g.user.accpac_ids
                    else:
                        if not permissions['wms']:
                            return jsonify({'text' : "Your user profile is not configured to search orders.."}), 401

                order_id = [x.strip() for x in request.form['orderid'].split(',')]
                if order_id == ['']:
                    order_id = ''

                # The flag list should come in as an array from the front-end multiselect plug-in
                # Because the multiselect cannot return a dictionary, we must parse the notation
                # used to denote flag keys and values, which is key_value; error_false should
                # create an "error" : "false" entry in our flag dictionary
                flags = request.form.getlist('flags')
                flag_dictionary = {}
                for flag in flags:
                    flag = flag.split('_')
                    flag_dictionary[flag[0]] = flag[1]

                payload = { "id" : order_id,
                            "xref" : request.form['orderxref'],
                            "end_date" : end_date,
                            "start_date": start_date,
                            "status" : request.form.getlist('status'),
                            "type" : request.form.getlist('order_type'),
                            "flags" : flag_dictionary,
                            "client" : request.form['client'],
                            "sales_rep" : request.form.getlist('sales_rep'),
                            "permissions": permissions,
                            "result_limit" : RESULT_LIMIT
                            }
                data = rest_client.search_orders(json.dumps(payload))

            except:
                traceback.print_exc()
                error_msg = "Search Failed"

            return jsonify(to_datatables(data))



    @app.route('/orders/po_loader/<po_nbr>', methods=['GET'])
    @login_required
    def po_loader(po_nbr):
        legacy_pos = LegacyPurchaseOrder.objects.filter(LegacyPurchaseOrder.po_nbr == po_nbr).one()
        return jsonify(legacy_pos.to_json())

    @app.route('/orders/get_bookmarks', methods=['GET'])
    @login_required
    def get_bookmarks():
        bookmarks = g.user.bookmarks
        return jsonify({"bookmarks" : bookmarks})


    @app.route('/orders/detail/<source>/<item_id>', methods=['GET','POST'])
    @app.route('/orders/detail/', defaults={"item_id": None, "source": None}, methods=['POST'])
    @login_required
    def order_detail(item_id, source):
        if request.method == 'GET':
            order = rest_client.get_order_by_id(item_id)
            shipping = rest_client.get_shipping_methods()
            receipts = []
            invoices = []

            for invoice in order['invoices']:
                if invoice['invoice_nbr'] == "_RECEIPT":
                  receipts.append(invoice)
                else:
                  invoices.append(invoice)

            if source == "numen":
                if g.permissions.have_permission('read_fulfillment'):
                    return render_template('order_detail.html', order=order, shipping_methods = shipping['items'])
                abort(403)
            else:
                allowed_accpac_ids = g.user.accpac_ids
                if g.permissions.have_permission('query_division'):
                    division_codes = []
                    for division in g.user.divisions:
                        [division_codes.extend(user.accpac_ids) for user in User.objects.filter(User.divisions == division)]
                    allowed_accpac_ids = list(set(division_codes))
                if order["salesrep"] in allowed_accpac_ids or g.permissions.have_permission('access_executive') or g.permissions.have_permission('read_orders_all'):
                    return render_template('order_detail_accpac.html', invoices=invoices, receipts=receipts, order=order)
                abort(403)


    @app.route('/orders/bookmarks', methods=['GET', 'POST'])
    @login_required
    def order_bookmarks():
        if request.method == 'GET':
            return render_template('order_bookmarks.html')
        else:
            payload = { 'id' : g.user.bookmarks}
            data = rest_client.search_orders(json.dumps(payload))
            return jsonify(to_datatables(data))



    @app.route('/user/bookmark', methods=['POST'])
    @login_required
    def toggle_bookmark():
        order_id = request.form['order']
        msg = ""
        if g.user.bookmarks and order_id in g.user.bookmarks:
            g.user.bookmarks.remove(order_id)
            msg = 'removed'
        else:
            g.user.bookmarks.append(order_id)
            msg = 'added'

        g.user.save()
        return jsonify({'msg' : msg})

    @app.route('/tools/warehouse/bins', methods=['GET', 'POST'])
    @login_required
    @requires_permission('access_warehouse_bins')
    def bin_select():
        error_msg = None
        success_msg = None

        if request.method == "POST":
            try:
                bins = request.form.getlist('bin')

                if not bins:
                    error_msg = "Please Select Bins to Delete"
                else:
                    rest_client.delete_bins(bins)
                    success_msg = "Bin Delete Success"
            except:
                traceback.print_exc()
                error_msg = "Bin Delete Failure"

        data = rest_client.get_bins_for_deletion()

        return render_template('bin_select.html', data=data, success_msg=success_msg, error_msg=error_msg)


    @app.route('/sub_modal', methods=['POST'])
    @login_required
    def sub_modal():
        try:
            print 'sub_modal endpoint called'
            job_name, payload = helpers.sub_params_setter(form_params=request.form)

            rest_client.create_job(payload)
            return 'job created'

        except:
            traceback.print_exc()
            return 'job create fail', 500



    @app.route('/reports/subscriptions/modify/<subscription_name>', methods=['GET', 'POST'])
    @login_required
    def modify_subscription(subscription_name):
        try:
            job_name, payload = helpers.sub_params_setter(form_params=request.form, subscription_name=subscription_name)

            rest_client.modify_job(g.user.id, job_name, payload)
            return 'job modified'
        except:
            traceback.print_exc()
            return 'job modify fail', 500

    @app.route('/reports/subscriptions/delete/<subscription_name>', methods=['GET'])
    @login_required
    def delete_subscription(subscription_name):
        rest_client.delete_job(g.user.id, subscription_name)

        return redirect(url_for("sub_list"))


    @app.route('/reports/subscriptions/get/<subscription_name>', methods=['GET', 'POST'])
    @login_required
    def get_subscription(subscription_name):
        sub = rest_client.get_job(g.user.id, subscription_name)

        return jsonify(sub)


    @app.route('/reports/sub_list', methods=['GET', 'POST'])
    @login_required
    def sub_list():
        print 'sub_list endpoint called'
        job_list = rest_client.get_jobs(user=g.user.id)

        return render_template('sub_list.html', names=[item['name'] for item in job_list['items']])



    @app.route('/deliv_form/<file_format>', methods=['POST'])
    @login_required
    def deliv_form(file_format):
        try:
            print "The /deliv_form endpoint has been called."
            rqst_params = request.form
            report_name = request.form['report_name']

            params = {}
            for key, value in rqst_params.items():
                params[key] = value

            fileName = None
            print file_format

            if 'client_id' in request.form:
                client = rqst_params["client_id"]
                fileName = "Report_" + report_name + "_" + client + "." + file_format

            if 'sales_codes' in request.form:
                params['sales_codes'] = request.form.getlist('sales_codes')
                fileName = "Report_" + report_name + "_" + g.user.id + "." + file_format

            if not fileName:
                fileName = 'Report.' + file_format

            form_params = json.dumps(params)

            print "The form params have been dumps"


            report_data = rest_client.exec_report(form_params, report_name, file_format)

            payload = report_data["payload"]
            print "payload was collected"
            print fileName
            response = make_response(base64.b64decode(payload))
            response.headers['Content-Type'] = "application/" + file_format
            response.headers["Content-Disposition"] = "attachment; filename=" + fileName
            return response
        except:
            traceback.print_exc()
            abort(500)


    @app.route('/reports/executive/<report_name>')
    @login_required
    @requires_permission('access_executive')
    def executive_report(report_name):
        if report_name not in app.config['valid_executive_reports']:
            abort(404)


        return render_template('reports/executive/{0}.html'.format(report_name.replace(' ','_')),
                               pretty_report_name=app.config['valid_executive_reports'][report_name],
                               report_name='executive '+report_name)


    @app.route('/reports/personal/<report_name>')
    @login_required
    @requires_permission('access_reports_ar')
    def personal_report(report_name):
        if report_name not in app.config['valid_personal_reports']:
            abort(404)

        if g.permissions.have_permission('access_executive'):
            allowed_users = User.objects.filter(User.accpac_ids != [])


        elif g.permissions.have_permission('query_division'):
            allowed_users = [user for user in User.objects.filter(User.accpac_ids != [])
                            if any([ True for div in g.user.divisions
                            if div in user.divisions ])]
        else:
            allowed_users = [g.user]

        user_list = []

        [user_list.append({'user': user,
                           'url_params': {
                             'user_name': user.first_name + ' ' + user.last_name,
                                'accpac_cd': user.accpac_ids
                             }
                             }) for user in allowed_users]
        return render_template('reports/personal/{0}.html'.format(report_name.replace(' ', '_')),
                               pretty_report_name=app.config['valid_personal_reports'][report_name],
                               allowed_users=sorted(user_list, cmp=sort_user_list),
                               report_name='personal ' + report_name)




    @app.route('/reports/division/<report_name>')
    @login_required
    @requires_permission('query_division')
    def division_report(report_name):
        if report_name not in app.config['valid_division_reports']:
            abort(404)

        if g.permissions.have_permission('access_executive'):
            allowed_divisions = app.config['divisions']
        elif g.permissions.have_permission('query_division'):
            allowed_divisions = g.user.divisions
        else:
            abort(500)

        division_list = []


        for division in allowed_divisions:
            user_list = []
            for user in User.objects:
                list = []
                for div in user.divisions:
                    if div == division:
                        list += [True]
                if any(list):
                    user_list += [user]

            accpac_ids = []

            for userobject in user_list:
                accpac_ids += userobject.accpac_ids
            accpac_ids = set(accpac_ids)
            division_list.append({'division': division,
                                  'url_params': {
                                                 'division': division,
                                                 'accpac_cd': accpac_ids
                                                 }
                                  })

        return render_template('reports/division/{0}.html'.format(report_name.replace(' ', '_')),
                               pretty_report_name=app.config['valid_division_reports'][report_name],
                               allowed_divisions=sorted(division_list, cmp=lambda l, r: cmp(l['division'], r['division'])),
                               divisions=app.config['divisions'],
                               report_name='division ' + report_name)




    @app.route('/reports/ad-hoc/<report_name>')
    @login_required
    def ad_hoc_report(report_name):
        if report_name not in app.config['valid_adhoc_reports']:
            abort(404)
        resp = requests.get(app.config['ESB_URI'] + app.config['ESB_GET_CLIENTS'], headers=default_header)

        open_stores = CollegeShirtStore.objects.filter(
            CollegeShirtStore.close_date > datetime.datetime.now())

        closed_stores = CollegeShirtStore.objects.filter(
            CollegeShirtStore.close_date < datetime.datetime.now())

        return render_template('reports/ad-hoc/{0}.html'.format(report_name.replace(' ', '_')),
                               pretty_report_name=app.config['valid_adhoc_reports'][report_name],
                               report_name=report_name,
                               clients=resp.json()['items'],

                               open_stores=open_stores,
                               closed_stores=closed_stores)


    @app.route('/admin/edit_client/<client_id>', methods=['GET'])
    @app.route('/admin/edit_client', defaults={"client_id": None}, methods=['GET', 'POST'])
    @login_required
    @requires_permission('access_admin')
    def edit_client(client_id=None):
        configed_list = []
        wms_Client_list = []

        wms_Client_dict = rest_client.get_wms_customer_list()
        wms_Client_list = wms_Client_dict['items']

        configed_dict = rest_client.get_customer_config_list()
        configed_list = configed_dict['items']

        print request.args.get("success_msg")
        request.args.get("client_id")

        return render_template('edit_client.html', clients=wms_Client_list, configed_list=configed_list, client_id=client_id)



    @app.route('/tools/invoice_reminders', methods=['GET', 'POST'])
    @login_required
    @requires_permission('access_invoices')
    def invoice_reminders():
        error_msg = None
        success_msg = None

        if request.method == "POST":
            try:
                custnos = request.form.getlist('custno')
                rest_client.send_invoice_reminders(custnos)
                success_msg="Invoice Send Success"

            except:
                error_msg="Invoice Send Failure"


        data = rest_client.get_invoices_by_age(50)

        return render_template('invoice_reminders.html',data=data, success_msg=success_msg, error_msg=error_msg)



    @app.route('/tools/disney_invoice', methods=['GET', 'POST'])
    @login_required
    @requires_permission('access_invoices')
    def disney_invoice():
        error_msg = None
        fileName = "GGDSNY_Invoices"

        if request.method == "POST":

            try:
                from_date = datetime.datetime.strptime(request.form['from_date'], "%m/%d/%Y")
                to_date = datetime.datetime.strptime(request.form['to_date'], "%m/%d/%Y").replace(hour=23, minute=59, second=59, microsecond=999999)

                excel_data = rest_client.generate_collaborate_invoice_ss('GGDSNY', from_date, to_date)

                response = make_response(base64.b64decode(excel_data["payload"]))
                response.headers['Content-Type'] = "application/xls"
                response.headers["Content-Disposition"] = "attachment; filename=" + fileName + "_" + request.form['from_date'] + "_TO_" + request.form['to_date'] + ".xls"
                return response

            except:
                traceback.print_exc()
                error_msg="Generate Spreadsheet Failure"


        return render_template('disney_invoice.html', error_msg=error_msg)


    @app.route('/tools/disney_tool', methods=['GET', 'POST'])
    @login_required
    @requires_permission('access_disney')
    def disney_tool():
        error_msg = None
        success_msg = None
        data = rest_client.get_sku_rollup('GGDSNY')
        items = []

        if request.method == "POST":

            for k,v in request.form.iteritems():
                if k != "doc_name":
                    for item in data['items']:
                        if item["sku"] == k:
                            desc = item["desc"]

                            items.append({ "sku" : k,
                                           "qty" : int(v),
                                           "desc": desc
                                          })
            try:
                doc_name = request.form['doc_name']

                payload = {
                    "id": doc_name,
                    "vendor_nbr": "G&G",
                    "vendor": "G&G Outfitters",
                    "client": "GGDSNY",
                    "items": items
                    }

                payload_json = json.dumps(payload)
                rest_client.create_receiving_doc(payload_json)
                success_msg="Receiving Document Send Success"

            except:
                traceback.print_exc()
                error_msg="Receiving Document Send Failure"

        return render_template('disney_orders.html', data=data, success_msg=success_msg, error_msg=error_msg)



    @app.route('/admin/edit_client_post', methods=['GET', 'POST'])
    @login_required
    @requires_permission('access_admin')
    def edit_client_post():
        # store all the form values in vars for later use

        adr1 = request.form['address[addr_line1]']
        state = request.form['address[state]']
        footer = request.form['email_config[footer_text]']
        city = request.form['address[city]']
        adr2 = request.form['address[addr_line2]']
        phone = request.form['phone']
        orden = request.form['email_config[order_enabled]']
        zip = request.form['address[zip]']
        shipen = request.form['email_config[shipment_enabled]']
        lglnme = request.form['legal_name']
        id = request.form['id']
        presort = request.form['presort']

        cxml_enabled = request.form['cxml[enabled]']
        cxml_invoicing_enabled = request.form['cxml_invoicing[enabled]']
        cxml_identity = request.form['cxml[identity]']
        cxml_ship_method = request.form['cxml[ship_method]']
        cxml_network = request.form['cxml[network]']

        settlement = request.form['financial[settlement]']
        cybersource_user = request.form['financial[cybersource_user]']
        cybersource_key = request.form['financial[cybersource_api_key]']

        invoice_company = request.form['financial[invoice_company]']
        invoice_customer = request.form['financial[invoice_customer]']
        invoicing_enabled = request.form['financial[invoicing_enabled]']

        default_id = request.form['default_id']

        cntry = request.form['address[country]']

        print "Everything but the img file!"

        mimetype = request.files['logo[data]'].mimetype

        print "The flask requests were picked up."



        # Here we store the image path and rename it based on the client id

        if mimetype in ["image/png", "image/jpeg"]:

            image_path = "webapp/public/img/" + id + os.path.splitext(request.files['logo[data]'].filename)[1]
            request.files['logo[data]'].save(image_path)
            image_data = StringIO(open(image_path, 'rb').read())
            image_pil = Image.open(image_data)

            basewidth = 150
            wpercent = (basewidth/float(image_pil.size[0]))
            hsize = int((float(image_pil.size[1])*float(wpercent)))
            image_pil = image_pil.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
            image_pil.save(image_data, format=mimetype.split('/')[1])
            base64code = base64.b64encode(image_data.getvalue())
            image_data.close()
            os.remove(image_path)

            print "A new image file upload exists and was encoded correctly"
        else:
            print "No new image file upload exists so the old image data will be added to the data form."
            base64code = request.form['logo_data']
            mimetype = request.form['logo_mimetype']
            
        flag_dictionary = {}
        flag_dictionary['presort'] = True if presort == "True" else False
        # Data is our python dict object that is formatted for the client json data oabject
        data = {
                "address": {
                    "addr_line1": adr1,
                    "addr_line2": adr2,
                    "city": city,
                    "country": cntry,
                    "state": state,
                    "zip": zip
                },

                "email_config": {
                    "footer_text": footer,
                    "order_enabled": orden == "True",
                    "shipment_enabled": shipen == "True"
                },

                "id": id,
                "legal_name": lglnme,
                "flags": flag_dictionary,

                "logo": {
                    "data": base64code,
                    "mime_type": mimetype,
                    "update_time": int(time.time())
                },
                "phone": phone,

                "cxml": {
                    "enabled": cxml_enabled == "True",
                    "network": cxml_network,
                    "identity": cxml_identity,
                    "ship_method": cxml_ship_method,
                    "invoicing_enabled" : cxml_invoicing_enabled == "True"
                },

                "financial": {
                    "settlement": settlement,
                    "cybersource_user": cybersource_user,
                    "cybersource_api_key": cybersource_key,
                    "invoice_company": invoice_company,
                    "invoice_customer": invoice_customer,
                    "invoicing_enabled": invoicing_enabled == "True"
                }
                }
        print"The data form was created."

        # prepare data for json
        client_json = json.dumps(data)
        print client_json


        if default_id == "DEFAULT":
            # the json is added anew into the database
            rest_client.create_customer_config(client_json)

        else:
            # or the json is updating the existing client id
            rest_client.update_customer_config(client_json, id)
            # the view is sent back to the original form with a parameter message
        return redirect(url_for("edit_client", success_msg="The client information was saved.", client_id=id))




    @app.route('/client_config_ajax/<client_id>', methods=['GET', 'POST'])
    @login_required
    @requires_permission('access_admin')
    def get_client_config(client_id):

        json_data = rest_client.get_customer_config(client_id)

        return jsonify(json_data)


    @app.route('/tools/warehouse/aarp_bundle', methods=['GET'])
    @login_required
    @requires_permission('read_bundles')
    def aarp_bundle():
        bundles = Bundle.objects
        last_updated = Bundle.objects.sort('-updated').first().updated
        return render_template('aarp_bundle.html', bundles=bundles, last_updated=last_updated)

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if check_browser():
            return render_template('unsupported.html')

        next = request.args.get("next")

        if request.method == 'POST':
            next = request.form["next"]
            try:
                #check our User collection for a matching id, then authenticate according to the auth settings of the user
                user = User.objects.filter(User.id == request.form['user'].lower()).one()

                if len(request.form['password']) == 0 or not user:
                    raise Exception('No password or user')

                if user.auth == 'ad':
                    #if AD auth, try a LDAP bind to our AD server and see if it works
                    l = ldap.open(app.config['ldap.host'])
                    l.protocol_version = ldap.VERSION3
                    l.set_option(ldap.OPT_REFERRALS, 0)

                    #if this bind fails (invalid password, etc.) then an exception will be raised
                    l.simple_bind_s(request.form['user'].lower() + '@ggoutfitters.com', request.form['password'])
                elif user.auth == 'pw':
                    if not pwd_context.verify(request.form['password'], user.password):
                        raise Exception('Invalid password')
                else:
                    raise Exception('Unknown authentication method')
            except Exception as e:
                traceback.print_exc()
                return redirect(url_for('login',
                                        next=next,
                                        error_msg="Please enter a correct username and password. Note that both fields are case-sensitive.",
                                        failed=True))

            session['user'] = request.form['user'].lower()
            NumenAudit.record(User.objects.filter(User.id == session['user']).one(), request)

            return redirect(next)

        elif request.method == 'GET':
            return render_template('login.html', next=next, failed=False)

    @app.route('/logout', methods=['GET'])
    @login_required
    def logout():
        session.clear()
        return redirect(url_for('index'))


    @app.route('/spreadsheet/ss-upload', methods=['POST'])
    @login_required
    @requires_permission('create_fulfillment', 'create_receiving', 'create_bundles')
    def spreadsheet_upload():
        print request.form
        SpreadsheetUpload.record(
            user=g.user.id,
            file_name=request.files['file'].filename,
            file_data=base64.b64encode(request.files['file'].read()),
            client_id=request.form['client_id'] if 'client_id' in request.form else None,
            ss_type=request.form['ss_type']
            )

        return redirect(url_for('my_spreadsheet_uploads'))

    @app.route('/spreadsheet/my-ss-uploads', methods=['GET', 'POST'])
    @login_required
    @requires_permission('create_fulfillment')
    def my_spreadsheet_uploads():
        resp = requests.get(app.config['ESB_URI'] + app.config['ESB_GET_CLIENTS'], headers=default_header)
        selected_user = None

        if g.permissions.have_permission('access_executive'):
            users = User.objects.sort('+last_name')
        elif g.permissions.have_permission('query_division'):
            users = [user for user in User.objects.filter(User.divisions == g.user.divisions).sort('+last_name')]
        else:
            users = None

        if request.method == 'POST':
            uploads = uploads = SpreadsheetUpload.objects.filter(SpreadsheetUpload.user == request.form['user_id'])
            selected_user = request.form['user_id']
        else:
            uploads = SpreadsheetUpload.objects.filter(SpreadsheetUpload.user == g.user.id)

        return render_template('my_spreadsheet_uploads.html', uploads=uploads, users=users, selected_user=selected_user, clients=resp.json()['items'])

    @app.route('/spreadsheet/my-ss-uploads/<upload_id>', methods=['GET'])
    @login_required
    @requires_permission('create_fulfillment')
    def view_spreadsheet_upload(upload_id):
        upload = SpreadsheetUpload.objects.filter(SpreadsheetUpload.id == upload_id).one()
        if not upload:
            return 404

        return render_template('spreadsheet_upload_results.html', upload=upload)

    @app.route('/spreadsheet/my-ss/uploads/errors/<upload_id>', methods=['GET'])
    @login_required
    @requires_permission('create_fulfillment')
    def view_spreadsheet_errors(upload_id):
        upload = SpreadsheetUpload.objects.filter(SpreadsheetUpload.id == upload_id).one()
        if not upload:
            return 404

        return jsonify(upload.to_json())

    @app.route('/spreadsheet/my-ss-uploads/file/<upload_id>', methods=['GET'])
    @login_required
    @requires_permission('create_fulfillment')
    def download_spreadsheet(upload_id):
        upload = SpreadsheetUpload.objects.filter(SpreadsheetUpload.id == upload_id).one()
        if not upload:
            return 404

        resp = make_response(base64.b64decode(upload.file_data))
        resp.headers['Content-Disposition'] = 'attachment; filename=' + upload.file_name

        return resp


    @app.route('/admin/esb-dashboard', methods=['GET'])
    @login_required
    @requires_permission('access_admin')
    def esb_dashboard():
        return render_template('esb_dashboard.html')

    @app.route('/esb-dashboard-update/<timespan>/<increment>', methods=['GET'])
    @login_required
    @requires_permission('access_admin')
    def esb_dashboard_update(timespan, increment):
        req_uri = app.config['ESB_URI'] + app.config['ESB_AUDIT_BY_TIME'] + timespan + '/' + increment
        resp = requests.get(req_uri, headers=default_header)
        return jsonify(resp.json())

    @app.route('/mq-dashboard-update', methods=['GET'])
    @login_required
    @requires_permission('access_admin')
    def mq_dashboard_update():
        creds = pika.PlainCredentials(app.config['mq.user'], app.config['mq.pass'])
        connection = pika.BlockingConnection(pika.ConnectionParameters(
                host=app.config['mq.host'],
                credentials=creds))
        channel = connection.channel()

        rabbitQ = requests.get(app.config['mq.api_url'], auth=(app.config['mq.user'], app.config['mq.pass']))

        queues = []
        for x in rabbitQ.json():
            queues.append(x['name'])

        items = []
        for queue in queues:
            items.append({'name':queue, 'cnt':channel.queue_declare(passive=True, queue=queue).method.message_count})

        return jsonify({'items':items})

    @app.route('/mq_requeue/<queue_name>', methods=['GET'])
    @login_required
    @requires_permission('access_admin')
    def mq_requeue(queue_name):
        creds = pika.PlainCredentials(app.config['mq.user'], app.config['mq.pass'])
        connection = pika.BlockingConnection(pika.ConnectionParameters(
                host=app.config['mq.host'],
                credentials=creds))
        connection2 = pika.BlockingConnection(pika.ConnectionParameters(
                host=app.config['mq.host'],
                credentials=creds))

        channel = connection.channel()
        channel2 = connection2.channel()

        queue_obj = channel.queue_declare(queue=queue_name, passive=True)
        count = queue_obj.method.message_count

        for x in range(0, count):
            msg = channel.basic_get(queue=queue_name)
            msg_json = json.loads(msg[2])

            queue_mod = queue_name[:-6]

            channel2.basic_publish(exchange='', routing_key=queue_mod + '.request', body=msg_json['orig_msg'])

            channel.basic_ack(delivery_tag=msg[0].delivery_tag)

        return redirect(url_for('esb_dashboard'))

    @app.route('/audit/order/<order_id>', methods=['GET'])
    @login_required
    @requires_permission('access_admin')
    def get_audit_by_order(order_id):
        req_uri = app.config['ESB_URI'] + app.config['ESB_AUDIT_DETAIL'] + order_id

        resp = requests.get(req_uri, headers=default_header)

        items = []
        # format the date fields in the response
        for item in resp.json()['items']:
            items.append({'update_time': datetime.datetime.fromtimestamp(item['update_time']).strftime('%Y-%m-%d %H:%M:%S'),
                          'method': item['method'],
                          'service': item['service'],
                          'status': item['status']})

        return jsonify({'items': items})


    @app.route('/admin/users', methods=['GET'])
    @login_required
    @requires_permission('access_admin')
    def view_user_profiles():
        users = User.objects
        groups_list = {}
        groups = UserGroup.objects
        for group in groups:
            groups_list[group.id] = group.name

        return render_template("view_profiles.html", users=users, groups_list=groups_list)


    @app.route('/admin/user', methods=['GET', 'POST'], defaults={'user_id': None})
    @app.route('/admin/user/<user_id>', methods=['GET','POST','DELETE'])
    @login_required
    @requires_permission('access_admin')
    def manage_user(user_id):
        #get is either editing a current user or creating a new user.  We can use the same template for this
        if request.method == 'GET':
            numen_users = [ user.id for user in User.objects ]

            l = ldap.open(app.config['ldap.host'])
            l.protocol_version = ldap.VERSION3
            l.set_option(ldap.OPT_REFERRALS, 0)
            l.simple_bind_s(app.config['ldap.bind.user'], app.config['ldap.bind.pass'])

            res_id = l.search(app.config['ldap.search.tree'], ldap.SCOPE_SUBTREE, app.config['ldap.search.class'], None)

            avail_users = []

            user = User.objects.filter(User.id == user_id).one()

            while 1:
                type, data = l.result(res_id, 0)
                if data == []:
                    break
                if 'mailNickname' in data[0][1] and data[0][1]['mailNickname'][0].lower() not in numen_users:
                    if all(word in data[0][1] for word in [
                            'mailNickname',
                            'givenName',
                            'sn',
                            'mail']):
                        avail_users.append({
                                'username': data[0][1]['mailNickname'][0],
                                'first': data[0][1]['givenName'][0],
                                'last': data[0][1]['sn'][0],
                                'email': data[0][1]['mail'][0]
                                })
            if user:
                user_groups = [{"name" : group['name'], "id" : group['id']} for group in rest_client.get_groups_for_user(user_id)['groups']]
            else:
                user_groups = []
            all_groups = [{"name" : group['name'], "id" : group['id']} for group in rest_client.get_groups()['groups']]

            return render_template("manage_user.html",
                                   avail_users=sorted(avail_users,
                                                        cmp=lambda x, y: (cmp(x['last'], y['last'])) if (x['last'] != y['last']) else (cmp(x['first'], y['first']))),
                                   divisions=app.config['divisions'],
                                   roles=app.config['roles'],
                                   user=user,
                                   user_groups=user_groups,
                                   all_groups=all_groups
                                   )
        elif request.method == 'POST':
            #POST is either going to be creating a new user or editing an existing user.
            #If we have a user_id param, then it's editing.  Else it's new.

            # perform some basic validation
            if any(div not in app.config['divisions'] for div in request.form.getlist('division')):
                return redirect(url_for('manage_user', error_msg='Invalid division specified'))

            if user_id:
                user = User.objects.filter(User.id == user_id).one()
            else:
                user = User.record(id=request.form['userid'],
                                   first_name=request.form['first_name'],
                                   last_name=request.form['last_name'],
                                   email=request.form['email']
                                   )

            if not user:
                return redirect(url_for('manage_user', error_msg='Error creating user'))

            user.accpac_ids = filter(None, request.form.getlist('accpac'))
            user.wms_id = request.form['wms'] if 'wms' in request.form else None
            user.workspace_id = request.form['workspace'] if 'workspace' in request.form else None
            user.divisions = request.form.getlist('division')
            
            if not user_id:
                if request.form['selectedUser'] == 'non-ad':
                    user.auth = 'pw'

            user.save()
            
            payload = {"groups" : request.form.getlist('group')}
            rest_client.update_groups_for_user(request.form['userid'], json.dumps(payload))

            #if auth == 'pw' and new user, we have to generate a password and send out an email telling them
            if user.auth == 'pw' and not user_id:
                chars = string.ascii_letters + string.digits + '!@#$%^&*()'
                random.seed = (os.urandom(1024))
                password = ''.join(random.choice(chars) for i in range(16))
                user.password = pwd_context.encrypt(password)
                user.prev_passwords = [user.password]
                user.password_change_date = datetime.datetime.now()
                user.save()

                email = {}
                email['to'] = user.email
                email['subject'] = "Your G&G Outfitters Numen account has been created"
                email['template'] = 'new_numen_user.html'
                email['params'] = { 'username': user.id,
                                    'password': password
                                    }
                email['attachments'] = []

                rest_client.send_email(json.dumps(email))

            return redirect(url_for('view_user_profiles', success_msg='User '+('created' if not user_id else 'edited')+' successfully'))
        elif request.method == 'DELETE':
            user = User.objects.filter(User.id == user_id).one()

            if user:
                #delete all subscriptions and user
                jobs = rest_client.get_jobs(user.id)
                for job in jobs['items']:
                        rest_client.delete_job(user.id, job['name'])
                user.delete()
            else:
                return jsonify({'msg': 'No User'}),500
            return jsonify({'msg': 'OK'})

    @app.route('/edit_profile', methods=['GET','POST'])
    @login_required
    def edit_profile():
        err_msg = None
        success_msg = None
        if request.method == 'POST':
            #let's do some basic validation first
            if len(request.form['first_name']) == 0 or len(request.form['last_name']) == 0 or len(request.form['email']) == 0:
                err_msg = 'Please make sure all fields are filled out'
            else:
                #password validation.  This is going to be a bit trickier
                if len(request.form['password-current']) > 0:
                    if request.form['password-new'] != request.form['password-new2']:
                        err_msg = 'Your new password does not match.  Please check it and try again'
                    elif not pwd_context.verify(request.form['password-current'], g.user.password):
                        err_msg = 'Your old password does not match.  Please check it and try again'
                    elif any([pwd_context.verify(request.form['password-new'], oldpw) for oldpw in g.user.prev_passwords]):
                        err_msg = 'You appear to have used your new password before.  Please choose a new password and try again.'
            if not err_msg:
                g.user.first_name = request.form['first_name']
                g.user.last_name = request.form['last_name']
                g.user.email = request.form['email']
                if len(request.form['password-current']) > 0:
                    g.user.password = pwd_context.encrypt(request.form['password-new'])
                    g.user.prev_passwords.append(g.user.password)
                    g.user.password_change_date = datetime.datetime.now()
                g.user.save()
                success_msg = "Your profile has been updated"


        return render_template('edit_profile.html', form=request.form if request.method == 'POST' else None, error_msg = err_msg, success_msg = success_msg)


    @app.route('/custom_ink', methods=['GET'])
    @login_required
    @requires_permission('access_customink')
    def custom_ink():
        return render_template("custom_ink.html")

    @app.route('/tools/schedules', methods=['GET','POST'])
    @login_required
    @requires_permission('create_schedule')
    def manage_schedules():
        success_msg = None
        if request.method == 'POST':
            upload_file = request.files['file']
            schedule_name = request.form['schedule_name']
            success_msg = 'Upload successful'

            schedule = ScheduleFile.objects.with_id(schedule_name)
            if not schedule:
                schedule = ScheduleFile(id = schedule_name)
            schedule.user_id = g.user.id
            schedule.last_update = datetime.datetime.now()
            schedule.filename = upload_file.filename
            schedule.data = base64.b64encode(upload_file.read())
            schedule.save()

        return render_template('manage_schedules.html',
                               schedules = ScheduleFile.objects,
                               success_msg = success_msg)


    @app.route('/schedules', methods=['GET'])
    def view_schedules():
        return render_template('view_schedules.html',
                               schedules = ScheduleFile.objects)

    @app.route('/schedule/<schedule_id>', methods=['GET'])
    def download_schedule(schedule_id):
        schedule = ScheduleFile.objects.with_id(schedule_id)

        if not schedule:
            abort(404)

        response = make_response(base64.b64decode(schedule.data))
        response.headers['Content-Type'] = "application/" + schedule.filename.split('.')[-1]
        response.headers["Content-Disposition"] = "attachment; filename=" + schedule.filename
        return response
