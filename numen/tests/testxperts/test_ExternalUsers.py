
import pytest
import time
import re
from selenium import webdriver
from random import randint
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException
from selenium.webdriver.common.keys import Keys

class TestExternalUsers_better:

    # ======================================222=====================================14 marc==================
    def test_ExternalGenerateReportButtonFunctionality_C222(self, impersonate_external):
        # Verify Generate Report button functionality.
        driver = impersonate_external['webdriver']
        # Verify Date and Time of generated report
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Out of stock tab.
        driver.find_element_by_link_text("Out of Stock").click()
        time.sleep(1)
        expected_header_out_of_stock_report = "Out of Stock Report"
        actual_header_out_of_stock_report = driver.find_element_by_id("content-header").text
        assert actual_header_out_of_stock_report in expected_header_out_of_stock_report
        # Click on Generate Report button.
        driver.find_element_by_class_name("btn-success").click()
        # Report should be generated successfully on the same page.
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(4)
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_displayed()
        time.sleep(1)

    # ======================================220==================================================================
    def test_ExternalVerifyContentOfOutOfStock_C220(self, impersonate_external):
        # Verify the content on "Out of stock" page.
        driver = impersonate_external['webdriver']
         # Verify Date and Time of generated report
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Inventory").is_displayed()
        assert driver.find_element_by_link_text("Orders").is_displayed()
        # Click on Inventory tab.
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # check Inventory on Hand tab.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'fa-folder-open-o')))
        assert driver.find_element_by_class_name("fa-folder-open-o").is_displayed()
        # Check other controls
        assert driver.find_element_by_link_text("Out of Stock").is_displayed()
        assert driver.find_element_by_link_text("Open Purchase Orders").is_displayed()
        assert driver.find_element_by_link_text("Inventory Receipts").is_displayed()
        assert driver.find_element_by_link_text("Inventory by Business Unit").is_displayed()
        assert driver.find_element_by_link_text("Product Usage").is_displayed()
        # Click on Out of stock tab.
        driver.find_element_by_link_text("Out of Stock").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        time.sleep(1)
        expected_header_out_of_stock_report = "Out of Stock Report"
        actual_header_out_of_stock_report = driver.find_element_by_id("content-header").text
        assert actual_header_out_of_stock_report in expected_header_out_of_stock_report
        # Verify the contents on Out of stock page
        # Drop down with prefilled client name like "ARPM"
        expected_dropdown = "ARPM"
        actual_dropdown = driver.find_element_by_id("CustomerNumber").text
        assert actual_dropdown in expected_dropdown
        # Report: Out of Stock (Title) top left of the page.
        expected_panel_heading = "Report: Out of Stock"
        actual_panel_heading = driver.find_element_by_class_name("panel-heading").text
        assert expected_panel_heading in actual_panel_heading
        # Generate Report button.
        assert driver.find_element_by_class_name("btn-success").is_displayed()
        # Make a Subscription button.
        assert driver.find_element_by_class_name("btn-primary").is_displayed()

    # ========================================166===============================================================

    def test_ExternalVerifyContentOnOrderSearch_C166(self, impersonate_external):
        driver = impersonate_external['webdriver']
        # Open the 'Order search page and verify the Order Search page opened properly.
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Orders')))
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Order Search')))
        time.sleep(1)
        driver.find_element_by_link_text("Order Search").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        time.sleep(1)
        actualTitle = driver.find_element_by_id("content-header").text
        expectedTitle = "Order Search"
        assert expectedTitle in actualTitle
        time.sleep(1)
        # Click Advanced filters button
        wait.until(EC.visibility_of_element_located((By.ID,'search_input_toggle')))

        # Check Content(label) on Order Search
        lblgroup = driver.find_element_by_class_name("col-md-12").text
        time.sleep(1)
        assert "ID / SO #:" in lblgroup
        assert "Client PO #:" in lblgroup
        assert "Order Status:" in lblgroup
        assert "Date Submitted:" in lblgroup

        assert driver.find_element_by_id("gen_search").is_displayed()
        assert driver.find_element_by_id("reset").is_displayed()

        # verifying the tags for fields

        expected_order_id = "input"
        actual_order_id = driver.find_element_by_id("orderid").tag_name

        expected_order_status = "button"
        # same class name is used for multiple blocks, to avoid use of xpath using css selector
        actual_order_status = driver.find_element_by_css_selector(".multiselect.dropdown-toggle.btn.btn-default").tag_name

        # to verify the calender clicking on the field to generate the calender pop up
        driver.find_element_by_name("submitted_start_date").click()
        driver.find_element_by_name("submitted_start_date").send_keys("02/15/2016")
        driver.find_element_by_name("submitted_start_date").send_keys(Keys.TAB)
        time.sleep(1)
        driver.find_element_by_name("submitted_end_date").click()
        driver.find_element_by_name("submitted_end_date").send_keys("02/29/2016")
        driver.find_element_by_name("submitted_end_date").send_keys(Keys.TAB)
        time.sleep(1)

        expected_search = "button"
        actual_search = driver.find_element_by_id("gen_search").tag_name
        time.sleep(1)
        expected_reset = "button"
        actual_reset = driver.find_element_by_id("reset").tag_name
        time.sleep(1)

        assert expected_order_id in actual_order_id
        assert expected_order_status in actual_order_status
        assert expected_search in actual_search
        assert expected_reset in actual_reset

    # =======================================168===================================================

    def test_ExternalVerifyContentOnAdvanceFilterSearch_C168(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)

        # Verify the Order Search Advance Search tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Orders')))
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        driver.find_element_by_link_text("Order Search").click()

        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        time.sleep(1)
        actualTitle = driver.find_element_by_id("content-header").text
        expectedTitle = "Order Search"
        assert expectedTitle in actualTitle
        time.sleep(1)
        # Check Content on Order Search
        # Verifying labels Client PO, Client Name, Tracking, Invoice, Art Title
        # as no attributes available so using class name for verifying the labels
        actual_column1 = driver.find_element_by_class_name("col-md-12").text
        arr = actual_column1.split("\n")
        # print(arr)
        exp_order_search_lbls = ["ID / SO #:","Client PO #:","Tracking #:","Invoice #:","Art Title:","Order Type:","Order Origin:","Flags:","Production Date:","Ship by Date:","In Hands Date:"]
        # Verify all labels
        for i in range(len(exp_order_search_lbls)):
            assert exp_order_search_lbls[i] in arr

        # Verifying tag input field
        input_tag = "input"
        order_ref = driver.find_element_by_id("orderxref").tag_name
        clientid = driver.find_element_by_id("orderid").tag_name
        tracking = driver.find_element_by_id("tracking").tag_name
        invoice = driver.find_element_by_id("invoice_nbr").tag_name
        artTitle = driver.find_element_by_id("art_title").tag_name
        assert input_tag in order_ref
        assert input_tag in clientid
        assert input_tag in tracking
        assert input_tag in invoice
        assert input_tag in artTitle

        # Verifying tag button
        button_tag = "button"
        select_button = driver.find_elements_by_css_selector(".multiselect.dropdown-toggle.btn.btn-default")
        order_type = select_button[1].tag_name
        order_origin = select_button[2].tag_name
        flag = select_button[3].tag_name
        assert button_tag in order_type
        assert button_tag in order_origin
        assert button_tag in flag

        # Verifying the Calender for multiple date picker fields
        driver.find_element_by_name("inhands_start_date").click()
        time.sleep(1)
        inhands_startDate = driver.find_element_by_class_name("month").is_displayed()
        # to avoid the overlapping of the calender pop up on field refreshing the site
        driver.refresh()
        driver.find_element_by_name("shipby_start_date").click()
        time.sleep(1)
        shipbystartDate = driver.find_element_by_class_name("month").is_displayed()
        driver.refresh()
        driver.find_element_by_name("paid_start_date").click()
        time.sleep(1)
        ppstartDate = driver.find_element_by_class_name("month").is_displayed()
        driver.refresh()
        time.sleep(1)
        # verify content
        # print(ppstartDate)
        assert ppstartDate == 1
        assert shipbystartDate == 1
        assert inhands_startDate == 1

    # ===============================================221=====================================================

    def test_ExternalVerifyContentOnBookmarks_C221(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Orders").click()  # click on Orders tab
        time.sleep(1)
        # bookmark
        driver.find_element_by_css_selector(".fa.fa-bookmark-o.fa-fw").click()
        time.sleep(1)
        # Click on Bookmark
        # Verify Bookmarks page is displayed.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        time.sleep(1)
        actualtitle = driver.find_element_by_id("content-header").text
        expectedtitle = "Bookmarks"
        assert expectedtitle in actualtitle
        time.sleep(1)
        # Verify the Header columns content
        tr = driver.find_element_by_id('orders_table').text
        arr = tr.split("\n")
        exp_data = ["ID", "Client Name", "Status", "Sales Rep", "Date Submitted", "Production Date", "Ship-by Date"]
        for i in range(len(exp_data)):
            assert exp_data[i] in arr

    # ====================30 November=========================================================================
    # ==================================246===================================================================
    def test_ExternalVerifyBackButtonFunctionalityOnSubscription_C246(self, impersonate_external):
        # Verify the Back button functionality on Subscription for: Out of Stock Report for ARPM form.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on report tab.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        #Click on 'Out of stock' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Out of Stock')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Out of Stock").click()
        time.sleep(1)
        # Verify 'Out of stock' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header_Inventory_On_Hand_Report ="Out of Stock Report"
        actual_header_Inventory_On_Hand_Report=driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_On_Hand_Report in expected_header_Inventory_On_Hand_Report
        
        # Click on "Make a subscription"button right side of the page.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        expected_subscription_label = "Subscription for: Out of Stock Report for ARPM"
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'modal-content')))
        actual_subscription_label = driver.find_element_by_class_name("modal-content").text
        assert expected_subscription_label in actual_subscription_label
        # Click on Back button under Subscription for: Out of Stock Report for ARPM form.
        driver.back()
        driver.find_element_by_link_text("Dashboard").click()
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        time.sleep(1)
        actual_dashboard_header = driver.find_element_by_id("content-header").text
        expected_dashboard_header = "Fulfillment Dashboard"
        assert expected_dashboard_header in actual_dashboard_header

    # ================================241=====================================================================
    def test_ExternalVerifyBackButtonFunctionalityInSubscriptionForm_C241(self, impersonate_external):
        # Verify user email Id display by default in subscription form.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        driver.find_element_by_link_text("Inventory").click()
        # Click on Out of stock tab.
        time.sleep(1)
        driver.find_element_by_link_text("Out of Stock").click()
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        time.sleep(1)
        expected_header_out_of_stock_report = "Out of Stock Report"
        actual_header_out_of_stock_report = driver.find_element_by_id("content-header").text
        assert actual_header_out_of_stock_report in expected_header_out_of_stock_report
        # Click on "Make a subscription"button right side of the page.
        driver.find_element_by_class_name("btn-primary").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        # Verify the "Email To" text box.
        expected_email = "clipford@ggoutfitters.com"
        actual_email = driver.find_element_by_id("email").get_attribute("value")
        assert expected_email in actual_email
        driver.find_element_by_class_name("btn-default").click()

    # ===========================================234===========================================================
    def test_ExternalVerifyRefreshButtonFunctionalityInGeneratedReports_C234(self, impersonate_external):
        # Verify refresh button functionality in the generated report.
        # Click on Reports tab.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Out of stock tab.
        driver.find_element_by_link_text("Out of Stock").click()
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        time.sleep(1)
        expected_header_out_of_stock_report = "Out of Stock Report"
        actual_header_out_of_stock_report = driver.find_element_by_id("content-header").text
        assert actual_header_out_of_stock_report in expected_header_out_of_stock_report
        # Click on Generate Report button.
        driver.find_element_by_class_name("btn-success").click()
        # Clic on Refresh Button
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(1)
        driver.find_element_by_name("ReportViewerControl$ctl05$ctl05$ctl00$ctl00$ctl00").click()
        # Report should be refreshed successfully
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_displayed()

    # ===============================01 December=========================================

    # ================================160==============================================================
    def test_ExternalVerifyLogoutFunctionality_C160(self, impersonate_external):
        # Verify the logout functionality.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        logout_title = "Numen - Login"
        driver.find_element_by_class_name("dropdown-toggle").click()
        driver.find_element_by_link_text("Logout").click()
        assert logout_title == driver.title
        time.sleep(5)
        driver.find_element_by_name('user').send_keys('testuser')
        driver.find_element_by_name('password').send_keys('X91VW9u^B6kEBWIw')
        driver.find_element_by_name('user').submit()
        time.sleep(5)

    # ===========================================232====================================================
    def test_ExternalVerifyHomeButtonFunctionality_C232(self, impersonate_external):
        # Verify home button functionality in all the pages in clipford - external user.
        # Click on orders
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        driver.find_element_by_link_text("Order Search").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Home')))
        driver.find_element_by_link_text("Home").click()
        # Dashboard page should be display.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        time.sleep(1)
        driver.find_element_by_link_text("Dashboard").click()
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        time.sleep(1)
        actual_dashboard_header = driver.find_element_by_id("content-header").text
        expected_dashboard_header = "Fulfillment Dashboard"
        assert expected_dashboard_header in actual_dashboard_header

    # ===========================================145====================================================
    def test_ExternalProfileImpersonate_C145(self, impersonate_external):
        #  Simple test to check if impersonating worked.  If we've reached this point,
        #  we've already verified that the correct user is logged in.  Simply assert True
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Verify Dashboard tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Dashboard')))
        time.sleep(1)
        driver.find_element_by_link_text('Dashboard').click()
        time.sleep(1)
        # Verify that dashboard page shows Sales Dashboard for user
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))

    # ===============C225================================================================================

    def test_VerifypaginationfunctionalitygeneratedReport_C225(self, impersonate_external):
        # Verify pagination functionality on generated Report
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Out of stock tab.
        driver.find_element_by_link_text("Out of Stock").click()
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        time.sleep(1)
        expected_header_out_of_stock_report = "Out of Stock Report"
        actual_header_out_of_stock_report = driver.find_element_by_id("content-header").text
        assert actual_header_out_of_stock_report in expected_header_out_of_stock_report
        # Click on Generate Report button.
        driver.find_element_by_class_name("btn-success").click()
        # Report should be generated successfully on the same page.
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)

        # Verify the first page
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_First_ctl01_ctl00").is_displayed()

        tp = driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").text
        tps = tp.split(" ")
        tpcnt = tps[0]
        # If total pages are 1
        if int(tpcnt) == 1:
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_First_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Previous_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Next_ctl00').get_attribute("class") == "NormalButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Last_ctl00').get_attribute("class") == "NormalButton"

        # Check next page & previous if total pages > 1
        if int(tpcnt) > 1:
            # Click Last button and verify controls NormalButton
            driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Last_ctl00_ctl00').click()
            time.sleep(5)
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Next_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Last_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Previous_ctl00').get_attribute("class") == "NormalButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_First_ctl00').get_attribute("class") == "NormalButton"
            # Click on First button
            driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_First_ctl00_ctl00').click()
            time.sleep(10)
            # Check First,Last,Next,Prev state
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_First_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Previous_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Next_ctl00').get_attribute("class") == "NormalButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Last_ctl00').get_attribute("class") == "NormalButton"

    # ========================C164=====================================================================================

    def test_VerifySubscription_in_subscription_page_C164(self, impersonate_external):
        # Verify Subscription on subscription page
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on report tab.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        #Click on 'Out of stock' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Out of Stock')))
        time.sleep(1)
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Out of Stock").click()
        time.sleep(1)
        # Verify 'Out of stock' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        time.sleep(1)
        expected_header_Inventory_On_Hand_Report ="Out of Stock Report"
        actual_header_Inventory_On_Hand_Report=driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_On_Hand_Report in expected_header_Inventory_On_Hand_Report
        
        # Click on "Make a subscription"button right side of the page.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()

        wait.until(EC.visibility_of_element_located((By.ID,'sub_name')))
        expected_subscription_label = "Subscription for: Out of Stock Report for ARPM"
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'modal-content')))
        actual_subscription_label = driver.find_element_by_class_name("modal-content").text
        assert expected_subscription_label in actual_subscription_label
        
        # Verify Subscription Name
        wait.until(EC.visibility_of_element_located((By.ID,'sub_name')))
        
        # Verify Subscription Name
        driver.find_element_by_id("sub_name").send_keys("test123")
        # Verify time
        driver.find_element_by_id("time").is_displayed()
        # Verify receive report day
        driver.find_element_by_id("modal_selector").is_displayed()
        driver.find_element_by_name("days_of_week").click()
        
        # Verify save Subscription button
        wait.until(EC.visibility_of_element_located((By.ID,'next_btn')))
        driver.find_element_by_id("next_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'noty_text')))
        time.sleep(1)
        assert driver.find_element_by_class_name("fa-rss-square").is_displayed()
        driver.find_element_by_class_name("fa-rss-square").click()
        
        wait.until(EC.visibility_of_element_located((By.ID,'jobs_table')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Modify')))
        assert driver.find_element_by_partial_link_text("Modify").is_displayed()
        assert driver.find_element_by_partial_link_text("Delete").is_displayed()    

    # =====================C301=====================================================================================
    def test_Verify_cancel_button_In_Delete_button_functionality_C301(self, impersonate_external):
        # Verify cancel button in Delete button functionality
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Verify the Back button functionality on Subscription for: Out of Stock Report for ARPM form.
        # Click on report tab.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        #Click on 'Out of stock' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Out of Stock')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Out of Stock").click()
        time.sleep(1)
        # Verify 'Out of stock' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header_Inventory_On_Hand_Report ="Out of Stock Report"
        actual_header_Inventory_On_Hand_Report=driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_On_Hand_Report in expected_header_Inventory_On_Hand_Report
        
        # Click on "Make a subscription"button right side of the page.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()
        expected_subscription_label = "Subscription for: Out of Stock Report for ARPM"
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'modal-content')))
        actual_subscription_label = driver.find_element_by_class_name("modal-content").text
        assert expected_subscription_label in actual_subscription_label
        
        # Verify Subscription Name
        wait.until(EC.visibility_of_element_located((By.ID,'sub_name')))
        driver.find_element_by_id("sub_name").send_keys("test123")
        # Verify time
        driver.find_element_by_id("time").is_displayed()
        # Verify receive report day
        driver.find_element_by_id("modal_selector").is_displayed()
        driver.find_element_by_name("days_of_week").click()
        
        # Verify save Subscription button
        wait.until(EC.visibility_of_element_located((By.ID,'next_btn')))
        driver.find_element_by_id("next_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'noty_text')))

        wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'fa-rss-square')))
        time.sleep(1)
        driver.find_element_by_class_name("fa-rss-square").click()

        wait.until(EC.visibility_of_element_located((By.ID,'jobs_table')))
        assert driver.find_element_by_partial_link_text("Modify").is_displayed()
        assert driver.find_element_by_partial_link_text("Delete").is_displayed()
        driver.find_element_by_partial_link_text("Delete").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'btn-default')))
        driver.find_element_by_class_name("btn-default").click()
        actual_subscription_name = driver.find_element_by_id("jobs_table").text
        time.sleep(1)
        expected_subscription_name = "test123"
        assert expected_subscription_name in actual_subscription_name


    # =====================C300=====================================================================================
    def test_Verify_contents_in_Subscription_form_C300(self, impersonate_external):
        # Verify contents in Subscription form 
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on report tab.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        #Click on 'Out of stock' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Out of Stock')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Out of Stock").click()
        time.sleep(1)
        # Verify 'Out of stock' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header_Inventory_On_Hand_Report ="Out of Stock Report"
        actual_header_Inventory_On_Hand_Report=driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_On_Hand_Report in expected_header_Inventory_On_Hand_Report
        
        # Click on "Make a subscription"button right side of the page.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()
        time.sleep(1)
        expected_subscription_label = "Subscription for: Out of Stock Report for ARPM"
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'modal-content')))
        actual_subscription_label = driver.find_element_by_class_name("modal-content").text
        assert expected_subscription_label in actual_subscription_label
        
        # Verify Subscription Name
        wait.until(EC.visibility_of_element_located((By.ID,'sub_name')))
        assert driver.find_element_by_id("sub_name").is_displayed()
        # Verify Email to field
        assert driver.find_element_by_id("email").is_displayed()
        # Verify  Delivery format in excel
        assert driver.find_element_by_class_name("radio").is_displayed()
        # Verify time
        assert driver.find_element_by_id("time").is_displayed()
        # Verify receive report day
        assert driver.find_element_by_id("modal_selector").is_displayed()
        actual_week_day = driver.find_element_by_id("modal_selector").is_displayed()
        
        # Verify all day of week check box
        for tr in driver.find_elements_by_id("modal_selector"):
            ths = tr.find_elements_by_name("days_of_week")
            if ths: actual_weekday = [th.text for th in ths]
            exp_weekday = ("Sunday", "Monday", "Tuesday", "Thursday", "Friday", "Saturday")

            size = len(exp_weekday)
            for i in range(size):
                assert actual_weekday[i] in exp_weekday[i]
        # Verify back button
        assert driver.find_element_by_class_name("btn-default").is_displayed()
        # Verify save Subscription button
        assert driver.find_element_by_id("next_btn").is_displayed() 

    # ==================================02 December==============242======================================

    def test_ExternalVerifySubscriptionShowInSubscriptionPage_C242(self, impersonate_external):
        # Verify submitted subscription show in the subscription page.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Verify the Back button functionality on Subscription for: Out of Stock Report for ARPM form.
        # Click on report tab.
        # Click on report tab.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        #Click on 'Out of stock' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Out of Stock')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Out of Stock").click()
        time.sleep(1)
        # Verify 'Out of stock' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header_Inventory_On_Hand_Report ="Out of Stock Report"
        actual_header_Inventory_On_Hand_Report=driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_On_Hand_Report in expected_header_Inventory_On_Hand_Report

        # Click on "Make a subscription"button right side of the page.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()
        time.sleep(1)
        expected_subscription_label = "Subscription for: Out of Stock Report for ARPM"
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'modal-content')))
        actual_subscription_label = driver.find_element_by_class_name("modal-content").text
        assert expected_subscription_label in actual_subscription_label

        # Verify Subscription Name
        wait.until(EC.visibility_of_element_located((By.ID,'sub_name')))

        random_number = str(randint(10, 999))
        subs_name = "Test1Subscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(subs_name)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"

        driver.find_element_by_id("email").send_keys(email)

        # Verify save Subscription button
        wait.until(EC.visibility_of_element_located((By.ID,'next_btn')))
        driver.find_element_by_id("next_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'noty_text')))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'fa-rss-square')))
        time.sleep(1)
        driver.find_element_by_class_name("fa-rss-square").click()
        wait.until(EC.visibility_of_element_located((By.ID,'jobs_table')))
        time.sleep(1)
        subscriptions = driver.find_element_by_id("jobs_table").text
        time.sleep(1)
        assert subs_name in subscriptions

    # ================================239=====2nd Dec,2015================================================================
    def test_ExternalVerifyMakeSubscriptionContent_C239(self, impersonate_external):
        # Verify the Make a subscription content.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Out of stock tab.
        driver.find_element_by_link_text("Out of Stock").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'btn-primary')))
        time.sleep(1)
        # Subscription
        driver.find_element_by_class_name("btn-primary").click()
        time.sleep(1)

        # Verify Subscription Name
        driver.find_element_by_id("sub_name").is_displayed()
        # Verify Email to field
        driver.find_element_by_id("email").is_displayed()
        # Verify Delivery format in excel
        driver.find_element_by_class_name("radio").is_displayed()
        # Verify time
        driver.find_element_by_id("time").is_displayed()
        # Verify receive report day
        driver.find_element_by_id("modal_selector").is_displayed()
        expected_days = ['Sunday',
                         'Monday',
                         'Tuesday',
                         'Wednesday',
                         'Thursday',
                         'Friday',
                         'Saturday']
        actual_days = driver.find_elements_by_class_name("checkbox")
        time.sleep(1)
        for day in actual_days:
            name = day.text
            assert name in expected_days
        # Verify back button
        driver.find_element_by_class_name("btn-default").is_displayed()
        # Verify save Subscription button
        driver.find_element_by_id("next_btn").is_displayed()
        driver.find_element_by_class_name("btn-default").click()

    # ===========================================223====2nd Dec,2015================================================

    def test_ExternalVerifyEnteriesInGeneratedReport_C223(self, impersonate_external):
        # Verify Showing 1 of xx entries functionality in generated report.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Out of stock tab.
        driver.find_element_by_link_text("Out of Stock").click()
        expected_header_out_of_stock_report = "Out of Stock Report"
        actual_header_out_of_stock_report = driver.find_element_by_id("content-header").text
        assert actual_header_out_of_stock_report in expected_header_out_of_stock_report
        # Click on Generate Report button.
        driver.find_element_by_class_name("btn-success").click()
        # Report should be generated successfully on the same page.
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_displayed()
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()

    # ======================C235====2nd Dec,15==========================================
    def test_Verify_Date_and_Time_on_generated_report_C235(self, impersonate_external):
        # Verify Date and Time on generated report
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on report tab.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        #Click on 'Out of stock' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Out of Stock')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Out of Stock").click()
        time.sleep(1)
        # Verify 'Out of stock' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header_Inventory_On_Hand_Report ="Out of Stock Report"
        actual_header_Inventory_On_Hand_Report=driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_On_Hand_Report in expected_header_Inventory_On_Hand_Report
        
        # Click on Generate Report button.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'btn-success')))
        driver.find_element_by_class_name("btn-success").click()
        
        # Report should be generated successfully on the same page.
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID,'ReportViewerControl_ctl05_ctl00_CurrentPage')))
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_displayed()
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()
        
        # Verify Report Creation time.
        wait.until(EC.visibility_of_element_located((By.ID,'VisibleReportContentReportViewerControl_ctl09')))
        actual_text = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        expected_text = "Report Created On"
        assert expected_text in actual_text

    # ==============================C233==2nd Dec,2015===========================================
    def test_Verify_Export_button_functionality_in_Report_C233(self, impersonate_external):
        # Verify Export button functionality in Report for type of report
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on report tab.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        #Click on 'Out of stock' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Out of Stock')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Out of Stock").click()
        time.sleep(1)
        # Verify 'Out of stock' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Out of Stock Report"
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header
        
        # Click on Generate Report button.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'btn-success')))
        driver.find_element_by_class_name("btn-success").click()
        
        # Report should be generated successfully on the same page.
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID,'ReportViewerControl_ctl05_ctl00_CurrentPage')))
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_displayed()
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl04_ctl00_ButtonLink").click()
        
        # Verify report can be exported in following format 
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'HoverButton')))
        assert driver.find_element_by_class_name("HoverButton").is_displayed()
        act = driver.find_elements_by_class_name("ActiveLink")
        time.sleep(1)
        exp_report_type = ['XML file with report data',
                           'CSV (comma delimited)',
                           'PDF',
                           'MHTML (web archive)',
                           'Excel',
                           'TIFF file',
                           'Word']
        for v in act:
            name = v.text
            assert name in exp_report_type
        
    # ==========================03 December============================================================================
    # ==================================304==============================================
    def test_ExternalVerifyBackButtonFunctionalityInModifySubscription_C304(self, impersonate_external):
        # To verify the back button functionality in modify Subscription for: Executive Accounts Receivable pop up
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Out of stock tab.
        driver.find_element_by_link_text("Out of Stock").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'btn-primary')))
        # Click on Make a Subscription button.
        driver.find_element_by_class_name("btn-primary").click()
        # Create Subscription
        wait.until(EC.visibility_of_element_located((By.ID,'email')))
        assert driver.find_element_by_class_name("modal-header").is_displayed()
        random_number = str(randint(10, 999))
        name = "Test1Subscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"

        driver.find_element_by_id("email").send_keys(email)
        driver.find_element_by_id("next_btn").click()
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Subscriptions')))
        driver.find_element_by_link_text("Subscriptions").click()
        time.sleep(3)
        # Subscription for: Executive Accounts Receivable pop up is displayed.
        driver.find_element_by_link_text("Modify").click()
        time.sleep(1)
        # Data in Subscription for: Executive Accounts should be edited successfully.
        sName_value = driver.find_element_by_id("job_name").get_attribute("value")
        driver.find_element_by_id("sub_name").send_keys("newabc123")
        # Cancel Subscription for: Executive Accounts
        driver.find_element_by_class_name("btn-default").click()
        time.sleep(1)
        driver.find_element_by_link_text("Modify").click()
        time.sleep(1)
        # Subscription should not be updated successfully.
        sNameNew_value = driver.find_element_by_id("job_name").get_attribute("value")
        assert sName_value in sNameNew_value

    # ==================================284==================================================================
    def test_ExternalVerifyContentInSubscriptionPage_C284(self, impersonate_external):
        # Verify content in Subscriptions page.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Subscriptions tab.
        driver.find_element_by_link_text("Subscriptions").click()
        time.sleep(1)
        # Verify Subscriptions page is displayed.
        actualtitle = driver.find_element_by_id("content-header").text
        expectedtitle = "Subscriptions"
        assert expectedtitle in actualtitle
        # Verify content
        subscription = driver.find_element_by_id("criteria").is_displayed()
        tablecol1 = driver.find_element_by_css_selector(".table.table-striped.table-bordered thead tr th:nth-of-type(1)").text
        tablecol3 = driver.find_element_by_css_selector(".table.table-striped.table-bordered thead tr th:nth-of-type(3)").text
        # verify columns
        td1 = "Subscription Name"
        td3 = "Modify/Delete"
        assert subscription == 1
        assert td1 in tablecol1
        assert td3 in tablecol3

    # ==================================268============================================================================
    def test_ExternalVerifyBackButtonFunctionalityOnSubscriptionPageForOpenPurchaseOrders_C268(self,impersonate_external):
        # Verify the Back button functionality on Subscription for: Open Purchase Orders for ARPM form
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Open Purchase Orders.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Open Purchase Orders')))
        driver.find_element_by_link_text("Open Purchase Orders").click()
        time.sleep(1)
        # Click on "Make a subscription"button right side of the page.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()
        time.sleep(1)
        # Click on Back button under Subscription for: Open Purchase Orders for ARPM form.
        assert driver.find_element_by_class_name("modal-header").is_displayed()
        driver.find_element_by_class_name("btn-default").click()
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        # User should be redirected to " Open Purchase Orders Report" page successfully.
        assert driver.find_element_by_id("content-header").is_displayed()

    # ==================================267===========================================================================
    def test_ExternalVerifyEmailIdDisplaySubscriptionPage_C267(self, impersonate_external):
        # Verify user Email Id display by default in subscription form.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Open Purchase Orders tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Open Purchase Orders')))
        driver.find_element_by_link_text("Open Purchase Orders").click()
        time.sleep(1)
        # Click on "Make a subscription"button right side of the page.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()
        # Verify the "Email To" text box.
        wait.until(EC.visibility_of_element_located((By.ID,'email')))
        exp_value = "clipford@ggoutfitters.com"
        actual_value = driver.find_element_by_id("email").get_attribute("value")
        assert exp_value in actual_value
        driver.find_element_by_class_name("btn-default").click()
        time.sleep(1)

    # ===============================C237===3rd Dec===========================================================

    def test_Verify_content_of_generated_report__out_of_stock_C237(self, impersonate_external):
        # Verify the content of generated report out of stock
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Out of stock tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Out of Stock')))
        driver.find_element_by_link_text("Out of Stock").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header_out_of_stock_report = "Out of Stock Report"
        actual_header_out_of_stock_report = driver.find_element_by_id("content-header").text
        assert actual_header_out_of_stock_report in expected_header_out_of_stock_report
        # Click on Generate Report button.
        driver.find_element_by_class_name("btn-success").click()
        # Report should be generated successfully on the same page
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        # Verify the first page
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_First_ctl01_ctl00").is_displayed()
        # Verify the Previous page
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Previous_ctl01_ctl00").is_displayed()
        # Verify the current page text box
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_displayed()
        # Verify the  Total Pages
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()
        # Verify the next Pages
        if driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Next_ctl01").is_displayed():
            assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Next_ctl01").is_displayed()
        else:
            assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Next_ctl00").is_displayed()
        # Verify the last Pages link
        if driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Last_ctl00").is_displayed():
            assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Last_ctl00").is_displayed()
        else:
            assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Last_ctl01").is_displayed()
        # Verify search text box
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl00").is_displayed()
        # Verify find link
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl01").is_displayed()
        # Verify find next link
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl03").is_displayed()
        # Verify export button
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl04_ctl00_ButtonImg").is_displayed()
        # Verify refresh button
        assert driver.find_element_by_name("ReportViewerControl$ctl05$ctl05$ctl00$ctl00$ctl00").is_displayed()
        # Verify export to data feed button
        assert driver.find_element_by_name("ReportViewerControl$ctl05$ctl07$ctl00$ctl00$ctl00").is_displayed()
        # Verify report content
        act = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        time.sleep(1)
        exp_content = ['Out Of Stock Report',
                       'Customer Number',
                       'SKU', ' Description',
                       'Held Short',
                       'Qty. on Order',
                       'Next Delivery Date']
        for v in exp_content:
            assert v in act

    # ==============================C238===========3rd dec================================================================

    def test_Verify_content_of_generated_report_Inventory_on_Hand_tab_C238(self, impersonate_external):
        # Verify the content of generated report Inventory on Hand tab.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory on Hand tab.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'fa-folder-open-o')))
        ioh = driver.find_elements_by_class_name('fa-folder-open-o')
        ioh[1].click()
        time.sleep(1)
        # Report: Inventory on Hand (Title) top left side of the page.
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Inventory_On_Hand_Report = "Inventory on Hand Report"
        actual_header_Inventory_On_Hand_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_On_Hand_Report in expected_header_Inventory_On_Hand_Report
        # Click on Generate Report button.
        driver.find_element_by_class_name("btn-success").click()
        # Report should be generated successfully on the same page.
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerControl_ctl05_ctl00_First_ctl01_ctl00')))
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)

        # Verify the first page
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_First_ctl01_ctl00").is_displayed()
        # Verify the Previous page
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Previous_ctl01_ctl00").is_displayed()
        # Verify the current page text box
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_displayed()
        # Verify the  Total Pages
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()
        # Verify the next Pages
        if driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Next_ctl01").is_displayed():
            assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Next_ctl01").is_displayed()
        else:
            assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Next_ctl00").is_displayed()
        # Verify the last Pages link
        if driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Last_ctl00").is_displayed():
            assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Last_ctl00").is_displayed()
        else:
            assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Last_ctl01").is_displayed()
        # Verify search text box
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl00").is_displayed()
        # Verify find link
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl01").is_displayed()
        # Verify find next link
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl03").is_displayed()
        # Verify export button
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl04_ctl00_ButtonImg").is_displayed()
        # Verify refresh button
        assert driver.find_element_by_name("ReportViewerControl$ctl05$ctl05$ctl00$ctl00$ctl00").is_displayed()
        # Verify export to data feed button
        assert driver.find_element_by_name("ReportViewerControl$ctl05$ctl07$ctl00$ctl00$ctl00").is_displayed()
        # Verify report content
        act = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        exp_content = ['Inventory On Hand Report',
                       'SKU', 'Description',
                       'On Hand',
                       'On Sales',
                       'Net Qty', 'On Order', 'Future Net Stock', 'Next Delivery Date']
        for v in exp_content:
            assert v in act

    # ==================================04 December==============================================
    # ==================================270==============================================

    def test_ExternalVerifyContentsInReportsOrderProcessingByKeycode_C270(self, impersonate_external):
        # Verify the content in Reports/Orders/Order Processing by Keycode page.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        time.sleep(1)
        # Click on Operations tab.
        Operations = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        Operations.click()
        time.sleep(1)
        # Click on Orders tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Orders')))
        time.sleep(1)
        order_linktext = driver.find_elements_by_link_text("Orders")
        order_linktext[1].click()
        # Click on Open Orders by Business Unit
        odr = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Order Processing by Keycode')))
        odr.click()
        # Verify content in Open Orders by Business Unit page.
        # Open Orders by Business Unit Report(heading)
        expected_report_heading = "Order Processing by Keycode"
        Order_Processing_by_Keycode = wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_report_heading = Order_Processing_by_Keycode.text
        assert expected_report_heading in actual_report_heading
        # Report: Order Processing by Keycode(Label)
        expected_report_label = "Report: Order Processing by Keycode"
        actual_report_label = driver.find_element_by_id("criteria").text
        assert expected_report_label in actual_report_label
        # Make a subscription.(button) is displayed
        assert driver.find_element_by_class_name("btn-primary").is_displayed()
        # Client Name(button/dropdown) is displayed
        exp_tag = "select"
        actual_tag = driver.find_element_by_id("Client").tag_name
        assert exp_tag in actual_tag
        # Date field - from and to (Calendar) is displayed
        assert driver.find_element_by_name("daterange").is_displayed()
        # Key Code(text field) is displayed
        assert driver.find_element_by_id("KeyCode").is_displayed()
        # Business Units(button/dropdown) is displayed
        exp_tag = "select"
        actual_tag = driver.find_element_by_id("BU").tag_name
        assert exp_tag in actual_tag
        # Generate Report (button) is displayed
        assert driver.find_element_by_id("sub_btn").is_displayed()

    # ==================================277==============================================
    def test_ExternalVerifyMakeSubscriptionButtonInOrderProcessingByKeycode_C277(self, impersonate_external):
        # Verify the make a subscription button functionality in Reports/Orders/Order Processing by Keycode page.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(3)
        # Click on Orders tab.
        order_tab = driver.find_elements_by_link_text("Orders")
        order_tab[1].click()
        # Click on Order Processing by Keycode tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Order Processing by Keycode')))
        time.sleep(1)
        driver.find_element_by_link_text("Order Processing by Keycode").click()
        # Report: Order Processing by Keycode(Label) is displayed
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        # Click on make a subscription button.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()

        wait.until(EC.visibility_of_element_located((By.ID,'myModal')))
        assert driver.find_element_by_id("myModal").is_displayed()

        driver.find_element_by_class_name("btn-default").click()
        time.sleep(1)

    # ==================================280==============================================
    def test_ExternalVerifyContentInSubscriptionForARPMPopupOrderProcessingByKeycode_C280(self, impersonate_external):
        # Verify the content in Subscription for: Order Processing by Keycode Report for ARPM pop up
        # in Reports/Orders/Order Processing by Keycode page.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(3)
        # Click on Orders tab.
        order_tab = driver.find_elements_by_link_text("Orders")
        order_tab[1].click()
        # Click on Order Processing by Keycode tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Order Processing by Keycode')))
        time.sleep(1)
        driver.find_element_by_link_text("Order Processing by Keycode").click()
        # Report: Order Processing by Keycode(Label) is displayed
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        time.sleep(1)
        expected_panel_heading = "Report: Order Processing by Keycode"
        actual_panel_heading = driver.find_element_by_class_name("panel-heading").text
        assert expected_panel_heading in actual_panel_heading
        # Make a subscription.(button) is displayed
        assert driver.find_element_by_class_name("btn-primary").is_displayed()
        # Click on make a subscription button.
        driver.find_element_by_class_name("btn-primary").click()
        wait.until(EC.visibility_of_element_located((By.ID,'email')))
        # Subscription for: Order Processing by Keycode Report for ARPM(label)
        assert driver.find_element_by_class_name("modal-header").is_displayed()
        # Verify Subscription Name:(textfield)
        assert driver.find_element_by_id("sub_name").is_displayed()
        # Verify Email To: (textfield)
        assert driver.find_element_by_id("email").is_displayed()
        # Verify  Delivery Format:(text)
        expected_delivery_text = "Delivery Format:"
        actual_delivery_text = driver.find_element_by_id("form_modal").text
        assert expected_delivery_text in actual_delivery_text
        # Excel(radiobutton)
        assert driver.find_element_by_class_name("radio").is_displayed()
        # Verify time
        assert driver.find_element_by_id("time").is_displayed()
        # Verify Receive report on:(text)
        actual_receiver_report_text = driver.find_element_by_id("form_modal").text
        expected_receiver_report_text = "Receive report on:"
        assert expected_receiver_report_text in actual_receiver_report_text
        # Verify all day of week check box
        for chkbox in driver.find_elements_by_class_name("checkbox"):
            chkbox.is_displayed()
        # Verify back button
        assert driver.find_element_by_class_name("btn-default").is_displayed()
        # Verify save Subscription button
        assert driver.find_element_by_id("next_btn").is_displayed()
        # click back
        driver.find_element_by_class_name("btn-default").click()
        time.sleep(1)

    # =========================C231==4th Dec=================================================
    def test_External_Verify_content_in_Open_Orders_by_Business_Unit_Page_C231(self, impersonate_external):
        # Verify content in Open Orders by Business Unit
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Orders tab.
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Orders").click()
        time.sleep(3)
        # Click on Open Orders by Business Unit.
        driver.find_element_by_id("operations-orders-report-items").find_element_by_link_text("Open Orders by Business Unit").click()
        # Verify  header for "Open Orders by Business Unit Report"
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        time.sleep(1)
        expected_header_Open_Orders_Business_Report = "Open Orders by Business Unit Report"
        actual_header_Open_Orders_Business_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Open_Orders_Business_Report in expected_header_Open_Orders_Business_Report

        # Verify make subscription button
        assert driver.find_element_by_class_name("btn-primary").is_displayed()
        # Verify Business Units
        assert driver.find_element_by_id("BU").is_displayed()
        # Verify Generate report button is displayed
        assert driver.find_element_by_id("sub_btn").is_displayed()

    # =========================C236=======4th Dec===========================================
    def test_External_Verify_contents_in_Subscription_form_Open_Orders_Business_C236(self, impersonate_external):
        # Verify contents in Subscription form for Open Orders Business
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Orders").click()
        time.sleep(4)
        # Click on Open Orders by Business Unit.
        driver.find_element_by_id("operations-orders-report-items").find_element_by_link_text("Open Orders by Business Unit").click()
        # Click Subscription
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()
        # Verify from header
        wait.until(EC.visibility_of_element_located((By.ID,'email')))
        expected_header_Open_Orders_Business_Report_ARPM = "Subscription for: Open Orders by Business Report for ARPM"
        actual_header_Open_Orders_Business_Report_ARPM = driver.find_element_by_class_name("modal-title").text
        assert actual_header_Open_Orders_Business_Report_ARPM in expected_header_Open_Orders_Business_Report_ARPM
        # Verify Subscription Name
        time.sleep(1)
        assert driver.find_element_by_id("sub_name").is_displayed()
        # Verify Email to field
        assert driver.find_element_by_id("email").is_displayed()
        # Verify  Delivery format in excel
        assert driver.find_element_by_class_name("radio").is_displayed()
        # Verify time
        assert driver.find_element_by_id("time").is_displayed()
        # Verify receive report day
        assert driver.find_element_by_id("modal_selector").is_displayed()
        actual_week_day = driver.find_element_by_id("modal_selector").is_displayed()
        # Verify all day of week check box
        for tr in driver.find_elements_by_id("modal_selector"):
            ths = tr.find_elements_by_name("days_of_week")
            if ths: actual_weekday = [th.text for th in ths]
            exp_weekday = ("Sunday", "Monday", "Tuesday", "Thursday", "Friday", "Saturday")
            size = len(exp_weekday)
            for i in range(size):
                assert actual_weekday[i] in exp_weekday[i]

        # Verify back button
        assert driver.find_element_by_class_name("btn-default").is_displayed()
        # Verify save Subscription button
        assert driver.find_element_by_id("next_btn").is_displayed()

    # ======================C271================4Dec=============================================================

    def test_External_Verify_back_button_functionality_for_Open_Orders_Business_C271(self, impersonate_external):
        # Verify back button functionality for Open Orders Business Unit
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Orders").click()
        time.sleep(1)
        # Click on Out of stock tab.
        driver.find_element_by_id("operations-orders-report-items").find_element_by_link_text("Open Orders by Business Unit").click()
        # Subscriptions
        driver.find_element_by_class_name("btn-primary").click()
        wait.until(EC.visibility_of_element_located((By.ID,'email')))
        time.sleep(1)
        # Verify from header
        expected_header_Open_Orders_Business_Report_ARPM = "Subscription for: Open Orders by Business Report for ARPM"
        actual_header_Open_Orders_Business_Report_ARPM = driver.find_element_by_class_name("modal-title").text
        assert actual_header_Open_Orders_Business_Report_ARPM in expected_header_Open_Orders_Business_Report_ARPM
        # Entering valid data in form
        # Enter Subscription Name
        driver.find_element_by_id("sub_name").send_keys("Damco123")
        # Enter Email to field
        driver.find_element_by_id("email").send_keys("apriest@ggoutfitters.com")
        # Verify  Delivery format in excel
        driver.find_element_by_class_name("radio").is_displayed()
        # Verify time is displayed
        assert driver.find_element_by_id("time").is_displayed()
        # Verify receive report day
        assert driver.find_element_by_id("modal_selector").is_displayed()
        # Select receive report day
        driver.find_element_by_id("modal_selector").click()
        # Click on back button so that subscription should not saved
        driver.find_element_by_class_name("btn-default").click()
        # Verify we are on "Open Orders by Business Unit Report" page
        expected_header_Open_Orders_Business_Report = "Open Orders by Business Unit Report"
        actual_header_Open_Orders_Business_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Open_Orders_Business_Report in expected_header_Open_Orders_Business_Report

    # ==================================07 December==============================================
    # ==================================289==============================================
    def test_ExternalVerifyDateTimeOfGeneratedReportsInventoryReceipts_C289(self, impersonate_external):
        # Verify Date and Time of generated report.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory Receipts.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory Receipts')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Inventory Receipts").click()
        # Verify Inventory Receipts Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Inventory_Receipts_Report = "Inventory Receipts Report "
        actual_header_Inventory_Receipts_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_Receipts_Report in expected_header_Inventory_Receipts_Report
        time.sleep(1)
        # Select the Start and end date
        wait.until(EC.visibility_of_element_located((By.NAME,'daterange')))
        driver.find_element_by_name("daterange").click()
        time.sleep(1)

        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("02/22/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("02/24/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)

        # Report
        driver.find_element_by_class_name("btn-success").click()
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        # Verify the Date and Time of the generated report
        actual_dateTime = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        exp_dateTime = "Report Created on"
        exp_dateTime1 = "AM"
        exp_dateTime2 = "PM"
        exp_dateTime3 = ":"
        assert exp_dateTime in actual_dateTime
        assert ((exp_dateTime1 in actual_dateTime) | (exp_dateTime2 in actual_dateTime)) & (exp_dateTime3 in actual_dateTime)


    # ==================================291==============================================
    def test_ExternalVerifyContentOfSubscriptionForReportsInventoryReceipts_C291(self, impersonate_external):
        # Verify the content of Subscription for: Inventory Receipts Report for ARPM from.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory Receipts tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory Receipts')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Inventory Receipts").click()
        time.sleep(1)
        # Verify Inventory Receipts Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        # Subscription
        driver.find_element_by_class_name("btn-primary").click()
        time.sleep(1)
        # Verify Subscription Name
        driver.find_element_by_id("sub_name").is_displayed()
        # Verify Email to field
        driver.find_element_by_id("email").is_displayed()
        # Verify Delivery format in excel
        driver.find_element_by_class_name("radio").is_displayed()
        # Verify time
        driver.find_element_by_id("time").is_displayed()
        # Verify receive report day
        driver.find_element_by_id("modal_selector").is_displayed()
        expected_days = ['Sunday',
                         'Monday',
                         'Tuesday',
                         'Wednesday',
                         'Thursday',
                         'Friday',
                         'Saturday']
        actual_days = driver.find_elements_by_class_name("checkbox")
        for day in actual_days:
            name = day.text
            assert name in expected_days
        # Verify back button
        driver.find_element_by_class_name("btn-default").is_displayed()
        # Verify save Subscription button
        driver.find_element_by_id("next_btn").is_displayed()
        driver.find_element_by_class_name("btn-default").click()
        time.sleep(1)

    # ==================================681==============================================
    def test_ExternalVerifyRefreshFunctionalityForReportsInventoryReceipts_C681(self, impersonate_external):
        # Verify refresh button functionality in the report
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        # Click on Inventory Receipts.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory Receipts')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Inventory Receipts").click()
        # Verify Inventory Receipts Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Inventory_Receipts_Report = "Inventory Receipts Report "
        actual_header_Inventory_Receipts_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_Receipts_Report in expected_header_Inventory_Receipts_Report
        po_number = "123"
        time.sleep(1)
        # Verify Inventory Receipts Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        time.sleep(1)

        # Select the Start and end date
        wait.until(EC.visibility_of_element_located((By.NAME,'daterange')))
        driver.find_element_by_name("daterange").click()
        time.sleep(1)

        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("02/22/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("02/24/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)
        #Gen Report
        driver.find_element_by_class_name("btn-success").click()
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        # Generated report should be refreshed.
        original_text = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").is_displayed()
        driver.find_element_by_name("ReportViewerControl$ctl05$ctl05$ctl00$ctl00$ctl00").click()
        time.sleep(5)
        latest_text = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        assert (original_text is not latest_text)
    # =========================================C293=================7th Dec=============================================
    def test_External_Verify_EmailId_display_in_subscription_form_C293(self, impersonate_external):
        # Verify user Email Id display by default in subscription form
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        # Click on Inventory Receipts tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory Receipts')))
        time.sleep(1)
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Inventory Receipts").click()
        time.sleep(1)
        # Verify Inventory Receipts Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Inventory_Receipts_Report = "Inventory Receipts Report "
        actual_header_Inventory_Receipts_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_Receipts_Report in expected_header_Inventory_Receipts_Report
        # Click on make a Subscription button
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()

        # Verify form header
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        expected_header_Inventory_Receipts_Report_ARPM = "Subscription for: Inventory Receipts Report for ARPM"
        actual_header_Inventory_Receipts_Report_ARPM = driver.find_element_by_class_name("modal-title").text
        assert actual_header_Inventory_Receipts_Report_ARPM in expected_header_Inventory_Receipts_Report_ARPM

        # Verify Email id for "clipford@ggoutfitters.com"
        assert driver.find_element_by_id("email").is_displayed()
        expected_email = "clipford@ggoutfitters.com"
        actual_email = driver.find_element_by_id("email").get_attribute("value")
        assert actual_email in expected_email
        driver.find_element_by_class_name("btn-default").click()
        time.sleep(1)

    # ===============================C294=================7th Dec=====================================
    def test_External_Verify_Back_button_Subscription_Inventory_Receipts_C294(self, impersonate_external):
        # Verify Back button functionality on Subscription for: Inventory Receipts
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory Receipts tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory Receipts')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Inventory Receipts").click()
        time.sleep(1)
        # Verify Inventory Receipts Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        # Click on make a Subscription button
        driver.find_element_by_class_name("btn-primary").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        # Verify form header
        expected_header_Inventory_Receipts_Report_ARPM = "Subscription for: Inventory Receipts Report for ARPM"
        actual_header_Inventory_Receipts_Report_ARPM = driver.find_element_by_class_name("modal-title").text
        assert actual_header_Inventory_Receipts_Report_ARPM in expected_header_Inventory_Receipts_Report_ARPM
        # Click on back button
        driver.find_element_by_class_name("btn-default").click()
        time.sleep(1)
        # Verify Inventory Receipts Report page
        expected_header_Inventory_Receipts_Report = "Inventory Receipts Report "
        actual_header_Inventory_Receipts_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_Receipts_Report in expected_header_Inventory_Receipts_Report

    # ===========================C295=================7th Dec=============================
    def test_External_Verify_in_SubscriptionName_textbox_only_letters_and_numbers_allowed_for_Inventory_Receipts_C295(self, impersonate_external):
        # Verify in "Subscription Name" text box only letters and numbers are allowed for: Inventory Receipts
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory Receipts tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory Receipts')))
        time.sleep(1)
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Inventory Receipts").click()
        time.sleep(1)
        # Verify Inventory Receipts Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))

        # Click on make a Subscription button
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        # Verify form header
        expected_header_Inventory_Receipts_Report_ARPM = "Subscription for: Inventory Receipts Report for ARPM"
        actual_header_Inventory_Receipts_Report_ARPM = driver.find_element_by_class_name("modal-title").text
        assert actual_header_Inventory_Receipts_Report_ARPM in expected_header_Inventory_Receipts_Report_ARPM
        # Verify Subscription Name
        driver.find_element_by_id("sub_name").send_keys("Test123")
        # Verify time
        driver.find_element_by_id("time").is_displayed()
        # Verify receive report day
        driver.find_element_by_id("modal_selector").is_displayed()
        # Select day of week
        driver.find_element_by_name("days_of_week").click()
        # Click on save Subscription button
        driver.find_element_by_id("next_btn").click()
        time.sleep(1)
        # Click again on make a subscription button
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        # Enter symbol in text user name text field
        driver.find_element_by_id("sub_name").send_keys("*#@")
        # Verify time
        driver.find_element_by_id("time").is_displayed()
        # Verify error message "Only use letters and numbers." on clicking Save
        driver.find_element_by_id("next_btn").click()
        time.sleep(1)
        expected_error_message = "Only use letters and numbers."
        actual_error_message = driver.find_element_by_id("sub_name").get_attribute("title")
        assert actual_error_message in expected_error_message
        # click back
        driver.find_element_by_class_name("btn-default").click()
        time.sleep(1)

    # ================================08 Dec===================================================================
    # ==================================163====================================================================

    def test_ExternalVerifyContentOnSubscriptionForInventoryReportForARPMForm_C163(self, impersonate_external):
        # Verify the content on Subscription for Inventory Report for ARPM form.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # wait for Inventory Receipts tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory Receipts')))
        # Click on Inventory on Hand tab.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'fa-folder-open-o')))
        time.sleep(1)
        ioh = driver.find_elements_by_class_name('fa-folder-open-o')
        ioh[1].click()
        time.sleep(1)
        # Report: Inventory on Hand (Title) top left side of the page.
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header = "Inventory on Hand Report"
        actual_header = driver.find_element_by_id("content-header").text
        assert expected_header in actual_header
        #Subscription
        driver.find_element_by_class_name("btn-primary").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        time.sleep(1)
        # Verify Subscription Name
        driver.find_element_by_id("sub_name").is_displayed()
        # Verify Email to field
        driver.find_element_by_id("email").is_displayed()
        # Verify Delivery format in excel
        driver.find_element_by_class_name("radio").is_displayed()
        # Verify time
        driver.find_element_by_id("time").is_displayed()
        # Verify receive report day
        driver.find_element_by_id("modal_selector").is_displayed()
        expected_days = ['Sunday',
                         'Monday',
                         'Tuesday',
                         'Wednesday',
                         'Thursday',
                         'Friday',
                         'Saturday']
        actual_days = driver.find_elements_by_class_name("checkbox")
        for day in actual_days:
            name = day.text
            assert name in expected_days
        # Verify save Subscription button
        driver.find_element_by_id("next_btn").is_displayed()
        time.sleep(1)
        # Verify back button
        driver.find_element_by_class_name("btn-default").is_displayed()
        driver.find_element_by_class_name("btn-default").click()
        time.sleep(1)

    # ================================156=====================================================================

    def test_ExternalVerifyDateTimeInGeneratedReportInventoryOnHandPage_C156(self, impersonate_external):
        # Verify the generated report Date and Time in the report Inventory on Hand page.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory on Hand tab.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'fa-folder-open-o')))
        time.sleep(1)
        ioh = driver.find_elements_by_class_name('fa-folder-open-o')
        ioh[1].click()
        time.sleep(1)
        # Report: Inventory on Hand (Title) top left side of the page.
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        # Generate Report
        driver.find_element_by_class_name("btn-success").click()
        time.sleep(1)
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        # Verify the Date and Time of the generated report
        actual_dateTime = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        exp_dateTime = "Report Created On"
        exp_dateTime1 = "AM"
        exp_dateTime2 = "PM"
        exp_dateTime3 = ":"
        assert exp_dateTime in actual_dateTime
        assert ((exp_dateTime1 in actual_dateTime) | (exp_dateTime2 in actual_dateTime)) & (exp_dateTime3 in actual_dateTime)

    # ===========================================147====================================================
    def test_ExternalVerifyContentsOnUserProfileDashboardPage_C147(self, impersonate_external):
        # Verify the contents on User profile Dashboard page.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        #  These are the widgets that we expect to find
        expected_widgets = [
            'Orders Shipped by Business Unit',
            'New Orders by Business Unit',
            'Performance by Campaign',
            'Items on Backorder',
            'Highest Performing SKU\'s',
            'Yesterday\'s Shipments'
        ]
        # Click on Dashboard
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Dashboard')))
        driver.find_element_by_link_text('Dashboard').click()
        #  First, collect all the widgets on the page
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'widget')))
        time.sleep(3)
        widgets = driver.find_elements_by_class_name('widget')
        time.sleep(1)
        #  We can now verify that we have the expected number of widgets on the page:
        assert len(expected_widgets) == len(widgets)

        #  Now verify that all the widgets we expect to see are in our found widgets.
        #  We should find our expected widget titles in the widgets we collected from the page:
        widget_titles = [w.find_element_by_class_name('panel-heading').text for w in widgets]
        time.sleep(1)
        for title in expected_widgets:
            assert title in widget_titles

        # Last 90days default (dropdown)
        dropdowns = driver.find_elements_by_class_name("timeframe-select")
        time.sleep(1)
        tagName = "select"
        for dd in dropdowns:
            assert dd.tag_name in tagName
        time.sleep(1)
        # Direct Mail (dropdown)
        direct_mail = driver.find_element_by_class_name("bu-select").tag_name
        time.sleep(1)
        assert direct_mail in tagName

        performance_by_campaign = widgets[2].text
        items_on_backorder = widgets[3].text
        highest_performing_sku = widgets[4].text

        header1_performance_by_campaign = "Campaign"
        header2_performance_by_campaign = "Number of Orders"
        assert header1_performance_by_campaign in performance_by_campaign
        assert header2_performance_by_campaign in performance_by_campaign

        # Verify contents in Items on Backorder
        header1_items_on_backorder = "SKU"
        header2_items_on_backorder = "Description"
        header3_items_on_backorder = "Qty on Backorder"
        header4_items_on_backorder = "Days Out of Stock"
        assert header1_items_on_backorder in items_on_backorder
        assert header2_items_on_backorder in items_on_backorder
        assert header3_items_on_backorder in items_on_backorder
        assert header4_items_on_backorder in items_on_backorder
        # Verify contents in Highest Performing SKU
        header1_highest_performing_sku = "SKU"
        header2_highest_performing_sku = "Description"
        header3_highest_performing_sku = "Qty in Stock"
        header4_highest_performing_sku = "Qty Shipped"
        assert header1_highest_performing_sku in highest_performing_sku
        assert header2_highest_performing_sku in highest_performing_sku
        assert header3_highest_performing_sku in highest_performing_sku
        assert header4_highest_performing_sku in highest_performing_sku

        # Yesterday Shipments(Google Map)
        assert driver.find_element_by_class_name("gmnoprint").is_displayed()

        # Verify Graph
        graphs = driver.find_elements_by_class_name("dash-size")
        time.sleep(1)
        for g in graphs:
            assert g.is_displayed()
        time.sleep(1)
    # ===============09 Dec==============================================================
    # ==================================302==============================================

    def test_ExternalVerifyDeleteButtonFunctionalityOnSubscription_C302(self, impersonate_external):
        # To verify the Delete button functionality on Subscriptions page.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Orders tab.
        order_tab = driver.find_elements_by_link_text("Orders")
        order_tab[1].click()
        # Click on Order Processing by Keycode tab.
        time.sleep(1)
        driver.find_element_by_link_text("Order Processing by Keycode").click()
        # Report: Order Processing by Keycode(Label) is displayed
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        time.sleep(1)
        expected_panel_heading = "Report: Order Processing by Keycode"
        actual_panel_heading = driver.find_element_by_class_name("panel-heading").text
        assert expected_panel_heading in actual_panel_heading

        # Click on Make a Subscription button.
        driver.find_element_by_class_name("btn-primary").click()
        wait.until(EC.visibility_of_element_located((By.ID,'email')))
        random_number = str(randint(10, 999))
        name = "TestSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"

        driver.find_element_by_id("email").send_keys(email)
        driver.find_element_by_id("next_btn").click()
        time.sleep(3)
        # Select subscriptions.
        driver.find_element_by_link_text("Subscriptions").click()
        time.sleep(1)
        before_number_of_delete = driver.find_elements_by_link_text("Delete")
        # Select any subscription and click on delete button.
        driver.find_element_by_link_text("Delete").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'btn-danger')))
        driver.find_element_by_class_name("btn-danger").click()
        time.sleep(1)
        after_number_of_delete = driver.find_elements_by_link_text("Delete")
        # Subscription should be deleted
        assert before_number_of_delete != after_number_of_delete


    # ================================283=====================================================================
    def test_ExternalVerifyGenerateReportButtonFunctionalityInOrderProcessingByKeycodePage_C283(self,impersonate_external):
        # Verify the generate report button functionality in Reports/Orders/Order Processing by Keycode page.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Orders tab.
        order_tab = driver.find_elements_by_link_text("Orders")
        order_tab[1].click()
        # Click on Order Processing by Keycode tab.
        time.sleep(1)
        driver.find_element_by_link_text("Order Processing by Keycode").click()
        # Report: Order Processing by Keycode(Label) is displayed
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))

        time.sleep(1)
        expected_panel_heading = "Report: Order Processing by Keycode"
        actual_panel_heading = driver.find_element_by_class_name("panel-heading").text
        assert expected_panel_heading in actual_panel_heading

        # Report: Order Processing by Keycode(Label) is displayed
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        time.sleep(1)

        # Enter data in Client Name , date , Key Code and Business Units
        keycode = "abc123"
        driver.find_element_by_id("KeyCode").send_keys(keycode)
        driver.find_element_by_id("KeyCode").clear()
        bu_select = driver.find_element_by_id("BU")
        business_unit = "All"
        for option in bu_select.find_elements_by_tag_name('option'):
            if option.text == business_unit:
                option.click()
                break
        # Select Dates
        wait.until(EC.visibility_of_element_located((By.NAME,'daterange')))
        driver.find_element_by_name("daterange").click()
        time.sleep(1)
        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("02/22/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("02/24/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)

        # Generate Report
        driver.find_element_by_class_name("btn-success").click()
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)

    # ===========================================282====================================================
    def test_ExternalVerifyBackButtonFunctionality_C282(self, impersonate_external):
        # Verify the back button functionality in Subscription  for: Order Processing by Keycode Report
        # for ARPM pop up  in Reports/Orders/Order Processing by Keycode page.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)

        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Orders tab.
        order_tab = driver.find_elements_by_link_text("Orders")
        order_tab[1].click()
        # Click on Order Processing by Keycode tab.
        time.sleep(1)
        driver.find_element_by_link_text("Order Processing by Keycode").click()
        # Report: Order Processing by Keycode(Label) is displayed
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        time.sleep(1)
        expected_panel_heading = "Report: Order Processing by Keycode"
        actual_panel_heading = driver.find_element_by_class_name("panel-heading").text
        assert expected_panel_heading in actual_panel_heading

        # Click on Make a Subscription button.
        driver.find_element_by_class_name("btn-primary").click()
        wait.until(EC.visibility_of_element_located((By.ID,'email')))
        time.sleep(1)
        assert driver.find_element_by_class_name("modal-header").is_displayed()
        random_number = str(randint(10, 999))
        name = "TestSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"

        driver.find_element_by_id("email").send_keys(email)
        driver.find_element_by_name("days_of_week").click()
        # Cancel
        driver.find_element_by_class_name("btn-default").click()
        time.sleep(1)
        # Subscription for: Order Processing by Keycode Report for ARPM pop up should be closed.
        driver.find_element_by_link_text("Subscriptions").click()
        wait.until(EC.visibility_of_element_located((By.ID,'jobs_table')))
        time.sleep(1)
        # Subscription should not be display in subscriptions page with correct data
        sNameNew_value = driver.find_element_by_id("jobs_table").text
        time.sleep(1)
        assert name not in sNameNew_value


    # ==================================281======================================================
    def test_ExternalVerifySaveSubscriptionFunctionality_C281(self, impersonate_external):
        # Verify the save Subscription functionality in Subscription  for: Order Processing by Keycode Report
        # for ARPM pop up  in Reports/Orders/Order Processing by Keycode page.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Orders tab.
        order_tab = driver.find_elements_by_link_text("Orders")
        order_tab[1].click()
        # Click on Order Processing by Keycode tab.
        time.sleep(1)
        driver.find_element_by_link_text("Order Processing by Keycode").click()
        # Report: Order Processing by Keycode(Label) is displayed
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        time.sleep(1)
        expected_panel_heading = "Report: Order Processing by Keycode"
        actual_panel_heading = driver.find_element_by_class_name("panel-heading").text
        assert expected_panel_heading in actual_panel_heading

        # Click on Make a Subscription button.
        driver.find_element_by_class_name("btn-primary").click()
        wait.until(EC.visibility_of_element_located((By.ID,'email')))
        assert driver.find_element_by_class_name("modal-header").is_displayed()
        random_number = str(randint(10, 999))
        name = "TestSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"

        driver.find_element_by_id("email").send_keys(email)
        driver.find_element_by_name("days_of_week").click()
        # Save
        driver.find_element_by_id("next_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'noty_text')))
        # "Subscription saved" message should be displayed.
        assert driver.find_element_by_class_name("noty_text").is_displayed()
        assert driver.find_element_by_name("daterange").is_displayed()
        # Order Processing by Keycode Report page should be displayed.
        assert driver.find_element_by_id("sub_btn").is_displayed()
        # Subscription should be display in subscriptions page with correct data.
        driver.find_element_by_link_text("Subscriptions").click()
        time.sleep(1)
        NameNew_value = driver.find_element_by_id("jobs_table").text
        assert name in NameNew_value

    # ==============================C251=====9th Dec===================================================

    def test_External_Verify_selected_Business_Unit__report_Open_Orders_Business_Unit_C251(self,impersonate_external):
        # Verify the selected Business Unit in generated report for Open Orders by Business Unit
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Orders").click()
        time.sleep(1)
        # Click on Out of stock tab.
        driver.find_element_by_id("operations-orders-report-items").find_element_by_link_text("Open Orders by Business Unit").click()
        # Verify  header
        expected_header_Open_Orders_Business_Unit_Report = "Open Orders by Business Unit Report"
        actual_header_Open_Orders_Business_Unit_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Open_Orders_Business_Unit_Report in expected_header_Open_Orders_Business_Unit_Report
        # Select business unit drop down value
        select = Select(driver.find_element_by_id('BU'))
        # select by visible text 'Alt Media'
        select.select_by_visible_text('Alt Media')
        # Click on Generate Report button.
        driver.find_element_by_class_name("btn-success").click()
        # Report should be generated successfully on the same page.
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        # Verify report content
        act = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        actual = act.split('\n')
        exp_content = ['Alt Media']
        # Verify selected business 'Alt Media' is present in generated report
        for v in exp_content:
            assert v in actual

    # ============================C253===========================================9th Dec===========================

    def test_External_Verify_functionality_view_report_button_Open_Orders_Business_Unit_C253(self,impersonate_external):
        # Verify functionality of view report button for Open Orders by Business Unit
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Orders tab. fa-folder-open-o
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'fa-folder-open-o')))
        orders = driver.find_elements_by_link_text("Orders")
        orders[1].click()
        time.sleep(1)
        # Click on Open Orders by Business Unit
        driver.find_element_by_link_text("Open Orders by Business Unit").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        time.sleep(1)
        # Verify content in Open Orders by Business Unit page.
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_report_heading = "Open Orders by Business Unit Report"
        actual_report_heading = driver.find_element_by_id("content-header").text
        assert expected_report_heading in actual_report_heading

        # Click on Generate Report button.
        driver.find_element_by_class_name("btn-success").click()
        # Report should be generated successfully on the same page.
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        # Verify the first page
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_First_ctl01_ctl00").is_displayed()
        # Verify the Previous page
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Previous_ctl01_ctl00").is_displayed()
        # Verify the current page text box
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_displayed()
        # Verify the  Total Pages
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()
        # Verify the next Pages link ReportViewerControl_ctl05_ctl00_Next_ctl01_ctl00
        if driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Next_ctl01").is_displayed():
            assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Next_ctl01").is_displayed()
        else:
            assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Next_ctl00").is_displayed()
        # Verify the last Pages link ReportViewerControl_ctl05_ctl00_Last_ctl01_ctl00
        if driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Last_ctl00").is_displayed():
            assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Last_ctl00").is_displayed()
        else:
            assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Last_ctl01").is_displayed()

        # Verify search text box
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl00").is_displayed()
        # Verify find link
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl01").is_displayed()
        # Verify find next link
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl03").is_displayed()
        # Verify export button
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl04_ctl00_ButtonImg").is_displayed()
        # Verify refresh button
        assert driver.find_element_by_name("ReportViewerControl$ctl05$ctl05$ctl00$ctl00$ctl00").is_displayed()
        # Verify export to data feed button
        assert driver.find_element_by_name("ReportViewerControl$ctl05$ctl07$ctl00$ctl00$ctl00").is_displayed()


    # ============================C254======9th Dec=================================================================

    def test_External_Verify_content_in_generated_report_Open_Orders_Business_Unit_C254(self, impersonate_external):
        # Verify the content in generated report for Open Orders by Business Unit
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Orders tab. fa-folder-open-o
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'fa-folder-open-o')))
        orders = driver.find_elements_by_link_text("Orders")
        orders[1].click()
        time.sleep(1)
        # Click on Open Orders by Business Unit
        driver.find_element_by_link_text("Open Orders by Business Unit").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        time.sleep(1)
        # Verify content in Open Orders by Business Unit page.
        expected_report_heading = "Open Orders by Business Unit Report"
        actual_report_heading = driver.find_element_by_id("content-header").text
        assert expected_report_heading in actual_report_heading

        # Click on Generate Report button.
        driver.find_element_by_class_name("btn-success").click()
        # Report should be generated successfully on the same page.
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        # Verify report content
        tr = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        arr = tr.split('\n')
        exp_content = ['Open Orders by Business Unit','Premium', 'Description','Business Unit','Open Orders']

        # Verify selected business 'Alt Media' is present in generated report
        for i in range(len(exp_content)):
            assert exp_content[i] in arr

    # ===============================11 Dec===========================================
    # ==================================149==============================================

    def test_ExternalVerifyContentOfInventoryOnHandPage_C149(self, impersonate_external):
        # Verify the content of Inventory on Hand page in user report section.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory on Hand tab.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'fa-folder-open-o')))
        ioh = driver.find_elements_by_class_name('fa-folder-open-o')
        ioh[1].click()
        time.sleep(1)
        # Verify Inventory on Hand Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Inventory_On_Hand_Report = "Inventory on Hand Report"
        actual_header_Inventory_On_Hand_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_On_Hand_Report in expected_header_Inventory_On_Hand_Report
        # Drop down with prefilled client name like ARPM.
        wait.until(EC.visibility_of_element_located((By.ID, 'cClientName')))
        time.sleep(1)
        expected_dropdown = "ARPM"
        actual_dropdown = driver.find_element_by_id("cClientName").text
        assert expected_dropdown in actual_dropdown
        # Generate Report button.
        assert driver.find_element_by_id("sub_btn").is_displayed()
        # Make a Subscription button.
        assert driver.find_element_by_class_name("btn-primary").is_displayed()

    # ===========================================150====================================================
    def test_ExternalVerifyGenerateReportButtonFunctionality_C150(self, impersonate_external):
        # Verify Generate Report button functionality in Inventory on Hand page.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory on Hand tab.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'fa-folder-open-o')))
        ioh = driver.find_elements_by_class_name('fa-folder-open-o')
        ioh[1].click()
        time.sleep(1)
        # Verify Inventory on Hand Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Inventory_On_Hand_Report = "Inventory on Hand Report"
        actual_header_Inventory_On_Hand_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_On_Hand_Report in expected_header_Inventory_On_Hand_Report
        # Drop down with prefilled client name like ARPM.
        wait.until(EC.visibility_of_element_located((By.ID, 'cClientName')))
        # Click on Generate Report button.
        driver.find_element_by_id("sub_btn").click()
        # Report should be generated successfully on the same page.
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        assert driver.find_element_by_id("ReportViewerControl_fixedTable").is_displayed()

    # ===========================================151====================================================
    def test_ExternalVerifyShowingEntriesFunctionality_C151(self, impersonate_external):
        # Verify Showing 1 of xx entries functionality in report section in Inventory on Hand page.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory on Hand tab.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'fa-folder-open-o')))
        ioh = driver.find_elements_by_class_name('fa-folder-open-o')
        ioh[1].click()
        time.sleep(1)
        # Verify Inventory on Hand Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Inventory_On_Hand_Report = "Inventory on Hand Report"
        actual_header_Inventory_On_Hand_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_On_Hand_Report in expected_header_Inventory_On_Hand_Report
        # Drop down with prefilled client name like ARPM.
        wait.until(EC.visibility_of_element_located((By.ID, 'cClientName')))
        # Click on Generate Report button.
        driver.find_element_by_id("sub_btn").click()
        # Report should be generated successfully on the same page.
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        assert driver.find_element_by_id("ReportViewerControl_fixedTable").is_displayed()
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_displayed()

    # ============================C152======11th Dec=================================================================
    def test_External_Verify_pagination_functionality__in_report_for_Inventory_On_Hand_C152(self, impersonate_external):
        # Verify pagination functionality in Report for Inventory On Hand
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory on Hand tab.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'fa-folder-open-o')))
        ioh = driver.find_elements_by_class_name('fa-folder-open-o')
        ioh[1].click()
        time.sleep(1)
        # Verify Inventory on Hand Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Inventory_On_Hand_Report = "Inventory on Hand Report"
        actual_header_Inventory_On_Hand_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_On_Hand_Report in expected_header_Inventory_On_Hand_Report
        # Drop down with prefilled client name like ARPM.
        wait.until(EC.visibility_of_element_located((By.ID, 'cClientName')))
        # Click on Generate Report button.
        driver.find_element_by_id("sub_btn").click()
        # Report should be generated successfully on the same page.
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)

        # Verify the first page
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_First_ctl01_ctl00").is_displayed()

        tp = driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").text
        tps = tp.split(" ")
        tpcnt = tps[0]
        # If total pages are 1
        if int(tpcnt) == 1:
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_First_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Previous_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Next_ctl00').get_attribute("class") == "NormalButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Last_ctl00').get_attribute("class") == "NormalButton"

        # Check next page & previous if total pages > 1
        if int(tpcnt) > 1:
            # Click Last button and verify controls NormalButton
            driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Last_ctl00_ctl00').click()
            time.sleep(5)
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Next_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Last_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Previous_ctl00').get_attribute("class") == "NormalButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_First_ctl00').get_attribute("class") == "NormalButton"
            # Click on First button
            driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_First_ctl00_ctl00').click()
            time.sleep(10)
            # Check First,Last,Next,Prev state
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_First_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Previous_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Next_ctl00').get_attribute("class") == "NormalButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Last_ctl00').get_attribute("class") == "NormalButton"

    # ============================C153==============11th Dec==================================================================
    def test_External_Verify_Search_functionality_in_Report_for_Inventory_On_Hand_C153(self, impersonate_external):
        # Verify Search functionality in Report for Inventory On Hand
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory on Hand tab.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'fa-folder-open-o')))
        ioh = driver.find_elements_by_class_name('fa-folder-open-o')
        ioh[1].click()
        time.sleep(1)
        # Verify Inventory on Hand Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Inventory_On_Hand_Report = "Inventory on Hand Report"
        actual_header_Inventory_On_Hand_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_On_Hand_Report in expected_header_Inventory_On_Hand_Report
        # Drop down with prefilled client name like ARPM.
        wait.until(EC.visibility_of_element_located((By.ID, 'cClientName')))

        # Click on Generate Report button.
        driver.find_element_by_id("sub_btn").click()
        # Report should be generated successfully on the same page.
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)

        # enter SKU no- AARPBD060
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl00").send_keys("AARPBD060")
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl01").click()
        time.sleep(10)
        try:
            alert = driver.switch_to_alert()
            assert alert.text == "The search text was not found."
            alert.accept()
            alert_found = True
        except NoAlertPresentException as e:
            alert_found = False

        if alert_found == False:
            driver.find_element_by_css_selector("span[style='COLOR:highlighttext;BACKGROUND-COLOR:highlight;']").is_displayed()

        # Verify wrong entry could not be searched
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl00").send_keys("test12345")
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl01").click()

        try:
            WebDriverWait(driver, 15).until(EC.alert_is_present(), 'The search text was not found.')
            alert = driver.switch_to_alert()
            assert alert.text == "The search text was not found."
            alert.accept()
            alert_found3 = True
        except NoAlertPresentException as e:
            alert_found3 = False

    # ===================C154==============================11th Dec=================================================

    def test_External_Verify_Export_button_functionality_report_Inventory_On_Hand_C154(self,impersonate_external):
        # Verify Export button functionality in the report for Inventory On Hand
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory on Hand tab.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'fa-folder-open-o')))
        ioh = driver.find_elements_by_class_name('fa-folder-open-o')
        ioh[1].click()
        time.sleep(1)
        # Verify Inventory on Hand Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Inventory_On_Hand_Report = "Inventory on Hand Report"
        actual_header_Inventory_On_Hand_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_On_Hand_Report in expected_header_Inventory_On_Hand_Report
        # Drop down with prefilled client name like ARPM.
        wait.until(EC.visibility_of_element_located((By.ID, 'cClientName')))
        # Click on Generate Report button.
        driver.find_element_by_id("sub_btn").click()
        # Report should be generated successfully on the same page.
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_displayed()
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl04_ctl00_ButtonLink").click()
        time.sleep(5)
        # Verify report can be exported in following format
        assert driver.find_element_by_class_name("HoverButton").is_displayed()
        act = driver.find_elements_by_class_name("ActiveLink")
        exp_export_option = ['XML file with report data',
                             'CSV (comma delimited)',
                             'PDF',
                             'MHTML (web archive)',
                             'Excel',
                             'TIFF file',
                             'Word']
        for v in act:
            name = v.text
            assert name in exp_export_option

    # ===============================C155====11 Dec========================================

    def test_External_Verify_refresh_Button_for_Inventory_On_Hand_C155(self, impersonate_external):
        # Verify refresh button functionality in the report for Inventory On Hand
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory on Hand tab.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'fa-folder-open-o')))
        ioh = driver.find_elements_by_class_name('fa-folder-open-o')
        ioh[1].click()
        time.sleep(1)
        # Verify Inventory on Hand Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Inventory_On_Hand_Report = "Inventory on Hand Report"
        actual_header_Inventory_On_Hand_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_On_Hand_Report in expected_header_Inventory_On_Hand_Report
        # Drop down with prefilled client name like ARPM.
        wait.until(EC.visibility_of_element_located((By.ID, 'cClientName')))
        # Click on Generate Report button.
        driver.find_element_by_id("sub_btn").click()
        # Report should be generated successfully on the same page.
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)

        # Verify refresh button
        assert driver.find_element_by_name("ReportViewerControl$ctl05$ctl07$ctl00$ctl00$ctl00").is_displayed()
        driver.find_element_by_name("ReportViewerControl$ctl05$ctl07$ctl00$ctl00$ctl00").click()

    # =====================15 Dec================170===================================================================

    def test_ExternalVerifyResetFunctionality_C170(self, impersonate_external):
        # Verify the reset functionality in Orders/Orders Search page.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Check for Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Orders')))
        time.sleep(3)
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Order Search')))
        time.sleep(1)
        driver.find_element_by_link_text("Order Search").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        time.sleep(4)

        invoice_number = "ABC123"
        driver.find_element_by_id("invoice_nbr").send_keys(invoice_number)
        # Order Number
        orderid_number = "ABC123"
        driver.find_element_by_id("orderid").send_keys(orderid_number)
        # Select the Start and end date
        driver.find_element_by_name("submitted_start_date").click()
        time.sleep(1)
        days_start_date = driver.find_elements_by_class_name("day")
        start_date = "20"
        for i in range(len(days_start_date)):
            if (start_date in days_start_date[i].text):
                days_start_date[i].click()
                break
        driver.find_element_by_name("submitted_end_date").click()
        days_end_date = driver.find_elements_by_class_name("day")
        end_date = "25"
        for i in range(len(days_end_date)):
            if (end_date in days_end_date[i].text):
                days_end_date[i].click()
                break
        driver.find_element_by_id("reset").click()
        time.sleep(1)
        act_orderid = driver.find_element_by_id("orderid").get_attribute("value")
        act_invoice = driver.find_element_by_id("invoice_nbr").get_attribute("value")
        assert orderid_number is not act_orderid
        assert invoice_number is not act_invoice
        actEndDate = driver.find_element_by_name("submitted_end_date").get_attribute("value")
        actStartDate = driver.find_element_by_name("submitted_start_date").get_attribute("value")
        exp_StartDate = ""
        exp_EndDate = ""
        assert exp_StartDate == actStartDate
        assert exp_EndDate == actEndDate

    # ================================16 Dec====================================================================
    # ==================================C919====================================================================

    def test_ExternalVerifyBackButtonFunctionality_C919(self, impersonate_external):
        # Verify the Back button functionality on Subscription
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Check for Reports tab.
        # Open the 'Inventory by Business Unit' page and verify the page opened properly.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()

        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()

        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()

        # Click on 'Inventory by Business Unit' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Open Purchase Orders')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Inventory by Business Unit").click()

        # Verify 'Inventory by Business Unit' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header = "Inventory by Business Unit Report "
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header
        # Verify Radio Button
        wait.until(EC.visibility_of_element_located((By.ID, 'ProdClass')))
        radio_Buttons = driver.find_elements_by_id("ProdClass")
        for rb in radio_Buttons:
            assert rb.is_displayed()
        # Verify Business Unit Button/Dropdown
        assert driver.find_element_by_id("BU").is_displayed()
        # Click on Make a subscription button.
        driver.find_element_by_class_name("btn-primary").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal-content')))
        # Subscription for: Inventory by Business Unit Report for ARPM form should appear.
        exp_header = ['Subscription for:','Inventory by Business Unit Report for ARPM']
        act_header = driver.find_element_by_class_name("modal-content").text
        for eh in exp_header:
            assert eh in act_header
        # Click on Back button under Subscription for: Inventory by Business Unit Report for ARPM form.
        driver.back()
        time.sleep(1)
        driver.find_element_by_link_text("Dashboard").click()
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        time.sleep(1)
        actual_dashboard_header = driver.find_element_by_id("content-header").text
        expected_dashboard_header = "Fulfillment Dashboard"
        assert expected_dashboard_header in actual_dashboard_header

    # ==================================C927==============================================
    def test_ExternalVerifyRefreshButtonFunctionality_C927(self, impersonate_external):
        # Verify refresh button functionality
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Check for Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Operations
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory by Business Unit
        driver.find_element_by_link_text("Inventory by Business Unit").click()
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        time.sleep(1)
        # Verify Radio Button
        wait.until(EC.visibility_of_element_located((By.ID, 'ProdClass')))
        radio_Buttons = driver.find_elements_by_id("ProdClass")
        for rb in radio_Buttons:
            assert rb.is_displayed()
        # Verify Business Unit Button/Dropdown
        assert driver.find_element_by_id("BU").is_displayed()
        # Click on Generate report button.
        driver.find_element_by_id("sub_btn").click()
        # Verify the Date and Time of the generated report.
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        driver.find_element_by_name("ReportViewerControl$ctl05$ctl05$ctl00$ctl00$ctl00").click()
        time.sleep(3)
        assert driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").is_displayed()

    # ==================================C915==============================================
    def test_ExternalVerifyDateAndTimeFunctionality_C915(self, impersonate_external):
        # Verify Date and Time of generated report
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Check for Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Operations
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory by Business Unit
        driver.find_element_by_link_text("Inventory by Business Unit").click()
        time.sleep(1)
        # Verify Radio Button
        wait.until(EC.visibility_of_element_located((By.ID, 'ProdClass')))
        radio_Buttons = driver.find_elements_by_id("ProdClass")
        for rb in radio_Buttons:
            assert rb.is_displayed()
        # Verify Business Unit Button/Dropdown
        assert driver.find_element_by_id("BU").is_displayed()
        # Click on Generate report button.
        driver.find_element_by_id("sub_btn").click()
        # Verify the Date and Time of the generated report.
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        actual_dateTime = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        exp_dateTime = "Report Created On"
        exp_dateTime1 = "AM"
        exp_dateTime2 = "PM"
        exp_dateTime3 = ":"
        assert exp_dateTime in actual_dateTime
        assert ((exp_dateTime1 in actual_dateTime) | (exp_dateTime2 in actual_dateTime)) & (exp_dateTime3 in actual_dateTime)

    # =========================C306====16Dec========================================================================

    def test_ExternalVerifyContentsOnInventoryBusinessUnitReportPage_C306(self, impersonate_external):
        # Verify the contents on Inventory by Business Unit Report page.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Check for Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Operations
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory by Business Unit
        driver.find_element_by_link_text("Inventory by Business Unit").click()
        # Verify Inventory by Business Unit Report
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        time.sleep(1)
        expected_header_Inventory_by_Business_Unit = "Inventory by Business Unit Report"
        actual_header_Inventory_by_Business_Unit = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_by_Business_Unit in expected_header_Inventory_by_Business_Unit
        # Verify Business Units dropdown
        assert driver.find_element_by_id("BU").is_displayed()
        # Verify radio button
        assert driver.find_element_by_class_name("radio").is_displayed()
        #  Verify Product Class label
        assert driver.find_element_by_id("ProdClass").is_displayed()
        # Verify Generate report button
        assert driver.find_element_by_class_name("btn-success").is_displayed()
        # Make a subscription button
        assert driver.find_element_by_class_name("btn-primary").is_displayed()

    # =====================C913====16Dec=========================================================================

    def test_ExternalVerifySearchFunctionalityInGeneratedReport_C913(self, impersonate_external):
        # Verify Search functionality in generated report
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Check for Reports tab.
        # Open the 'Inventory by Business Unit' page and verify the page opened properly.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()

        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on 'Inventory by Business Unit' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Open Purchase Orders')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Inventory by Business Unit").click()
        time.sleep(1)
        # Verify 'Inventory by Business Unit' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header = "Inventory by Business Unit Report "
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        # Verify Inventory by Business Unit Report
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        time.sleep(4)
        expected_header_Inventory_by_Business_Unit = "Inventory by Business Unit Report"
        actual_header_Inventory_by_Business_Unit = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_by_Business_Unit in expected_header_Inventory_by_Business_Unit
        # Verify radio button
        assert driver.find_element_by_class_name("radio").is_displayed()
        #  Verify Product Class label
        assert driver.find_element_by_id("ProdClass").is_displayed()
        # Verify Business Units dropdown
        assert driver.find_element_by_id("BU").is_displayed()
        # Select value from drop down
        select = Select(driver.find_element_by_id("BU"))
        select.select_by_visible_text("Alt Media")
        # Verfiy Make a subscription button
        assert driver.find_element_by_class_name("btn-primary").is_displayed()
        # Verify Generate report button
        assert driver.find_element_by_class_name("btn-success").is_displayed()
        driver.find_element_by_class_name("btn-success").click()
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        # Send entry in search text field
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl00").send_keys("AARP00811")
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl01").click()
        time.sleep(5)
        try:
            alert = driver.switch_to_alert()
            assert alert.text == "The search text was not found."
            alert.accept()
            found = True
        except NoAlertPresentException as e:
            found = False

        if found is False:
            driver.find_element_by_css_selector("span[style='COLOR:highlighttext;BACKGROUND-COLOR:highlight;']").is_displayed()

        # Verify wrong entry could not be searched
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl00").send_keys("test12345")
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl01").click()
        WebDriverWait(driver, 15).until(EC.alert_is_present(), 'The search text was not found.')
        try:
            alert = driver.switch_to_alert()
            assert alert.text == "The search text was not found."
            alert.accept()
            found3 = True
        except NoAlertPresentException as e:
            found3 = False

    # ===========================C307====16Dec===================================
    def test_ExternalVerifyGenerateReport_FunctionalityInventoryByBusinessUnitReport_C307(self,impersonate_external):
        # Verify generate report button functionality in  Inventory by Business Unit Report page
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Check for Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Operations
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory by Business Unit
        driver.find_element_by_link_text("Inventory by Business Unit").click()
        # Verify Inventory by Business Unit Report
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        time.sleep(1)

        expected_header_Inventory_by_Business_Unit = "Inventory by Business Unit Report"
        actual_header_Inventory_by_Business_Unit = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_by_Business_Unit in expected_header_Inventory_by_Business_Unit

        # Verify radio button
        assert driver.find_element_by_class_name("radio").is_displayed()
        #  Verify Product Class label is selected
        assert driver.find_element_by_id("ProdClass").is_selected()
        # Verify bussiness report drop down
        assert driver.find_element_by_id("BU").is_displayed()
        # Verify bussiness report drop down selection
        select = Select(driver.find_element_by_id("BU"))
        select.select_by_visible_text("Alt Media")
        # Verify make a subscription button
        assert driver.find_element_by_class_name("btn-primary").is_displayed()
        # Verify generate report button
        assert driver.find_element_by_class_name("btn-success").is_displayed()
        # click on generate report button
        driver.find_element_by_class_name("btn-success").click()
        # Switch to report
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        # Verify report content
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()

    # ==================18 Dec====================================================================================
    # =================================C308====18Dec===========================================================
    def test_ExternalVerifyMakeSubscriptionButtonFunctionalityInventoryBusinessUnit_C308(self, impersonate_external):
        # Verify the  Make a subscription button functionality in  Inventory by Business Unit Report page
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Check for Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations
        driver.find_element_by_link_text("Operations").click()
        # Click on Inventory
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory by Business Unit
        driver.find_element_by_link_text("Inventory by Business Unit").click()
        # Verify Inventory by Business Unit Report
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))

        expected_header_Inventory_by_Business_Unit = "Inventory by Business Unit Report"
        actual_header_Inventory_by_Business_Unit = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_by_Business_Unit in expected_header_Inventory_by_Business_Unit
        # Verify and click on make subscription button
        assert driver.find_element_by_class_name("btn-primary").is_displayed()
        driver.find_element_by_class_name("btn-primary").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'myModalLabel')))
        # Verify Inventory by Business Unit Report for ARPM pop up.
        expected_Inventory_Business_Unit_ARPM = "Subscription for: Inventory by Business Unit Report for ARPM"
        actual_Inventory_Business_Unit_ARPM = driver.find_element_by_id("myModalLabel").text
        assert actual_Inventory_Business_Unit_ARPM in expected_Inventory_Business_Unit_ARPM

    # ==========================================C911====18Dec===================================================

    def test_ExternalVerifyShowing1OfTotalPagesEnteriesFunctionalityInReport_C911(self, impersonate_external):
        # Verify Showing 1 of 'xx' entries functionality in generated report
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Check for Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Operations
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory by Business Unit
        driver.find_element_by_link_text("Inventory by Business Unit").click()
        # Verify Inventory by Business Unit Report
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        time.sleep(1)
        expected_header_Inventory_by_Business_Unit = "Inventory by Business Unit Report"
        actual_header_Inventory_by_Business_Unit = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_by_Business_Unit in expected_header_Inventory_by_Business_Unit
        # Verify radio button
        assert driver.find_element_by_class_name("radio").is_displayed()
        #  Verify Product Class label is selected
        assert driver.find_element_by_id("ProdClass").is_selected()
        # Verify bussiness report drop down
        assert driver.find_element_by_id("BU").is_displayed()
        # Verify bussiness report drop down selection
        select = Select(driver.find_element_by_id("BU"))
        select.select_by_visible_text("Alt Media")
        # Verify make a subscription button
        assert driver.find_element_by_class_name("btn-primary").is_displayed()
        # Verify generate report button
        assert driver.find_element_by_class_name("btn-success").is_displayed()
        # click on generate report button
        driver.find_element_by_class_name("btn-success").click()
        # Switch to report
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        # Verify current page of report out of totals
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_displayed()
        # Verify total pages of report
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()

    # ================================================C914====18Dec============================================

    def test_ExternalVerifyExportButtonFunctionality_C914(self, impersonate_external):
        # Verify Export button functionality
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Check for Reports tab.
        # Open the 'Inventory by Business Unit' page and verify the page opened properly.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()

        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()

        # Click on 'Inventory by Business Unit' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Open Purchase Orders')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Inventory by Business Unit").click()

        # Verify 'Inventory by Business Unit' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header = "Inventory by Business Unit Report "
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header
        # Verify Inventory by Business Unit Report
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        time.sleep(1)
        expected_header_Inventory_by_Business_Unit = "Inventory by Business Unit Report"
        actual_header_Inventory_by_Business_Unit = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_by_Business_Unit in expected_header_Inventory_by_Business_Unit
        # Verfiy radio button is displayed
        assert driver.find_element_by_class_name("radio").is_displayed()
        # Verify checkbox is present.
        assert driver.find_element_by_id("ProdClass").is_selected()
        # Verify Business Unit drop down
        assert driver.find_element_by_id("BU").is_displayed()
        select = Select(driver.find_element_by_id("BU"))
        # Verify Selection from drop down
        select.select_by_visible_text("Alt Media")
        # Verify make a subscription button
        assert driver.find_element_by_class_name("btn-primary").is_displayed()
        # Verify report generate button
        assert driver.find_element_by_class_name("btn-success").is_displayed()
        driver.find_element_by_class_name("btn-success").click()
        # Switch to report-items
        driver.switch_to_frame("report_src")
        # Verify the ReportViewerForm displayed for report
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerForm')))
        # Verify search text input is displayed
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(1)
        # Report should be generated successfully on the same page.
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_displayed()
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl04_ctl00_ButtonImgDown").click()
        # Verify report can be exported in following format
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'HoverButton')))
        act = driver.find_elements_by_class_name("ActiveLink")
        exp_report_type = ['XML file with report data',
                           'CSV (comma delimited)',
                           'PDF',
                           'MHTML (web archive)',
                           'Excel',
                           'TIFF file',
                           'Word']
        for v in act:
            name = v.text
            assert name in exp_report_type

    # ============================C303=========21Dec=======================================================================

    def test_ExternalSaveFunctionalityInModifySubscription_C303(self, impersonate_external):
        # To verify the save functionality in modify Subscription 
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)

        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        driver.find_element_by_link_text("Operations").click()
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_link_text("Inventory").click()
        # Click on Open Purchase Orders.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Open Purchase Orders')))
        driver.find_element_by_link_text("Open Purchase Orders").click()
        # Report: (Title) top left side of the page
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'panel-heading')))
        time.sleep(1)
        # Click on Make a subscription button right side of the page.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()
        # Verify the content on the subscription form
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        random_number = str(randint(10, 999))
        name = "TestSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        driver.find_element_by_id("next_btn").click()
        # "Subscription saved" message should be displayed.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'noty_text')))
        time.sleep(1)
        # On subscriptions page, Subscription name should reflect with Modify and Delete button.
        driver.find_element_by_link_text("Subscriptions").click()
        time.sleep(1)
        NameNew_value = driver.find_element_by_id("jobs_table").text
        assert name in NameNew_value
        # Verify Delete Button for newly created Subscription
        # Check number of subscriptions
        trs = driver.find_element_by_id('jobs_table').find_elements_by_tag_name('tr')
        time.sleep(1)
        trsc = len(trs)
        # Get number of modify buttons
        trm = driver.find_elements_by_link_text("Modify")
        trmc = len(trm)
        # Get number of Delete buttons
        trd = driver.find_elements_by_link_text("Delete")
        trdc = len(trd)

        # Check number of subscriptions equal to Modify buttons
        assert int(trsc) == int(trmc)
        # Check number of subscriptions equal to Delete buttons
        assert int(trsc) == int(trdc)

    # ==========================C305=====21Dec====================================================================

    def test_ExternalVerifyMoreThanOneEmailCanBeSavedInSubscription_C305(self, impersonate_external):
        # To verify more than one email can be saved in modify Subscription
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        driver.find_element_by_link_text("Operations").click()
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_link_text("Inventory").click()
        # Click on Open Purchase Orders.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Open Purchase Orders')))
        driver.find_element_by_link_text("Open Purchase Orders").click()
        time.sleep(1)
        # Report:  (Title) top left side of the page
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'panel-heading')))
        # Click on Make a subscription button right side of the page.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()
        # Verify the content on the subscription form
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        random_number = str(randint(10, 999))
        name = "TestSubscription" + random_number
        # Send name for subscription
        driver.find_element_by_id("sub_name").send_keys(name)
        # Select days_of_week
        driver.find_element_by_name("days_of_week").click()
        # Clear email text box
        driver.find_element_by_id("email").clear()
        # Send two email ids in Email field
        email = "apriest@ggoutfitters.com,TestB.gutpa@damcosoft.com"
        driver.find_element_by_id("email").send_keys(email)
        # Select save button
        driver.find_element_by_id("next_btn").click()
        # Subscription saved with two email id" Verifying "Subscription saved" message is displayed.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'noty_text')))
        time.sleep(1)

    # ====================22 Dec======================================================================================
    # ==========================================C248=====22Dec========================================================

    def test_ExternalVerifyGenerateReportButtonFunctionality_C248(self, impersonate_external):
        # Verify Generate Report button functionality
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        driver.find_element_by_link_text("Operations").click()
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_link_text("Inventory").click()
        # Click on Open Purchase Orders.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Open Purchase Orders')))
        driver.find_element_by_link_text("Open Purchase Orders").click()
        time.sleep(3)
        # Report:  (Title) top left side of the page
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'panel-heading')))
        # Verify  header
        expected_header_Open_Purchase_Orders_Report = "Open Purchase Orders Report"
        actual_header_Open_Purchase_Orders_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Open_Purchase_Orders_Report in expected_header_Open_Purchase_Orders_Report
        # Click on Generate Report button.
        driver.find_element_by_class_name("btn-success").click()
        # Switch to report-items
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        # Report should be generated successfully on the same page.
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_displayed()
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()

    # =============================C262=====22Dec=======================================================================
    def test_ExternalVerifyExportButtonFunctionalityInGeneratedReport_C262(self, impersonate_external):
        # Verify Export button functionality in generated report.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        driver.find_element_by_link_text("Operations").click()
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Open Purchase Orders.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Open Purchase Orders')))
        driver.find_element_by_link_text("Open Purchase Orders").click()
        time.sleep(1)
        # Report: Open Purchase Orders Report
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'panel-heading')))
        # Verify  header
        expected_header_Open_Purchase_Orders_Report = "Open Purchase Orders Report"
        actual_header_Open_Purchase_Orders_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Open_Purchase_Orders_Report in expected_header_Open_Purchase_Orders_Report
        # Click on Generate Report button.
        driver.find_element_by_class_name("btn-success").click()
        # Switch to report-items.
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        # Report should be generated successfully on the same page.
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_displayed()
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl04_ctl00_ButtonLink").click()
        # Verify report can be exported in following format
        assert driver.find_element_by_class_name("HoverButton").is_displayed()
        act = driver.find_elements_by_class_name("ActiveLink")
        exp_report_type = ['XML file with report data',
                           'CSV (comma delimited)',
                           'PDF',
                           'MHTML (web archive)',
                           'Excel',
                           'TIFF file',
                           'Word']
        for v in act:
            name = v.text
            assert name in exp_report_type

    # =============================C263=====23Dec=======================================================================

    def test_ExternalVerifyDateAndTimeInGeneratedReport_C263(self, impersonate_external):
        # Verify Date and Time of generated report.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        driver.find_element_by_link_text("Operations").click()
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Open Purchase Orders.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Open Purchase Orders')))
        driver.find_element_by_link_text("Open Purchase Orders").click()
        time.sleep(1)
        # Report: Open Purchase Orders Report
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'panel-heading')))
        # Verify  header
        expected_header_Open_Purchase_Orders_Report = "Open Purchase Orders Report"
        actual_header_Open_Purchase_Orders_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Open_Purchase_Orders_Report in expected_header_Open_Purchase_Orders_Report
        # Click on Generate Report button.
        driver.find_element_by_class_name("btn-success").click()
        # Switch to report-items.
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        # Verify the Date and Time of the generated report
        actual_dateTime = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        exp_dateTime = "Report Created On:"
        exp_dateTime1 = "AM"
        exp_dateTime2 = "PM"
        assert exp_dateTime in actual_dateTime
        assert exp_dateTime in actual_dateTime
        assert ((exp_dateTime1 in actual_dateTime) | (exp_dateTime2 in actual_dateTime))

    # =============================C264=====23Dec===================================================================
    def test_ExternalVerifyContentOfGeneratedReport_C264(self, impersonate_external):
        # Verify the content of generated report.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        driver.find_element_by_link_text("Operations").click()
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Open Purchase Orders.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Open Purchase Orders')))
        driver.find_element_by_link_text("Open Purchase Orders").click()
        time.sleep(1)
        # Report: Open Purchase Orders Report
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'panel-heading')))
        # Verify  header
        expected_header_Open_Purchase_Orders_Report = "Open Purchase Orders Report"
        actual_header_Open_Purchase_Orders_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Open_Purchase_Orders_Report in expected_header_Open_Purchase_Orders_Report
        # Click on Generate Report button.
        driver.find_element_by_class_name("btn-success").click()
        # Switch to report-items.
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        # Verify the first page
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_First_ctl01_ctl00").is_displayed()
        # Verify the Previous page
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Previous_ctl01_ctl00").is_displayed()
        # Verify the current page text box
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_displayed()
        # Verify the  Total Pages
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()
        # Verify the next Pages
        if driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Next_ctl01").is_displayed():
            assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Next_ctl01").is_displayed()
        else:
            assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Next_ctl00").is_displayed()
        # Verify the last Pages link
        if driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Last_ctl00").is_displayed():
            assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Last_ctl00").is_displayed()
        else:
            assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Last_ctl01").is_displayed()
        # Verify search text box
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl00").is_displayed()
        # Verify find link
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl01").is_displayed()
        # Verify find next link
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl03").is_displayed()
        # Verify export button
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl04_ctl00_ButtonImg").is_displayed()
        # Verify refresh button
        assert driver.find_element_by_name("ReportViewerControl$ctl05$ctl05$ctl00$ctl00$ctl00").is_displayed()
        # Verify export to data feed button
        assert driver.find_element_by_name("ReportViewerControl$ctl05$ctl07$ctl00$ctl00$ctl00").is_displayed()
        # Verify report content
        tr = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        arr = tr.split("\n")
        exp_data = ['SKU','Description','PO Issue Date', 'Due Date','Qty on Order','Vendor', 'PO Number']
        for i in range(len(exp_data)):
            assert exp_data[i] in arr

    # ================================C265=====23Dec===================================================================

    def test_ExternalVerifyContentOfSubscriptionForOpenPurchaseOrders_C265(self, impersonate_external):
        # Verify the content of Subscription for: Open Purchase Orders for ARPM form.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        driver.find_element_by_link_text("Operations").click()
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Open Purchase Orders.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Open Purchase Orders')))
        driver.find_element_by_link_text("Open Purchase Orders").click()
        time.sleep(1)
        # Report: Open Purchase Orders Report
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'panel-heading')))
        # Verify  header
        expected_header_Open_Purchase_Orders_Report = "Open Purchase Orders Report"
        actual_header_Open_Purchase_Orders_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Open_Purchase_Orders_Report in expected_header_Open_Purchase_Orders_Report

        time.sleep(1)
        # Click on make a subscription
        driver.find_element_by_class_name("btn-primary").click()
        # Verify form heading
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        expected_header_subscription_form = "Subscription for: Open Purchase Orders for ARPM"
        actual_header_subscription_form = driver.find_element_by_id("myModalLabel").text
        assert actual_header_subscription_form in expected_header_subscription_form
        # Verify Subscription Name
        assert driver.find_element_by_id("sub_name").is_displayed()
        # Verify Email to field
        assert driver.find_element_by_id("email").is_displayed()
        # Verify  Delivery format in excel
        assert driver.find_element_by_class_name("radio").is_displayed()
        # Verify time
        assert driver.find_element_by_id("time").is_displayed()
        # Verify receive report day
        assert driver.find_element_by_id("modal_selector").is_displayed()
        # Verify back button
        assert driver.find_element_by_class_name("btn-default").is_displayed()
        # Verify save Subscription button
        assert driver.find_element_by_id("next_btn").is_displayed()

    # ==================================22 Jan===========================================================
    # ==================================C278==========22 Jan=============================================
    def test_ExternalVerifyContentsOnInventoryReceipts_C278(self, impersonate_external):
        # Verify the content on Inventory Receipts
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory Receipts tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory Receipts')))
        time.sleep(1)
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Inventory Receipts").click()
        time.sleep(1)
        # Verify Inventory Receipts Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        # Report: Inventory Receipts
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'panel-heading')))
        time.sleep(1)
        expected_header = "Report: Inventory Receipts"
        actual_header = driver.find_element_by_class_name("panel-heading").text
        assert expected_header in actual_header
        # Drop down with multiple clients
        expected_clients = "select"
        actual_clients = driver.find_element_by_id("CustomerNumber").tag_name
        assert expected_clients in actual_clients
        # Generate Report button
        assert driver.find_element_by_id("sub_btn").is_displayed()
        # Make a Subscription button
        assert driver.find_element_by_class_name("btn-primary").is_displayed()
        # Start Date/End date daterange field
        assert driver.find_element_by_name("daterange").is_displayed()

    # ==================================C279==========22 Jan=============================================
    def test_ExternalVerifyContentsOnEditProfile_C279(self, impersonate_external):
        # Verify Generate Report button functionality
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory Receipts tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory Receipts')))
        time.sleep(1)
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Inventory Receipts").click()
        # Verify Inventory Receipts Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.ID, 'CustomerNumber')))
        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("CustomerNumber"))
        select.select_by_visible_text("ARPM")
        # Select the ship Start date  and ship end date
        wait.until(EC.visibility_of_element_located((By.NAME,'daterange')))
        driver.find_element_by_name("daterange").click()
        time.sleep(1)

        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("02/22/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("02/24/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)

        # Click on Generate report button.
        driver.find_element_by_class_name("btn-success").click()
        # Switch to report
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_displayed()
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()

    # ==================================C682==========22 Jan=============================================
    def test_ExternalVerifyRefreshButtonFunctionality_C682(self, impersonate_external):
        # Verify refresh button functionality in the Open Purchase Orders report.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        driver.find_element_by_link_text("Operations").click()
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Open Purchase Orders.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Open Purchase Orders')))
        driver.find_element_by_link_text("Open Purchase Orders").click()
        # Report: Open Purchase Orders Report
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        time.sleep(1)
        # Verify  header
        expected_header_Open_Purchase_Orders_Report = "Open Purchase Orders Report"
        actual_header_Open_Purchase_Orders_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Open_Purchase_Orders_Report in expected_header_Open_Purchase_Orders_Report
        # Click on Generate report button.
        driver.find_element_by_class_name("btn-success").click()
        # Switch to  report content.
        wait.until(EC.visibility_of_element_located((By.ID, 'report_src')))
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        original_text = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        # Click on Refresh icon.
        driver.find_element_by_name("ReportViewerControl$ctl05$ctl05$ctl00$ctl00$ctl00").click()
        # Generated report should be refreshed.
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        latest_text = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        assert (original_text is not latest_text)

    # ==================================C703==========25 Jan=============================================
    def test_external_content_of_product_usage_report_page_C703(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        # Click on Product Usage.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Product Usage')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Product Usage").click()
        # Verify Product Usage  page header
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header = "Product Usage Report"
        actual_header = driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        assert driver.find_element_by_id('customerNumber')
        # Select the client from the drop down
        clients = Select(driver.find_element_by_id('customerNumber'))
        clients.select_by_visible_text('ARPM')

        actual_selected_option = clients.first_selected_option.text
        expected_selection_option = "ARPM"
        assert expected_selection_option in actual_selected_option

        # Check iDays from the drop down
        idays = Select(driver.find_element_by_id('iDays'))
        idays.select_by_visible_text("7 Days")
        actual_selected_option = idays.first_selected_option.text
        expected_selection_option = "7 Days"
        assert expected_selection_option in actual_selected_option

        # check Generate report button visibility
        assert driver.find_element_by_id("sub_btn").is_displayed()
        # Check Make a subscription button right side of the page.
        assert driver.find_element_by_id("subscription_btn").is_displayed()

    # ==================================C704==========25 Jan=============================================
    def test_external_content_of_product_usage_Generate_report_C704(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Product Usage.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Product Usage')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Product Usage").click()
        time.sleep(1)
        # Verify Product Usage  page header
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header = "Product Usage Report"
        actual_header = driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        assert driver.find_element_by_id('customerNumber')
        # Select the client from the drop down.
        clients = Select(driver.find_element_by_id('customerNumber'))
        clients.select_by_visible_text('ARPM')
        actual_selected_option = clients.first_selected_option.text
        expected_selection_option = "ARPM"
        assert expected_selection_option in actual_selected_option

        # Check iDays from the drop down

        idays = Select(driver.find_element_by_id('iDays'))
        idays.select_by_visible_text("7 Days")
        actual_selected_option = idays.first_selected_option.text
        expected_selection_option = "7 Days"
        assert expected_selection_option in actual_selected_option
        # Check Make a subscription button right side of the page.
        assert driver.find_element_by_id("subscription_btn").is_displayed()
        # check Generate report button visibility
        assert driver.find_element_by_id("sub_btn").is_displayed()
        driver.find_element_by_id("sub_btn").click()

        # Check report loads.
        wait.until(EC.visibility_of_element_located((By.ID, 'report_src')))
        driver.switch_to.frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerForm')))
        # Verify current page and total pages are displayed
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl00_CurrentPage')))
        time.sleep(1)
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_enabled()
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()

        # Check total pages
        tpc = driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").text
        tps = tpc.split(" ")
        tp = tps[0]
        assert int(tp) >= 1

        # Verify report headers
        hdrs = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        time.sleep(3)
        exp_content = ['SKU', 'Description', 'Quantity Fulfilled', 'Average Usage per Day', 'Quantity on Hand', 'Days of Inventory']
        for v in exp_content:
            assert v in hdrs

    # ==================================C705======================25 Jan=============================================

    def test_external_content_of_product_usage_report_pagination_C705(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        # Click on Product Usage.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Product Usage')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Product Usage").click()
        # Verify Product Usage  page header
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header = "Product Usage Report"
        actual_header = driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        assert driver.find_element_by_id('customerNumber')
        # Select the client from the drop down.

        clients = Select(driver.find_element_by_id('customerNumber'))
        clients.select_by_visible_text('ARPM')

        actual_selected_option = clients.first_selected_option.text
        expected_selection_option = "ARPM"
        assert expected_selection_option in actual_selected_option

        # Check iDays from the drop down

        idays = Select(driver.find_element_by_id('iDays'))
        idays.select_by_visible_text("7 Days")
        actual_selected_option = idays.first_selected_option.text
        expected_selection_option = "7 Days"
        assert expected_selection_option in actual_selected_option
        # Check Make a subscription button right side of the page.
        assert driver.find_element_by_id("subscription_btn").is_displayed()
        # check Generate report button visibility
        assert driver.find_element_by_id("sub_btn").is_displayed()
        driver.find_element_by_id("sub_btn").click()
        # Check report loads
        wait.until(EC.visibility_of_element_located((By.ID, 'report_src')))
        driver.switch_to.frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerForm')))
        # Verify current page and total pages are displayed
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_displayed()
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl00_CurrentPage')))
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_enabled()
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()
        # Check total pages
        tpc = driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").text
        tps = tpc.split(" ")
        tp = tps[0]
        assert int(tp) >= 1

    # ==================================C707==========25 Jan=============================================
    def test_external_search_functionality_product_usage_report_C707(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        # Click on Product Usage.
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Product Usage')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Product Usage").click()
        # Verify Product Usage  page header
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header = "Product Usage Report"
        actual_header = driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        assert driver.find_element_by_id('customerNumber')
        # Select the client from the drop down.
        clients = Select(driver.find_element_by_id('customerNumber'))
        clients.select_by_visible_text('ARPM')
        actual_selected_option = clients.first_selected_option.text
        expected_selection_option = "ARPM"
        assert expected_selection_option in actual_selected_option

        # Check iDays from the drop down
        idays = Select(driver.find_element_by_id('iDays'))
        idays.select_by_visible_text("7 Days")
        actual_selected_option = idays.first_selected_option.text
        expected_selection_option = "7 Days"
        assert expected_selection_option in actual_selected_option
        # Check Make a subscription button right side of the page.
        assert driver.find_element_by_id("subscription_btn").is_displayed()

        # check Generate report button visibility
        assert driver.find_element_by_id("sub_btn").is_displayed()
        driver.find_element_by_id("sub_btn").click()
        # Check report loads
        wait.until(EC.visibility_of_element_located((By.ID, 'report_src')))
        driver.switch_to.frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        # Search SKU no "AARP00811"
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl00").send_keys("AARP00811")
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl01").click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        try:
            alert = driver.switch_to_alert()
            assert alert.text == "The search text was not found."
            alert.accept()
            found = True
        except NoAlertPresentException as e:
            found = False

        if found == False:
            driver.find_element_by_css_selector("span[style='COLOR:highlighttext;BACKGROUND-COLOR:highlight;']").is_displayed()

        # Verify wrong entry could not be searched
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl00").send_keys("test12345")
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl01").click()
        WebDriverWait(driver, 15).until(EC.alert_is_present(), 'The search text was not found.')
        try:
            alert = driver.switch_to_alert()
            assert alert.text == "The search text was not found."
            alert.accept()
            found3 = True
        except NoAlertPresentException as e:
            found3 = False

    # ==================================C708==========25 Jan=============================================
    def test_external_content_export_product_usage_report_C708(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Product Usage.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Product Usage')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Product Usage").click()
        time.sleep(1)
        # Verify Product Usage  page header
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header = "Product Usage Report"
        actual_header = driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        assert driver.find_element_by_id('customerNumber')
        # Select the client from the drop down.
        clients = Select(driver.find_element_by_id('customerNumber'))
        clients.select_by_visible_text('ARPM')
        actual_selected_option = clients.first_selected_option.text
        expected_selection_option = "ARPM"
        assert expected_selection_option in actual_selected_option

        # Check iDays from the drop down
        idays = Select(driver.find_element_by_id('iDays'))
        idays.select_by_visible_text("7 Days")
        actual_selected_option = idays.first_selected_option.text
        expected_selection_option = "7 Days"
        assert expected_selection_option in actual_selected_option
        # Check Make a subscription button at the right of the page
        assert driver.find_element_by_id("subscription_btn").is_displayed()

        # check Generate report button visibility
        assert driver.find_element_by_id("sub_btn").is_displayed()
        driver.find_element_by_id("sub_btn").click()
        # Check report loads
        wait.until(EC.visibility_of_element_located((By.ID, 'report_src')))
        driver.switch_to.frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerForm')))

        time.sleep(4)
        # Report should be generated successfully on the same page.
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_displayed()
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl04_ctl00_ButtonLink").click()
        # Verify report can be exported in following format
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'HoverButton')))
        act = driver.find_elements_by_class_name("ActiveLink")
        exp_report_type = ['XML file with report data',
                           'CSV (comma delimited)',
                           'PDF',
                           'MHTML (web archive)',
                           'Excel',
                           'TIFF file',
                           'Word']
        for v in act:
            name = v.text
            assert name in exp_report_type
    # ==================================C709==========25 Jan=============================================

    def test_external_datetime_content_of_product_usage_report_C709(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 150)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        # Click on Product Usage.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Product Usage')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Product Usage").click()
        # Verify Product Usage  page header
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header = "Product Usage Report"
        actual_header = driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        assert driver.find_element_by_id('customerNumber')
        # Select the client from the drop down.
        clients = Select(driver.find_element_by_id('customerNumber'))
        clients.select_by_visible_text('ARPM')
        actual_selected_option = clients.first_selected_option.text
        expected_selection_option = "ARPM"
        assert expected_selection_option in actual_selected_option

        # Check iDays from the drop down
        idays = Select(driver.find_element_by_id('iDays'))
        idays.select_by_visible_text("7 Days")
        actual_selected_option = idays.first_selected_option.text
        expected_selection_option = "7 Days"
        assert expected_selection_option in actual_selected_option
        # Check Make a subscription button right side of the page.
        assert driver.find_element_by_id("subscription_btn").is_displayed()

        # check Generate report button visibility
        assert driver.find_element_by_id("sub_btn").is_displayed()
        driver.find_element_by_id("sub_btn").click()

        # Check report loads
        wait.until(EC.visibility_of_element_located((By.ID, 'report_src')))
        driver.switch_to.frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerForm')))
        time.sleep(4)

        # Verify the Date and Format of the generated report
        actual_dateTime = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        label_dateTime = "Report Created On:"
        exp_dateTime1 = "AM"
        exp_dateTime2 = "PM"
        repdate1 = int(time.strftime("%m"))
        repdate2 = int(time.strftime("%d"))
        repdate3 = int(time.strftime("%Y"))
        todays_date = str(repdate1) + "/" + str(repdate2) + "/" + str(repdate3)

        assert todays_date in actual_dateTime
        assert label_dateTime in actual_dateTime
        assert ((exp_dateTime1 in actual_dateTime) | (exp_dateTime2 in actual_dateTime))

    # ==================================C710==========25 Jan=============================================

    def test_external_content_of_product_usage_reportitems_C710(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        # Click on Product Usage.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Product Usage')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Product Usage").click()
        # Verify Product Usage  page header
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header = "Product Usage Report"
        actual_header = driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        assert driver.find_element_by_id('customerNumber')
        # check Days dropdown
        assert driver.find_element_by_id('iDays')

        # Check Make a subscription button right side of the page.
        assert driver.find_element_by_id("subscription_btn").is_displayed()

        # check Generate report button visibility
        assert driver.find_element_by_id("sub_btn").is_displayed()
        driver.find_element_by_id("sub_btn").click()

        # Check report loads
        wait.until(EC.visibility_of_element_located((By.ID, 'report_src')))

        driver.switch_to.frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerForm')))

        # Verify current page and total pages are displayed
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_displayed()
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl00_CurrentPage')))

        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_enabled()
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))

        # Verify report headers
        hdrs = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        exp_content = ['SKU', 'Description', 'Quantity Fulfilled', 'Average Usage per Day', 'Quantity on Hand','Days of Inventory']
        for v in exp_content:
            assert v in hdrs

        # Verify Report controls.
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_displayed()
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl04_ctl00_ButtonLink").is_displayed()

        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_First_ctl01_ctl00").is_displayed()
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Previous_ctl01_ctl00").is_displayed()
        if driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Next_ctl01_ctl00").is_displayed():
            assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Next_ctl01_ctl00").is_displayed()
            assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Last_ctl01_ctl00").is_displayed()
        else:
            assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Next_ctl00_ctl00").is_displayed()
            assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Last_ctl00_ctl00").is_displayed()

        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl01").is_displayed()
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl03").is_displayed()
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl05_ctl00_ctl00").is_displayed()
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl07_ctl00").is_displayed()
        assert driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").is_displayed()

    # ==================================C266==========27 Jan========================================================

    def test_external_open_purchase_orders_modaldialog_empty_submission_C266(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        driver.find_element_by_link_text("Operations").click()
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_link_text("Inventory").click()
        # Click on Open Purchase Orders.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Open Purchase Orders')))
        driver.find_element_by_link_text("Open Purchase Orders").click()
        # Verify the contents on Open Purchase order Report page.
        # Report: (Title) top left side of the page
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'panel-heading')))
        expected_header = "Report: Open Purchase Orders"
        actual_header = driver.find_element_by_class_name("panel-heading").text
        assert expected_header in actual_header

        # Select the client from the drop down.
        clients = Select(driver.find_element_by_id('CustomerNumber'))
        clients.select_by_visible_text('ARPM')
        # Click on Make a Subscription button
        driver.find_element_by_id("subscription_btn").click()

        # Verify Modal Dialog Text
        wait.until(EC.visibility_of_element_located((By.ID, 'myModalLabel')))
        modal_text = driver.find_element_by_id("myModalLabel").text
        assert modal_text == 'Subscription for: Open Purchase Orders for ARPM'
        assert driver.find_element_by_id("excel1").is_displayed()
        assert driver.find_element_by_id("day_box").is_displayed()

        # Verify Save Subscription button is displayed
        assert driver.find_element_by_id("next_btn").is_displayed()
        # Verify Empty subscription not submitted
        driver.find_element_by_id("next_btn").click()
        # Verify that Subscription Name is Empty and Dialog is still open with Save Subscription button being displayed
        assert driver.find_element_by_id("sub_name").text == ''
        assert driver.find_element_by_id("next_btn").is_displayed()
        # Verify Modal Dialog Text is still displayed
        modal_text = driver.find_element_by_id("myModalLabel").text
        assert modal_text == 'Subscription for: Open Purchase Orders for ARPM'
        # Click back button to close modal dialog
        driver.find_element_by_class_name("btn-default").click()

    # ==================================C711==========27 Jan=============================================
    def test_external_content_of_product_usage_modaldialog_C711(self, impersonate_external):
        driver = impersonate_external['webdriver']
        # External user - Reports/operations/Inventory/Product Usage]Verify the content of Subscription for: Product Usage Report for ARPM form.
        # Click on Reports tab.
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        # Click on Product Usage.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Product Usage')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Product Usage").click()
        # Verify Product Usage  page header
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header = "Product Usage Report"
        actual_header = driver.find_element_by_id("content-header").text
        assert actual_header in expected_header
        time.sleep(1)
        # Select the client from the drop down.
        clients = Select(driver.find_element_by_id('customerNumber'))
        clients.select_by_visible_text('ARPM')

        time.sleep(1)
        # Click on 'Make a subscription' button
        wait.until(EC.visibility_of_element_located((By.ID,'subscription_btn')))
        time.sleep(1)
        driver.find_element_by_id("subscription_btn").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'myModalLabel')))
        # Verify Modal Dialog Text
        modal_text = driver.find_element_by_id("myModalLabel").text
        assert modal_text == 'Subscription for: Product Usage Report for ARPM'
        random_number = str(randint(10, 999))
        name = "TestBSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        # Verify email textbox is displayed
        assert driver.find_element_by_id("email").is_displayed()
        driver.find_element_by_id("email").send_keys(email)

        assert driver.find_element_by_id("excel1").is_displayed()
        assert driver.find_element_by_id("day_box").is_displayed()

        # Verify time
        assert driver.find_element_by_id("time").is_displayed()
        # Verify receive report day
        driver.find_element_by_id("modal_selector").is_displayed()
        expected_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        actual_days = driver.find_elements_by_class_name("checkbox")
        for day in actual_days:
            name = day.text
            assert name in expected_days
        # Verify back button
        assert driver.find_element_by_class_name("btn-default").is_displayed()
        # Verify save Subscription button
        assert driver.find_element_by_id("next_btn").is_displayed()

    # ==================================C712==========27 Jan=============================================
    def test_external_product_usage_modaldialog_emptysubmission_fails_C712(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # External user- Reports/operations/Inventory/Product Usage]Verify with blank fields subscription form not submitted.
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        # Click on Inventory tab.
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Product Usage')))
        # Click on Product Usage
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Product Usage").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'customerNumber')))
        # Select the client from the drop down.
        clients = Select(driver.find_element_by_id('customerNumber'))
        clients.select_by_visible_text('ARPM')
        # Click on Make a Subscription button
        driver.find_element_by_id("subscription_btn").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'myModalLabel')))
        # Verify Modal Dialog Text
        modal_text = driver.find_element_by_id("myModalLabel").text
        assert modal_text == 'Subscription for: Product Usage Report for ARPM'
        assert driver.find_element_by_id("excel1").is_displayed()
        assert driver.find_element_by_id("day_box").is_displayed()

        # Verify Save Subscription button is displayed
        assert driver.find_element_by_id("next_btn").is_displayed()
        # Verify Empty subscription not submitted
        driver.find_element_by_id("next_btn").click()
        # Verify that Subscription Name is Empty and Dialog is still open with Save Subscription button being displayed
        assert driver.find_element_by_id("sub_name").text == ''
        assert driver.find_element_by_id("next_btn").is_displayed()
        # Verify Modal Dialog Text is still displayed
        modal_text = driver.find_element_by_id("myModalLabel").text
        assert modal_text == 'Subscription for: Product Usage Report for ARPM'
        # Click cancel button to close modal dialog
        driver.find_element_by_class_name("btn-default").click()
        time.sleep(1)

    # ==================================C713==========27 Jan=============================================
    def test_external_product_usage_modaldialog_defaultemail_C713(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # External user - Reports - Product Usage]Verify user Email Id display by default in subscription form.
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        # Click on Inventory tab.
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Product Usage')))
        # Click on Product Usage
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Product Usage").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'customerNumber')))

        # Select the client from the drop down.
        clients = Select(driver.find_element_by_id('customerNumber'))
        clients.select_by_visible_text('ARPM')

        # Click on Make a Subscription button
        driver.find_element_by_id("subscription_btn").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'myModalLabel')))
        # Verify Modal Dialog Text
        modal_text = driver.find_element_by_id("myModalLabel").text
        assert modal_text == 'Subscription for: Product Usage Report for ARPM'
        assert driver.find_element_by_id("excel1").is_displayed()
        assert driver.find_element_by_id("day_box").is_displayed()

        # Verify Save Subscription button is displayed
        assert driver.find_element_by_id("next_btn").is_displayed()

        # Verify Email id for "clipford@ggoutfitters.com"
        assert driver.find_element_by_id("email").is_displayed()
        expected_email = "clipford@ggoutfitters.com"
        actual_email = driver.find_element_by_id("email").get_attribute("value")
        assert actual_email in expected_email

        # Click cancel button to close modal dialog
        driver.find_element_by_class_name("btn-default").click()
        time.sleep(20)

    # ==================================C714==========27 Jan=========================================================
    def test_verify_product_usage_modaldialog_backbutton_C714(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # External user - Reports/operations/Inventory/Product Usage] Verify Back button functionality on Subscription
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        # Click on Inventory tab.
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Product Usage')))
        # Click on Product Usage
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Product Usage").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'customerNumber')))

        # Select the client from the drop down.
        clients = Select(driver.find_element_by_id('customerNumber'))
        clients.select_by_visible_text('ARPM')

        # Click on Make a Subscription button
        driver.find_element_by_id("subscription_btn").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'myModalLabel')))
        # Verify Modal Dialog Text
        modal_text = driver.find_element_by_id("myModalLabel").text
        assert modal_text == 'Subscription for: Product Usage Report for ARPM'
        assert driver.find_element_by_id("excel1").is_displayed()
        assert driver.find_element_by_id("day_box").is_displayed()

        # Verify Save Subscription button is displayed
        assert driver.find_element_by_id("next_btn").is_displayed()
        # Verify Email id for "clipford@ggoutfitters.com"
        assert driver.find_element_by_id("email").is_displayed()

        # Click back button to close modal dialog
        driver.find_element_by_class_name("btn-default").click()

        # Verify Inventory Receipts Report page
        expected_header_Products_Usage_Report = "Product Usage Report"
        actual_header = driver.find_element_by_id("content-header").text
        assert actual_header in expected_header_Products_Usage_Report


    # ==================================C249==========28 Jan=============================================
    def test_verify_open_purchaseorders_report_pagination_C249(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # External user - Reports - Open Purchase Orders - Verify Showing 1 of 'xx' entries functionality
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        # Click on Inventory tab.
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Open Purchase Orders link
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Open Purchase Orders").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        # Verify  header
        expected_header = "Open Purchase Orders Report"
        actual_header = driver.find_element_by_id("content-header").text
        assert actual_header in expected_header
        assert driver.find_element_by_id('CustomerNumber')
        # Select the client from the drop down.
        clients = Select(driver.find_element_by_id('CustomerNumber'))
        clients.select_by_visible_text('ARPM')
        actual_selected_option = clients.first_selected_option.text
        expected_selection_option = "ARPM"
        assert expected_selection_option in actual_selected_option
        # Check Generate report button visibility
        assert driver.find_element_by_id("sub_btn").is_displayed()
        driver.find_element_by_id("sub_btn").click()
        # Check Report loads
        wait.until(EC.visibility_of_element_located((By.ID, 'report_src')))
        driver.switch_to.frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerForm')))
        time.sleep(1)
        # Verify current page and total pages are displayed
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl00_CurrentPage')))
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_displayed()
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_enabled()
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()
        assert int(driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").text) >= 1

    # ==================================C278==========28 Jan=============================================
    def test_ExternalVerifyContentOnInventoryReceipts_C278(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory Receipts tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory Receipts')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Inventory Receipts").click()
        time.sleep(1)
        # Verify Inventory Receipts Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Inventory_Receipts_Report = "Inventory Receipts Report "
        actual_header_Inventory_Receipts_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_Receipts_Report in expected_header_Inventory_Receipts_Report
        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("CustomerNumber"))
        select.select_by_visible_text("ARPM")
        # Select Dates - Start and End date
        wait.until(EC.visibility_of_element_located((By.NAME,'daterange')))
        driver.find_element_by_name("daterange").click()
        time.sleep(1)

        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("02/22/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("02/24/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)
        # Verify PO number selection
        driver.find_element_by_id("RcvSlip").send_keys("PO00012028-1")
        time.sleep(1)
        expected_po_number = "PO00012028-1"
        actual_po_number = driver.find_element_by_id("RcvSlip").get_attribute("value")
        assert actual_po_number in expected_po_number
        # Verify Generate report button.
        assert driver.find_element_by_class_name("btn-success").is_displayed()
        # Verify make a subscription button.
        assert driver.find_element_by_id("subscription_btn").is_displayed()


    # ==================================C279==========28 Jan=============================================

    def test_ExternalVerifyGenerateReportButtonFunctionality_C279(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Verify Generate Report button functionality.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory Receipts tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory Receipts')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Inventory Receipts").click()
        time.sleep(1)
        # Verify Inventory Receipts Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Inventory_Receipts_Report = "Inventory Receipts Report "
        actual_header_Inventory_Receipts_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_Receipts_Report in expected_header_Inventory_Receipts_Report
        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("CustomerNumber"))
        select.select_by_visible_text("ARPM")
        # Select the Start and end date
        wait.until(EC.visibility_of_element_located((By.NAME,'daterange')))
        driver.find_element_by_name("daterange").click()
        time.sleep(1)

        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("02/22/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("02/24/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)
        # Verify PO number selection
        driver.find_element_by_id("RcvSlip").send_keys("PO00012028-1")
        expected_po_number = "PO00012028-1"
        actual_po_number = driver.find_element_by_id("RcvSlip").get_attribute("value")
        time.sleep(1)
        assert actual_po_number in expected_po_number
        driver.find_element_by_id("sub_btn").click()
        # Switch to generated report.
        wait.until(EC.visibility_of_element_located((By.ID, 'report_src')))
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(5)
        # Verify the first page
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_First_ctl01_ctl00").is_displayed()
        # Verify the Previous page
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Previous_ctl01_ctl00").is_displayed()


    # ==================================C285==========28 Jan=============================================
    def test_ExternalVerifyShowing1OfXXEntriesFunctionality_C285(self, impersonate_external):
        # Verify Showing 1 of 'xx' entries functionality in generated report.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory Receipts tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory Receipts')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Inventory Receipts").click()
        time.sleep(1)
        # Verify Inventory Receipts Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Inventory_Receipts_Report = "Inventory Receipts Report "
        actual_header_Inventory_Receipts_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_Receipts_Report in expected_header_Inventory_Receipts_Report
        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("CustomerNumber"))
        select.select_by_visible_text("ARPM")
        # Select the Start and end date
        # Select Dates
        wait.until(EC.visibility_of_element_located((By.NAME,'daterange')))
        driver.find_element_by_name("daterange").click()
        time.sleep(1)

        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("02/22/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("02/24/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)
        # Verify PO number selection
        driver.find_element_by_id("RcvSlip").send_keys("PO00012028-1")
        expected_po_number = "PO00012028-1"
        actual_po_number = driver.find_element_by_id("RcvSlip").get_attribute("value")
        assert actual_po_number in expected_po_number
        # Click on Generate report button.
        driver.find_element_by_id("sub_btn").click()
        # Switch to generated report.
        wait.until(EC.visibility_of_element_located((By.ID, 'report_src')))
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(5)
        # In report, Verify show 1 of x page by default
        expected_value = "1"
        actual_value = driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").get_attribute("value")
        assert expected_value in actual_value
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()
        expected_of = "of"
        actual_of = driver.find_element_by_class_name("ToolBarButtonsCell").text
        assert expected_of in actual_of
        time.sleep(1)

    # ==================================C287==========28 Jan=============================================
    def test_ExternalVerifyShowing1OfXXEntriesFunctionality_C287(self, impersonate_external):
        # Verify Search functionality in generated report.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory Receipts')))
        driver.find_element_by_link_text("Inventory Receipts").click()
        time.sleep(1)
        expected_header_Inventory_Receipts = "Inventory Receipts Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Inventory_Receipts = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_Receipts in expected_header_Inventory_Receipts
        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("CustomerNumber"))
        select.select_by_visible_text("ARPM")
        # Select the Start and end date
        wait.until(EC.visibility_of_element_located((By.NAME,'daterange')))
        driver.find_element_by_name("daterange").click()
        time.sleep(1)
        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("02/22/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("02/23/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)
        # Click on Generate report button.
        driver.find_element_by_id("sub_btn").click()
        # Switch to report content
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        # Send and Verify valid entry that can be searched AARP04261
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl00").send_keys("AARP04261")
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl01").click()
        time.sleep(10)
        try:
            alert = driver.switch_to_alert()
            assert alert.text == "The search text was not found."
            alert.accept()
            found = True
        except NoAlertPresentException as e:
            found = False

        if found == False:
            driver.find_element_by_css_selector("span[style='COLOR:highlighttext;BACKGROUND-COLOR:highlight;']").is_displayed()

        # Verify wrong entry could not be searched
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl00").send_keys("test12345")
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl01").click()
        WebDriverWait(driver, 15).until(EC.alert_is_present(), 'The search text was not found.')
        try:
            alert = driver.switch_to_alert()
            assert alert.text == "The search text was not found."
            alert.accept()
            found3 = True
        except NoAlertPresentException as e:
            found3 = False

    # ==================================C292==========29 Jan=============================================
    def test_external_InventoryReceipts_blank_subscription_C292(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory Receipts')))
        driver.find_element_by_link_text("Inventory Receipts").click()
        time.sleep(1)
        expected_header_Inventory_Receipts = "Inventory Receipts Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Inventory_Receipts = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_Receipts in expected_header_Inventory_Receipts
        # Subscription Details
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()
        # Verify Subscription Name
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        driver.find_element_by_id("sub_name").is_displayed()
        # Verify Email to field
        driver.find_element_by_id("email").is_displayed()
        # Verify Save Subscription button is displayed
        assert driver.find_element_by_id("next_btn").is_displayed()
        # Verify Empty subscription not submitted
        driver.find_element_by_id("next_btn").click()
        time.sleep(1)
        # Verify that Subscription Name is Empty and Dialog is still open with Save Subscription button being displayed
        assert driver.find_element_by_id("sub_name").text == ''
        assert driver.find_element_by_id("next_btn").is_displayed()
        # Verify error message "Only use letters and numbers."
        driver.find_element_by_id("next_btn").click()
        expected_error_message = "Only use letters and numbers."
        actual_error_message = driver.find_element_by_id("sub_name").get_attribute("title")
        assert actual_error_message in expected_error_message
        # Verify Modal Dialog box is still displayed after trying to submit with empty name
        wait.until(EC.visibility_of_element_located((By.ID, 'myModalLabel')))
        modal_text = driver.find_element_by_id("myModalLabel").text
        assert modal_text == 'Subscription for: Inventory Receipts Report for ARPM'
        # Click back button to close modal dialog
        driver.find_element_by_class_name("btn-default").click()
        time.sleep(1)

    # ==================================C297==========29 Jan=============================================
    def test_external_OutOfStock_modaldialog_invalid_subscriptionname_C297(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # External user - Reports -Out of Stock- Verify in "Subscription Name" text box only letters and numbers are allowed
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Out of Stock.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Out of Stock')))
        driver.find_element_by_link_text("Out of Stock").click()
        time.sleep(1)
        # Select the client from the drop down.
        wait.until(EC.visibility_of_element_located((By.ID, 'CustomerNumber')))
        clients = Select(driver.find_element_by_id('CustomerNumber'))
        clients.select_by_visible_text('ARPM')

        # Click on Make a Subscription button
        wait.until(EC.visibility_of_element_located((By.ID, 'subscription_btn')))
        driver.find_element_by_id("subscription_btn").click()
        # Verify Modal Dialog Text
        wait.until(EC.visibility_of_element_located((By.ID, 'myModalLabel')))
        modal_text = driver.find_element_by_id("myModalLabel").text
        assert modal_text == 'Subscription for: Out of Stock Report for ARPM'
        assert driver.find_element_by_id("excel1").is_displayed()
        assert driver.find_element_by_id("day_box").is_displayed()
        # Submit the subscription form with all the details.
        random_number = str(randint(10, 999))
        name = "TestSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("next_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'noty_text')))
        time.sleep(1)
        # Click again on make a subscription button
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()
        # Enter symbol in text user name text field
        wait.until(EC.visibility_of_element_located((By.ID, 'time')))
        driver.find_element_by_id("sub_name").send_keys("*#@")
        # Verify time
        driver.find_element_by_id("time").is_displayed()
        # Verify error message "Only use letters and numbers."
        driver.find_element_by_id("next_btn").click()

        expected_error_message = "Only use letters and numbers."
        actual_error_message = driver.find_element_by_id("sub_name").get_attribute("title")
        assert actual_error_message in expected_error_message
        # Click Cancel button to close modal dialog
        driver.find_element_by_class_name("btn-default").click()

    # ==================================C717==========29 Jan=============================================
    def test_external_contents_in_Subscription_form_C717(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # External user - Reports - Product Usage - Verify submitted subscription show in the "subscription" page.
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Product Usage
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Out of Stock')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Product Usage").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'customerNumber')))
        # Select the client from the drop down.
        wait.until(EC.visibility_of_element_located((By.ID, 'customerNumber')))
        clients = Select(driver.find_element_by_id('customerNumber'))
        clients.select_by_visible_text('ARPM')
        # Click on Make a Subscription button
        wait.until(EC.visibility_of_element_located((By.ID, 'subscription_btn')))
        driver.find_element_by_id("subscription_btn").click()
        # Verify Modal Dialog Text
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        modal_text = driver.find_element_by_id("myModalLabel").text
        assert modal_text == 'Subscription for: Product Usage Report for ARPM'
        assert driver.find_element_by_id("excel1").is_displayed()
        assert driver.find_element_by_id("day_box").is_displayed()
        random_number = str(randint(10, 999))
        name = "TestSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        # Verify Save Subscription button is displayed
        assert driver.find_element_by_id("next_btn").is_displayed()
        driver.find_element_by_id("next_btn").click()
        time.sleep(1)
        # On subscriptions page, Subscription name should display with Modify and Delete button.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Subscriptions')))
        driver.find_element_by_link_text("Subscriptions").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'jobs_table')))
        newname_value = driver.find_element_by_id("jobs_table").text
        assert name in newname_value

        # Verify Delete Button for newly created Subscription
        # Check number of subscriptions
        trs = driver.find_element_by_id('jobs_table').find_elements_by_tag_name('tr')
        time.sleep(1)
        trsc = len(trs)
        # Get number of modify buttons
        trm = driver.find_elements_by_link_text("Modify")
        trmc = len(trm)
        # Get number of Delete buttons
        trd = driver.find_elements_by_link_text("Delete")
        trdc = len(trd)

        # Check number of subscriptions equal to Modify buttons
        assert int(trsc) == int(trmc)
        # Check number of subscriptions equal to Delete buttons
        assert int(trsc) == int(trdc)

    # ==================================C727==========29 Jan=============================================
    def test_external_days_dropdown_values_product_usage_reportpage_C727(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # External user - Reports/operations/Inventory/Product Usage] To Verify the "Days" drop down functionality.
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Product Usage
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Product Usage')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Product Usage").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'customerNumber')))
        # Verify  header
        expected_header = "Product Usage Report"
        actual_header = driver.find_element_by_id("content-header").text
        assert actual_header in expected_header
        assert driver.find_element_by_id('customerNumber')
        # Select the client from the drop down.
        clients = Select(driver.find_element_by_id('customerNumber'))
        clients.select_by_visible_text('ARPM')
        actual_selected_option = clients.first_selected_option.text
        expected_selection_option = "ARPM"
        assert expected_selection_option in actual_selected_option
        # Check Make a subscription button right side of the page.
        assert driver.find_element_by_id("subscription_btn").is_displayed()
        # Check iDays values for report generation exist in the drop down
        idays = Select(driver.find_element_by_id('iDays'))
        idays.select_by_value("30")
        assert (idays.first_selected_option.text == "30 Days")
        idays.select_by_value("90")
        assert (idays.first_selected_option.text == "90 Days")
        idays.select_by_value("7")
        assert (idays.first_selected_option.text == "7 Days")
        time.sleep(1)
    # ================================C167===============29 Jan====================
    def test_ExternalVerifyEmailIdDisplayByDefaultInSubscription_C167(self, impersonate_external):
        #  Verify user email Id display by default in subscription form.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory on Hand tab.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'fa-folder-open-o')))
        ioh = driver.find_elements_by_class_name('fa-folder-open-o')
        ioh[1].click()
        time.sleep(1)
        # Verify Inventory on Hand Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Inventory_On_Hand_Report = "Inventory on Hand Report"
        actual_header_Inventory_On_Hand_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_On_Hand_Report in expected_header_Inventory_On_Hand_Report
        # Click on make a subscription button.
        driver.find_element_by_id("subscription_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal-title')))
        expected_Subscription_PopUp = "Subscription for: Inventory Report for ARPM"
        actual_Subscription_PopUp = driver.find_element_by_id("myModalLabel").text
        assert actual_Subscription_PopUp in expected_Subscription_PopUp
        # Verify the "Email To" text box.
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        exp_value = "clipford@ggoutfitters.com"
        actual_value = driver.find_element_by_id("email").get_attribute("value")
        assert exp_value in actual_value
        time.sleep(1)

    # ================================C203===============29 Jan=======================================================

    def test_ExternalVerifyBackButtonFunctionalityInSubscription_C203(self, impersonate_external):
        #  Verify Back button functionality on the subscription form.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory on Hand tab.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'fa-folder-open-o')))
        ioh = driver.find_elements_by_class_name('fa-folder-open-o')
        ioh[1].click()
        # Verify Inventory on Hand Report page
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Inventory_On_Hand_Report = "Inventory on Hand Report"
        actual_header_Inventory_On_Hand_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_On_Hand_Report in expected_header_Inventory_On_Hand_Report
        # Click on make a subscription button.
        driver.find_element_by_id("subscription_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal-title')))
        time.sleep(1)
        expected_Subscription_PopUp = "Subscription for: Inventory Report for ARPM"
        actual_Subscription_PopUp = driver.find_element_by_id("myModalLabel").text
        assert actual_Subscription_PopUp in expected_Subscription_PopUp
        # Click on back button so that subscription should not saved
        driver.find_element_by_class_name("btn-default").click()
        # Verify Inventory on Hand Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Inventory_On_Hand_Report = "Inventory on Hand Report"
        actual_header_Inventory_On_Hand_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_On_Hand_Report in expected_header_Inventory_On_Hand_Report
        time.sleep(1)


    # ================================C288===============29 Jan========================================================
    def test_ExternalVerifyExportButtonFunctionality_C288(self, impersonate_external):
        #  Verify Export button visibility in generated report.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory Receipts tab.
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Inventory Receipts").click()
        time.sleep(1)
        # Verify Inventory Receipts Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Inventory_Receipts_Report = "Inventory Receipts Report "
        actual_header_Inventory_Receipts_Report = driver.find_element_by_id("content-header").text
        time.sleep(1)
        assert actual_header_Inventory_Receipts_Report in expected_header_Inventory_Receipts_Report
        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("CustomerNumber"))
        select.select_by_visible_text("ARPM")

        # Select the Start and end date
        wait.until(EC.visibility_of_element_located((By.NAME,'daterange')))
        driver.find_element_by_name("daterange").click()
        time.sleep(1)
        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("02/22/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("02/24/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)

        # Click on Generate report button.
        driver.find_element_by_id("sub_btn").click()
        # Switch to report content
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_displayed()
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl04_ctl00_ButtonLink").click()
        # Verify report can be exported in following format
        assert driver.find_element_by_class_name("HoverButton").is_displayed()
        act = driver.find_elements_by_class_name("ActiveLink")
        exp_report_type = ['CSV (comma delimited)', 'Excel', ]
        for v in act:
            name = v.text
            assert name in exp_report_type
        time.sleep(1)

    # ================================C290===============29 Jan===========================================================
    def test_ExternalVerifyContentOfGeneratedReport_C290(self, impersonate_external):
        #  Verify the content of generated report..
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory Receipts tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory Receipts')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Inventory Receipts").click()
        # Verify Inventory Receipts Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        time.sleep(1)
        expected_header_Inventory_Receipts_Report = "Inventory Receipts Report "
        actual_header_Inventory_Receipts_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_Receipts_Report in expected_header_Inventory_Receipts_Report
        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("CustomerNumber"))
        select.select_by_visible_text("ARPM")
        # Select the Start and end date
        wait.until(EC.visibility_of_element_located((By.NAME,'daterange')))
        driver.find_element_by_name("daterange").click()
        time.sleep(1)
        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("02/22/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("02/24/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)
        # Click on Generate report button.
        driver.find_element_by_id("sub_btn").click()
        # Switch to report content
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)

        # Verify the first page
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_First_ctl01_ctl00").is_displayed()
        # Verify the Previous page
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Previous_ctl01_ctl00").is_displayed()
        # Verify the current page text box
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_displayed()
        # Verify the  Total Pages
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()
        # Verify the next Page
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Next").is_displayed()
        # Verify the last Pages
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Last").is_displayed()
        # Verify search text box
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl00").is_displayed()
        # Verify find link
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl01").is_displayed()
        # Verify find next link
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl03").is_displayed()
        # Verify export button
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl04_ctl00_ButtonImg").is_displayed()
        # Verify refresh button
        assert driver.find_element_by_name("ReportViewerControl$ctl05$ctl05$ctl00$ctl00$ctl00").is_displayed()
        # Verify export to data feed button
        assert driver.find_element_by_name("ReportViewerControl$ctl05$ctl07$ctl00$ctl00$ctl00").is_displayed()

        # Verify report content
        tr = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        arr = tr.split("\n")
        exp_data = ['SKU', 'Description', 'PO Issue Date', 'Due Date', 'Date Received', 'Qty on Order',
                       'Qty Received', 'Vendor', 'PO Number', 'Received By']
        for i in range(len(exp_data)):
            assert exp_data[i] in arr
        time.sleep(1)


    # ==================================C686===========29 Jan========================================================
    def test_ExternalVerifySubmittedSubscriptionShowSubscriptionPage_C686(self, impersonate_external):
        # Verify submitted subscription show in the "subscription"page.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory Receipts tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory Receipts')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Inventory Receipts").click()
        time.sleep(1)
        # Verify Inventory Receipts Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Inventory_Receipts_Report = "Inventory Receipts Report "
        actual_header_Inventory_Receipts_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_Receipts_Report in expected_header_Inventory_Receipts_Report
        # Click on make a subscription button.
        driver.find_element_by_id("subscription_btn").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal-title')))
        # Submit the subscription form with all the details.
        random_number = str(randint(10, 999))
        name = "TestSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        # Click save
        driver.find_element_by_id("next_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'noty_text')))
        # Subscription form submitted successfully and display message Subscription Saved.
        expected_message = "Subscription saved."
        actual_message = driver.find_element_by_class_name("noty_text").text
        assert expected_message in actual_message
        # Click on Subscriptions Page
        time.sleep(1)
        driver.find_element_by_link_text("Subscriptions").click()
        # On subscriptions page, Subscription name should reflect with Modify and Delete button.
        wait.until(EC.visibility_of_element_located((By.ID, 'jobs_table')))
        time.sleep(3)
        NameNew_value = driver.find_element_by_id("jobs_table").text
        time.sleep(1)
        assert name in NameNew_value
        # Verify Delete Button for newly created Subscription
        # Check number of subscriptions
        trs = driver.find_element_by_id('jobs_table').find_elements_by_tag_name('tr')
        time.sleep(1)
        trsc = len(trs)
        # Get number of modify buttons
        trm = driver.find_elements_by_link_text("Modify")
        trmc = len(trm)
        # Get number of Delete buttons
        trd = driver.find_elements_by_link_text("Delete")
        trdc = len(trd)

        # Check number of subscriptions equal to Modify buttons
        assert int(trsc) == int(trmc)
        # Check number of subscriptions equal to Delete buttons
        assert int(trsc) == int(trdc)

    # ==================================C715==========01 Feb =============================================
    def test_external_product_usage_modaldialog_invalidsubscriptionname_C715(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text('Inventory').click()
        time.sleep(1)
        # Click on Product Usage
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Product Usage')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Product Usage").click()
        time.sleep(1)
        # Select the client from the drop down.
        wait.until(EC.visibility_of_element_located((By.ID, 'customerNumber')))
        clients = Select(driver.find_element_by_id('customerNumber'))
        clients.select_by_visible_text('ARPM')

        # Click on Make a Subscription button
        driver.find_element_by_id("subscription_btn").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'myModalLabel')))
        # Verify Modal Dialog Text
        modal_text = driver.find_element_by_id("myModalLabel").text
        assert modal_text == 'Subscription for: Product Usage Report for ARPM'
        assert driver.find_element_by_id("excel1").is_displayed()
        assert driver.find_element_by_id("day_box").is_displayed()
        # Verify Valid Subscription Name
        # Submit the subscription form with all the details.
        random_number = str(randint(10, 999))
        name = "TestSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("next_btn").click()
        time.sleep(1)
        # Click again on make a subscription button
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()
        # Enter symbol in text user name text field
        wait.until(EC.visibility_of_element_located((By.ID, 'sub_name')))
        driver.find_element_by_id("sub_name").send_keys("*#@")
        # Verify time
        driver.find_element_by_id("time").is_displayed()
        # Verify error message "Only use letters and numbers."
        driver.find_element_by_id("next_btn").click()
        expected_error_message = "Only use letters and numbers."
        actual_error_message = driver.find_element_by_id("sub_name").get_attribute("title")
        assert actual_error_message in expected_error_message
        # Click back button to close modal dialog
        driver.find_element_by_class_name("btn-default").click()
        time.sleep(1)

    # ==================================C716==========01 Feb =============================================
    def test_Externaluser_product_usage_report_refresh_C716(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # =External user- Reports/operations/Inventory/Product Usage- Verify refresh button functionality in the report.
        # Click on Reports tab
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Product Usage
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Product Usage')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Product Usage").click()
        time.sleep(1)
        # Verify page header
        expected_header = "Product Usage Report"
        actual_header = driver.find_element_by_id("content-header").text
        assert actual_header in expected_header
        # Check Customer id control
        assert driver.find_element_by_id('customerNumber')
        # check Days dropdown
        assert driver.find_element_by_id('iDays')
        # Check Make a subscription button right side of the page.
        assert driver.find_element_by_id("subscription_btn").is_displayed()
        # check Generate report button visibility
        assert driver.find_element_by_id("sub_btn").is_displayed()
        driver.find_element_by_id("sub_btn").click()
        # Check report loads
        wait.until(EC.visibility_of_element_located((By.ID, 'report_src')))
        driver.switch_to.frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(4)
        # Verify current page is displayed
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_displayed()
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl00_CurrentPage')))
        # Verify Report Refresh control
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl05_ctl00_ctl00").is_displayed()
        driver.find_element_by_name("ReportViewerControl$ctl05$ctl05$ctl00$ctl00$ctl00").click()
        # Check on clicking Refresh , Cancel dialog shows up with Loading... & Cancel text
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Cancel')))
        assert driver.find_element_by_link_text("Cancel").is_displayed()
        msg = driver.find_element_by_class_name("WaitInfoCell").text
        assert re.search('Loading...', msg, re.IGNORECASE)
        assert re.search('Cancel', msg)
        # Check content before and after Refresh is different
        original_text = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        latest_text = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        assert (original_text is not latest_text)
        time.sleep(1)
    
    # ==================================C299==========02 Feb =============================================
    
    def test_externaluser_Subscription_VerifyModifyFunctionalityInSubscriptionPage_C299(self, impersonate_external):
        # Verify 'Subscription for: Executive Accounts Receivable' form on clicking 'Modify' link of subscription.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # click on Reports Tab
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        time.sleep(1)
        # Click on Subscription on left panel
        driver.find_element_by_class_name("fa-rss-square").click()
        time.sleep(1)
        # Click on modify link and verify the 'Subscription for: Executive Accounts Receivable' form.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Modify')))
        driver.find_element_by_partial_link_text("Modify").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID,'myModal')))
        expected_Subscription_PopUp ="Subscription for:"
        actual_Subscription_PopUp=driver.find_element_by_id("myModalLabel").text
        #print(actual_Subscription_PopUp)

        assert expected_Subscription_PopUp in actual_Subscription_PopUp
        # Cancel Subscription
        driver.find_element_by_class_name("btn-default").click()
        time.sleep(1)
    # ==================================C687==========02 Feb =============================================
    
    def test_externaluser_Reports_Operations_VerifySubmittedSubscriptionShowInSubscriptionPage_C687(self, impersonate_external):
        driver = impersonate_external['webdriver']
        # Verify submitted subscription is displayed in subscription page.
        wait = WebDriverWait(driver, 90)
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory on Hand tab.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'fa-folder-open-o')))
        ioh = driver.find_elements_by_class_name('fa-folder-open-o')
        ioh[1].click()
        time.sleep(1)
        # Verify Inventory on Hand Report page
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header_Inventory_On_Hand_Report ="Inventory on Hand Report"
        actual_header_Inventory_On_Hand_Report=driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_On_Hand_Report in expected_header_Inventory_On_Hand_Report

        #Click on make a subscription button
        driver.find_element_by_id("subscription_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'modal-title')))

        expected_Subscription_PopUp ="Subscription for: Inventory Report for ARPM"
        actual_Subscription_PopUp=driver.find_element_by_id("myModalLabel").text
        assert actual_Subscription_PopUp in expected_Subscription_PopUp

        #Submit the subscription form with all the details.
        random_number=str(randint(10,999))
        name="TestBSubscription"+random_number
        driver.find_element_by_id("sub_name").send_keys(name)

        driver.find_element_by_id("email").clear()
        email="apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("next_btn").click()

        # Subscription form submitted successfully and display message Subscription Saved.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'noty_text')))
        time.sleep(1)
        expected_message="Subscription saved."
        actual_message=driver.find_element_by_class_name("noty_text").text
        assert expected_message in actual_message

        # Click on subscription link and verify newly created subscription displayed on subscription page.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'fa-rss-square')))
        driver.find_element_by_class_name("fa-rss-square").click()
        assert driver.find_element_by_partial_link_text("Modify").is_displayed()
        assert driver.find_element_by_partial_link_text("Delete").is_displayed()
        tableContent = driver.find_element_by_id("jobs_table").text
        assert name in tableContent
        time.sleep(1)
    # ==================================C296==========02 Feb =============================================
    
    def test_externaluser_VerifySubscriptionNameTextBoxAllowOnlyLettersAndNumber_C296(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Report Tab
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory on Hand tab.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'fa-folder-open-o')))
        ioh = driver.find_elements_by_class_name('fa-folder-open-o')
        ioh[1].click()
        time.sleep(1)
        # Verify Inventory on Hand Report page
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header_Inventory_On_Hand_Report ="Inventory on Hand Report"
        actual_header_Inventory_On_Hand_Report=driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_On_Hand_Report in expected_header_Inventory_On_Hand_Report

        # Click on make a subscription button.
        wait.until(EC.visibility_of_element_located((By.ID,'subscription_btn')))
        time.sleep(1)
        driver.find_element_by_id("subscription_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'modal-title')))
        time.sleep(1)
        expected_Subscription_PopUp ="Subscription for: Inventory Report for ARPM"
        actual_Subscription_PopUp=driver.find_element_by_id("myModalLabel").text
        assert actual_Subscription_PopUp in expected_Subscription_PopUp

        #Submit the subscription form with all the details.
        random_number=str(randint(10,999))
        name="TestBSubscription"+random_number
        driver.find_element_by_id("sub_name").send_keys(name)

        driver.find_element_by_id("email").clear()
        email="apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("next_btn").click()

        # Subscription form submitted successfully and display message Subscription Saved.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'noty_text')))
        expected_message="Subscription saved."
        actual_message=driver.find_element_by_class_name("noty_text").text
        assert expected_message in actual_message

        # Click on 'Make a subscription' link and enter special characters in subscription text box.
        wait.until(EC.visibility_of_element_located((By.ID,'subscription_btn')))
        time.sleep(1)
        driver.find_element_by_id("subscription_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'modal-title')))
        driver.find_element_by_id("sub_name").send_keys("*%&")
        driver.find_element_by_id("next_btn").click()
        wait.until(EC.visibility_of_element_located((By.ID,'sub_name')))

        # Verify the warning message.
        expected_message="Only use letters and numbers."
        actual_message=driver.find_element_by_id("sub_name").get_attribute("title")
        assert expected_message in actual_message
        # close subscription dialog
        driver.find_element_by_class_name("btn-default").click()

    # ==================================C197==========03 Feb =============================================
    
    def test_externaluser_Order_VerifyPaginationFunctionalityOnOrderSearchPage_C197(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Verify pagination functionality on 'Order Search' page.
        # Open the 'Order search page and verify the Order Search page opened properly.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        driver.find_element_by_link_text("Orders").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Order Search')))
        driver.find_element_by_link_text("Order Search").click()

        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        time.sleep(1)
        actualTitle = driver.find_element_by_id("content-header").text
        expectedTitle = "Order Search"
        assert expectedTitle in actualTitle

        # Click Advanced filters button
        # wait.until(EC.visibility_of_element_located((By.ID,'toggle')))
        # driver.find_element_by_id("toggle").click()
        time.sleep(1)
        # Click Search button
        wait.until(EC.visibility_of_element_located((By.ID,'gen_search')))
        driver.find_element_by_id("gen_search").click()
        wait.until(EC.visibility_of_element_located((By.ID,'orders_table_previous')))
        time.sleep(4)
        # Verify by default previous button is displayed as disabled.
        expected_disable_previous = "disabled"
        actual_disable_previous = driver.find_element_by_id("orders_table_previous").get_attribute("class")
        assert expected_disable_previous in actual_disable_previous
        expected_current_page_color = "rgba(229, 65, 45, 1)"

        # Verify error message from orders table if empty
        wait.until(EC.visibility_of_element_located((By.ID,'orders_table')))
        ord_tab_content = driver.find_element_by_id("orders_table").text
        no_data_message = "No results found for your search."
        if no_data_message in ord_tab_content:
            flag = 2
            assert no_data_message in ord_tab_content
        else:
            # data exists
            flag = 1

        if flag == 1 and driver.find_element_by_link_text("2").is_displayed():
        # Verify link '2' is displayed, if displayed then click and verify pagination functionality. orders_table_next
        #if driver.find_element_by_link_text("2").is_displayed():
            next_Button = driver.find_element_by_id("orders_table_next").get_attribute("class")
            assert expected_disable_previous not in next_Button
            driver.find_element_by_link_text("2").click()
            time.sleep(5)
            actual_disable_previous = driver.find_element_by_id("orders_table_previous").get_attribute("class")
            assert expected_disable_previous not in actual_disable_previous
            actual_current_page_color = driver.find_element_by_link_text("2").value_of_css_property("background-color")
            assert expected_current_page_color in actual_current_page_color

            # Click on '1' link and verify the pagination functionality.
            driver.find_element_by_link_text("1").click()
            time.sleep(5)
            actual_current_page_color = driver.find_element_by_link_text("1").value_of_css_property("background-color")
            assert expected_current_page_color in actual_current_page_color

    # ==================================C196==========03 Feb =============================================
    
    def test_externaluser_Order_VerifySortingFunctionalityOnInOrder_OrdersSearch_C196(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Verify search columns value are sorted properly on order search page.
        # Open the 'Order search page and verify the Order Search page opened properly.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Order Search')))
        driver.find_element_by_link_text("Order Search").click()
        time.sleep(1)
        actualTitle = driver.find_element_by_id("content-header").text
        expectedTitle = "Order Search"
        assert expectedTitle in actualTitle

        # Click Advanced filters button
        #wait.until(EC.visibility_of_element_located((By.ID,'toggle')))
        #driver.find_element_by_id("toggle").click()
        time.sleep(1)
        # Click Search button
        wait.until(EC.visibility_of_element_located((By.ID,'gen_search')))
        driver.find_element_by_id("gen_search").click()
        wait.until(EC.visibility_of_element_located((By.ID,'orders_table_previous')))


        # Verify ascending and descending order for 'Id' column on 'Order Search' page.
        expected_Ascending_order="ascending"
        expected_Descending_order="descending"

        # Verify error message from orders table if empty
        wait.until(EC.visibility_of_element_located((By.ID,'orders_table')))
        ord_tab_content = driver.find_element_by_id("orders_table").text
        no_data_message = "No results found for your search."
        if no_data_message in ord_tab_content:
            flag = 2
            assert no_data_message in ord_tab_content
        else:
            # data exists
            flag = 1
        if flag == 1:
            actual_order = driver.find_element_by_id("orders_table").find_element_by_class_name("col-id").get_attribute("aria-sort")
            assert actual_order in expected_Ascending_order
            driver.find_element_by_class_name("col-id").click()
            time.sleep(3)
            actual_order=driver.find_element_by_class_name("col-id").get_attribute("aria-sort")
            assert actual_order in expected_Descending_order
            time.sleep(1)

            # Verify ascending and descending order for 'Client Name' column on 'Order Search' page.
            a=driver.find_elements_by_class_name("col-client-name")
            a[0].click()
            time.sleep(3)
            actual_order = driver.find_element_by_id("orders_table").find_element_by_class_name("col-client-name").get_attribute("aria-sort")
            assert  actual_order in expected_Ascending_order
            a=driver.find_element_by_class_name("col-client-name")
            a.click()
            time.sleep(3)
            actual_order=a.get_attribute("aria-sort")
            assert actual_order in expected_Descending_order
            time.sleep(1)

            # Verify ascending and descending order for 'Status' column on 'Order Search' page.
            a=driver.find_elements_by_class_name("col-status")
            a[0].click()
            time.sleep(3)
            actual_order = driver.find_element_by_id("orders_table").find_element_by_class_name("col-status").get_attribute("aria-sort")
            assert  actual_order in expected_Ascending_order
            a=driver.find_element_by_class_name("col-status")
            a.click()
            time.sleep(3)
            actual_order=a.get_attribute("aria-sort")
            assert actual_order in expected_Descending_order
            time.sleep(1)

            # Verify ascending and descending order for 'Date Submitted' column on 'Order Search' page.
            a=driver.find_elements_by_class_name("col-date-submitted")
            a[0].click()
            time.sleep(3)
            actual_order = driver.find_element_by_id("orders_table").find_element_by_class_name("col-date-submitted").get_attribute("aria-sort")
            assert  actual_order in expected_Ascending_order
            a=driver.find_element_by_class_name("col-date-submitted")
            a.click()
            time.sleep(3)
            actual_order=a.get_attribute("aria-sort")
            assert actual_order in expected_Descending_order
            time.sleep(1)

            # Verify ascending and descending order for 'Production Date' column on 'Order Search' page.
            a=driver.find_elements_by_class_name("col-date-pp")
            a[0].click()
            time.sleep(3)
            actual_order = driver.find_element_by_id("orders_table").find_element_by_class_name("col-date-pp").get_attribute("aria-sort")
            assert  actual_order in expected_Ascending_order
            a=driver.find_element_by_class_name("col-date-pp")
            a.click()
            time.sleep(3)
            actual_order=a.get_attribute("aria-sort")
            assert actual_order in expected_Descending_order
            time.sleep(1)
            # Verify ascending and descending order for 'Ship by date' column on 'Order Search' page.
            a=driver.find_elements_by_class_name("col-date-shipby")
            a[0].click()
            time.sleep(3)
            actual_order = driver.find_element_by_id("orders_table").find_element_by_class_name("col-date-shipby").get_attribute("aria-sort")
            assert  actual_order in expected_Ascending_order
            a=driver.find_element_by_class_name("col-date-shipby")
            a.click()
            time.sleep(3)
            actual_order=a.get_attribute("aria-sort")
            assert actual_order in expected_Descending_order
            time.sleep(1)

    # ==================================C240==========03 Feb =============================================
    
    def test_externaluser_Reports_Operations_VerifyBlankFieldSubscriptionNotSubmitted_C240(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Verify application not allowed to submit subscription with blank data fields.
        #Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Operations')))
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        #Click on 'Out of stock' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Out of Stock')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Out of Stock").click()
        time.sleep(1)
        # Verify 'Out of stock' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header_report ="Out of Stock Report"
        actual_header_report=driver.find_element_by_id("content-header").text
        assert actual_header_report in expected_header_report

        time.sleep(1)
        # Click on 'Make a subscription' button
        wait.until(EC.visibility_of_element_located((By.ID,'subscription_btn')))
        time.sleep(1)
        driver.find_element_by_id("subscription_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'modal-title')))


        # Verify if expected form has been opened up on clicking 'Make a Subscription'
        expected_Subscription_PopUp ="Subscription for: Out of Stock Report for ARPM"
        actual_Subscription_PopUp=driver.find_element_by_id("myModalLabel").text
        assert actual_Subscription_PopUp in expected_Subscription_PopUp

        # Click on submit button and Verify Subscription form remain displaying.
        driver.find_element_by_id("next_btn").click()
        time.sleep(1)
        assert driver.find_element_by_id("myModalLabel").is_displayed()
        # Click back to close popup
        driver.find_element_by_class_name("btn-default").click()
        time.sleep(1)
        # Note : Error message 'error message " Please fill out this field".' is not verified because id is not found.

    # ==================================C171==========03 Feb =============================================
    
    def test_externaluser_Order_VerifyContentInSearchResultOnOrdersSearch_C171(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Verify the content in search result on 'Order Search' page.
        # Open the 'Order search page and verify the Order Search page opened properly.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        driver.find_element_by_link_text("Orders").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Order Search')))
        driver.find_element_by_link_text("Order Search").click()
        time.sleep(1)
        actualTitle = driver.find_element_by_id("content-header").text
        expectedTitle = "Order Search"
        assert expectedTitle in actualTitle

        # Click Advanced filters button
        #wait.until(EC.visibility_of_element_located((By.ID,'toggle')))
        #driver.find_element_by_id("toggle").click()

        # Click Search button
        wait.until(EC.visibility_of_element_located((By.ID,'gen_search')))
        driver.find_element_by_id("gen_search").click()
        wait.until(EC.visibility_of_element_located((By.ID,'orders_table_previous')))

        # Verify error message from orders table if empty
        wait.until(EC.visibility_of_element_located((By.ID,'orders_table')))
        ord_tab_content = driver.find_element_by_id("orders_table").text
        no_data_message = "No results found for your search."
        if no_data_message in ord_tab_content:
            flag = 2
            assert no_data_message in ord_tab_content
        else:
            # data exists
            flag = 1
        if flag == 1:
            # Verify if expected content is displayed in search result on 'Order Search' page.
            driver.find_element_by_class_name("ColVis_MasterButton").is_displayed()
            driver.find_element_by_class_name("input-sm").is_displayed()
            driver.find_element_by_id("orders_table_paginate").is_displayed()
            driver.find_element_by_id("orders_table_wrapper").find_element_by_class_name("ColVis_MasterButton").click()
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'ColVis_collection')))
            actual=driver.find_element_by_class_name("ColVis_collection").text
            time.sleep(1)
            # Verify if expected column exists in search result.
            expected = ["ID","Client Name","Status","Sales Rep","Date Submitted","Production Date","Ship-by Date","Tracking","Invoice", "Order Origin"]
            size=len(expected)
            for i in range(size):
                assert expected[i] in actual
            driver.refresh()
            time.sleep(4)

    # ==================================C172==========03 Feb =============================================
    
    def test_externaluser_Order_VerifyChangeColumnFunctionalityInSearchResultOnOrdersSearch_C172(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Verify the Change column functionality in search result on 'Order Search' page.
        # Open the 'Order search page and verify the Order Search page opened properly.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        driver.find_element_by_link_text("Orders").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Order Search')))
        driver.find_element_by_link_text("Order Search").click()
        time.sleep(1)
        actualTitle = driver.find_element_by_id("content-header").text
        expectedTitle = "Order Search"
        assert expectedTitle in actualTitle

        # Click Advanced filters button
        # wait.until(EC.visibility_of_element_located((By.ID,'toggle')))
        # driver.find_element_by_id("toggle").click()
        time.sleep(1)
        # Click Search button
        wait.until(EC.visibility_of_element_located((By.ID,'gen_search')))
        driver.find_element_by_id("gen_search").click()
        wait.until(EC.visibility_of_element_located((By.ID,'orders_table_previous')))
        time.sleep(1)

        # Verify error message from orders table if empty
        wait.until(EC.visibility_of_element_located((By.ID,'orders_table')))
        ord_tab_content = driver.find_element_by_id("orders_table").text
        no_data_message = "No results found for your search."
        if no_data_message in ord_tab_content:
            flag = 2
            assert no_data_message in ord_tab_content
        else:
            # data exists
            flag = 1
        if flag == 1:
            # Click on 'Change Column' button and observe that the all header name are displayed under list
            driver.find_element_by_id("orders_table_wrapper").find_element_by_class_name("ColVis_MasterButton").click()
            actual=driver.find_element_by_class_name("ColVis_collection").text
            for tr in driver.find_elements_by_id('orders_table'):
                ths=tr.find_elements_by_tag_name('th')
                if ths:
                    data= [th.text for th in ths]
            array = actual.split("\n")
            size = len(data)
            for i in range(size):
                assert data[i] in array
            driver.refresh()
            time.sleep(4)
    # ===========================250===================================08 feb=================================================
    
    def test_ExternalReportOperationInventoryOpenPurchaseOrder_VerifyPaginationfunctionality_C250(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)	
        
        # Open the 'Open Purchase Orders and verify the Open Purchase Orders page opened properly.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()

        #Click on 'Open Purchase Orders' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Open Purchase Orders')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Open Purchase Orders").click()
        time.sleep(1)
        # Verify 'Open Purchase Orders' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Open Purchase Orders Report"
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        # Click on Generate report button
        driver.find_element_by_id("sub_btn").click()
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)

        # Verify the first page
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_First_ctl01_ctl00").is_displayed()

        tp = driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").text
        tps = tp.split(" ")
        tpcnt = tps[0]
        # If total pages are 1
        if int(tpcnt) == 1:
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_First_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Previous_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Next_ctl00').get_attribute("class") == "NormalButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Last_ctl00').get_attribute("class") == "NormalButton"

        # Check next page & previous if total pages > 1
        if int(tpcnt) > 1:
            # Click Last button and verify controls NormalButton
            driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Last_ctl00_ctl00').click()
            time.sleep(5)
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Next_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Last_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Previous_ctl00').get_attribute("class") == "NormalButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_First_ctl00').get_attribute("class") == "NormalButton"
            # Click on First button
            driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_First_ctl00_ctl00').click()
            time.sleep(10)
            # Check First,Last,Next,Prev state
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_First_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Previous_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Next_ctl00').get_attribute("class") == "NormalButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Last_ctl00').get_attribute("class") == "NormalButton"

    # ===========================228=============================08 feb=======================================================
    def test_ExternalBookMarks_VerifySortingfunctionality_C228(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Open the 'BookMarks' page.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        driver.find_element_by_link_text("Orders").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Order Search')))
        time.sleep(1)
        driver.find_element_by_css_selector(".fa.fa-bookmark-o.fa-fw").click()  # Click on Bookmark
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        actualTitle = driver.find_element_by_id("content-header").text
        expectedTitle = "Bookmarks"
        assert expectedTitle in actualTitle
        wait.until(EC.visibility_of_element_located((By.ID, 'orders_table_previous')))
        time.sleep(1)

        # Verify error message from orders table if no Bookmark
        wait.until(EC.visibility_of_element_located((By.ID,'panel_body')))
        ord_tab_content = driver.find_element_by_id("panel_body").text
        no_data_message = "No Orders Bookmarked"
        if no_data_message in ord_tab_content:
            flag = 2
            assert no_data_message in ord_tab_content
        else:
            # data exists
            flag = 1

        # Verify ascending and descending order for 'Id' column on 'Order Search' page.
        expected_Ascending_order="ascending"
        expected_Descending_order="descending"
        time.sleep(1)

        # Get Headers  of displayed columns data-column-index
        actualhdrs = driver.find_element_by_id('orders_table').find_elements_by_tag_name('th')

        # Check Headers are visible and data exists before sorting
        if flag == 1 and len(actualhdrs) > 0:
            for i in range(0, len(actualhdrs)):
                time.sleep(1)
                print(driver.find_element_by_id("orders_table").find_elements_by_tag_name('th')[i].text)
                # Skip first col click as it is in ascending order
                if int(i) != 0:
                    actualhdrs[i].click()
                    time.sleep(3)
                asc_order = driver.find_element_by_id("orders_table").find_elements_by_tag_name('th')[i].get_attribute("aria-sort")
                print(asc_order)
                assert asc_order in expected_Ascending_order
                # Click column for Descending Order
                actualhdrs[i].click()
                time.sleep(3)
                desc_order = driver.find_element_by_id("orders_table").find_elements_by_tag_name('th')[i].get_attribute("aria-sort")
                print(desc_order)
                assert desc_order in expected_Descending_order

    # ========================================917================09 Feb==============================================

    def test_ExternalReportsInventoryByBusinessUnit_VerifyBlankFieldSubscriptionFieldNotSubmitted_C917(self, impersonate_external):
        driver = impersonate_external['webdriver']
        # Verify that user is not allowed to submit a subscription field with blank fields.
        wait = WebDriverWait(driver, 90)
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on 'Inventory by Business Unit' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Open Purchase Orders')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Inventory by Business Unit").click()
        time.sleep(1)
        # Verify 'Inventory by Business Unit' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Inventory by Business Unit Report "
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        # Click on make a subscription button.
        wait.until(EC.visibility_of_element_located((By.ID,'subscription_btn')))
        time.sleep(1)
        driver.find_element_by_id("subscription_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'modal-title')))

        # Click on submit button and Verify Subscription form remain displaying.
        wait.until(EC.visibility_of_element_located((By.ID,'next_btn')))
        driver.find_element_by_id("next_btn").click()
        assert driver.find_element_by_id("myModalLabel").is_displayed()
        # Note : Error message 'error message " Please fill out this field".' is not verified because id is not found.

    # ========================================918================09 Feb==============================================

    def test_ExternalReportsInventoryByBusinessUnit_VerifyUserEmailIDDisplayedByDefault_C918(self, impersonate_external):
        driver = impersonate_external['webdriver']
        # Verify that user email id is displayed by default in email text box on subscription page of 'Inventory by business unit'.
        wait = WebDriverWait(driver, 90)
        # Open the 'Inventory by Business Unit' page and verify the page opened properly.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        #Click on 'Inventory by Business Unit' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Open Purchase Orders')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Inventory by Business Unit").click()
        time.sleep(1)
        # Verify 'Inventory by Business Unit' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Inventory by Business Unit Report "
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        #Click on make a subscription button.
        wait.until(EC.visibility_of_element_located((By.ID,'subscription_btn')))
        driver.find_element_by_id("subscription_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'modal-title')))

        # Verify the "Email To" text box.
        expected_email = "clipford@ggoutfitters.com"
        actual_email = driver.find_element_by_id("email").get_attribute("value")
        assert expected_email in actual_email
        driver.find_element_by_class_name("btn-default").click()
        time.sleep(1)

    # ========================================706================09 Feb==============================================

    def test_ExternaloperationsInventoryProductUsage_VerifyPaginationFunctionalityInGeneratedReport_C706(self, impersonate_external):
        driver = impersonate_external['webdriver']
        # verify the pagination functionality in generated report of 'Product Usage' page.
        wait = WebDriverWait(driver, 90)
        # Open the 'Product Usage' page and verify the 'Product Usage' page opened properly.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        #Click on 'Product Usage' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Open Purchase Orders')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Product Usage").click()
        time.sleep(1)
        # Verify 'Product Usage' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Product Usage Report"
        actual_header =driver.find_element_by_id("content-header").text
        assert actual_header in expected_header


        # Click on Generate report button
        driver.find_element_by_id("sub_btn").click()
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)

        # Verify the first page
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_First_ctl01_ctl00").is_displayed()

        tp = driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").text
        tps = tp.split(" ")
        tpcnt = tps[0]
        # If total pages are 1
        if int(tpcnt) == 1:
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_First_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Previous_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Next_ctl00').get_attribute("class") == "NormalButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Last_ctl00').get_attribute("class") == "NormalButton"

        # Check next page & previous if total pages > 1
        if int(tpcnt) > 1:
            # Click Last button and verify controls NormalButton
            driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Last_ctl00_ctl00').click()
            time.sleep(5)
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Next_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Last_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Previous_ctl00').get_attribute("class") == "NormalButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_First_ctl00').get_attribute("class") == "NormalButton"
            # Click on First button
            driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_First_ctl00_ctl00').click()
            time.sleep(10)
            # Check First,Last,Next,Prev state
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_First_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Previous_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Next_ctl00').get_attribute("class") == "NormalButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Last_ctl00').get_attribute("class") == "NormalButton"

    # ========================================165================09 Feb==============================================

    def test_ExternalReportoperationsInventoryOnHand_VerifyBlankFieldSubscriptionFieldNotSubmitted_C165(self, impersonate_external):
        driver = impersonate_external['webdriver']
        # Verify application doesn't allow to submit a subscription with blank field value on 'Inventory On hand' page.
        wait = WebDriverWait(driver, 90)
        # Verify the Change column functionality in search result on 'Order Search' page.
        # Open the 'Order search page and verify the Order Search page opened properly.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        #Click on 'Inventory on Hand' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Open Purchase Orders')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Inventory on Hand").click()
        time.sleep(1)
        # Verify 'Inventory on Hand' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header_Inventory_On_Hand_Report ="Inventory on Hand Report"
        actual_header_Inventory_On_Hand_Report=driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_On_Hand_Report in expected_header_Inventory_On_Hand_Report

        #Click on make a subscription button.
        wait.until(EC.visibility_of_element_located((By.ID,'subscription_btn')))
        driver.find_element_by_id("subscription_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'modal-title')))

        # Click on submit button and Verify Subscription form remain displaying.
        wait.until(EC.visibility_of_element_located((By.ID,'next_btn')))
        driver.find_element_by_id("next_btn").click()
        assert driver.find_element_by_id("myModalLabel").is_displayed()
        # Note : Error message 'error message " Please fill out this field".' is not verified because id is not found.

    # ========================================928================09 Feb==============================================

    def test_ExternalReportsInventoryByBusinessUnit_VerifySubmittedSubscription_C928(self, impersonate_external):
        driver = impersonate_external['webdriver']
        # Verify subscription has been submitted properly on 'Inventory By Business Unit' page.
        wait = WebDriverWait(driver, 90)
        # Open the 'Inventory by Business Unit' page and verify the 'Inventory by Business Unit' page opened properly.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on 'Inventory by Business Unit' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Open Purchase Orders')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Inventory by Business Unit").click()
        time.sleep(1)
        # Verify 'Inventory by Business Unit' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Inventory by Business Unit Report "
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        #Click on make a subscription button.
        wait.until(EC.visibility_of_element_located((By.ID,'subscription_btn')))
        driver.find_element_by_id("subscription_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'modal-title')))

        #Submit the subscription form with all the details.
        random_number=str(randint(10,999))
        name="TestSubscription"+random_number
        driver.find_element_by_id("sub_name").send_keys(name)

        driver.find_element_by_id("email").clear()
        email="apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("next_btn").click()

        # Subscription form submitted successfully and display message Subscription Saved.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'noty_text')))
        expected_message="Subscription saved."
        actual_message=driver.find_element_by_class_name("noty_text").text
        assert expected_message in actual_message
        time.sleep(1)
        # Click on subscription link and verify newly created subscription displayed on subscription page.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Subscriptions')))
        time.sleep(1)
        driver.find_element_by_link_text("Subscriptions").click()
        wait.until(EC.visibility_of_element_located((By.ID,'jobs_table')))
        time.sleep(1)
        assert driver.find_element_by_partial_link_text("Modify").is_displayed()
        assert driver.find_element_by_partial_link_text("Delete").is_displayed()
        tableContent = driver.find_element_by_id("jobs_table").text
        time.sleep(1)
        assert name in tableContent

    # ========================================916================10 Feb==============================================
    def test_ExternalReportsInventoryByBusinessUnit_VerifyContentInGeneratedReport_C916(self, impersonate_external):
        driver = impersonate_external['webdriver']
        # Verify the content in generated report on 'Inventory By Business Unit' page.
        wait = WebDriverWait(driver, 30)
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()

        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on 'Inventory by Business Unit' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Open Purchase Orders')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Inventory by Business Unit").click()
        time.sleep(1)
        # Verify 'Inventory by Business Unit' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Inventory by Business Unit Report "
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        # Click on Generate report button.
        driver.find_element_by_class_name("btn-success").click()
        # Verify the Date and Time of the generated report.
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(4)

        # Verify the first page
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_First_ctl01_ctl00").is_displayed()
        # Verify the Previous page
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Previous_ctl01_ctl00").is_displayed()
        # Verify the current page text box
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_displayed()
        # Verify the  Total Pages
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()
        # Verify the next Pages
        if driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Next_ctl00").is_displayed():
            assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Next_ctl00").is_displayed()
        else:
            assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Next_ctl01").is_displayed()
        # Verify the last Pages
        if driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Last_ctl00").is_displayed():
            assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Last_ctl00").is_displayed()
        else:
            assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Last_ctl01").is_displayed()

        # Verify search text box
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl00").is_displayed()
        # Verify find link
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl01").is_displayed()
        # Verify find next link
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl03").is_displayed()
        # Verify export button
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl04_ctl00_ButtonImg").is_displayed()
        # Verify refresh button
        assert driver.find_element_by_name("ReportViewerControl$ctl05$ctl05$ctl00$ctl00$ctl00").is_displayed()
        # Verify export to data feed button
        assert driver.find_element_by_name("ReportViewerControl$ctl05$ctl07$ctl00$ctl00$ctl00").is_displayed()
        # Verify report content
        act = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        exp_content = ['Premium', 'Business Unit', 'Premium Description', 'Total', 'Total All Business Units']
        for content in exp_content:
            assert content in act

    # ========================================920================10 Feb==============================================

    def test_ExternalReportsInventoryByBusinessUnit_VerifySubscriptionNameAcceptsOnlyLetterAndNumber_C920(self, impersonate_external):
        driver = impersonate_external['webdriver']
        # Verify subscription accept only letters and numbers on 'Inventory By Businee Unit' page.
        wait = WebDriverWait(driver, 30)
        # Open the 'Inventory by Business Unit' page and verify the page opened properly.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        #Click on 'Inventory by Business Unit' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Open Purchase Orders')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Inventory by Business Unit").click()
        time.sleep(1)
        # Verify 'Inventory by Business Unit' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Inventory by Business Unit Report "
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        #Click on make a subscription button.
        driver.find_element_by_id("subscription_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'modal-title')))

        #Submit the subscription form with all the details.
        random_number=str(randint(10,999))
        name="TestBSubscription"+random_number
        driver.find_element_by_id("sub_name").send_keys(name)

        driver.find_element_by_id("email").clear()
        email="apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("next_btn").click()

        # Subscription form submitted successfully and display message Subscription Saved.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'noty_text')))
        expected_message="Subscription saved."
        actual_message=driver.find_element_by_class_name("noty_text").text
        assert expected_message in actual_message

        time.sleep(1)
        # Click on 'Make a subscription' button
        wait.until(EC.visibility_of_element_located((By.ID,'subscription_btn')))
        time.sleep(1)
        driver.find_element_by_id("subscription_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'modal-title')))
        driver.find_element_by_id("sub_name").send_keys("*%&")
        driver.find_element_by_id("next_btn").click()
        wait.until(EC.visibility_of_element_located((By.ID,'sub_name')))

        # Verify the warning message.
        expected_message="Only use letters and numbers."
        actual_message=driver.find_element_by_id("sub_name").get_attribute("title")
        assert expected_message in actual_message

    # ========================================286================10 Feb==============================================
    def test_ExternalReportsOperationsInventoryInventoryReceipts_VerifyPagination_C286(self, impersonate_external):
        driver = impersonate_external['webdriver']
        # Verify tha pagination functionality in generated report on 'Inventory Receipt' page.
        wait = WebDriverWait(driver, 30)
        # Open the 'Inventory by Business Unit' page and verify the page opened properly.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        #Click on 'Inventory Receipt' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Open Purchase Orders')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Inventory Receipts").click()
        time.sleep(1)
        # Verify 'Inventory Receipt' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Inventory Receipts Report"
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        # Select the Start and end date
        wait.until(EC.visibility_of_element_located((By.NAME,'daterange')))
        driver.find_element_by_name("daterange").click()
        time.sleep(1)
        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("02/22/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("02/24/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)
        # Click on Generate report button.
        driver.find_element_by_id("sub_btn").click()
        # Switch to report content
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)

        # Verify the first page
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_First_ctl01_ctl00").is_displayed()

        tp = driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").text
        tps = tp.split(" ")
        tpcnt = tps[0]
        # If total pages are 1
        if int(tpcnt) == 1:
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_First_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Previous_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Next_ctl00').get_attribute("class") == "NormalButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Last_ctl00').get_attribute("class") == "NormalButton"

        # Check next page & previous if total pages > 1
        if int(tpcnt) > 1:
            # Click Last button and verify controls NormalButton
            driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Last_ctl00_ctl00').click()
            time.sleep(5)
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Next_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Last_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Previous_ctl00').get_attribute("class") == "NormalButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_First_ctl00').get_attribute("class") == "NormalButton"
            # Click on First button
            driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_First_ctl00_ctl00').click()
            time.sleep(10)
            # Check First,Last,Next,Prev state
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_First_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Previous_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Next_ctl00').get_attribute("class") == "NormalButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Last_ctl00').get_attribute("class") == "NormalButton"

    # ========================================298================10 Feb==============================================
    def test_ExternalReportsOpenPurchaseOrders_VerifySubscription_OnlyLettersAndNumber_C298(self, impersonate_external):
        driver = impersonate_external['webdriver']
        # Verify that subscription accepts only letters and number on 'Open Purchase Order' page.
        wait = WebDriverWait(driver, 30)
        # Open the 'Inventory by Business Unit' page and verify the page opened properly.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        #Click on 'Open Purchase Orders' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Open Purchase Orders')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Open Purchase Orders").click()
        time.sleep(1)
        # Verify 'Open Purchase Orders' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Open Purchase Orders Report"
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        #Click on make a subscription button.
        wait.until(EC.visibility_of_element_located((By.ID,'subscription_btn')))
        driver.find_element_by_id("subscription_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'modal-title')))

        #Submit the subscription form with all the details.
        random_number=str(randint(10,999))
        name="TestBSubscription"+random_number
        driver.find_element_by_id("sub_name").send_keys(name)

        driver.find_element_by_id("email").clear()
        email="apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("next_btn").click()

        # Subscription form submitted successfully and display message Subscription Saved.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'noty_text')))
        expected_message="Subscription saved."
        actual_message=driver.find_element_by_class_name("noty_text").text
        assert expected_message in actual_message
        time.sleep(1)
        # Click on 'Make a subscription' link and enter special characters in subscription text box.
        wait.until(EC.visibility_of_element_located((By.ID,'subscription_btn')))
        time.sleep(1)
        driver.find_element_by_id("subscription_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'modal-title')))
        driver.find_element_by_id("sub_name").send_keys("*%&")
        driver.find_element_by_id("next_btn").click()
        wait.until(EC.visibility_of_element_located((By.ID,'sub_name')))

        # Verify the warning message.
        expected_message="Only use letters and numbers."
        actual_message=driver.find_element_by_id("sub_name").get_attribute("title")
        assert expected_message in actual_message

    # ========================================275================10 Feb==============================================
    def test_ExternalReportsOperationsInventoryOpenPurchaseOrders_SubscriptionSubmitted_C275(self, impersonate_external):
        driver = impersonate_external['webdriver']
        # Verify that user is able to submit subscription properly.
        wait = WebDriverWait(driver, 30)
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        #Click on 'Open Purchase Orders' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Open Purchase Orders')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Open Purchase Orders").click()
        time.sleep(1)
        # Verify 'Open Purchase Orders' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Open Purchase Orders Report"
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        #Click on make a subscription button.
        wait.until(EC.visibility_of_element_located((By.ID,'subscription_btn')))
        driver.find_element_by_id("subscription_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'modal-title')))

        #Submit the subscription form with all the details.
        random_number=str(randint(10,999))
        name="TestSubscription"+random_number
        driver.find_element_by_id("sub_name").send_keys(name)

        driver.find_element_by_id("email").clear()
        email="apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("next_btn").click()

        # Subscription form submitted successfully and display message Subscription Saved.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'noty_text')))
        expected_message="Subscription saved."
        actual_message=driver.find_element_by_class_name("noty_text").text
        assert expected_message in actual_message
        time.sleep(1)
        # Click on subscription link and verify newly created subscription displayed on subscription page.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Subscriptions')))
        time.sleep(1)
        driver.find_element_by_link_text("Subscriptions").click()
        wait.until(EC.visibility_of_element_located((By.ID,'jobs_table')))
        assert driver.find_element_by_partial_link_text("Modify").is_displayed()
        assert driver.find_element_by_partial_link_text("Delete").is_displayed()
        time.sleep(1)
        tableContent = driver.find_element_by_id("jobs_table").text
        time.sleep(1)
        assert name in tableContent

    # =============================226=============2Dec==============================================================
    def test_Verify_Search_functionality_in_generated_Report_C226(self, impersonate_external):
        # Verify Search functionality in generated Report
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 30)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Out of stock tab.
        driver.find_element_by_link_text("Out of Stock").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_out_of_stock_report = "Out of Stock Report"
        actual_header_out_of_stock_report = driver.find_element_by_id("content-header").text
        assert actual_header_out_of_stock_report in expected_header_out_of_stock_report
        time.sleep(1)
        # Select the client from the drop down.
        wait.until(EC.visibility_of_element_located((By.ID, 'CustomerNumber')))
        clients = Select(driver.find_element_by_id('CustomerNumber'))
        clients.select_by_visible_text('ARPM')
        time.sleep(1)
        # Click on Generate Report button.
        driver.find_element_by_class_name("btn-success").click()
        # Report should be generated successfully on the same page.
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl00").send_keys("ARPM")
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl01").click()
        time.sleep(10)
        try:
            alert = driver.switch_to_alert()
            assert alert.text == "The search text was not found."
            alert.accept()
            alert_found = True
        except NoAlertPresentException as e:
            alert_found = False

        if alert_found == False:
            driver.find_element_by_css_selector("span[style='COLOR:highlighttext;BACKGROUND-COLOR:highlight;']").is_displayed()

        # Verify wrong entry could not be searched
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl00").send_keys("test12345")
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl01").click()
        time.sleep(1)
        try:
            WebDriverWait(driver, 15).until(EC.alert_is_present(), 'The search text was not found.')
            alert = driver.switch_to_alert()
            assert alert.text == "The search text was not found."
            alert.accept()
            alert_found3 = True
        except NoAlertPresentException as e:
            alert_found3 = False

    # ======================================C261=====22Dec===========================================================

    def test_ExternalVerifySearchFunctionalityInGeneratedReport_C261(self, impersonate_external):
        # Verify Search functionality in generated report.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 30)
        # Click on Reports tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        driver.find_element_by_link_text("Reports").click()
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Open Purchase Orders.
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Open Purchase Orders").click()
        time.sleep(1)
        # Verify  header
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Open_Purchase_Orders_Report = "Open Purchase Orders Report"
        actual_header_Open_Purchase_Orders_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Open_Purchase_Orders_Report in expected_header_Open_Purchase_Orders_Report
        # Click on generate report button
        driver.find_element_by_class_name("btn-success").click()
        # Switch to report
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(5)
        # Search SKU no "AARP00811"
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl00").send_keys("AARP00811")
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl01").click()
        time.sleep(10)
        try:
            alert = driver.switch_to_alert()
            assert alert.text == "The search text was not found."
            alert.accept()
            alert_found = True
        except NoAlertPresentException as e:
            alert_found = False

        if alert_found == False:
            driver.find_element_by_css_selector("span[style='COLOR:highlighttext;BACKGROUND-COLOR:highlight;']").is_displayed()

        # Verify wrong entry could not be searched
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl00").send_keys("test12345")
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl01").click()
        time.sleep(1)
        try:
            WebDriverWait(driver, 15).until(EC.alert_is_present(), 'The search text was not found.')
            alert = driver.switch_to_alert()
            assert alert.text == "The search text was not found."
            alert.accept()
            alert_found3 = True
        except NoAlertPresentException as e:
            alert_found3 = False

    # ======================================157==============================================================
    def test_ExternalVerifyContentsOnEditProfile_C157(self, impersonate_external):
        # Verify the contents on edit profile page.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 30)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        # Edit Profile check
        driver.find_element_by_class_name("fa-user").click()
        time.sleep(1)
        driver.find_element_by_class_name("fa-gears").click()
        time.sleep(4)
        # Edit User Profile(Label) is displayed
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'panel-heading')))
        expected_editUserLabel = "Edit User Profile"
        actual_editUserLabel = driver.find_element_by_class_name("panel-heading").text
        assert actual_editUserLabel in expected_editUserLabel
        # First Name (Text Field) is displayed
        assert driver.find_element_by_id("first_name").is_displayed()
        # Last Name (Text Field) is displayed
        assert driver.find_element_by_id("last_name").is_displayed()
        # Email (Text Field) is displayed
        assert driver.find_element_by_id("email").is_displayed()
        # Password (current)(Text Field) is displayed
        assert driver.find_element_by_name("password-current").is_displayed()
        # Password (new)(Text Field) is displayed
        assert driver.find_element_by_name("password-new").is_displayed()
        # Password (confirm)(Text Field) is displayed
        assert driver.find_element_by_name("password-new2").is_displayed()
        # Save(Button) is displayed
        assert driver.find_element_by_class_name("btn-success").is_displayed()


    # ==================================C158==========28 Jan=============================================
    def test_external_editprofile_save_C158(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 30)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        # Edit Profile check
        driver.find_element_by_class_name("fa-user").click()
        time.sleep(1)
        driver.find_element_by_class_name("fa-gears").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'first_name')))
        # Verify Edit User Profile(Label) is displayed
        expected_editUserLabel = "Edit User Profile"
        actual_editUserLabel = driver.find_element_by_class_name("panel-heading").text
        assert actual_editUserLabel in expected_editUserLabel
        # Actual Details
        fn = 'Chandra'
        ln = 'Lipford'
        email = 'clipford@aarp.org'
        # New details
        fn1 = 'Chandra1'
        ln1 = 'Lipford1'
        email1 = 'clipford1@aarp.org'
        # First Name (Text Field) is displayed
        assert driver.find_element_by_id("first_name").get_attribute('value') == fn
        # Last Name (Text Field) is displayed
        assert driver.find_element_by_id("last_name").get_attribute('value') == ln
        # Email (Text Field) is displayed
        assert driver.find_element_by_id("email").get_attribute('value') == email
        # Password (current)(Text Field) is displayed
        assert driver.find_element_by_name("password-current").is_displayed()
        # Password (new)(Text Field) is displayed
        assert driver.find_element_by_name("password-new").is_displayed()
        # Password (confirm)(Text Field) is displayed
        assert driver.find_element_by_name("password-new2").is_displayed()
        # Change field values to new
        driver.find_element_by_id("first_name").clear()
        driver.find_element_by_id("first_name").send_keys(fn1)
        driver.find_element_by_id("last_name").clear()
        driver.find_element_by_id("last_name").send_keys(ln1)
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys(email1)
        # Click Save
        time.sleep(1)
        driver.find_element_by_class_name("btn-success").click()
        time.sleep(5)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'fa-user')))
        # Verify saved details
        driver.find_element_by_class_name("fa-user").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'fa-gears')))
        driver.find_element_by_class_name("fa-gears").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'first_name')))
        # First Name (Text Field) is displayed
        assert driver.find_element_by_id("first_name").get_attribute('value') == fn1
        # Last Name (Text Field) is displayed
        assert driver.find_element_by_id("last_name").get_attribute('value') == ln1
        # Email (Text Field) is displayed
        assert driver.find_element_by_id("email").get_attribute('value') == email1
        ## Reset original values
        driver.find_element_by_id("first_name").clear()
        driver.find_element_by_id("first_name").send_keys(fn)
        driver.find_element_by_id("last_name").clear()
        driver.find_element_by_id("last_name").send_keys(ln)
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys(email)
        # Click Save
        time.sleep(1)
        assert driver.find_element_by_class_name("btn-success").is_displayed()
        driver.find_element_by_class_name("btn-success").click()
        time.sleep(4)
        # Click Dashboard
        driver.find_element_by_class_name("fa-dashboard").click()
        time.sleep(1)

    # ==================================C159==========28 Jan=============================================
    def test_external_edit_profile_cancel_C159(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 30)
        # Verify page loaded
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        # Edit Profile check
        driver.find_element_by_class_name("fa-user").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'fa-gears')))
        driver.find_element_by_class_name("fa-gears").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'first_name')))
        # Verify Edit User Profile(Label) is displayed
        expected_editUserLabel = "Edit User Profile"
        actual_editUserLabel = driver.find_element_by_class_name("panel-heading").text
        assert actual_editUserLabel in expected_editUserLabel
        # Verify Cancel(Button) is displayed
        #assert driver.find_element_by_class_name("btn-warning").is_displayed()
        #driver.find_element_by_class_name("btn-warning").click()
        # Verify Dashboard is displayed on Cancel
        # Click Dashboard
        driver.find_element_by_class_name("fa-dashboard").click()
        time.sleep(5)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header = "Fulfillment Dashboard"
        actual_header = driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

    # ==================================C688==========28 Jan=============================================
    def test_external_verify_top_button_functionality_C688(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 30)
        # External user - Verify Top button functionality on page content
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        driver.find_element_by_class_name("fa-user").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'fa-gears')))
        driver.find_element_by_class_name("fa-gears").click()

        wait.until(EC.visibility_of_element_located((By.ID, 'first_name')))
        # Verify Edit User Profile(Label) is displayed
        expected_editUserLabel = "Edit User Profile"
        actual_editUserLabel = driver.find_element_by_class_name("panel-heading").text
        assert actual_editUserLabel in expected_editUserLabel
        # Verify Cancel(Button) is displayed
        #assert driver.find_element_by_class_name("btn-warning").is_displayed()
        #driver.find_element_by_class_name("btn-warning").click()
        # Verify Dashboard is displayed on Cancel
        # Click Dashboard
        driver.find_element_by_class_name("fa-dashboard").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header = "Fulfillment Dashboard"
        actual_header = driver.find_element_by_id("content-header").text
        assert actual_header in expected_header
        # Scroll to bottom of page
        driver.execute_script("window.scrollTo(0, 1200)")
        wait.until(EC.visibility_of_element_located((By.ID, 'back-to-top')))
        driver.find_element_by_id("back-to-top").click()
        # Verify that UP button disappears when at top of page
        wait.until(EC.invisibility_of_element_located((By.ID, 'back-to-top')))
        assert (driver.find_element_by_id("back-to-top").is_displayed() == False)

    # ============================================15 Feb=============================================

    def test_external_verify_OrderSearch_functionality_C169(self, impersonate_external):
        # Verify the search functionality in Orders/Orders Search page.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 30)
        # Verify Order Link displayed
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Order Search')))
        driver.find_element_by_link_text("Order Search").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        actualTitle = driver.find_element_by_id("content-header").text
        expectedTitle = "Order Search"
        assert expectedTitle in actualTitle
        #Search all orders
        wait.until(EC.visibility_of_element_located((By.ID,'gen_search')))
        driver.find_element_by_id("gen_search").click()
        # Verify error message from orders table if empty
        wait.until(EC.visibility_of_element_located((By.ID,'orders_table')))
        ord_tab_content = driver.find_element_by_id("orders_table").text
        no_data_message = "No results found for your search."
        if no_data_message in ord_tab_content:
            flag = 2
            assert no_data_message in ord_tab_content
        else:
            # data exists
            flag = 1
        if flag == 1:
            # Fetch Order Id dynamically for Valid search criteria
            v_orderid = driver.find_element_by_class_name('glyphicon-bookmark').get_attribute('data-order-id')
            time.sleep(1)
            driver.find_element_by_id("orders_table_filter").find_element_by_class_name("input-sm").send_keys(v_orderid)
            time.sleep(4)
            wait.until(EC.visibility_of_element_located((By.ID,'orders_table_previous')))
            time.sleep(1)
            # Verify if expected content is displayed in search result on 'Order Search' page.
            wait.until(EC.visibility_of_element_located((By.ID,'orders_table')))
            time.sleep(1)
            actual=driver.find_element_by_id("orders_table").text
            time.sleep(1)
            assert v_orderid in actual
            # Verify if expected column exists in search result.
            expected = ["ID", "Client Name","Status","Sales Rep","Date Submitted","Production Date","Ship-by Date"]
            size = len(expected)
            for i in range(size):
                assert expected[i] in actual
            time.sleep(1)
            # Verify Invalid Search
            driver.find_element_by_id('search_input_toggle').click()
            time.sleep(1)
            driver.find_element_by_id("orderid").send_keys('abcde12345')
            driver.find_element_by_id("gen_search").click()
            time.sleep(1)
            # Check Table is empty dataTables_empty
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'dataTables_empty')))
            assert driver.find_element_by_class_name("dataTables_empty").is_displayed()


    # ============================================15Feb============================================================

    def test_external_verify_OrderSearch_filter_C187(self, impersonate_external):
        # Verify the filter functionality in search results section in Orders/Orders Search page.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 30)
        # Click on order tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        # Click on Order Search
        driver.find_element_by_class_name("sub-nav").find_element_by_link_text("Order Search").click()
        time.sleep(1)
        # Click on advance filter button
        # driver.find_element_by_id("toggle").click()
        # driver.find_element_by_class_name("dropdown-toggle").click()
        # Click on generate report button
        driver.find_element_by_id("gen_search").click()
        # Wait orders_table_info
        wait.until(EC.visibility_of_element_located((By.ID,'orders_table_info')))
        time.sleep(1)
        # Verify error message from orders table if empty
        wait.until(EC.visibility_of_element_located((By.ID,'orders_table')))
        ord_tab_content = driver.find_element_by_id("orders_table").text
        no_data_message = "No results found for your search."
        if no_data_message in ord_tab_content:
            flag = 2
            assert no_data_message in ord_tab_content
        else:
            # data exists
            flag = 1
        if flag == 1:
            assert driver.find_element_by_class_name("input-sm").is_displayed()
            # Verify valid order entry and search for the same
            v_orderid = driver.find_element_by_class_name('glyphicon-bookmark').get_attribute('data-order-id')
            driver.find_element_by_id("orders_table_filter").find_element_by_class_name("input-sm").send_keys(v_orderid)
            time.sleep(4)
            actual = driver.find_element_by_id("orders_table").find_element_by_class_name("odd").text
            exp_content = v_orderid
            for b in exp_content:
                assert b in actual
            driver.find_element_by_id("orders_table_filter").find_element_by_class_name("input-sm").clear()
            time.sleep(1)
            # Send wrong entry in search
            driver.find_element_by_id("orders_table_filter").find_element_by_class_name("input-sm").send_keys("xyz123")
            time.sleep(3)
            # CHECK DATA TABLE EMPTY TEXT
            dt_text = driver.find_element_by_class_name('dataTables_empty').text
            expected_message = "No results found for your search."
            assert dt_text in expected_message

    # ============================================15Feb============================================================

    def test_external_verify_OrderSearch_bookmarks_C188(self, impersonate_external):
        #  Verify the bookmark functionality in search results section in Orders/Orders Search page.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 30)
        # Click on order tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        driver.find_element_by_link_text("Orders").click()
        time.sleep(3)
        # Click on Order Search
        driver.find_element_by_link_text("Order Search").click()
        time.sleep(1)

        # Click on Search button
        wait.until(EC.visibility_of_element_located((By.ID,'gen_search')))
        driver.find_element_by_id("gen_search").click()
        time.sleep(10)
        # Wait orders_table_info
        wait.until(EC.visibility_of_element_located((By.ID,'orders_table_info')))
        time.sleep(1)
        # Verify error message from orders table if empty
        wait.until(EC.visibility_of_element_located((By.ID,'orders_table')))
        ord_tab_content = driver.find_element_by_id("orders_table").text
        no_data_message = "No results found for your search."
        if no_data_message in ord_tab_content:
            flag = 2
            assert no_data_message in ord_tab_content
        else:
            # data exists
            flag = 1
        if flag == 1:
            assert driver.find_element_by_class_name("input-sm").is_displayed()
            # Verify valid entry and search for same    glyphicon glyphicon-bookmark pull-left bookmarked
            # Check valid bookmark id glyphicon-bookmark , check Previous button displayed to ensure records exist
            if driver.find_element_by_link_text('Previous').is_displayed():
                v_orderid = driver.find_element_by_class_name('glyphicon-bookmark').get_attribute('data-order-id')
                driver.find_element_by_id("orders_table_filter").find_element_by_class_name("input-sm").send_keys(v_orderid)
                time.sleep(4)
                v_clsname  = driver.find_element_by_class_name('glyphicon-bookmark').get_attribute('class')
                if v_clsname == 'glyphicon glyphicon-bookmark pull-left bookmarked':
                    # goto bookmark
                    bm_flag = 1
                else:
                    driver.find_element_by_class_name('glyphicon-bookmark').click()
                    time.sleep(1)

                # Open Bookmark page and search for bookmarked order
                driver.find_element_by_css_selector(".fa.fa-bookmark-o.fa-fw").click()
                time.sleep(1)
                # Search for Orderid in Bookmarks table class input-sm
                driver.find_element_by_id("orders_table_filter").find_element_by_class_name("input-sm").send_keys(v_orderid)
                time.sleep(4)
                # Check row count displayed orders_table_info  Showing 1 to 1 of 1 entries
                rc_text = driver.find_element_by_id('orders_table_info').text
                assert rc_text == 'Showing 1 to 1 of 1 entries'
                time.sleep(1)
                # Come back to Order Search page
                # Click on Order Search
                driver.find_element_by_link_text("Order Search").click()
                time.sleep(1)

                # Click on Search button
                wait.until(EC.visibility_of_element_located((By.ID,'gen_search')))
                driver.find_element_by_id("gen_search").click()
                time.sleep(3)

                # Filter same orderid
                driver.find_element_by_id("orders_table_filter").find_element_by_class_name("input-sm").send_keys(v_orderid)
                time.sleep(4)
                # Click on bookmark icon to remove bookmark
                driver.find_element_by_class_name('glyphicon-bookmark').click()
                time.sleep(1)
                # Open Bookmarks page and Search for orderid that no longer has bookmark
                driver.find_element_by_css_selector(".fa.fa-bookmark-o.fa-fw").click()
                time.sleep(1)
                # Check Bookmarks Exist
                wait.until(EC.visibility_of_element_located((By.ID,'orders_table')))
                rws = len(driver.find_element_by_id('orders_table').find_elements_by_tag_name('tr'))
                if rws > 1:
                    # Search for Orderid in Bookmarks table class input-sm
                    driver.find_element_by_id("orders_table_filter").find_element_by_class_name("input-sm").send_keys(v_orderid)
                    time.sleep(4)
                    # Check row count displayed orders_table_info  Showing 0 to 0 of 0 entries
                    srch_text = driver.find_element_by_id('orders_table_info').text
                    assert srch_text == 'Showing 0 to 0 of 0 entries'
                    time.sleep(1)


    # =====================================16 Feb================192=================================================

    def test_external_verify_Ordersearch_Pagefilters_C192(self, impersonate_external):
        # Verify the 1 to 'xx' of 'xxx' entries functionality in search results section in Orders/Orders Search page.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 30)
        # Click on order tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        # Click on Order Search
        driver.find_element_by_class_name("sub-nav").find_element_by_link_text("Order Search").click()
        time.sleep(1)

        # Click on Search button
        wait.until(EC.visibility_of_element_located((By.ID,'gen_search')))
        driver.find_element_by_id("gen_search").click()
        time.sleep(10)

        # Verify error message from orders table if empty
        wait.until(EC.visibility_of_element_located((By.ID,'orders_table')))
        ord_tab_content = driver.find_element_by_id("orders_table").text
        no_data_message = "No results found for your search."
        if no_data_message in ord_tab_content:
            flag = 2
            assert no_data_message in ord_tab_content
        else:
            # data exists
            flag = 1
        # if records exist, proceed verifying filters
        if flag == 1:
            # Select 25 entries orders_table_length
            wait.until(EC.visibility_of_element_located((By.ID,'orders_table_length')))
            entry_sel = driver.find_element_by_id("orders_table_length")
            v_optsel = "25"
            for opt in entry_sel.find_elements_by_tag_name("option"):
                if opt.text == v_optsel:
                    opt.click()
                    break
            # Check row count displayed orders_table_info  Showing 1 to xx of yy entries orders_table_info
            time.sleep(5)
            srch_text = driver.find_element_by_id('orders_table_info').text
            time.sleep(1)
            assert 'Showing 1 to 25' in srch_text

            # Select 10 entries orders_table_length
            v_optsel = "10"
            for opt in entry_sel.find_elements_by_tag_name("option"):
                if opt.text == v_optsel:
                    opt.click()
                    break
            # Check row count displayed orders_table_info  Showing 1 to xx of yy entries orders_table_info
            time.sleep(5)
            srch_text = driver.find_element_by_id('orders_table_info').text
            time.sleep(1)
            assert 'Showing 1 to 10' in srch_text

            # Select 50 entries orders_table_length
            v_optsel = "50"
            for opt in entry_sel.find_elements_by_tag_name("option"):
                if opt.text == v_optsel:
                    opt.click()
                    break
            # Check row count displayed orders_table_info  Showing 1 to xx of yy entries orders_table_info
            time.sleep(7)
            srch_text = driver.find_element_by_id('orders_table_info').text
            time.sleep(1)
            assert 'Showing 1 to 50' in srch_text
            time.sleep(1)

            # Select 100 entries orders_table_length
            v_optsel = "100"
            for opt in entry_sel.find_elements_by_tag_name("option"):
                if opt.text == v_optsel:
                    opt.click()
                    break
            # Check row count displayed orders_table_info  Showing 1 to xx of yy entries orders_table_info
            time.sleep(8)
            srch_text = driver.find_element_by_id('orders_table_info').text
            time.sleep(1)
            assert 'Showing 1 to 100' in srch_text
            time.sleep(1)

    # =============================================227==========16Feb===============================================

    def test_external_verify_orders_bookmark_filters_C227(self, impersonate_external):
        # Verify the filter functionality in Orders/Bookmarks Page.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 30)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Orders").click()  # click on Orders tab
        time.sleep(1)
        # bookmark
        driver.find_element_by_css_selector(".fa.fa-bookmark-o.fa-fw").click()
        time.sleep(1)
        # Click on Bookmark link
        # Verify Bookmarks page is displayed.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        time.sleep(1)
        actualtitle = driver.find_element_by_id("content-header").text
        expectedtitle = "Bookmarks"
        assert expectedtitle in actualtitle
        time.sleep(1)

        # Check Bookmarks Exist
        rws = len(driver.find_element_by_id('orders_table').find_elements_by_tag_name('tr'))
        #print (rws)
        if int(rws) > 1:
            # Check if Page 1 is visible to see bookmarks exist
            if driver.find_element_by_link_text('1').is_enabled():
                # Fetch Order Id dynamically for Valid search criteria
                v_orderid = driver.find_element_by_class_name('glyphicon-bookmark').get_attribute('data-order-id')
                driver.find_element_by_id("orders_table_filter").find_element_by_class_name("input-sm").send_keys(v_orderid)
                time.sleep(4)
                # Check row count displayed orders_table_info  Showing 1 to 1 of 1 entries
                rc_text = driver.find_element_by_id('orders_table_info').text
                time.sleep(1)
                assert 'Showing 1 to 1' in rc_text
                time.sleep(1)
                # Enter invalid Search Data
                driver.find_element_by_id("orders_table_filter").find_element_by_class_name("input-sm").clear()
                driver.find_element_by_id("orders_table_filter").find_element_by_class_name("input-sm").send_keys('ABCDE12345')
                time.sleep(4)
                # Check row count displayed orders_table_info  Showing 0 to 0 of 0 entries
                rc_text = driver.find_element_by_id('orders_table_info').text
                time.sleep(1)
                assert 'Showing 0 to 0 of 0 entries' in rc_text
                time.sleep(1)

    # =============================================230==========16Feb===============================================

    def test_external_verify_orders_bookmark_count_changes_C230(self, impersonate_external):
        # Verify the count of bookmarks in Orders/Bookmarks Page..
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 30)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))

        # Click on order tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        # Check bookmarks count
        driver.find_element_by_css_selector(".fa.fa-bookmark-o.fa-fw").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID,'orders_table')))
        badge_pages = len(driver.find_element_by_id('orders_table').find_elements_by_tag_name('tr'))
        bk_rows = int(badge_pages)-1
        # Click on Order Search
        time.sleep(1)
        driver.find_element_by_class_name("sub-nav").find_element_by_link_text("Order Search").click()
        time.sleep(1)

        # Click on Search button
        wait.until(EC.visibility_of_element_located((By.ID,'gen_search')))
        driver.find_element_by_id("gen_search").click()
        time.sleep(10)
        # Wait orders_table_info
        wait.until(EC.visibility_of_element_located((By.ID,'orders_table_info')))
        time.sleep(1)
        # Verify valid entry and search for same    glyphicon glyphicon-bookmark pull-left bookmarked
        # Check valid bookmark id glyphicon-bookmark , check Previous button displayed to ensure records exist
        no_of_orders = len(driver.find_element_by_id('orders_table').find_elements_by_tag_name('tr'))
        if int(no_of_orders) > 1:
            if driver.find_element_by_link_text('1').is_displayed():
                v_orderid = driver.find_element_by_class_name('glyphicon-bookmark').get_attribute('data-order-id')
                driver.find_element_by_id("orders_table_filter").find_element_by_class_name("input-sm").send_keys(v_orderid)
                time.sleep(4)
                # Bookmark the record
                driver.find_element_by_class_name('glyphicon-bookmark').click()
                time.sleep(4)
                # Open Bookmark page
                driver.find_element_by_css_selector(".fa.fa-bookmark-o.fa-fw").click()
                time.sleep(4)
                # Check row count is changed for book marks
                wait.until(EC.visibility_of_element_located((By.ID,'orders_table')))
                rc_new = len(driver.find_element_by_id('orders_table').find_elements_by_tag_name('tr'))
                rcount= int(rc_new) - 1
                time.sleep(1)
                # Check number of bookmarked elements changed
                assert int(rcount) != int(bk_rows)


    # ========================================916=======================16 feb=======================================
    def test_ExternalReportsInventoryByBusinessUnit_VerifyContentInGeneratedReport_C916(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 10)

        # Open the 'Inventory by Business Unit' page and verify the page opened properly.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Operations')))

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)

        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)

        #Click on 'Inventory by Business Unit' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory by Business Unit')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Inventory by Business Unit").click()
        time.sleep(1)

        # Verify 'Inventory by Business Unit' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Inventory by Business Unit Report"
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        # Verify bussiness report drop down selection
        wait.until(EC.visibility_of_element_located((By.ID,'BU')))
        select = Select(driver.find_element_by_id("BU"))
        select.select_by_visible_text("Alt Media")

        # Click on Generate Report button.
        driver.find_element_by_class_name("btn-success").click()
        # Switch to report-items
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        # Verify the first page
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_First_ctl01_ctl00").is_displayed()
        # Verify the Previous page
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Previous_ctl01_ctl00").is_displayed()
        # Verify the current page text box
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_displayed()
        # Verify the  Total Pages
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()
        # Verify the next Pages
        if driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Next_ctl01").is_displayed():
            assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Next_ctl01").is_displayed()
        else:
            assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Next_ctl00").is_displayed()
        # Verify the last Pages link
        if driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Last_ctl00").is_displayed():
            assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Last_ctl00").is_displayed()
        else:
            assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Last_ctl01").is_displayed()
        # Verify search text box
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl00").is_displayed()
        # Verify find link
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl01").is_displayed()
        # Verify find next link
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl03").is_displayed()
        # Verify export button
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl04_ctl00_ButtonImg").is_displayed()
        # Verify refresh button
        assert driver.find_element_by_name("ReportViewerControl$ctl05$ctl05$ctl00$ctl00$ctl00").is_displayed()
        # Verify export to data feed button
        assert driver.find_element_by_name("ReportViewerControl$ctl05$ctl07$ctl00$ctl00$ctl00").is_displayed()
        # Verify report content
        act = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        exp_content = ['Premium','Business Unit','Premium Description','Total']
        for v in exp_content:
            assert v in act

    # ========================================920============================16 feb==================================
    def test_ExternalReportsInventoryByBusinessUnit_SubscriptionAccept_LetterAndNumber_C920(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 10)
        # Open the 'Inventory by Business Unit' page and verify the page opened properly.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Operations')))

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)

        #Click on 'Inventory by Business Unit' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory by Business Unit')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Inventory by Business Unit").click()
        time.sleep(1)

        # Verify 'Inventory by Business Unit' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Inventory by Business Unit Report"
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        # Verify bussiness report drop down selection
        wait.until(EC.visibility_of_element_located((By.ID,'BU')))
        select = Select(driver.find_element_by_id("BU"))
        select.select_by_visible_text("Alt Media")

        time.sleep(1)
        # Click on 'Make a subscription' button
        wait.until(EC.visibility_of_element_located((By.ID,'subscription_btn')))
        time.sleep(1)
        driver.find_element_by_id("subscription_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'modal-title')))

        #Submit the subscription form with all the details.
        random_number=str(randint(10,999))
        name="TestSubscription"+random_number
        wait.until(EC.visibility_of_element_located((By.ID,'sub_name')))
        driver.find_element_by_id("sub_name").send_keys(name)

        driver.find_element_by_id("email").clear()
        email="apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("next_btn").click()

        # Subscription form submitted successfully and display message Subscription Saved.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'noty_text')))
        expected_message="Subscription saved."
        actual_message=driver.find_element_by_class_name("noty_text").text
        assert expected_message in actual_message

        time.sleep(1)
        # Click on 'Make a subscription' button
        wait.until(EC.visibility_of_element_located((By.ID,'subscription_btn')))
        time.sleep(1)
        driver.find_element_by_id("subscription_btn").click()
        wait.until(EC.visibility_of_element_located((By.ID,'sub_name')))
        driver.find_element_by_id("sub_name").send_keys("*%&")
        driver.find_element_by_id("next_btn").click()
        wait.until(EC.visibility_of_element_located((By.ID,'sub_name')))

        # Verify the warning message.
        expected_message="Only use letters and numbers."
        actual_message=driver.find_element_by_id("sub_name").get_attribute("title")
        assert expected_message in actual_message

	# ===================================18feb===========================912=====================================

    def test_external_Verify_Reportpagination_InventoryByBusinessUnitReport_C912(self,impersonate_external):
        # Reports/Inventory by Business Unit - Verify the pagination functionality in generated Report.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        #Reports/Inventory by Business Unit ]:- Verify the pagination functionality in generated Report.
        # Check for Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Operations
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory by Business Unit
        driver.find_element_by_link_text("Inventory by Business Unit").click()
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        time.sleep(1)
        # Verify Radio Button
        wait.until(EC.visibility_of_element_located((By.ID, 'ProdClass')))
        radio_Buttons = driver.find_elements_by_id("ProdClass")
        for rb in radio_Buttons:
            assert rb.is_displayed()
        # Verify Business Unit Button/Dropdown
        assert driver.find_element_by_id("BU").is_displayed()
        # Select business unit drop down value
        select = Select(driver.find_element_by_id('BU'))
        # select by visible text 'Alt Media'
        select.select_by_visible_text('Alt Media')
        # Click on Generate report button.
        driver.find_element_by_id("sub_btn").click()
        # Verify the Date and Time of the generated report.
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(5)
        # Check total pages
        tp = driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").text
        tps = tp.split(" ")
        tpcnt = tps[0]
        # If total pages are 1
        if int(tpcnt) == 1:
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_First_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Previous_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Next_ctl00').get_attribute("class") == "NormalButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Last_ctl00').get_attribute("class") == "NormalButton"

        # Check next page & previous if total pages > 1
        if int(tpcnt) > 1:
            # Click Last button and verify controls NormalButton
            driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Last_ctl00_ctl00').click()
            time.sleep(5)
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Next_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Last_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Previous_ctl00').get_attribute("class") == "NormalButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_First_ctl00').get_attribute("class") == "NormalButton"
            # Click on First button
            driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_First_ctl00_ctl00').click()
            time.sleep(10)
            # Check First,Last,Next,Prev state
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_First_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Previous_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Next_ctl00').get_attribute("class") == "NormalButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Last_ctl00').get_attribute("class") == "NormalButton"

    # ========================================18feb==================224==============================================

    def test_external_verify_Orders_bookmark_Pagefilters_C224(self, impersonate_external):
        # Verify 'Showing 1 to 'xx'of 'xxx' entries functionality in Orders/Bookmarks Page.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Orders").click()  # click on Orders tab
        time.sleep(1)
        # bookmark
        driver.find_element_by_css_selector(".fa.fa-bookmark-o.fa-fw").click()
        time.sleep(1)
        # Click on Bookmark link
        # Verify Bookmarks page is displayed.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        time.sleep(1)
        actualtitle = driver.find_element_by_id("content-header").text
        expectedtitle = "Bookmarks"
        assert expectedtitle in actualtitle
        time.sleep(1)
        # Check bookmark exist
        # Check table row count orders_table
        rc = len(driver.find_element_by_id('orders_table').find_elements_by_tag_name("tr"))

        # Check bookmarks badges count
        if int(rc) > 1:
            badge_cnt = driver.find_element_by_class_name('badge').text
        else:
            badge_cnt = "0"
        # Check if Page 1 is visible to see bookmarks exist
        if int(badge_cnt) >= 10:
            # Verify  Bookmarks dropdowns 10,25,50,100
            if int(badge_cnt) >= 100:
                # Select 100 entries orders_table_length
                entry_sel = driver.find_element_by_id("orders_table_length")
                v_optsel = "100"
                for opt in entry_sel.find_elements_by_tag_name("option"):
                    if opt.text == v_optsel:
                        opt.click()
                        break
                time.sleep(3)
                srch_text = driver.find_element_by_id('orders_table_info').text
                time.sleep(3)
                assert 'Showing 1 to 100' in srch_text
            if int(badge_cnt) >= 50:
                # Select 50 entries orders_table_length
                entry_sel = driver.find_element_by_id("orders_table_length")
                v_optsel = "50"
                for opt in entry_sel.find_elements_by_tag_name("option"):
                    if opt.text == v_optsel:
                        opt.click()
                        break
                time.sleep(3)
                srch_text = driver.find_element_by_id('orders_table_info').text
                time.sleep(3)
                assert 'Showing 1 to 50' in srch_text
            if int(badge_cnt) >= 25:
                # Select 25 entries orders_table_length
                entry_sel = driver.find_element_by_id("orders_table_length")
                v_optsel = "25"
                for opt in entry_sel.find_elements_by_tag_name("option"):
                    if opt.text == v_optsel:
                        opt.click()
                        break
                time.sleep(3)
                srch_text = driver.find_element_by_id('orders_table_info').text
                time.sleep(3)
                assert 'Showing 1 to 25' in srch_text
            if int(badge_cnt) >= 10:
                # Select 10 entries orders_table_length
                entry_sel = driver.find_element_by_id("orders_table_length")
                v_optsel = "10"
                for opt in entry_sel.find_elements_by_tag_name("option"):
                    if opt.text == v_optsel:
                        opt.click()
                        break
                time.sleep(3)
                srch_text = driver.find_element_by_id('orders_table_info').text
                time.sleep(3)
                assert 'Showing 1 to 10' in srch_text
        else:
                print("Insufficient bookmarks count to validate Bookmark filters")
        time.sleep(1)

# ======================================18feb==============229====================================================

    def test_external_verify_Orders_bookmark_pagination_C229(self, impersonate_external):
        # Verify the pagination functionality in Orders/Bookmarks Page.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Wait for Orders tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Orders')))
        driver.find_element_by_link_text("Orders").click()  # click on Orders tab
        time.sleep(1)
        # bookmark
        driver.find_element_by_css_selector(".fa.fa-bookmark-o.fa-fw").click()
        time.sleep(1)
        # Click on Bookmark link
        # Verify Bookmarks page is displayed.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        time.sleep(1)
        actualtitle = driver.find_element_by_id("content-header").text
        expectedtitle = "Bookmarks"
        assert expectedtitle in actualtitle
        time.sleep(1)

        # Check table row count orders_table
        rc = len(driver.find_element_by_id('orders_table').find_elements_by_tag_name("tr"))

        # Check if Page 1 is visible to see that bookmarks exist
        if int(rc) > 1:
            # verify presence of page navigation buttons orders_table_previous
            cls_next = driver.find_element_by_id('orders_table_next').get_attribute('class')  #paginate_button next disabled
            if cls_next == 'paginate_button next disabled':
                # One page only - do nothing
                print('Only one page exists')
            if cls_next != 'paginate_button next disabled':
                # Verify Next button and previous button functionality
                driver.find_element_by_link_text('Next').click()
                time.sleep(3)
                assert driver.find_element_by_link_text('Previous').is_enabled()
                driver.find_element_by_link_text('Previous').click()
                time.sleep(3)
                assert driver.find_element_by_link_text('Next').is_enabled()


# ==========================================18feb==========230============================================================

    def test_external_verify_Orders_bookmark_count_C230(self, impersonate_external):
        # Verify the count of bookmarks in Orders/Bookmarks Page.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Wait for Orders link to show up
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Orders')))
        driver.find_element_by_link_text("Orders").click()  # click on Orders tab
        time.sleep(1)
        # Bookmark Link
        driver.find_element_by_css_selector(".fa.fa-bookmark-o.fa-fw").click()
        time.sleep(1)
        # Click on Bookmark link
        # Verify Bookmarks page is displayed.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        time.sleep(1)
        actualtitle = driver.find_element_by_id("content-header").text
        expectedtitle = "Bookmarks"
        assert expectedtitle in actualtitle
        time.sleep(1)
        # Get bookmark count
        # Check table row count orders_table for bookmark
        rc = len(driver.find_element_by_id('orders_table').find_elements_by_tag_name("tr"))
        # Check that bookmarks exist
        if int(rc) > 1:
        # Check bookmarks badges count
            badge_pages_prev = driver.find_element_by_class_name('badge').text
        else:
            badge_pages_prev = "0"
        # Check if atleast 1 record  is visible to see bookmarks exist
        if int(badge_pages_prev) > 0:
            # Fetch Order Id dynamically for Valid search criteria
            v_orderid = driver.find_element_by_class_name('glyphicon-bookmark').get_attribute('data-order-id')
            driver.find_element_by_id("orders_table_filter").find_element_by_class_name("input-sm").send_keys(v_orderid)
            time.sleep(4)
            # Check row count displayed orders_table_info  Showing 1 to 1 of 1 entries
            rc_text = driver.find_element_by_id('orders_table_info').text
            time.sleep(1)
            assert 'Showing 1 to 1' in rc_text
            time.sleep(1)
            # Remove bookmark
            driver.find_element_by_class_name('glyphicon-bookmark').click()
            time.sleep(1)
            # Enter Bookmark id again and bookmark should no longer display
            driver.refresh()
            time.sleep(1)
            # Check bookmarks badges count
            badge_pagesnew = driver.find_element_by_class_name('badge').text
            time.sleep(1)
            # Check prev and new bookmark values
            assert badge_pages_prev != badge_pagesnew
            # Add bookmark again from Search page
            # Click on Order Search link to view all orders
            driver.find_element_by_class_name("sub-nav").find_element_by_link_text("Order Search").click()
            time.sleep(1)
            # Click on Search button
            driver.find_element_by_id("gen_search").click()
            time.sleep(5)
            # Wait orders_table_info
            wait.until(EC.visibility_of_element_located((By.ID,'orders_table_info')))
            time.sleep(1)
            # Verify error message from orders table if empty
            wait.until(EC.visibility_of_element_located((By.ID,'orders_table')))
            ord_tab_content = driver.find_element_by_id("orders_table").text
            no_data_message = "No results found for your search."
            if no_data_message in ord_tab_content:
                flag = 2
                assert no_data_message in ord_tab_content
            else:
                # data exists
                flag = 1
            if flag == 1:
                driver.find_element_by_id("orders_table_filter").find_element_by_class_name("input-sm").send_keys(v_orderid)
                time.sleep(1)
                # Bookmark the record
                driver.find_element_by_class_name('glyphicon-bookmark').click()
                time.sleep(4)

    # ======================================259=======================22 feb===========================================

    def test_ExternalReportOpenOrderByBusinessUnit_VerifyPagination_C259(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Operations')))
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Orders tab. fa-folder-open-o
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'fa-folder-open-o')))
        orders = driver.find_elements_by_link_text("Orders")
        orders[1].click()
        time.sleep(1)
        # Click on Open Orders by Business Unit
        driver.find_element_by_link_text("Open Orders by Business Unit").click()
        # Verify  header
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header_Open_Orders_Business_Unit_Report = "Open Orders by Business Unit Report"
        actual_header_Open_Orders_Business_Unit_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Open_Orders_Business_Unit_Report in expected_header_Open_Orders_Business_Unit_Report
        # Select business unit drop down value
        select = Select(driver.find_element_by_id('BU'))
        # select by visible text 'Alt Media'
        select.select_by_visible_text('Alt Media')

        # Click on Generate report button.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-success')))
        driver.find_element_by_class_name("btn-success").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'report_src')))
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)

        # Verify the first page
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_First_ctl01_ctl00").is_displayed()

        tp = driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").text
        tps = tp.split(" ")
        tpcnt = tps[0]
        # If total pages are 1
        if int(tpcnt) == 1:
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_First_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Previous_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Next_ctl00').get_attribute("class") == "NormalButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Last_ctl00').get_attribute("class") == "NormalButton"

        # Check next page & previous if total pages > 1
        if int(tpcnt) > 1:
            # Click Last button and verify controls NormalButton
            driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Last_ctl00_ctl00').click()
            time.sleep(5)
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Next_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Last_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Previous_ctl00').get_attribute("class") == "NormalButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_First_ctl00').get_attribute("class") == "NormalButton"
            # Click on First button
            driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_First_ctl00_ctl00').click()
            time.sleep(10)
            # Check First,Last,Next,Prev state
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_First_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Previous_ctl01').get_attribute("class") == "DisabledButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Next_ctl00').get_attribute("class") == "NormalButton"
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Last_ctl00').get_attribute("class") == "NormalButton"


    # ========================================1490============================23 feb==================================

    def test_ExternalReportsInventoryOpenPurchaseOrder_VerifySubscriptionAcceptOnlyLetterAndNumber_C1490(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 10)
        # Open the 'Open Purchase Order' page and verify the page opened properly.
        # Click on Reports tab.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Operations')))

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        #Click on 'Open Purchase Order' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Open Purchase Orders')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Open Purchase Orders").click()

        # Verify 'Open Purchase Order' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Open Purchase Orders Report"
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        # Select the client from the drop down
        wait.until(EC.visibility_of_element_located((By.ID, 'CustomerNumber')))
        clients = driver.find_element_by_id("CustomerNumber")
        client_option = "ARPM"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        #Click on make a subscription button.
        driver.find_element_by_id("subscription_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'modal-title')))

        #Submit the subscription form with all the details.
        random_number=str(randint(10,999))
        name="TestSubscription"+random_number
        wait.until(EC.visibility_of_element_located((By.ID,'sub_name')))
        driver.find_element_by_id("sub_name").send_keys(name)

        driver.find_element_by_id("email").clear()
        email="apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("next_btn").click()

        # Subscription form submitted successfully and display message Subscription Saved.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'noty_text')))
        expected_message="Subscription saved."
        actual_message=driver.find_element_by_class_name("noty_text").text
        assert expected_message in actual_message
        time.sleep(1)
        # Click on 'Make a subscription' link and enter special characters in subscription text box.
        wait.until(EC.visibility_of_element_located((By.ID,'subscription_btn')))
        time.sleep(1)
        driver.find_element_by_id("subscription_btn").click()
        wait.until(EC.visibility_of_element_located((By.ID,'sub_name')))
        driver.find_element_by_id("sub_name").send_keys("*%&")
        driver.find_element_by_id("next_btn").click()
        wait.until(EC.visibility_of_element_located((By.ID,'sub_name')))

        # Verify the warning message.
        expected_message = "Only use letters and numbers."
        actual_message=driver.find_element_by_id("sub_name").get_attribute("title")
        assert expected_message in actual_message
        # Click Back button btn-default
        driver.find_element_by_class_name("btn-default").click()
        time.sleep(1)

    # ========================================1491============================23 feb==================================

    def test_ExternalReportsInventoryOpenPurchaseOrder_VerifySubscriptionSubmitted_C1491(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 10)
        # Open the 'Open Purchase Orders' page and verify the page opened properly.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()

        #Click on Operations tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Operations')))
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()

        #Click on 'Open Purchase Order' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Open Purchase Orders')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Open Purchase Orders").click()

        # Verify 'Open Purchase Order' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Open Purchase Orders Report"
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        # Select the client from the drop down
        wait.until(EC.visibility_of_element_located((By.ID, 'CustomerNumber')))
        clients = driver.find_element_by_id("CustomerNumber")
        client_option = "ARPM"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        #Click on make a subscription button.
        driver.find_element_by_id("subscription_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'modal-title')))

        #Submit the subscription form with all the details.
        random_number=str(randint(10,999))
        name="TestSubscription"+random_number
        wait.until(EC.visibility_of_element_located((By.ID,'sub_name')))
        driver.find_element_by_id("sub_name").send_keys(name)

        driver.find_element_by_id("email").clear()
        email="apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("next_btn").click()

        # Subscription form submitted successfully and display message Subscription Saved.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'noty_text')))
        expected_message="Subscription saved."
        actual_message=driver.find_element_by_class_name("noty_text").text
        assert expected_message in actual_message

		# On subscriptions page, Subscription name should reflect with Modify and Delete button
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Subscriptions')))
        time.sleep(1)
        driver.find_element_by_link_text("Subscriptions").click()
        wait.until(EC.visibility_of_element_located((By.ID,'jobs_table')))
        time.sleep(1)
        assert driver.find_element_by_partial_link_text("Modify").is_displayed()
        assert driver.find_element_by_partial_link_text("Delete").is_displayed()
        subscriptions = driver.find_element_by_id("jobs_table").text
        assert name in subscriptions

    # ========================================1498============================23 feb==================================

    def test_ExternalReportsInventoryProductUsage_VerifySubscriptionAcceptOnlyLetterAndNumber_C1498(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        # Click on Product Usage.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Product Usage')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Product Usage").click()
        # Verify Product Usage  page header
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header = "Product Usage Report"
        actual_header = driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        assert driver.find_element_by_id('customerNumber')
        # Select the client from the drop down
        clients = Select(driver.find_element_by_id('customerNumber'))
        clients.select_by_visible_text('ARPM')

        actual_selected_option = clients.first_selected_option.text
        expected_selection_option = "ARPM"
        assert expected_selection_option in actual_selected_option

        # Check iDays from the drop down
        idays = Select(driver.find_element_by_id('iDays'))
        idays.select_by_visible_text("7 Days")
        actual_selected_option = idays.first_selected_option.text
        expected_selection_option = "7 Days"
        assert expected_selection_option in actual_selected_option

        # Click on make a subscription button.
        driver.find_element_by_id("subscription_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'modal-title')))

        #Submit the subscription form with all the details.
        random_number=str(randint(10,999))
        name="TestSubscription"+random_number
        wait.until(EC.visibility_of_element_located((By.ID,'sub_name')))
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_id("email").clear()
        email="apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("next_btn").click()

        # Subscription form submitted successfully and display message Subscription Saved.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'noty_text')))
        expected_message="Subscription saved."
        actual_message=driver.find_element_by_class_name("noty_text").text
        assert expected_message in actual_message
        time.sleep(1)
        # Click on 'Make a subscription' link and enter special characters in subscription text box.
        wait.until(EC.visibility_of_element_located((By.ID,'subscription_btn')))
        time.sleep(1)
        driver.find_element_by_id("subscription_btn").click()
        wait.until(EC.visibility_of_element_located((By.ID,'sub_name')))
        driver.find_element_by_id("sub_name").send_keys("*%&")
        driver.find_element_by_id("next_btn").click()
        wait.until(EC.visibility_of_element_located((By.ID,'sub_name')))

        # Verify the warning message.
        expected_message="Only use letters and numbers."
        actual_message=driver.find_element_by_id("sub_name").get_attribute("title")
        assert expected_message in actual_message

    # ========================================1425============================23 feb==================================

    def test_ExternalReportsInventoryOpenPurchaseOrder_VerifySubscriptionNotSubmittedWithBlankFields_C1425(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 10)
        # Open the 'Inventory by Business Unit' page and verify the page opened properly.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Operations')))

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()

        #Click on 'Open Purchase Order' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Open Purchase Orders')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Open Purchase Orders").click()

        # Verify 'Open Purchase Order' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Open Purchase Orders Report"
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        # Select the client from the drop down
        wait.until(EC.visibility_of_element_located((By.ID, 'CustomerNumber')))
        clients = driver.find_element_by_id("CustomerNumber")
        client_option = "ARPM"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break

        #Click on make a subscription button.
        wait.until(EC.visibility_of_element_located((By.ID,'subscription_btn')))
        driver.find_element_by_id("subscription_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'modal-title')))

        # Click on submit button and Verify Subscription form remain displaying.
        wait.until(EC.visibility_of_element_located((By.ID,'next_btn')))
        driver.find_element_by_id("next_btn").click()
        time.sleep(1)
        assert driver.find_element_by_id("myModalLabel").is_displayed()
        # Note : Error message 'error message " Please fill out this field".' is not verified because id is not found.

    # ========================================1496============================23 feb==================================

    def test_ExternalReportsOperationsOutOfStock_VerifySubscriptionNotSubmittedWithBlankFields_C1496(self, impersonate_external):
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 10)
        # Open the 'Inventory by Business Unit' page and verify the page opened properly.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Operations')))

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()

        #Click on 'Open Purchase Order' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Open Purchase Orders')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Open Purchase Orders").click()

        # Verify 'Open Purchase Order' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Open Purchase Orders Report"
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        # Select the client from the drop down
        wait.until(EC.visibility_of_element_located((By.ID, 'CustomerNumber')))
        clients = driver.find_element_by_id("CustomerNumber")
        client_option = "ARPM"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break

        #Click on make a subscription button.
        wait.until(EC.visibility_of_element_located((By.ID,'subscription_btn')))
        driver.find_element_by_id("subscription_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'modal-title')))

        # Click on submit button and Verify Subscription form remain displaying.
        wait.until(EC.visibility_of_element_located((By.ID,'next_btn')))
        driver.find_element_by_id("next_btn").click()
        time.sleep(1)
        assert driver.find_element_by_id("myModalLabel").is_displayed()
        # Note : Error message 'error message " Please fill out this field".' is not verified because id is not found.


    # ========================================1424============================24 feb===============================

    def test_ExternalInventoryByBusinessUnit_VerifySubscriptionAcceptOnlyNumberAndLetter_C1424(self, impersonate_external):
        driver = impersonate_external['webdriver']
        # Verify Subscription accept only number and letters on 'Inventory By Business Unit' page.
        wait = WebDriverWait(driver, 90)
        # Open the 'Inventory by Business Unit' page and verify the page opened properly.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        # Click on Operations tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Operations')))
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()

        # Click on 'Out of Stock' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Out of Stock')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Inventory by Business Unit").click()

        # Verify 'Out of Stock' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Inventory by Business Unit Report"
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        #Click on make a subscription button.
        wait.until(EC.visibility_of_element_located((By.ID,'subscription_btn')))
        driver.find_element_by_id("subscription_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'modal-title')))

        #Submit the subscription form with all the details.
        random_number=str(randint(10,999))
        name="TestSubscription"+random_number
        wait.until(EC.visibility_of_element_located((By.ID,'sub_name')))
        driver.find_element_by_id("sub_name").send_keys(name)

        driver.find_element_by_id("email").clear()
        email="apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("next_btn").click()

        # Subscription form submitted successfully and display message Subscription Saved.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'noty_text')))
        expected_message="Subscription saved."
        actual_message=driver.find_element_by_class_name("noty_text").text
        assert expected_message in actual_message
        time.sleep(1)
        # Click on 'Make a subscription' link and enter special characters in subscription text box.
        wait.until(EC.visibility_of_element_located((By.ID,'subscription_btn')))
        time.sleep(1)
        driver.find_element_by_id("subscription_btn").click()
        wait.until(EC.visibility_of_element_located((By.ID,'sub_name')))
        driver.find_element_by_id("sub_name").send_keys("*%&")
        driver.find_element_by_id("next_btn").click()
        wait.until(EC.visibility_of_element_located((By.ID,'sub_name')))

        # Verify the warning message.
        expected_message="Only use letters and numbers."
        actual_message=driver.find_element_by_id("sub_name").get_attribute("title")
        assert expected_message in actual_message

    # ==================================C718==========02March=============================================

    def test_external_ProductUsage_reportoutput_daysfilter_C718(self, impersonate_external):
        # Reports/Product Usage - Verify on changing the number of days from the dropdown report reflects
        # data according to that
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 240)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Product Usage
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Out of Stock')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Product Usage").click()
        time.sleep(1)
        # Select the client from the drop down.
        wait.until(EC.visibility_of_element_located((By.ID, 'customerNumber')))
        clients = Select(driver.find_element_by_id('customerNumber'))
        clients.select_by_visible_text('ARPM')
        # Check iDays values for report generation exist in the drop down
        idays = Select(driver.find_element_by_id('iDays'))
        idays.select_by_value("7")
        assert (idays.first_selected_option.text == "7 Days")

        # Click on Generate report button.
        driver.find_element_by_id("sub_btn").click()
        # Switch to Report content
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        #Row Count ReportViewerControl_fixedTable
        rc1 = len(driver.find_element_by_id('ReportViewerControl_fixedTable').find_elements_by_tag_name('tr'))
        # Verify Content 90 days
        # Check iDays values for report generation exist in the drop down
        driver.switch_to_default_content()
        idays = Select(driver.find_element_by_id('iDays'))
        idays.select_by_value("90")
        assert (idays.first_selected_option.text == "90 Days")
        # Click on Generate report button.
        driver.find_element_by_id("sub_btn").click()
        # Switch to Report content
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        #Row Count ReportViewerControl_fixedTable
        rc2 = len(driver.find_element_by_id('ReportViewerControl_fixedTable').find_elements_by_tag_name('tr'))
        # Verify Row count mismatch on different criteris
        assert int(rc1) != int(rc2)



    # ============================C255======2March=================================================================

    def test_external_report_Open_Orders_Business_Unit_exporttype_C255(self, impersonate_external):
        #Open Orders by Business Unit- Verify the export functionality in report generated in Business unit report tool
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Orders tab. fa-folder-open-o
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'fa-folder-open-o')))
        orders = driver.find_elements_by_link_text("Orders")
        orders[1].click()
        time.sleep(1)
        # Click on Open Orders by Business Unit
        driver.find_element_by_link_text("Open Orders by Business Unit").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        time.sleep(1)
        # Verify content in Open Orders by Business Unit page.
        expected_report_heading = "Open Orders by Business Unit Report"
        actual_report_heading = driver.find_element_by_id("content-header").text
        assert expected_report_heading in actual_report_heading

        # Click on Generate Report button.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-success')))
        time.sleep(1)
        driver.find_element_by_class_name("btn-success").click()
        # Report should be generated successfully on the same page.
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        # Verify report can be exported in following format
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl04_ctl00_ButtonLink").click()
        time.sleep(5)
        assert driver.find_element_by_class_name("HoverButton").is_displayed()
        act = driver.find_elements_by_class_name("ActiveLink")
        exp_export_option = ['Excel',
                             'CSV (comma delimited)']
        for v in act:
            name = v.text
            assert name in exp_export_option
        # Step 8 - Export the Report in all the export formats can't be verified using automation

    # ============================C256=========================2March==========================================

    def test_external_report_Open_Orders_Business_Unit_refresh_pagi_search_C256(self, impersonate_external):
        # Reports/Orders/Open Orders by Business Unit- Verify the refresh,pagination,Search functionality in
        # the Business unit report tool in Business unit report tool in Open Orders by Business Unit page.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Orders tab. fa-folder-open-o
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'fa-folder-open-o')))
        orders = driver.find_elements_by_link_text("Orders")
        orders[1].click()
        time.sleep(1)
        # Click on Open Orders by Business Unit
        driver.find_element_by_link_text("Open Orders by Business Unit").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        time.sleep(1)
        # Verify content in Open Orders by Business Unit page.
        expected_report_heading = "Open Orders by Business Unit Report"
        actual_report_heading = driver.find_element_by_id("content-header").text
        assert expected_report_heading in actual_report_heading

        # Click on Generate Report button.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-success')))
        time.sleep(1)
        driver.find_element_by_class_name("btn-success").click()
        # Report should be generated successfully on the same page.
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        rc1 = len(driver.find_element_by_id('ReportViewerControl_fixedTable').find_elements_by_tag_name('tr'))
        if int(rc1) > 1:
            # Search  Premium AARP04229
            driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl00").send_keys("AARP04229")
            driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl01").click()
            time.sleep(10)
            try:
                alert = driver.switch_to_alert()
                assert alert.text == "The search text was not found."
                alert.accept()
                found = 1
            except NoAlertPresentException as e:
                found = 2

            if int(found) == 2:
                assert driver.find_element_by_css_selector("span[style='COLOR:highlighttext;BACKGROUND-COLOR:highlight;']").is_displayed()

            # Click Refresh
            driver.find_element_by_name("ReportViewerControl$ctl05$ctl05$ctl00$ctl00$ctl00").click()
            wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
            time.sleep(5)
            # Validate data cleared in search text
            assert driver.find_element_by_id('ReportViewerControl_ctl05_ctl03_ctl00').text == ""
            # Verify Next Last buttons
            if driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Next_ctl00_ctl00').is_displayed():
                # click Next
                driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Next_ctl00_ctl00').click()
                wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
                # Check current page no changes
                cp = driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").get_attribute("value")
                assert int(cp)>1
                # Click Last if visible
                if driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Last_ctl00_ctl00').is_displayed():
                    driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Last_ctl00_ctl00').click()
                    wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
                    # Verify Current Page No
                    cp2 = driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").get_attribute("value")
                    assert int(cp) != int(cp2)

            # Click Refresh again to see page reset
            driver.find_element_by_name("ReportViewerControl$ctl05$ctl05$ctl00$ctl00$ctl00").click()
            wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
            time.sleep(1)
            # Verify page no is 1
            cp3 = driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").get_attribute("value")
            assert int(cp3) == 1

    # ============================C258=========================2March==========================================

    def test_external_report_Open_Orders_Business_Unit_findnext_C258(self, impersonate_external):
        # Reports/Orders/Open Orders by Business Unit - Verify the find and next functionality in report generated
        # in Open Orders by Business Unit page.
        driver = impersonate_external['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Orders tab. fa-folder-open-o
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'fa-folder-open-o')))
        orders = driver.find_elements_by_link_text("Orders")
        orders[1].click()
        time.sleep(1)
        # Click on Open Orders by Business Unit
        driver.find_element_by_link_text("Open Orders by Business Unit").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        time.sleep(1)
        # Verify content in Open Orders by Business Unit page.
        expected_report_heading = "Open Orders by Business Unit Report"
        actual_report_heading = driver.find_element_by_id("content-header").text
        assert expected_report_heading in actual_report_heading

        # Click on Generate Report button.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-success')))
        time.sleep(1)
        driver.find_element_by_class_name("btn-success").click()
        # Report should be generated successfully on the same page.
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        rc1 = len(driver.find_element_by_id('ReportViewerControl_fixedTable').find_elements_by_tag_name('tr'))
        if int(rc1) > 1:
            # Search  Premium AARP00933 click on Find
            driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl00").send_keys("AARP00933")
            driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl01").click()
            time.sleep(10)
            try:
                alert = driver.switch_to_alert()
                assert alert.text == "The search text was not found."
                alert.accept()
                found = 1
            except NoAlertPresentException as e:
                found = 2
            # Verify search text is highlighted
            if int(found) == 2:
                assert driver.find_element_by_css_selector("span[style='COLOR:highlighttext;BACKGROUND-COLOR:highlight;']").is_displayed()
                # If first search found, Click Next to search again
                driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl03").click()
                time.sleep(10)
                try:
                    alert = driver.switch_to_alert()
                    assert alert.text == "The entire report has been searched."
                    alert.accept()
                    found2 = 1
                except NoAlertPresentException as e:
                    found2 = 2
                if int(found2) == 2:
                    # Element fount again
                    assert int(found2) == 2
            time.sleep(1)

    # =================================================================================
