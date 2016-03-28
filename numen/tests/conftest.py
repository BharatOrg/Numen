import pytest
import time
from selenium import webdriver
from random import randint
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait                                                     
from selenium.webdriver.common.by import By                                
from selenium.webdriver.support.ui import Select

#  Load credentials from yaml
import yaml
with open('../creds.yaml', 'r') as f:
    creds = yaml.load(f)

url = creds["url"] 
login_title = 'Numen - Login'

@pytest.fixture(scope="class")
def setup(request):
    '''Sets up webdriver and takes us to the login page'''

    #  Webdriver imports
    from selenium import webdriver
    #  Setup the webdriver and take us to the login page
    driver = webdriver.Firefox()
    driver.set_window_size(1280,720)
    #  Ensure the pages and elements have enough time to load
    driver.set_page_load_timeout(45)
    driver.implicitly_wait(30)
    driver.get(url)
    assert login_title == driver.title

    def breakdown():
        print 'All done, quitting browser.'
        driver.quit()
    request.addfinalizer(breakdown)

    return {
            'webdriver':driver,
            'creds':creds
            }

@pytest.fixture()
def login(setup, request):
    '''Logs into the main page (dashboard)'''

    print '\nLogging in'
    driver = setup['webdriver']
    creds = setup['creds']
    driver.get(url)
    driver.find_element_by_name('user').send_keys(creds['user'])
    driver.find_element_by_name('password').send_keys(creds['pass'])
    driver.find_element_by_name('user').submit()

    def breakdown():
        print '\nDone with function, logging out'
        driver = setup['webdriver']
        #  Make sure to come out of any iframes (ssrs reports) before exiting
        driver.switch_to_default_content()
        #  Coming out of modals causes the logout dropdown not to be available
        #  for a moment, causing some tests to have errors.  Refreshing the page
        #  before loggin out and using selenium waits to avoid this.
        driver.refresh()
        time.sleep(3)
        driver.get("https://numen.qa.ggoutfitters.com/logout")
        time.sleep(2)
    request.addfinalizer(breakdown)

    return {
            'webdriver':driver,
            }

@pytest.fixture()
def impersonate_sales(login):
    '''Will take off from where login leaves off and impersonates the User
        specified by the 'username' parameter'''

    #  Let's use the sales person Ann Schulman to impersonate a typical sales user
    username = 'aschulman'

    driver = login['webdriver']

    #  Click the Admin section from the navigation to expose the 'User Profiles'
    #  link
    nav_admin = driver.find_element_by_id('main-nav').find_element_by_link_text('Admin')
    nav_admin.click()

    #  Go to user profiles
    driver.find_element_by_link_text('User Profiles').click()

    #  Grab the filter element and search for our desired user
    filter = driver.find_element_by_id('user_table_filter').find_element_by_class_name('form-control')
    filter.send_keys(username)

    #  The search table should now just show our searched-for User
    #  Click on the corrosponding impersonate button
    user_row = driver.find_element_by_id('row-'+username)
    user_row.find_element_by_link_text('Impersonate').click()

    '''
      Now we should be in the user's profile, getting the user's name from the
      top right and comparing it to the username we used should tell us if we
      are in as the correct User
    '''
    name = driver.find_element_by_id('top-bar').find_element_by_class_name('dropdown-toggle').text
    derived_username = (name.split()[0][0] + name.split()[1]).lower()
    assert username == derived_username

    return {
            'webdriver':driver,
            }
    
@pytest.fixture()
def impersonate_external(login):
    '''Will take off from where login leaves off and impersonates the User
        specified by the 'username' parameter'''

    #  Let's use the sales person Ann Schulman to impersonate a typical sales user
    username = 'clipford'

    driver = login['webdriver']

    #  Click the Admin section from the navigation to expose the 'User Profiles'
    #  link
    nav_admin = driver.find_element_by_id('main-nav').find_element_by_link_text('Admin')
    nav_admin.click()

    #  Go to user profiles
    driver.find_element_by_link_text('User Profiles').click()

    #  Grab the filter element and search for our desired user
    filter = driver.find_element_by_id('user_table_filter').find_element_by_class_name('form-control')
    filter.send_keys(username)

    #  The search table should now just show our searched-for User
    #  Click on the corrosponding impersonate button
    user_row = driver.find_element_by_id('row-'+username)
    user_row.find_element_by_link_text('Impersonate').click()

    '''
      Now we should be in the user's profile, getting the user's name from the
      top right and comparing it to the username we used should tell us if we
      are in as the correct User
    '''
    name = driver.find_element_by_id('top-bar').find_element_by_class_name('dropdown-toggle').text
    derived_username = (name.split()[0][0] + name.split()[1]).lower()
    assert username == derived_username

    return {
            'webdriver':driver,
            }

@pytest.fixture()
def impersonate_fullfilment(login):
    '''Will take off from where login leaves off and impersonates the User
        specified by the 'username' parameter'''

    #  Let's use the sales person Vlucero to impersonate a typical fullfilment user
    username = 'vlucero'

    driver = login['webdriver']

    #  Click the Admin section from the navigation to expose the 'User Profiles'
    #  link
    nav_admin = driver.find_element_by_id('main-nav').find_element_by_link_text('Admin')
    nav_admin.click()

    #  Go to user profiles
    driver.find_element_by_link_text('User Profiles').click()

    #  Grab the filter element and search for our desired user
    filter = driver.find_element_by_id('user_table_filter').find_element_by_class_name('form-control')
    filter.send_keys(username)

    #  The search table should now just show our searched-for User
    #  Click on the corrosponding impersonate button
    user_row = driver.find_element_by_id('row-'+username)
    user_row.find_element_by_link_text('Impersonate').click()

    '''
      Now we should be in the user's profile, getting the user's name from the
      top right and comparing it to the username we used should tell us if we
      are in as the correct User
    '''
    name = driver.find_element_by_id('top-bar').find_element_by_class_name('dropdown-toggle').text
    derived_username = (name.split()[0][0] + name.split()[1]).lower()
    assert username == derived_username

    return {
            'webdriver':driver,
            }

@pytest.fixture()
def impersonate_accounting(login):
    '''Will take off from where login leaves off and impersonates the User
        specified by the 'username' parameter'''

    #  Let's use the accounting user jstorey to impersonate a typical accounting user
    username = 'jstorey'

    driver = login['webdriver']

    #  Click the Admin section from the navigation to expose the 'User Profiles'
    #  link
    nav_admin = driver.find_element_by_id('main-nav').find_element_by_link_text('Admin')
    nav_admin.click()

    #  Go to user profiles
    driver.find_element_by_link_text('User Profiles').click()

    #  Grab the filter element and search for our desired user
    filter = driver.find_element_by_id('user_table_filter').find_element_by_class_name('form-control')
    filter.send_keys(username)

    #  The search table should now just show our searched-for User
    #  Click on the corrosponding impersonate button
    user_row = driver.find_element_by_id('row-'+username)
    user_row.find_element_by_link_text('Impersonate').click()

    '''
      Now we should be in the user's profile, getting the user's name from the
      top right and comparing it to the username we used should tell us if we
      are in as the correct User
    '''
    name = driver.find_element_by_id('top-bar').find_element_by_class_name('dropdown-toggle').text
    derived_username = (name.split()[0][0] + name.split()[1]).lower()
    assert username == derived_username

    return {
            'webdriver':driver,
            }



@pytest.fixture()
def create_user(login):
    '''
    Try to open the 'User Profiles' menu item and create a user.
    '''

    successmsg_usercreated = 'User created successfully' 

    driver = login['webdriver']
    driver.find_element_by_link_text('Admin').click()
    driver.find_element_by_class_name('fa-users').click()
    driver.find_element_by_link_text('Create New User').click()
    dropdown = driver.find_element_by_id('selectedUser')
    from selenium.webdriver.support.ui import Select
    Select(dropdown).select_by_visible_text('Create Non-AD User')
    driver.find_element_by_id('userid').send_keys('qatestuser')
    driver.find_element_by_id('first_name').send_keys('qafirst')
    driver.find_element_by_id('last_name').send_keys('qalast')
    driver.find_element_by_id('email').send_keys('qatestuser@ggoutfitters.com')
    divisions = driver.find_element_by_class_name('btn-group')
    caret = divisions.find_element_by_class_name('caret')
    checkbox = divisions.find_element_by_xpath("//input[@value='GGO']")
    caret.click()
    checkbox.click()
    driver.find_element_by_name('accpac').send_keys('5RG')
    driver.find_element_by_name('wms').send_keys('')
    driver.find_element_by_name('workspace').send_keys('')
    driver.find_element_by_class_name('btn-success').click()

    #   Did we receive the User successfully created message?
    assert driver.find_element_by_class_name('noty_message').text == successmsg_usercreated

    #   Assert that our new user appears on under the 'Numen Users' table
    from selenium.webdriver.support.ui import Select
    dropdown = driver.find_element_by_name('user_table_length')
    Select(dropdown).select_by_visible_text('All')
    assert driver.find_element_by_link_text('qatestuser').text == 'qatestuser'

    return {
            'webdriver':driver,
            }

#  Generic url for reports in Numen
ecurl = '''https://numen.qa.ggoutfitters.com/reports/'''
@pytest.fixture()
def create_user_and_subscribe(create_user):
    '''Create user and subscribe user to subscriptions'''

    from selenium.webdriver.support.ui import Select
    import random
    import time

    successmsg_subcreated = '''Subscription saved.'''

    def set_date(driver, begin='4-01-2015', end='4-10-2015'):
        '''Utility function for setting date input'''

        fromdate = driver.find_element_by_name('from_date')
        todate = driver.find_element_by_name('to_date')

        todate.clear()
        fromdate.clear()

        fromdate.send_keys(begin)
        todate.send_keys(end)

    def set_client(driver, name):
        '''Utility function for setting client name'''
        dropdown = driver.find_element_by_id('client_id')
        Select(dropdown).select_by_visible_text(name)

    def fill_subform(driver, subname):
        '''Fills out subscription form'''
        #  fill subscription name
        driver.find_element_by_id('sub_name').send_keys(subname)
        #  select a user at random, if the user dropdown exists
        try:
            select_user = Select(driver.find_element_by_id('user_id'))
            random.choice(select_user.options).click()
        except:
            print('no user selector found')
        #  select division at random, if division dropdown exists
        try:
           select_div = Select(driver.find_element_by_id('division'))
           random.choice(select_div.options).click()
        except:
            print('no division selector found')
        #  select random days to receive report
        days = driver.find_element_by_id('day_box').find_elements_by_xpath('label')
        for i in range(random.randint(0,len(days))):
            random.choice(days).click()
        driver.find_element_by_id('next_btn').click()
        assert driver.find_element_by_class_name('noty_message').text == successmsg_subcreated


    driver = create_user['webdriver']
    for report in creds['subs'].keys():
        if(report == 'personal'):
            driver.get(ecurl+report+'/ar')
            select_user = Select(driver.find_element_by_id('selector'))
            #  Pick a random user to subscribe to a report from
            random.choice(select_user.options).click()
            driver.find_element_by_id('criteria').find_element_by_xpath('button').click()
            fill_subform(driver,'test'+report+str(int(time.clock()*100000)))
        elif(report == 'executive'):
            driver.get(ecurl+report+'/ar')
            driver.find_element_by_id('criteria').find_element_by_xpath('button').click()
            fill_subform(driver,'test'+report+str(int(time.clock()*100000)))
        elif(report == 'division'):
            driver.get(ecurl+report+'/ar')
            select_div = Select(driver.find_element_by_id('selector'))
            #  Pick a random division to subscribe to
            random.choice(select_div.options).click()
            driver.find_element_by_id('criteria').find_element_by_xpath('button').click()
            fill_subform(driver,'test'+report+str(int(time.clock()*100000)))
        elif(report == 'ad-hoc'):
            for type in creds['subs']['ad-hoc'].split():
                driver.get(ecurl+report+'/'+type)
                set_client(driver, 'UNARMR')
                set_date(driver)
                driver.find_element_by_id('sub_btn').click()

    return {
            'webdriver':driver,
            }
























#  Generic url for reports in Numen
ecurl = '''https://numen.qa.ggoutfitters.com/reports/'''
@pytest.fixture()
def create_user_and_subscribe(create_user):
    '''Create user and subscribe user to subscriptions'''

    from selenium.webdriver.support.ui import Select
    import random
    import time

    successmsg_subcreated = '''Subscription saved.'''

    def set_date(driver, begin='4-01-2015', end='4-10-2015'):
        '''Utility function for setting date input'''

        fromdate = driver.find_element_by_name('from_date')
        todate = driver.find_element_by_name('to_date')

        todate.clear()
        fromdate.clear()

        fromdate.send_keys(begin)
        todate.send_keys(end)

    def set_client(driver, name):
        '''Utility function for setting client name'''
        dropdown = driver.find_element_by_id('client_id')
        Select(dropdown).select_by_visible_text(name)

    def fill_subform(driver, subname):
        '''Fills out subscription form'''
        #  fill subscription name
        driver.find_element_by_id('sub_name').send_keys(subname)
        #  select a user at random, if the user dropdown exists
        try:
            select_user = Select(driver.find_element_by_id('user_id'))
            random.choice(select_user.options).click()
        except:
            print('no user selector found')
        #  select division at random, if division dropdown exists
        try:
           select_div = Select(driver.find_element_by_id('division'))
           random.choice(select_div.options).click()
        except:
            print('no division selector found')
        #  select random days to receive report
        days = driver.find_element_by_id('day_box').find_elements_by_xpath('label')
        for i in range(random.randint(0,len(days))):
            random.choice(days).click()
        driver.find_element_by_id('next_btn').click()
        assert driver.find_element_by_class_name('noty_message').text == successmsg_subcreated


    driver = create_user
    for report in creds['subs'].keys():
        if(report == 'personal'):
            driver.get(ecurl+report+'/ar')
            select_user = Select(driver.find_element_by_id('selector'))
            #  Pick a random user to subscribe to a report from
            random.choice(select_user.options).click()
            driver.find_element_by_id('criteria').find_element_by_xpath('button').click()
            fill_subform(driver,'test'+report+str(int(time.clock()*100000)))
        elif(report == 'executive'):
            driver.get(ecurl+report+'/ar')
            driver.find_element_by_id('criteria').find_element_by_xpath('button').click()
            fill_subform(driver,'test'+report+str(int(time.clock()*100000)))
        elif(report == 'division'):
            driver.get(ecurl+report+'/ar')
            select_div = Select(driver.find_element_by_id('selector'))
            #  Pick a random division to subscribe to
            random.choice(select_div.options).click()
            driver.find_element_by_id('criteria').find_element_by_xpath('button').click()
            fill_subform(driver,'test'+report+str(int(time.clock()*100000)))
        elif(report == 'ad-hoc'):
            for type in creds['subs']['ad-hoc'].split():
                driver.get(ecurl+report+'/'+type)
                set_client(driver, 'UNARMR')
                set_date(driver)
                driver.find_element_by_id('sub_btn').click()

























