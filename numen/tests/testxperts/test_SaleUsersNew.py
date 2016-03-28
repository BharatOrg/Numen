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
from selenium.webdriver.common.action_chains import ActionChains

class TestSalesUsers_better:
    # ===========================75=====================================14 march==========================
    def test_SalesProfileImpersonate_C75(self, impersonate_sales):
        # Simple test to check if impersonating worked.  If we've reached this point,
        # we've already verified that the correct user is logged in.  Simply assert True
        # Verify page load
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Verify Dashboard tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Dashboard')))
        driver.find_element_by_link_text('Dashboard').click()

        # Verify that dashboard page shows Sales Dashboard for user
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        header_expected = "Sales Dashboard"
        header_actual = driver.find_element_by_id("content-header").text
        assert header_expected in header_actual

    # ==========================76===================================================================================
    def test_SalesProfileVerifyContentOnDashboard_C76(self, impersonate_sales):
        #  Check that open orders widget, paid sales widget, and invoiced Sales widget appears for this sales user
        driver = impersonate_sales['webdriver']
        # Verify page load
        wait = WebDriverWait(driver, 90)
        # Verify Dashboard tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Dashboard')))
        driver.find_element_by_link_text('Dashboard').click()
        time.sleep(5)
        # These are the 5 widgets that are expected on page
        expected_widgets = [
            'Open Orders',
            'Paid Sales for the Past 12 Months',
            'Invoiced Sales for the Past 12 Months',
            'Top 5 Clients by Invoiced Sales',
            'Invoiced Sales Table'
        ]
        # First, collect all the widgets on the page
        widgets = driver.find_elements_by_class_name('widget')
        # Verify actual vs. expected widget count
        assert len(expected_widgets) == len(widgets)
        # Verify Widgets Display
        src = driver.page_source
        text_found1 = re.search(r'Open Orders', src)
        text_found2 = re.search(r'Paid Sales for the Past 12 Months', src)
        text_found3 = re.search(r'Invoiced Sales for the Past 12 Months', src)


    # ==============================================================78==============================================

    def test_SalesProfileVerifyLogoutFunctionality_C78(self, impersonate_sales):
        # Simple test to check the logout functionality
        driver = impersonate_sales['webdriver']
        # Verify page load
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        logout_title = "Numen - Login"
        driver.find_element_by_class_name("dropdown-toggle").click()
        driver.find_element_by_link_text("Logout").click()
        # User should be log out successfully.
        assert logout_title == driver.title
        time.sleep(5)
        driver.find_element_by_name('user').send_keys('testuser')
        driver.find_element_by_name('password').send_keys('X91VW9u^B6kEBWIw')
        driver.find_element_by_name('user').submit()
        time.sleep(5)


    # =========================================================79=============================================

    def test_SalesProfileVerifySharingFunctionality_C79(self, impersonate_sales):
        # Simple test to check the Sharing Navigation and validating different webelements/controls
        driver = impersonate_sales['webdriver']
        # Verify page load
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_class_name("dropdown-toggle").click()
        # driver.implicitly_wait(5)
        driver.find_element_by_link_text("Sharing").click()
        # driver.implicitly_wait(5)
        # Delegations header is displayed.
        delegation_header_expected = "Delegations"
        delegation_header_actual = driver.find_element_by_id("content-header").text
        assert delegation_header_expected in delegation_header_actual

        # Share Orders (label) is displayed.
        share_orders_heading_expected = "Share Orders"
        share_orders_heading_actual = driver.find_element_by_class_name("panel-heading").text
        assert share_orders_heading_expected in share_orders_heading_actual

        # Choose a user(dropdown) is displayed.
        user_dropdown = driver.find_element_by_class_name("form-control")
        assert user_dropdown.is_displayed()

        # Submit (button) is displayed.
        submit_button = driver.find_element_by_class_name("btn-default")
        assert submit_button.is_displayed()
        # Verify Panel visibility
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'panel-body')))
        # "You have not shared your orders with any users yet" message should display when there are no orders shared.
        chk = driver.find_elements_by_class_name("btn-danger")
        cnt = int(len(chk))
        if cnt > 0:
            while cnt > 0:
                driver.find_element_by_class_name("btn-danger").click()
                time.sleep(2)
                cnt = cnt - 1
        not_shared_message_expected = "You have not shared your orders with any users yet"
        not_shared_message_actual = driver.find_element_by_class_name("panel-body").text
        assert not_shared_message_expected in not_shared_message_actual

    # ========================================================87==================================================

    def test_SalesProfileVerifyContentOnDashboard_C87(self, impersonate_sales):
        driver = impersonate_sales['webdriver']
        # Verify page load
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Verify Order Search Page
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        driver.find_element_by_link_text("Order Search").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actualTitle = driver.find_element_by_id("content-header").text
        expectedTitle = "Order Search"
        assert expectedTitle in actualTitle

        # Check Content(label) on Order Search
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'col-md-12')))
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
        startDate = driver.find_element_by_class_name("month").is_displayed()
        driver.find_element_by_name("submitted_end_date").click()
        endDate = driver.find_element_by_class_name("month").is_displayed()
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


    # ============================================88============================================================

    def test_SalesProfileVerifyContentOnDashboard_C88(self, impersonate_sales):
        driver = impersonate_sales['webdriver']
        # Verify page load
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Verify the Order Search Advance Search tab
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        driver.find_element_by_link_text("Order Search").click()
        time.sleep(1)
        actualTitle = driver.find_element_by_id("content-header").text
        expectedTitle = "Order Search"
        assert expectedTitle in actualTitle

        # time reqd for toggle to display all elements mandatory
        time.sleep(1)

        # Check input boxes for Order Search Advanced filters
        # orderid,orderxref,client,tracking,invoice_nbr,art_title,shipto_name
        wait.until(EC.presence_of_element_located((By.ID, 'shipto_name')))
        assert driver.find_element_by_id("orderid").is_displayed()
        wait.until(EC.presence_of_element_located((By.ID, 'orderxref')))
        assert driver.find_element_by_id("orderxref").is_displayed()
        assert driver.find_element_by_id("client").is_displayed()
        assert driver.find_element_by_id("tracking").is_displayed()
        assert driver.find_element_by_id("invoice_nbr").is_displayed()
        assert driver.find_element_by_id("art_title").is_displayed()
        assert driver.find_element_by_id("shipto_name").is_displayed()

        # Check Date filter text boxes are visible
        wait.until(EC.presence_of_element_located((By.NAME, 'submitted_start_date')))
        assert driver.find_element_by_name("submitted_start_date").is_displayed()
        assert driver.find_element_by_name("submitted_end_date").is_displayed()
        assert driver.find_element_by_name("pp_start_date").is_displayed()
        assert driver.find_element_by_name("pp_end_date").is_displayed()
        assert driver.find_element_by_name("shipby_start_date").is_displayed()
        assert driver.find_element_by_name("shipby_end_date").is_displayed()
        assert driver.find_element_by_name("inhands_start_date").is_displayed()
        assert driver.find_element_by_name("inhands_end_date").is_displayed()
        assert driver.find_element_by_name("paid_start_date").is_displayed()
        assert driver.find_element_by_name("paid_end_date").is_displayed()
    # ===========================================91======================================================
    def test_SalesProfileVerifyContentInSearch_C91(self, impersonate_sales):
        # Verify the contents in search results section in Orders/Orders Search
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'fa-home')))
        driver.find_element_by_class_name("fa-home").click()

        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Orders')))
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        # Click on personal drop down
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Order Search')))
        driver.find_element_by_link_text("Order Search").click()

        wait.until(EC.visibility_of_element_located((By.ID, 'gen_search')))
        driver.find_element_by_id("gen_search").click()

        wait.until(EC.visibility_of_element_located((By.ID, 'orders_table')))
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
            actual=driver.find_element_by_id("orders_table").text
            #print(actual)
            # Verify if expected column exists in search result.
            expected = ['ID', 'Client Name', 'Status', 'Date Submitted', 'In Hands Date', 'PO #', 'Art Title', 'Ship-to Name','Type']
            size=len(expected)
            for i in range(size):
                assert expected[i] in actual
            time.sleep(4)

            # Verify Order table length control orders_table_length
            assert driver.find_element_by_name('orders_table_length').is_displayed()
            # Verify Filter control displayed form-control input-sm
            assert driver.find_element_by_class_name('input-sm').is_displayed()
            # Verify change column button displayed
            assert driver.find_element_by_class_name('ColVis_MasterButton').is_displayed()

    # ============================================98============================================================

    def test_SalesProfileVerifyContentInReport_C98(self, impersonate_sales):
        # Verify the content in Reports/Account Receivable page.
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Personal')))
        driver.find_element_by_link_text("Personal").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Accounts Receivable')))
        driver.find_element_by_link_text("Accounts Receivable").click()

        # By default user is selected in the drop down.
        wait.until(EC.visibility_of_element_located((By.ID, 'selector')))
        actual_user_name = driver.find_element_by_id("selector").text
        expected_user_name = "Schulman, Anne"
        assert expected_user_name in actual_user_name

        # Generate Report(button)
        assert driver.find_element_by_id("sub_btn").is_displayed()

        # Make a Subscription button.
        assert driver.find_element_by_class_name("btn-primary").is_displayed()

    # ============================================100================================================================

    def test_SalesProfileVerifyMakeSubscriptionContentInReport_C100(self, impersonate_sales):
        # Verify the " Make a subscription"  content in Reports/Account Receivable page
        driver = impersonate_sales['webdriver']
        # Reports Tab
        # Verify page load
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Personal')))
        driver.find_element_by_link_text("Personal").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Accounts Receivable')))
        driver.find_element_by_link_text("Accounts Receivable").click()

        # Click on Make a Subscription button
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-xs')))
        driver.find_element_by_class_name("btn-xs").click()

        # Subscription for: Personal Accounts Receivable pop up should be appear
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal-header')))
        assert driver.find_element_by_class_name("modal-header").is_displayed()

        # Subscription Name is displayed
        assert driver.find_element_by_id("sub_name").is_displayed()

        # Email To is displayed
        assert driver.find_element_by_id("email").is_displayed()

        # Delivery Format is displayed
        assert driver.find_element_by_id("excel1").is_displayed()

        # User is displayed
        driver.find_element_by_id("user_id").is_displayed()

        # Time is displayed
        assert driver.find_element_by_id("time").is_displayed()

        # Receive report on is displayed
        driver.find_element_by_class_name("well-sm").is_displayed()

        # Back button is displayed
        assert driver.find_element_by_class_name("btn-default").is_displayed()

        # Save Subscription button is displayed
        assert driver.find_element_by_id("next_btn").is_displayed()

    # ===============================================102=================================================================

    def test_SalesProfileVerifyContentOnDashboard_C102(self, impersonate_sales):
        driver = impersonate_sales['webdriver']
        # Verify page load
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Orders')))

        # click on Orders tab
        driver.find_element_by_link_text("Orders").click()
        # Click on Bookmark
        driver.find_element_by_css_selector(".fa.fa-bookmark-o.fa-fw").click()
        # Verify Bookmarks page is displayed
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_title = driver.find_element_by_id("content-header").text
        expected_title = "Bookmarks"
        assert expected_title in actual_title

        # Verify error message from orders table if no Bookmark
        wait.until(EC.visibility_of_element_located((By.ID,'panel_body')))
        ord_tab_content = driver.find_element_by_id("panel_body").text
        print(ord_tab_content)
        no_data_message = "No Orders Bookmarked"
        if no_data_message in ord_tab_content:
            flag = 2
            assert no_data_message in ord_tab_content
        else:
            # bookmarks exist
            flag = 1
        if flag == 1:
            actual=driver.find_element_by_id("orders_table").text
            # Verify if expected column exists in search result.
            expected = ['ID', 'Client Name', 'Status', 'Date Submitted', 'In Hands Date', 'PO #', 'Art Title', 'Ship-to Name','Type']
            size=len(expected)
            for i in range(size):
                assert expected[i] in actual
            time.sleep(4)

            # Verify Order table length control orders_table_length
            assert driver.find_element_by_id("orders_table_length").is_displayed()
            # Verify Filter control displayed form-control input-sm
            assert driver.find_element_by_class_name('input-sm').is_displayed()
            # Verify change column button displayed
            assert driver.find_element_by_class_name('ColVis_MasterButton').is_displayed()

    # =============================113==================================================

    def test_SalesProfileVerifyHomeButtonFunctionality_C113(self, impersonate_sales):
        # Verify the home button functionality in Aschulman - sales Page.
        driver = impersonate_sales['webdriver']
        # Verify page load
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Orders").click()
        driver.find_element_by_link_text("My Open Orders").click()
        time.sleep(1)
        driver.find_element_by_link_text("Home").click()
        time.sleep(1)
        driver.find_element_by_link_text("Dashboard").click()
        time.sleep(1)
        # Dashboard page should be display.
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_dashboard_header = driver.find_element_by_id("content-header").text
        expected_dashboard_header = "Sales Dashboard"
        assert expected_dashboard_header in actual_dashboard_header


    # ===========================================114================================================================

    def test_SalesProfileVerifyContentOnDashboard_C114(self, impersonate_sales):
        driver = impersonate_sales['webdriver']
        # Verify page load
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Orders").click()  # click on Orders tab
        time.sleep(1)
        driver.find_element_by_css_selector(".fa.fa-bookmark-o.fa-fw").click()  # click on bookmark
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actualTitle = driver.find_element_by_id("content-header").text
        expectedTitle = "Bookmarks"
        assert expectedTitle in actualTitle
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 580)")
        time.sleep(4)
        # Verify back to top button
        backtotop = driver.find_element_by_id("back-to-top").is_displayed()
        assert backtotop

    # ==============================116==================================================

    def test_SalesProfileVerifyBackButtonFunctionality_C116(self, impersonate_sales):
        # verify " Back" button functionality.
        driver = impersonate_sales['webdriver']
        # Verify page load
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Personal')))
        driver.find_element_by_link_text("Personal").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Accounts Receivable')))
        driver.find_element_by_link_text("Accounts Receivable").click()
        # Click Subscription
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'time')))
        # verify "Back" button displayed.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-default')))
        driver.find_element_by_class_name("btn-default").click()
        #Verify Make Subscription displayed
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        assert driver.find_element_by_class_name("btn-primary").is_displayed()

    # =============================117=========================================================

    def test_SalesProfileVerifyContentInOpenOrder_C117(self, impersonate_sales):
        # Verify the content in Open orders report page.
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))

        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Personal')))
        driver.find_element_by_link_text("Personal").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Open Orders')))
        driver.find_element_by_link_text("Open Orders").click()

        # Heading displayed " Report: Open Orders".
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_open_order_header = driver.find_element_by_id("content-header").text
        expected_open_order_header = "Open Orders Report"
        assert expected_open_order_header in actual_open_order_header

        # Generate Report(button)
        assert driver.find_element_by_id("sub_btn").is_displayed()

        # By default user is selected in the drop down.
        actual_user_name = driver.find_element_by_id("sales_rep").text
        expected_user_name = "Schulman, Anne"
        assert expected_user_name in actual_user_name

    # =================================118========================================================

    def test_SalesProfileVerifyAccountsReceivableReport_C118(self, impersonate_sales):
        # Verify Accounts receivable report
        driver = impersonate_sales['webdriver']
        # Verify page load
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))

        # Click on home
        driver.find_element_by_class_name("fa-home").click()
        # Click on report tab
        driver.find_element_by_link_text("Reports").click()
        # Click on report Personal dropdown
        driver.find_element_by_link_text("Personal").click()
        # Click on Accounts Receivable tab
        driver.find_element_by_link_text("Accounts Receivable").click()
        driver.find_element_by_id("sub_btn").click()
        # Switch to Report Frame
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        # Verify report pagination  control is visible
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_displayed()

    # ============================================125============================================================

    def test_SalesProfileVerifyLogoutFunctionality_C125(self, impersonate_sales):
        # Verify the content of Sales Order by Dollar Value Page
        driver = impersonate_sales['webdriver']
        # Verify page load
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))

        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Personal')))
        driver.find_element_by_link_text("Personal").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Sales Order by Dollar Value')))
        driver.find_element_by_link_text("Sales Order by Dollar Value").click()

        wait.until(EC.visibility_of_element_located((By.ID, 'form_criteria')))
        assert driver.find_element_by_name("daterange").is_displayed()
        assert driver.find_element_by_id("sub_btn").is_displayed()
        assert driver.find_element_by_class_name("btn-primary").is_displayed()

    # ============================================126============================================================

    def test_SalesProfileVerifySharingFunctionality_C126(self, impersonate_sales):
        # Verify the functionality in Reports/Sales Order by Dollar Value Page
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Personal')))
        driver.find_element_by_link_text("Personal").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Accounts Receivable')))
        driver.find_element_by_link_text("Accounts Receivable").click()
        # Click Subscription
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'time')))
        # verify "Back" button displayed.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-default')))
        driver.find_element_by_class_name("btn-default").click()
        #Verify Make Subscription displayed
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        assert driver.find_element_by_class_name("btn-primary").is_displayed()

    # ===============C128===================================================================

    def test_SalesProfileVerifyContentOnDashboard_C128(self, impersonate_sales):
        driver = impersonate_sales['webdriver']
        # Verify page load
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))

        driver.find_element_by_link_text("Reports").click()  # click on Reports tab
        driver.find_element_by_link_text("Subscriptions").click()  # click on Subscriptions block
        # Verify Subscriptions page is displayed.
        actualtitle = driver.find_element_by_id("content-header").text
        expectedtitle = "Subscriptions"
        assert expectedtitle in actualtitle
        # Verify subscriptions exist
        wait.until(EC.visibility_of_element_located((By.ID,'content-container')))
        ord_tab_content = driver.find_element_by_id("content-container").text
        no_data_message = "You have no subscriptions"
        if no_data_message in ord_tab_content:
            flag = 2
            assert no_data_message in ord_tab_content
        else:
            # data exists
            flag = 1
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

    # ===================================================C129=========================================================

    def test_SalesProfileVerifyModifyButtonOnSubscriptionPage_C129(self, impersonate_sales):
        driver = impersonate_sales['webdriver']
        # Verify page load
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Subscription
        driver.find_element_by_link_text("Subscriptions").click()
        # Verify Subscription page is displayed
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        assert driver.find_element_by_id("content-header").is_displayed()
        # Click on modify  form on Subscription page.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Modify')))
        time.sleep(1)
        driver.find_element_by_link_text('Modify').click()
        time.sleep(1)
        # Verify form modal dialog and Subscription page first content is displayed
        assert driver.find_element_by_class_name("modal-content").is_displayed()
        assert driver.find_element_by_id("sub_name").is_displayed()
        driver.find_element_by_class_name('btn-default').click()
        time.sleep(1)

    # ===============C130==========================================================================

    def test_SalesProfileVerifyConetentofSubscriptionForm_C130(self, impersonate_sales):
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Personal')))
        driver.find_element_by_link_text("Personal").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Accounts Receivable')))
        driver.find_element_by_link_text("Accounts Receivable").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-xs')))

        # Click on Accounts Receivable under personal drop down
        driver.find_element_by_id("criteria").click()
        time.sleep(1)
        driver.find_element_by_class_name("btn-xs").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'sub_name')))
        # Verify Subscription Name
        driver.find_element_by_id("sub_name").is_displayed()
        # Verify Email to field
        driver.find_element_by_id("email").is_displayed()
        # Verify Delivery format in excel
        driver.find_element_by_class_name("radio").is_displayed()
        # Verify user
        driver.find_element_by_id("user_id").is_displayed()
        # Verify time
        driver.find_element_by_id("time").is_displayed()
        # Verify receive report day
        driver.find_element_by_id("modal_selector").is_displayed()
        # Verify back button
        driver.find_element_by_class_name("btn-default").is_displayed()
        # Verify save Subscription button
        driver.find_element_by_id("next_btn").is_displayed()

    # =============================================134================================================================

    def test_SalesProfileVerifyBackButtonFunctionalityInSubscription_C134(self, impersonate_sales):
        # To verify the back button functionality in  Subscription for: aschulman Personal AR Report pop up.
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Personal')))
        driver.find_element_by_link_text("Personal").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Accounts Receivable')))
        driver.find_element_by_link_text("Accounts Receivable").click()

        # Check header
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        wait.until(EC.visibility_of_element_located((By.ID, 'subscription_btn')))

        # Enter subscription
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))

        random_number = str(randint(10, 999))
        name = "TestBSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        # Select User in subscription
        wait.until(EC.visibility_of_element_located((By.ID,'user_id')))
        select = Select(driver.find_element_by_id("user_id"))
        options = select.options
        options[1].click()
        time.sleep(1)
        #select.select_by_visible_text("ARPM")
        driver.find_element_by_id("next_btn").click()

        # "Subscription saved" message should be displayed.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'noty_text')))
        assert driver.find_element_by_class_name("noty_text").is_displayed()
        time.sleep(1)

        # Open Subscription page
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'fa-rss-square')))
        time.sleep(1)
        driver.find_element_by_class_name("fa-rss-square").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'jobs_table')))
        # Verify subscriptions exist
        wait.until(EC.visibility_of_element_located((By.ID,'content-container')))
        ord_tab_content = driver.find_element_by_id("content-container").text
        no_data_message = "You have no subscriptions"
        if no_data_message in ord_tab_content:
            flag = 2
            assert no_data_message in ord_tab_content
        else:
            # data exists
            flag = 1
            NameNew_value = driver.find_element_by_id("jobs_table").text
            assert name in NameNew_value

            # Check number of subscriptions
            trs = driver.find_element_by_id('jobs_table').find_elements_by_tag_name('tr')
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

    # ====================================== 01 December============257============================================

    def test_SalesVerifyDeleteButtonFunctionalityOnSubscription_C257(self, impersonate_sales):
        # Verify the Back button functionality on Subscription for: Out of Stock Report for ARPM form.
        driver = impersonate_sales['webdriver']
        # Verify page load
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Go to reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Select subscriptions.
        driver.find_element_by_link_text("Subscriptions").click()
        time.sleep(1)
        before_delete_cnt = len(driver.find_elements_by_link_text("Delete"))
        # Select any subscription and click on delete button.
        driver.find_element_by_link_text("Delete").click()
        time.sleep(1)
        driver.find_element_by_class_name("btn-danger").click()
        time.sleep(1)
        after_delete_cnt = len(driver.find_elements_by_link_text("Delete"))

        # Subscription should be deleted
        assert before_delete_cnt != after_delete_cnt

    # ===============C131=================================================================
    def test_SalesProfileVerifyerifyDeletebuttonfunctionalitySubscriptions_C131(self, impersonate_sales):
        driver = impersonate_sales['webdriver']
        # Verify page load
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        # Click on personal drop down
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'fa-smile-o')))
        driver.find_element_by_class_name("fa-smile-o").click()
        # Click on Accounts Receivable under personal drop down
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Accounts Receivable')))
        driver.find_element_by_link_text("Accounts Receivable").click()
        # Click on Accounts Receivable under personal drop down
        wait.until(EC.visibility_of_element_located((By.ID, 'criteria')))
        driver.find_element_by_id("criteria").click()
        driver.find_element_by_class_name("btn-xs").click()
        # first creating Subscription to delete
        wait.until(EC.visibility_of_element_located((By.ID, 'sub_name')))
        driver.find_element_by_id("sub_name").send_keys("test12345")
        # Verify time field
        driver.find_element_by_id("time").is_displayed()
        # Verify receive report day field
        driver.find_element_by_id("modal_selector").is_displayed()
        # Selecting day of week
        driver.find_element_by_name("days_of_week").click()
        wait.until(EC.visibility_of_element_located((By.ID,'user_id')))
        select = Select(driver.find_element_by_id("user_id"))
        options = select.options
        options[1].click()
        time.sleep(1)
        # Click on save Subscription button
        driver.find_element_by_id("next_btn").click()
        time.sleep(3)
        # Open Subscription page
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Subscriptions')))
        time.sleep(1)
        driver.find_element_by_link_text("Subscriptions").click()
        time.sleep(5)
        wait.until(EC.visibility_of_element_located((By.ID, 'jobs_table')))

        # Assert link text delete button is present on subscription
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Delete')))
        assert driver.find_element_by_link_text("Delete").is_displayed()
        # Click on Delete button
        driver.find_element_by_link_text("Delete").click()
        # Click on Cancel
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-default')))
        driver.find_element_by_class_name("btn-default").click()
        # Verify Subscription name still exists
        wait.until(EC.visibility_of_element_located((By.ID, 'jobs_table')))
        NameNew_value = driver.find_element_by_id("jobs_table").text
        assert "test12345" in NameNew_value

    # =========================08 Dec==========82=======================================================

    def test_SalesVerifyContentsInMyOpenOrders_C82(self, impersonate_sales):
        # Verify the contents in Orders/My Open Orders.
        driver = impersonate_sales['webdriver']
        # Verify page load
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Orders')))
        # Click on Orders tab button
        driver.find_element_by_link_text("Orders").click()
        # Select My Open Orders
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'My Open Orders')))
        driver.find_element_by_link_text("My Open Orders").click()

        # Contents of My Open Order
        wait.until(EC.visibility_of_element_located((By.ID, 'order-table')))

        actual_contents = driver.find_element_by_id("order-table").text
        exp_order_id = "Order ID"
        exp_client = "Client"
        exp_ship_by_date = "Ship by Date"
        exp_in_hands_date = "In Hands Date"
        exp_total_qty = "Total Qty"
        exp_status = "Status"
        exp_progress = "Progress"
        # Verify Contents on My Open Orders
        assert exp_order_id in actual_contents
        assert exp_client in actual_contents
        assert exp_ship_by_date in actual_contents
        assert exp_in_hands_date in actual_contents
        assert exp_total_qty in actual_contents
        assert exp_status in actual_contents
        assert exp_progress in actual_contents
        expected_search = "input"
        expected_show_entries = "select"
        actual_show_entries = driver.find_element_by_name("order-table_length").tag_name
        actual_search = driver.find_element_by_id("order-table_filter").find_element_by_class_name("form-control").tag_name
        # Verify Search (Search bar)
        assert expected_search in actual_search
        # Verify Show entries (dropdown)
        assert expected_show_entries in actual_show_entries

    # ==================================83==============================================
    def test_SalesVerifyShowingEntriesMyOpenOrders_C83(self, impersonate_sales):
        # Verify Showing number of entries change as per changed show enteries data in  Orders/My Open Orders.
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Orders')))
        # Click on Orders tab button
        driver.find_element_by_link_text("Orders").click()
        # Select My Open Orders
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'My Open Orders')))
        driver.find_element_by_link_text("My Open Orders").click()

        # Verify Show 10 entries is displayed by default
        select = Select(driver.find_element_by_name('order-table_length'))
        selected_option = select.first_selected_option
        expected_selection = "10"
        actual_selection = selected_option.text
        assert expected_selection in actual_selection
        total_entries = driver.find_element_by_id("order-table_info").text
        logic_1 = total_entries.split('of', 1)
        logic_2 = logic_1[1].strip(" ")
        logic_3 = logic_2.strip(" entries")
        logic_4 = int(logic_3)
        # Select 10 entries
        if (logic_4 >= 10):
            user_dropdown = driver.find_element_by_id("order-table_length").find_element_by_class_name("input-sm")
            option_text = "10"
            for option in user_dropdown.find_elements_by_tag_name('option'):
                if option.text == option_text:
                    option.click()
                    break
            driver.implicitly_wait(10)
            actual_message = driver.find_element_by_id("order-table_info").text
            expected_message = "Showing 1 to 10"
            assert expected_message in actual_message
        else:
            user_dropdown = driver.find_element_by_id("order-table_length").find_element_by_class_name("input-sm")
            option_text = "10"
            for option in user_dropdown.find_elements_by_tag_name('option'):
                if option.text == option_text:
                    option.click()
                    break
            driver.implicitly_wait(10)
            actual_message = driver.find_element_by_id("order-table_info").text
            expected_message = "Showing 1 to " + logic_4.__str__()
            assert expected_message in actual_message
        # Select 25 entries
        option_text = "25"
        user_dropdown = driver.find_element_by_id("order-table_length").find_element_by_class_name("input-sm")
        for option in user_dropdown.find_elements_by_tag_name('option'):
            if option.text == option_text:
                option.click()
                break

        if (logic_4 >= 25):
            actual_message = driver.find_element_by_id("order-table_info").text
            expected_message = "Showing 1 to 25"
            assert expected_message in actual_message
        else:
            actual_message = driver.find_element_by_id("order-table_info").text
            expected_message = "Showing 1 to " + logic_4.__str__()
            assert expected_message in actual_message

        # Select 50 entries
        option_text = "50"
        user_dropdown = driver.find_element_by_id("order-table_length").find_element_by_class_name("input-sm")
        for option in user_dropdown.find_elements_by_tag_name('option'):
            if option.text == option_text:
                option.click()
                break

        if (logic_4 >= 50):
            actual_message = driver.find_element_by_id("order-table_info").text
            expected_message = "Showing 1 to 50"
            assert expected_message in actual_message
        else:
            actual_message = driver.find_element_by_id("order-table_info").text
            expected_message = "Showing 1 to " + logic_4.__str__()
            assert expected_message in actual_message

        # Select 100 entries
        option_text = "100"
        user_dropdown = driver.find_element_by_id("order-table_length").find_element_by_class_name("input-sm")
        for option in user_dropdown.find_elements_by_tag_name('option'):
            if option.text == option_text:
                option.click()
                break

        if (logic_4 >= 100):
            actual_message = driver.find_element_by_id("order-table_info").text
            expected_message = "Showing 1 to 100"
            assert expected_message in actual_message
        else:
            actual_message = driver.find_element_by_id("order-table_info").text
            expected_message = "Showing 1 to " + logic_4.__str__()
        assert expected_message in actual_message

    # ======================================C84===============8Dec===============================================

    def test_Sales_Verify_Search_functionality_in_Orders_My_Open_Orders_C84(self, impersonate_sales):
        # Verify Search functionality in Orders/My Open Orders page.
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Verify Orders tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        # Click on Orders tab button
        driver.find_element_by_link_text("Orders").click()
        # Select My Open Orders
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'My Open Orders')))
        driver.find_element_by_link_text("My Open Orders").click()

        # Enter Valid Order Id
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'input-sm')))
        valid_orderId="01-497572"
        driver.find_element_by_xpath("//input[@class='form-control input-sm']").clear()
        driver.find_element_by_xpath("//input[@class='form-control input-sm']").send_keys(valid_orderId)
        driver.implicitly_wait(15)
        search_orderId=driver.find_element_by_xpath("//tbody/tr/td[1]").text
        # Check Search result
        assert search_orderId in valid_orderId

        # Enter Valid Client
        valid_client="Ratner"
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//input[@class='form-control input-sm']").clear()
        driver.find_element_by_xpath("//input[@class='form-control input-sm']").send_keys(valid_client)
        driver.implicitly_wait(15)
        search_client=driver.find_element_by_xpath("//tbody/tr/td[2]").text
        # Check Search result
        assert search_client in  valid_client

        #Enter Invalid Order Id
        valid_orderId="Ygyug267"
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//input[@class='form-control input-sm']").clear()
        driver.find_element_by_xpath("//input[@class='form-control input-sm']").send_keys(valid_orderId)
        driver.implicitly_wait(15)
        search_orderId=driver.find_element_by_class_name("dataTables_empty").text
        #Check Search result
        assert (search_orderId in valid_orderId) == 0

    # ======================C85===============8Dec========================================================

    def test_Sales_Verify_pagination_functionality_in_Orders_My_Open_Orders_C85(self, impersonate_sales):
        # Verify pagination functionality in Orders/My Open Orders page.
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Verify Orders tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        driver.find_element_by_link_text("Orders").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'My Open Orders')))
        driver.find_element_by_class_name("sub-nav").find_element_by_link_text("My Open Orders").click()
        # Next and previous button should work successfully
        wait.until(EC.visibility_of_element_located((By.ID,'order-table_previous')))
        expected_disable_previous = "disabled"
        actual_disable_previous = driver.find_element_by_id("order-table_previous").get_attribute("class")
        assert expected_disable_previous in actual_disable_previous
        # Click on Next
        driver.find_element_by_link_text("Next").click()
        # Verfiy previous button disabled
        expected_disable_previous = "paginate_button previous"
        actual_disable_previous = driver.find_element_by_id("order-table_previous").get_attribute("class")
        assert expected_disable_previous in actual_disable_previous
        # The current page number is highlighted
        expected_current_page_color = "rgba(229, 65, 45, 1)"
        actual_current_page_color = driver.find_element_by_link_text("2").value_of_css_property("background-color")
        assert expected_current_page_color in actual_current_page_color

    # ============================================C86===============8Dec======================================

    def test_Sales_Verify_Sorting_functionality_in_Orders_My_Open_Orders_C86(self, impersonate_sales):
        # Verify sorting functionality on different columns in Orders/My Open Orders page.
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Verify Orders tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        driver.find_element_by_link_text("Orders").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'My Open Orders')))
        driver.find_element_by_class_name("sub-nav").find_element_by_link_text("My Open Orders").click()

        # Verify ascending order for Order Id
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'td-order-id')))
        time.sleep(1)
        expected_order = "ascending"
        actual_order = driver.find_element_by_class_name("td-order-id").get_attribute("aria-sort")
        assert actual_order in expected_order

        # Verify descending order for Order Id
        driver.find_element_by_class_name("td-order-id").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'td-order-id')))
        time.sleep(1)
        expected_order = "descending"
        actual_order = driver.find_element_by_class_name("td-order-id").get_attribute("aria-sort")
        assert actual_order in expected_order

        # Verify ascending order for client
        a = driver.find_elements_by_class_name("sorting")
        a[0].click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'sorting_asc')))
        expected_order = "ascending"
        actual_order = driver.find_element_by_id("order-table").find_element_by_class_name("sorting_asc").get_attribute("aria-sort")
        assert actual_order in expected_order

        # Verify descending order for client
        a = driver.find_element_by_class_name("sorting_asc")
        a.click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'sorting_desc')))
        expected_order = "descending"
        actual_order = a.get_attribute("aria-sort")
        assert actual_order in expected_order

        # Verify ascending order for Ship by date
        a = driver.find_elements_by_class_name("sorting")
        a[1].click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'sorting_asc')))
        expected_order = "ascending"
        actual_order = driver.find_element_by_id("order-table").find_element_by_class_name("sorting_asc").get_attribute("aria-sort")
        assert actual_order in expected_order

        # Verify descending order for Ship by date
        a = driver.find_element_by_class_name("sorting_asc")
        a.click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'sorting_desc')))
        expected_order = "descending"
        actual_order = a.get_attribute("aria-sort")
        assert actual_order in expected_order

        # Verify ascending order for In hand Date
        a = driver.find_elements_by_class_name("sorting")
        a[2].click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'sorting_asc')))
        expected_order = "ascending"
        actual_order = driver.find_element_by_id("order-table").find_element_by_class_name("sorting_asc").get_attribute("aria-sort")
        assert actual_order in expected_order

        # Verify descending order for In hand Date
        a = driver.find_element_by_class_name("sorting_asc")
        a.click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'sorting_desc')))
        expected_order = "descending"
        actual_order = a.get_attribute("aria-sort")
        assert actual_order in expected_order


    # ===================================================10 Dec=====================================================
    # =============================================================101==============================================
    def test_SalesVerifyMakeSubscriptionFunctionality_C101(self, impersonate_sales):
        # Verify the Make a subscription functionality in Reports/Account Receivable page.
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        driver.find_element_by_link_text("Reports").click()
        # Click on Personal button.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Personal')))
        driver.find_element_by_link_text("Personal").click()
        # Click on Accounts Receivable tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Accounts Receivable')))
        driver.find_element_by_link_text("Accounts Receivable").click()
        # Click on "Make a Subscription" button.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()

        # Create Subscription
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'modal-header')))
        assert driver.find_element_by_class_name("modal-header").is_displayed()

        random_number = str(randint(10, 999))
        name = "SalesSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        # Select User in subscription
        wait.until(EC.visibility_of_element_located((By.ID,'user_id')))
        select = Select(driver.find_element_by_id("user_id"))
        options = select.options
        options[1].click()
        time.sleep(1)
        driver.find_element_by_id("next_btn").click()

        # "Subscription saved" message should be displayed.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'noty_text')))
        time.sleep(1)

        # Subscription should be display in subscriptions page with correct data.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Subscriptions')))
        driver.find_element_by_link_text("Subscriptions").click()
        wait.until(EC.visibility_of_element_located((By.ID,'jobs_table')))
        time.sleep(1)
        NameNew_value = driver.find_element_by_id("jobs_table").text
        assert name in NameNew_value

    # ========================================================99==============================================
    def test_SalesVerifyGenerateReportFunctionality_C99(self, impersonate_sales):
        # Verify the Generate Report functionality in Reports/Account Receivable page.
        driver = impersonate_sales['webdriver']
        # Verify page load
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Personal')))
        driver.find_element_by_link_text("Personal").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Accounts Receivable')))
        driver.find_element_by_link_text("Accounts Receivable").click()

        # check header
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        wait.until(EC.visibility_of_element_located((By.ID, 'subscription_btn')))

        # User name should be displayed in the drop down.
        select = Select(driver.find_element_by_id("selector"))
        selected_option = select.first_selected_option
        expected_selection = "Schulman, Anne"
        actual_selection = selected_option.text
        assert expected_selection in actual_selection

        # On clicking " Generate Report" button, Loading icon should display when collecting data.
        driver.find_element_by_class_name("btn-success").click()
        time.sleep(1)
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(3)
        # Generated report should be displayed on the same page.
        assert driver.find_element_by_id("ReportViewerForm").is_displayed()

    # ==================================110===========================================================

    def test_SalesVerifySubmittedSubscription_C110(self, impersonate_sales):
        # Verify submitted subscription show in the Subscriptions page.
        driver = impersonate_sales['webdriver']
        # Verify page load
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        # Click on Personal button.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Personal')))
        driver.find_element_by_link_text("Personal").click()
        # Click on Accounts Receivable tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Accounts Receivable')))
        driver.find_element_by_link_text("Accounts Receivable").click()

        # Click on Make a Subscription button.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()
        random_number = str(randint(10, 999))
        name = "SalesSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        # Select User in subscription
        wait.until(EC.visibility_of_element_located((By.ID,'user_id')))
        select = Select(driver.find_element_by_id("user_id"))
        options = select.options
        options[1].click()
        time.sleep(1)
        # Save Subscription
        driver.find_element_by_id("next_btn").click()

        # "Subscription saved" message should be displayed.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'noty_text')))
        assert driver.find_element_by_class_name("noty_text").is_displayed()

        # On subscriptions page, Subscription name should reflect with Modify and Delete button.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Subscriptions')))
        time.sleep(1)
        driver.find_element_by_link_text("Subscriptions").click()
        wait.until(EC.visibility_of_element_located((By.ID,'jobs_table')))
        NameNew_value = driver.find_element_by_id("jobs_table").text
        assert name in NameNew_value

        # Check number of subscriptions
        trs = driver.find_element_by_id('jobs_table').find_elements_by_tag_name('tr')
        trsc = len(trs)
        # Get number of modify buttons
        trm = driver.find_elements_by_link_text("Modify")
        trmc = len(trm)
        # Get number of Delete buttons
        trd = driver.find_elements_by_link_text("Delete")
        trdc = len(trd)

    # ==============================C89====10th Dec=========================================
    def test_SalesVerify_search_functionality_Orders_Orders_Search_page_C89(self, impersonate_sales):
        # Verify the search functionality in Orders/Orders Search page
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Orders tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        driver.find_element_by_link_text("Orders").click()
        # Click on Order Search
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Order Search')))
        driver.find_element_by_class_name("sub-nav").find_element_by_link_text("Order Search").click()

        # Click Search button
        wait.until(EC.visibility_of_element_located((By.ID,'gen_search')))
        driver.find_element_by_id("gen_search").click()
        # Verify table loaded
        wait.until(EC.visibility_of_element_located((By.ID,'orders_table_length')))
        assert driver.find_element_by_id("orders_table_length").is_displayed()
        # Verify search
        driver.find_element_by_id("search_input_toggle").click()

        # select filter dates
        driver.find_element_by_name("submitted_end_date").send_keys("02/24/2015")
        driver.find_element_by_name("submitted_end_date").send_keys(Keys.TAB)
        time.sleep(1)
        driver.find_element_by_name("submitted_start_date").send_keys("02/24/2015")
        time.sleep(1)
        # Click search button
        driver.find_element_by_id("gen_search").click()
        wait.until(EC.visibility_of_element_located((By.ID,'orders_table_filter')))
        assert driver.find_element_by_id("orders_table_filter").is_displayed()
        # Verify search
        driver.find_element_by_id("search_input_toggle").click()
        # Enter incorrect order to verify message
        driver.find_element_by_name("orderid").send_keys("233")
        # Click search button
        wait.until(EC.visibility_of_element_located((By.ID,'gen_search')))
        driver.find_element_by_id("gen_search").click()

        # Verify error message  in case table is empty
        wait.until(EC.visibility_of_element_located((By.ID,'orders_table')))
        ord_tab_content = driver.find_element_by_id("orders_table").text
        no_data_message = "No results found for your search."
        if no_data_message in ord_tab_content:
            flag = 2
            assert no_data_message in ord_tab_content
        else:
            # data exists
            flag = 1

    # ===============================97===============================10Dec===============================

    def test_Sales_Verify_pagination_functionality_in_search_results_section_C97(self, impersonate_sales):
        # Verify the pagination functionality in search results section in Orders
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Orders tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        # Click on Order Search
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Order Search')))
        driver.find_element_by_class_name("sub-nav").find_element_by_link_text("Order Search").click()

        # Click search button
        wait.until(EC.visibility_of_element_located((By.ID,'gen_search')))
        driver.find_element_by_id("gen_search").click()
        # Verify report-items
        wait.until(EC.visibility_of_element_located((By.ID,'orders_table_length')))
        assert driver.find_element_by_id("orders_table_length").is_displayed()

        # Next and previous button should work successfully
        wait.until(EC.visibility_of_element_located((By.ID,'orders_table_previous')))
        expected_disable_previous = "paginate_button previous disabled"
        actual_disable_previous = driver.find_element_by_id("orders_table_previous").get_attribute("class")
        assert expected_disable_previous in actual_disable_previous
        # Click on Next
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT,'Next')))
        time.sleep(1)
        driver.find_element_by_link_text("Next").click()
        wait.until(EC.visibility_of_element_located((By.ID,'orders_table_previous')))
        time.sleep(1)
        expected_disable_previous = "paginate_button previous"
        actual_disable_previous = driver.find_element_by_id("orders_table_previous").get_attribute("class")
        assert expected_disable_previous in actual_disable_previous
        # The current page number is highlighted
        expected_current_bkpage_color = "rgba(229, 65, 45, 1)"
        # Check report has loaded and previous button is clickable
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT,'Previous')))
        if driver.find_element_by_link_text("2").is_displayed():
            actual_current_bkpage_color = driver.find_element_by_link_text("2").value_of_css_property("background-color")
            assert expected_current_bkpage_color in actual_current_bkpage_color

    # ======================C111======================================14 Dec================================

    def test_Sales_Verify_NoOtherUserExceptOneSalesUserCanAccessDataOfAnotherUser_C111(self, impersonate_sales):
        # Verify the No other user except one sales user can access the data of another sales user.
        driver = impersonate_sales['webdriver']
        # Verify page load
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on back button
        driver.back()
        # Click on Impersonate button for any other user
        driver.find_element_by_class_name("sorting_1").find_element_by_class_name("btn-info").click()
        # Verify error message "Oops, Bad Link Sorry, that page can't be found"
        act = driver.find_element_by_id("content-container").find_element_by_class_name("jumbotron").text
        exp_weekday = ["Oops, Bad Link",
                       "Sorry, that page can't be found.",
                       "Need Help?"]
        for i in exp_weekday:
            assert i in act

    # ============================C112=========================14Dec=============================================

    def test_Sales_Verify_pagination_functionality_in_Report_in_Accounts_Receivable_C112(self, impersonate_sales):
        # Verify the pagination functionality in Report  in Accounts Receivable Report.
        driver = impersonate_sales['webdriver']
        # Verify page load
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))

        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        assert driver.find_element_by_link_text("Personal").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Personal").click()
        time.sleep(1)
        # Click on Accounts Receivable.
        driver.find_element_by_link_text("Accounts Receivable").click()
        # Verify Accounts Receivable Report
        expected_Personal_Accounts_Receivable_Report = "Personal Accounts Receivable Report"
        actual_Personal_Accounts_Receivable_Report = driver.find_element_by_id("content-header").text
        assert actual_Personal_Accounts_Receivable_Report in expected_Personal_Accounts_Receivable_Report
        # Click on generate report
        driver.find_element_by_class_name("btn-success").click()
        # Report should be generated successfully on the same page.
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(3)
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
        # Verify link for export button, refresh button, data feed button
        # Verify export button
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl04_ctl00_ButtonImg").is_displayed()
        # Verify refresh button
        assert driver.find_element_by_name("ReportViewerControl$ctl05$ctl05$ctl00$ctl00$ctl00").is_displayed()
        # Verify export to data feed button
        assert driver.find_element_by_name("ReportViewerControl$ctl05$ctl07$ctl00$ctl00$ctl00").is_displayed()

    # ==========================================C122==================14Dec=================================

    def test_Sales_VerifySearchFunctionalityInGeneratedReportOnReportsOrders_C122(self, impersonate_sales):
        # Verify the search functionality in generated report on Reports/Orders.
        driver = impersonate_sales['webdriver']
        # Verify page load
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))

        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        assert driver.find_element_by_link_text("Personal").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Personal").click()
        # Click on Open Orders.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Open Orders')))
        driver.find_element_by_link_text("Open Orders").click()
        # Verify Open Orders Report
        expected_header_Open_Orders_Report = "Open Orders Report "
        actual_header_Open_Orders_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Open_Orders_Report in expected_header_Open_Orders_Report
        # Click on generate report
        driver.find_element_by_class_name("btn-success").click()
        # Verify search field
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'input-sm')))
        assert driver.find_element_by_class_name("input-sm").is_displayed()
        # Send valid report content in search field "Anne Schulman" and verify same
        driver.find_element_by_id("dataTable_filter").find_element_by_class_name("input-sm").send_keys("Anne Schulman")
        actual = driver.find_element_by_class_name("sorting_1").text
        exp_content = ['Anne Schulman']
        for b in exp_content:
            assert b in actual
        driver.find_element_by_id("dataTable_filter").find_element_by_class_name("input-sm").clear()
        # Send wrong entry  and verify expected message
        driver.find_element_by_id("dataTable_filter").find_element_by_class_name("input-sm").send_keys("xyz123")
        assert driver.find_element_by_class_name("dataTables_empty").is_displayed()
        expected_message = "No matching records found"
        actual_message = driver.find_element_by_class_name("dataTables_empty").text
        assert actual_message in expected_message

    # ===============================================C119========================================================
    def test_Sales_VerifyShowingEntriesFunctionality_C119(self, impersonate_sales):
        # Verify Showing 1 to 10,25,100,All entries functionality in page total section in Open Orders page.
        driver = impersonate_sales['webdriver']
        # Verify page load
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Orders')))
        # Click on Orders tab button
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        # Select My Open Orders
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'My Open Orders')))
        driver.find_element_by_link_text("My Open Orders").click()
        time.sleep(1)
        # Contents of My Open Order
        wait.until(EC.visibility_of_element_located((By.ID, 'order-table')))
        # Wait for page load
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        #driver.find_element_by_id("sub_btn").click()

        # Verify Show 10 entries is displayed by default
        wait.until(EC.visibility_of_element_located((By.NAME, 'order-table_length')))
        select = Select(driver.find_element_by_name(('order-table_length')))
        selected_option = select.first_selected_option
        expected_selection = "10"
        actual_selection = selected_option.text
        assert expected_selection in actual_selection
        total_entries = driver.find_element_by_id("order-table_info").text
        logic_1 = total_entries.split('of', 1)
        logic_2 = logic_1[1].strip(" ")
        logic_3 = logic_2.strip(" entries")
        logic_4 = int(logic_3)
        # Select 10 entries
        if (logic_4 >= 10):
            user_dropdown = driver.find_element_by_id("order-table_length").find_element_by_class_name("input-sm")
            option_text = "10"
            for option in user_dropdown.find_elements_by_tag_name('option'):
                if option.text == option_text:
                    option.click()
                    break

            actual_message = driver.find_element_by_id("order-table_info").text
            expected_message = "Showing 1 to 10"
            assert expected_message in actual_message
        else:
            user_dropdown = driver.find_element_by_id("order-table_length").find_element_by_class_name("input-sm")
            option_text = "10"
            for option in user_dropdown.find_elements_by_tag_name('option'):
                if option.text == option_text:
                    option.click()
                    break

            actual_message = driver.find_element_by_id("order-table_info").text
            expected_message = "Showing 1 to " + logic_4.__str__()
            assert expected_message in actual_message

        # Select 25 entries
        option_text = "25"
        user_dropdown = driver.find_element_by_id("order-table_length").find_element_by_class_name("input-sm")
        for option in user_dropdown.find_elements_by_tag_name('option'):
            if option.text == option_text:
                option.click()
                break

        if (logic_4 >= 25):
            actual_message = driver.find_element_by_id("order-table_info").text
            expected_message = "Showing 1 to 25"
            assert expected_message in actual_message
        else:
            actual_message = driver.find_element_by_id("order-table_info").text
            expected_message = "Showing 1 to " + logic_4.__str__()
            assert expected_message in actual_message

        # Select 50 entries
        option_text = "50"
        user_dropdown = driver.find_element_by_id("order-table_length").find_element_by_class_name("input-sm")
        for option in user_dropdown.find_elements_by_tag_name('option'):
            if option.text == option_text:
                option.click()
                break

        if (logic_4 >= 50):
            actual_message = driver.find_element_by_id("order-table_info").text
            expected_message = "Showing 1 to 50"
            assert expected_message in actual_message
        else:
            actual_message = driver.find_element_by_id("order-table_info").text
            expected_message = "Showing 1 to " + logic_4.__str__()
            assert expected_message in actual_message

        # Select 100 entries
        option_text = "100"
        user_dropdown = driver.find_element_by_id("order-table_length").find_element_by_class_name("input-sm")
        for option in user_dropdown.find_elements_by_tag_name('option'):
            if option.text == option_text:
                option.click()
                break

        if (logic_4 >= 100):
            actual_message = driver.find_element_by_id("order-table_info").text
            expected_message = "Showing 1 to 100"
            assert expected_message in actual_message
        else:
            actual_message = driver.find_element_by_id("order-table_info").text
            expected_message = "Showing 1 to "
            assert expected_message in actual_message

    # ===============================================C90==================================================

    def test_Sales_VerifyResetFunctionality_C90(self, impersonate_sales):
        # Verify the reset functionality in Orders/Orders Search page.
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Orders tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        time.sleep(1)
        driver.find_element_by_link_text("Orders").click()
        # Click on Order Search
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Order Search')))
        driver.find_element_by_class_name("sub-nav").find_element_by_link_text("Order Search").click()

        # Click Advanced filters button
        # wait.until(EC.visibility_of_element_located((By.ID,'toggle')))
        # driver.find_element_by_id("toggle").click()
        # Invoice click
        wait.until(EC.visibility_of_element_located((By.ID,'invoice_nbr')))
        invoice_number = "ABC123"
        driver.find_element_by_id("invoice_nbr").send_keys(invoice_number)
        # Order Number
        orderid_number = "ABC123"
        driver.find_element_by_id("orderid").send_keys(orderid_number)
        # Select the Start and end date
        driver.find_element_by_name("submitted_start_date").click()
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
        wait.until(EC.visibility_of_element_located((By.ID,'orderid')))
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


    # ===================================================146==============================================

    def test_SalesVerifySubmittedSubscription_C146(self, impersonate_sales):
        # Verify submitted subscription show in the Subscriptions page
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Personal button
        driver.find_element_by_link_text("Personal").click()
        time.sleep(1)
        # Click on Accounts Receivable tab
        driver.find_element_by_link_text("Sales Order by Dollar Value").click()

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

        # Click on Make a Subscription button
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()
        random_number = str(randint(10, 999))
        name = "TestBSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        driver.find_element_by_id("next_btn").click()
        time.sleep(1)
        # On subscriptions page, Subscription name should reflect with Modify and Delete button
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Subscriptions')))
        time.sleep(1)
        driver.find_element_by_link_text("Subscriptions").click()
        wait.until(EC.visibility_of_element_located((By.ID,'jobs_table')))
        NameNew_value = driver.find_element_by_id("jobs_table").text
        assert name in NameNew_value

        # Check the Number of subscriptions
        trs = driver.find_element_by_id('jobs_table').find_elements_by_tag_name('tr')
        trsc = len(trs)
        # Get number of modify buttons
        trm = driver.find_elements_by_link_text("Modify")
        trmc = len(trm)
        # Get number of Delete buttons
        trd = driver.find_elements_by_link_text("Delete")
        trdc = len(trd)

    # ==================================124==============================================
    def test_SalesVerifyMakeSubscription_C124(self, impersonate_sales):
        # Verify the Make a subscription content in Reports/Open Orders.
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        driver.find_element_by_link_text("Reports").click()
        # Click on Personal button
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Personal')))
        driver.find_element_by_link_text("Personal").click()
        # Click on Open Orders tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Open Orders')))
        driver.find_element_by_link_text("Open Orders").click()
        wait.until(EC.visibility_of_element_located((By.ID,'sub_btn')))
        driver.find_element_by_id("sub_btn").click()

        # Excel button to load
        wait.until(EC.visibility_of_element_located((By.ID,'xls_btn')))
        assert driver.find_element_by_id("xls_btn").is_displayed()
        # Click on Make a Subscription button
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()

        # Subscription Name is displayed
        wait.until(EC.visibility_of_element_located((By.ID,'sub_name')))
        assert driver.find_element_by_id("sub_name").is_displayed()
        # Email To is displayed
        assert driver.find_element_by_id("email").is_displayed()
        # Delivery Format is displayed
        assert driver.find_element_by_id("excel1").is_displayed()
        # Time is displayed
        assert driver.find_element_by_id("time").is_displayed()
        # Receive report on is displayed
        driver.find_element_by_class_name("well-sm").is_displayed()
        # Back button is displayed
        assert driver.find_element_by_class_name("btn-default").is_displayed()
        # Save Subscription button is displayed
        assert driver.find_element_by_id("next_btn").is_displayed()

    # ==============C120===================15 Dec=========================================
    def test_SalesVerifySortingFunctionalityInGeneratedReportOnReportsOpen_C120(self, impersonate_sales):
        # Verify the sorting functionality in generated report on Reports/Open
        driver = impersonate_sales['webdriver']
        # Verify page load
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        assert driver.find_element_by_link_text("Personal").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Personal tab.
        driver.find_element_by_link_text("Personal").click()
        # Click on Open Orders tab.
        driver.find_element_by_link_text("Open Orders").click()
        # Verify Open Orders Report
        expected_header_Open_Orders_Report = "Open Orders Report "
        actual_header_Open_Orders_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Open_Orders_Report in expected_header_Open_Orders_Report
        # Click on generate report button
        driver.find_element_by_class_name("btn-success").click()
        # Verify ascending order for Account executive
        expected_order = "ascending"
        actual_order = driver.find_element_by_class_name("sorting_asc").get_attribute("aria-sort")
        assert actual_order in expected_order
        # Verify descending order for SO#
        driver.find_element_by_class_name("sorting").click()
        expected_order = "ascending"
        actual_order = driver.find_element_by_class_name("sorting_asc").get_attribute("aria-sort")
        assert actual_order in expected_order

    # ===========================C92=============================================15Dec===========================

    def test_SalesVerifyChangeColumnFunctionalityInOrdersSearch_C92(self, impersonate_sales):
        # Verify the change column functionality in search results section in Orders/Orders Search page.
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on order tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        # Click on Order Search
        driver.find_element_by_class_name("sub-nav").find_element_by_link_text("Order Search").click()
        # Click on advance search button
        #driver.find_element_by_id("toggle").click()
        # Enter client name
        wait.until(EC.visibility_of_element_located((By.ID,'client')))
        driver.find_element_by_id("client").send_keys("Ratner")
        # Select order status
        driver.find_element_by_class_name("dropdown-toggle").click()
        # Click on generate button
        driver.find_element_by_id("gen_search").click()
        # Verify input button
        assert driver.find_element_by_class_name("input-sm").is_displayed()
        # Click on change column
        driver.find_element_by_id("orders_table_wrapper").find_element_by_class_name("ColVis_MasterButton").click()
        wait.until(EC.visibility_of_element_located((By.ID,'orders_table')))
        actual=driver.find_element_by_class_name("ColVis_collection").text
        time.sleep(1)
        for tr in driver.find_elements_by_id('orders_table'):
            ths=tr.find_elements_by_tag_name('th')
            if ths:
                data= [th.text for th in ths]
        array = actual.split("\n")
        size=len(data)
        for i in range(size):
            assert data[i] in array
        driver.find_element_by_class_name("input-sm").click()
        time.sleep(1)
    # ===========================C93=========15 Dec==============================================================

    def test_SalesVerifyFilterColumnFunctionalityInOrdersSearch_C93(self, impersonate_sales):
        # Verify the filter functionality in search results section in Orders/Orders Search page.
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on order tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        driver.find_element_by_link_text("Orders").click()
        # Click on Order Search
        driver.find_element_by_class_name("sub-nav").find_element_by_link_text("Order Search").click()
        time.sleep(1)
        # Click on generate report button
        driver.find_element_by_id("gen_search").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'input-sm')))
        assert driver.find_element_by_class_name("input-sm").is_displayed()
        # Verify valid entry and search for same
        driver.find_element_by_id("orders_table_filter").find_element_by_class_name("input-sm").send_keys("Ratner")
        time.sleep(5)
        actual = driver.find_element_by_id("orders_table").find_element_by_class_name("odd").text
        exp_content = ['Ratner']
        for b in exp_content:
            assert b in actual
        driver.find_element_by_id("orders_table_filter").find_element_by_class_name("input-sm").clear()
        time.sleep(3)
        # Send wrong entry in search
        driver.find_element_by_id("orders_table_filter").find_element_by_class_name("input-sm").send_keys("xyz123")
        time.sleep(3)
        # CHECK DATA TABLE EMPTY TEXT
        dt_text = driver.find_element_by_class_name('dataTables_empty').text
        print (dt_text)
        expected_message = "No results found for your search."
        assert dt_text in expected_message

    # ==================================C142==========22 Jan====================================================

    def test_SalesVerifyContentOnSupplierDiversityPage_142(self, impersonate_sales):
        # Verify the contents on Supplier Diversity page.
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        time.sleep(1)
        # Click on Personal tab.
        operations = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Personal')))
        operations.click()
        time.sleep(1)
        # Click on Supplier Diversity tab.
        supplier_diversity = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Supplier Diversity')))
        supplier_diversity.click()
        time.sleep(1)
        # Verify the contents on reports / Personal / Supplier Diversity page.
        # Report: Supplier Diversity
        expected_header = "Report: Supplier Diversity"
        actual_header = driver.find_element_by_class_name("panel-heading").text
        assert expected_header in actual_header
        # Drop down with multiple clients
        expected_clients = "select"
        actual_clients = driver.find_element_by_id("custno").tag_name
        assert expected_clients in actual_clients
        # Generate Report button
        assert driver.find_element_by_id("sub_btn").is_displayed()
        # Make a Subscription button
        assert driver.find_element_by_class_name("btn-primary").is_displayed()
        # PO Start
        assert driver.find_element_by_name("daterange").is_displayed()

    # ==================================143==========22 Jan=============================================
    def test_SalesVerifyBackButtonFunctionalityOnSupplierDiversityPage_C143(self, impersonate_sales):
        # Verify the back button functionality on Supplier Diversity page.
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        time.sleep(1)
        # Click on Personal tab.
        operations = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Personal')))
        operations.click()
        time.sleep(1)
        # Click on Supplier Diversity tab.
        supplier_diversity = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Supplier Diversity')))
        supplier_diversity.click()
        # Verify the contents on reports / Personal / Supplier Diversity page.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'panel-heading')))
        expected_header = "Report: Supplier Diversity"
        actual_header = driver.find_element_by_class_name("panel-heading").text
        assert expected_header in actual_header
        # Drop down with multiple clients
        expected_clients = "select"
        actual_clients = driver.find_element_by_id("custno").tag_name
        assert expected_clients in actual_clients
        # Generate Report button
        assert driver.find_element_by_id("sub_btn").is_displayed()
        # Make a Subscription button
        assert driver.find_element_by_class_name("btn-primary").is_displayed()
        # PO Start
        assert driver.find_element_by_name("daterange").is_displayed()

        #Click on make a subscription button.
        driver.find_element_by_id("subscription_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'modal-title')))

        # Submit the subscription form with all the details.
        random_number=str(randint(10,999))
        name="TestSubscription"+random_number
        wait.until(EC.visibility_of_element_located((By.ID,'sub_name')))
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_id("email").clear()
        email="apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        time.sleep(1)
        driver.find_element_by_name("days_of_week").click()
        assert driver.find_element_by_class_name('btn-default').is_displayed()
        driver.find_element_by_id("next_btn").click()

        # Subscription form submitted successfully and display message Subscription Saved.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'noty_text')))
        actual_message=driver.find_element_by_class_name("noty_text").text
        time.sleep(1)
        expected_message="Subscription saved."
        assert expected_message in actual_message
        time.sleep(1)

    # ==================================C144==========22 Jan=============================================
    def test_SalesVerifyGenerateReportFunctionalityOnSupplierDiversityPage_144(self, impersonate_sales):
        # Verify the generate report functionality
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        time.sleep(1)
        # Click on Personal tab.
        personal = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Personal')))
        personal.click()
        time.sleep(1)
        # Click on Supplier Diversity tab.
        supplier_diversity = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Supplier Diversity')))
        supplier_diversity.click()
        time.sleep(1)

        # Selecting by Xpath for partial text
        driver.find_element_by_id('custno').find_element_by_xpath("//option[contains(text(),'ACVS')]").click()
        # Select the ship Start date  and ship end date
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
        # Click on Generate report button.
        driver.find_element_by_class_name("btn-success").click()
        # Switch to report
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(3)
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_displayed()
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()

    # ==================================C132==========25 Jan=============================================

    def test_SalesVerifyShowing1OfXXEntriesFunctionality_132(self, impersonate_sales):
        # Verify Showing 1 of 'xx' entries functionality in report section in Reports/Sales Order by Dollar Value page.
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        assert driver.find_element_by_link_text("Personal").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Personal tab.
        driver.find_element_by_link_text("Personal").click()
        # Click on Sales Order by Dollar Value.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Sales Order by Dollar Value')))
        driver.find_element_by_id("personal-report-items").find_element_by_link_text("Sales Order by Dollar Value").click()
        # Verify Sales Order by Dollar Value Report page
        expected_header_Sales_Order_by_Dollar_Value_Report = "Sales Order by Dollar Value Report"
        actual_header_Sales_Order_by_Dollar_Value_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Sales_Order_by_Dollar_Value_Report in expected_header_Sales_Order_by_Dollar_Value_Report
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
        # Click on Generate report button.
        driver.find_element_by_id("sub_btn").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'report_src')))
        driver.switch_to_frame("report_src")
        # Wait until report loads
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(3)

        # In report, Verify show 1 of x page by default
        expected_value = "1"
        actual_value = driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").get_attribute("value")
        assert expected_value in actual_value
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()
        expected_of = "of"
        actual_of = driver.find_element_by_class_name("ToolBarButtonsCell").text
        assert expected_of in actual_of
    # ==================================C136==========25 Jan=============================================
    def test_SalesVerifyExportButtonFunctionality_C136(self, impersonate_sales):
        # Verify Export button functionality in the report section on Reports/Sales Order by Dollar Value page.
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        assert driver.find_element_by_link_text("Personal").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Personal tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Personal')))
        driver.find_element_by_link_text("Personal").click()
        # Click on Sales Order by Dollar Value.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Sales Order by Dollar Value')))
        driver.find_element_by_id("personal-report-items").find_element_by_link_text("Sales Order by Dollar Value").click()
        # Verify Sales Order by Dollar Value Report   page
        expected_header_Sales_Order_by_Dollar_Value_Report = "Sales Order by Dollar Value Report"
        actual_header_Sales_Order_by_Dollar_Value_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Sales_Order_by_Dollar_Value_Report in expected_header_Sales_Order_by_Dollar_Value_Report
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
        # Click on Generate report button.
        driver.find_element_by_id("sub_btn").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'report_src')))
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(3)
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_displayed()
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()

        driver.find_element_by_id("ReportViewerControl_ctl05_ctl04_ctl00_ButtonLink").click()
        time.sleep(1)
        # Verify report can be exported in following format
        act = driver.find_elements_by_class_name("ActiveLink")
        time.sleep(1)
        exp_report_type = ['CSV (comma delimited)','Excel']
        for v in act:
            name = v.text
            assert name in exp_report_type
            time.sleep(1)

    # ==================================C137==========25 Jan=============================================

    def test_SalesVerifyRefreshButtonFunctionality_137(self, impersonate_sales):
        # Verify Refresh button functionality in Reports/Sales Order by Dollar Value page.
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        assert driver.find_element_by_link_text("Personal").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Personal tab.
        driver.find_element_by_link_text("Personal").click()
        # Click on Sales Order by Dollar Value.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Sales Order by Dollar Value')))
        driver.find_element_by_id("personal-report-items").find_element_by_link_text("Sales Order by Dollar Value").click()
        # Verify Sales Order by Dollar Value Report   page
        expected_header_Sales_Order_by_Dollar_Value_Report = "Sales Order by Dollar Value Report"
        actual_header_Sales_Order_by_Dollar_Value_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Sales_Order_by_Dollar_Value_Report in expected_header_Sales_Order_by_Dollar_Value_Report
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
        # Click on Generate report button.
        driver.find_element_by_id("sub_btn").click()
        # Switch to  report content.
        wait.until(EC.visibility_of_element_located((By.ID, 'report_src')))
        driver.switch_to_frame("report_src")
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(3)
        original_text = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        # Click on Refresh icon. Generated report should be refreshed.
        driver.find_element_by_name("ReportViewerControl$ctl05$ctl05$ctl00$ctl00$ctl00").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(1)
        latest_text = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        assert (original_text is not latest_text)

    # ==================================C138==========27 Jan=============================================
    def test_SalesVerifyDateAndTimeInReports_C138(self, impersonate_sales):
        # Verify the generated report Date and Time in Reports/Sales Order by Dollar Value page.
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Personal')))
        assert driver.find_element_by_link_text("Personal").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Personal tab.
        driver.find_element_by_link_text("Personal").click()
        # Click on Sales Order by Dollar Value.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Sales Order by Dollar Value')))
        driver.find_element_by_id("personal-report-items").find_element_by_link_text("Sales Order by Dollar Value").click()
        # Verify Sales Order by Dollar Value Report page
        expected_header_Sales_Order_by_Dollar_Value_Report = "Sales Order by Dollar Value Report"
        actual_header_Sales_Order_by_Dollar_Value_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Sales_Order_by_Dollar_Value_Report in expected_header_Sales_Order_by_Dollar_Value_Report
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
        # Click on Generate report button.
        driver.find_element_by_id("sub_btn").click()
        # Switch to  report content.
        wait.until(EC.visibility_of_element_located((By.ID, 'report_src')))
        driver.switch_to_frame("report_src")
        # Verify the Date and Time of the generated report.
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(4)
        actual_date_Time = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        exp_date_Time = "Report Created On:"
        exp_date_Time1 = "AM"
        exp_date_Time2 = "PM"
        assert exp_date_Time in actual_date_Time
        assert ((exp_date_Time1 in actual_date_Time) | (exp_date_Time2 in actual_date_Time))


    # ==================================C140==========27 Jan=============================================
    def test_SalesVerifyDateAndTimeInReports_C140(self, impersonate_sales):
        # Verify the generated report Date and Time in Reports/Sales Order by Dollar Value page.
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        assert driver.find_element_by_link_text("Personal").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Personal tab.
        driver.find_element_by_link_text("Personal").click()
        # Click on Sales Order by Dollar Value.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Sales Order by Dollar Value')))
        driver.find_element_by_id("personal-report-items").find_element_by_link_text("Sales Order by Dollar Value").click()
        # Verify Sales Order by Dollar Value Report page
        expected_header_Sales_Order_by_Dollar_Value_Report = "Sales Order by Dollar Value Report"
        actual_header_Sales_Order_by_Dollar_Value_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Sales_Order_by_Dollar_Value_Report in expected_header_Sales_Order_by_Dollar_Value_Report
        # Click on make a subscription button.
        driver.find_element_by_id("subscription_btn").click()
        # Verify subscription pop up
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal-header')))
        expected_PopUp_Sales_Order_by_Dollar_Value_Report = "Subscription for: Sales Order by Dollar Value Report"
        actual_PopUp_Sales_Order_by_Dollar_Value_Report = driver.find_element_by_id("myModalLabel").text
        assert actual_PopUp_Sales_Order_by_Dollar_Value_Report in expected_PopUp_Sales_Order_by_Dollar_Value_Report
        # Verify Subscription Name
        assert driver.find_element_by_id("sub_name").is_displayed()
        # Verify Email to field
        assert driver.find_element_by_id("email").is_displayed()
        # Verify Delivery format in excel
        assert driver.find_element_by_class_name("radio").is_displayed()
        # Verify time
        assert driver.find_element_by_id("time").is_displayed()
        # Verify receive report day
        assert driver.find_element_by_id("modal_selector").is_displayed()
        expected_days = ['Sunday',
                         'Monday',
                         'Tuesday',
                         'Wednesday',
                         'Thursday',
                         'Friday',
                         'Saturday']
        days = driver.find_element_by_id("day_box")
        actual_days = days.find_elements_by_class_name("checkbox")
        for day in actual_days:
            name = day.text
            assert name in expected_days
        # Verify back button
        assert driver.find_element_by_class_name("btn-default").is_displayed()
        # Verify save Subscription button
        assert driver.find_element_by_id("next_btn").is_displayed()

    # ==================================C864==========27 Jan=============================================

    def test_SalesVerifySubmittedSubscriptionShowInSubscriptionPage_C864(self, impersonate_sales):
        # Verify submitted subscription show in the "subscription"page.
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Personal')))
        assert driver.find_element_by_link_text("Personal").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Personal tab.
        driver.find_element_by_link_text("Personal").click()
        # Click on Open Orders.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Open Orders')))
        driver.find_element_by_id("personal-report-items").find_element_by_link_text("Open Orders").click()
        # Verify Open Orders Report page
        expected_header_Open_Orders_Report = "Open Orders Report"
        actual_header_Open_Orders_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Open_Orders_Report in expected_header_Open_Orders_Report

        # Click on Generate report button.
        driver.find_element_by_id("sub_btn").click()
        # Verify xls button
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        assert driver.find_element_by_id("xls_btn").is_displayed()
        # Click on make a subscription button.
        driver.find_element_by_class_name("btn-primary").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal-title')))
        # Submit the subscription form with all the details.
        random_number = str(randint(10, 999))
        name = "TestGSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)

        driver.find_element_by_id("next_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'noty_text')))
        # Subscription form submitted successfully and display message Subscription Saved.
        expected_message = "Subscription saved."
        actual_message = driver.find_element_by_class_name("noty_text").text
        assert expected_message in actual_message
        # Click on Subscriptions Page
        driver.find_element_by_link_text("Subscriptions").click()
        # On subscriptions page, Subscription name should reflect with Modify and Delete button.
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

        # ==================================C107==========01 Feb =============================================

    def test_Sales_Verify_Sorting_functionality_in_Orders_BookMarks_C107(self, impersonate_sales):
        driver = impersonate_sales['webdriver']
        # Verify page load
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))

        # Verify sorting functionality on different columns in Orders/BookMarks page.
        # Click on order tab
        driver.find_element_by_link_text("Orders").click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.fa.fa-bookmark-o.fa-fw')))
        driver.find_element_by_css_selector(".fa.fa-bookmark-o.fa-fw").click()  # Click on Bookmark
        # Verify Bookmarks page is displayed.
        actualtitle = driver.find_element_by_id("content-header").text
        expectedtitle = "Bookmarks"
        assert expectedtitle in actualtitle
        wait.until(EC.visibility_of_element_located((By.ID, 'orders_table_previous')))
        # Verify ascending and descending order for 'Id' column on bookmarks page.
        expected_Ascending_order = "ascending"
        expected_Descending_order = "descending"
        actual_order = driver.find_element_by_class_name("col-id").get_attribute("aria-sort")
        assert actual_order in expected_Ascending_order
        driver.find_element_by_class_name("col-id").click()
        time.sleep(1)
        actual_order = driver.find_element_by_class_name("col-id").get_attribute("aria-sort")
        assert actual_order in expected_Descending_order
        # Verify ascending and descending order for 'Client Name' column on bookmarks page.
        a = driver.find_elements_by_class_name("col-client-name")
        a[0].click()
        time.sleep(1)
        actual_order = driver.find_element_by_id("orders_table").find_element_by_class_name("col-client-name").get_attribute("aria-sort")
        assert actual_order in expected_Ascending_order
        a = driver.find_element_by_class_name("col-client-name")
        a.click()
        time.sleep(1)
        actual_order = a.get_attribute("aria-sort")
        assert actual_order in expected_Descending_order
        # Verify ascending and descending order for 'Status' column on bookmarks page.
        a = driver.find_elements_by_class_name("col-status")
        a[0].click()
        time.sleep(1)
        actual_order = driver.find_element_by_id("orders_table").find_element_by_class_name("col-status").get_attribute("aria-sort")
        assert actual_order in expected_Ascending_order
        a = driver.find_element_by_class_name("col-status")
        a.click()
        time.sleep(1)
        actual_order = a.get_attribute("aria-sort")
        assert actual_order in expected_Descending_order
        # Verify ascending and descending order for 'Date Submitted' column on bookmarks page.
        a = driver.find_elements_by_class_name("col-date-submitted")
        a[0].click()
        time.sleep(1)
        actual_order = driver.find_element_by_id("orders_table").find_element_by_class_name("col-date-submitted").get_attribute("aria-sort")
        assert actual_order in expected_Ascending_order
        a = driver.find_element_by_class_name("col-date-submitted")
        a.click()
        time.sleep(1)
        actual_order = a.get_attribute("aria-sort")
        assert actual_order in expected_Descending_order
        # Verify ascending and descending order for 'Hands Date' column on bookmarks page.
        a = driver.find_elements_by_class_name("col-in-hands-date")
        a[0].click()
        time.sleep(1)
        actual_order = driver.find_element_by_id("orders_table").find_element_by_class_name("col-in-hands-date").get_attribute("aria-sort")
        assert actual_order in expected_Ascending_order
        a = driver.find_element_by_class_name("col-in-hands-date")
        a.click()
        time.sleep(1)
        actual_order = a.get_attribute("aria-sort")
        assert actual_order in expected_Descending_order
        # Verify ascending and descending order for 'PO' column on bookmarks page.
        a = driver.find_elements_by_class_name("col-po")
        a[0].click()
        time.sleep(1)
        actual_order = driver.find_element_by_id("orders_table").find_element_by_class_name("col-po").get_attribute("aria-sort")
        assert actual_order in expected_Ascending_order
        a = driver.find_element_by_class_name("col-po")
        a.click()
        time.sleep(1)
        actual_order = a.get_attribute("aria-sort")
        assert actual_order in expected_Descending_order
        # Verify ascending and descending order for 'Art Title' column on bookmarks page.
        a = driver.find_elements_by_class_name("col-art-title")
        a[0].click()
        time.sleep(1)
        actual_order = driver.find_element_by_id("orders_table").find_element_by_class_name("col-art-title").get_attribute("aria-sort")
        assert actual_order in expected_Ascending_order
        a = driver.find_element_by_class_name("col-art-title")
        a.click()
        time.sleep(1)
        actual_order = a.get_attribute("aria-sort")
        assert actual_order in expected_Descending_order
        # Verify ascending and descending order for 'Ship to name' column on bookmarks page.
        a = driver.find_elements_by_class_name("col-shipto-name")
        a[0].click()
        time.sleep(1)
        actual_order = driver.find_element_by_id("orders_table").find_element_by_class_name("col-shipto-name").get_attribute("aria-sort")
        assert actual_order in expected_Ascending_order
        a = driver.find_element_by_class_name("col-shipto-name")
        a.click()
        time.sleep(1)
        actual_order = a.get_attribute("aria-sort")
        assert actual_order in expected_Descending_order
        # Verify ascending and descending order for 'Type' column on bookmarks page.
        a = driver.find_elements_by_class_name("col-type")
        a[0].click()
        time.sleep(1)
        actual_order = driver.find_element_by_id("orders_table").find_element_by_class_name("col-type").get_attribute("aria-sort")
        assert actual_order in expected_Ascending_order
        a = driver.find_element_by_class_name("col-type")
        a.click()
        time.sleep(1)
        actual_order = a.get_attribute("aria-sort")
        assert actual_order in expected_Descending_order

    # ==================================C108==========01 Feb =============================================

    def test_Sales_Verify_pagination_functionality_in_Orders_BookMarks_C108(self, impersonate_sales):
        driver = impersonate_sales['webdriver']
        # Verify page load
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Verify pagination functionality in Orders/Bookmarks page.
        # Click on order tab
        driver.find_element_by_link_text("Orders").click()
        time.sleep(3)
        # Click on Bookmark
        driver.find_element_by_css_selector(".fa.fa-bookmark-o.fa-fw").click()
        # Verify Bookmarks page is displayed.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        actualtitle = driver.find_element_by_id("content-header").text
        expectedtitle = "Bookmarks"
        assert expectedtitle in actualtitle
        wait.until(EC.visibility_of_element_located((By.ID, 'orders_table_previous')))
        # Verify by default previous button is displayed as disabled.
        expected_disable_previous = "disabled"
        actual_disable_previous = driver.find_element_by_id("orders_table_previous").get_attribute("class")
        assert expected_disable_previous in actual_disable_previous
        expected_current_page_color = "rgba(229, 65, 45, 1)"

        # Click on Next if button is enabled.
        next_Button = driver.find_element_by_id("orders_table_next").get_attribute("class")
        if next_Button.find(expected_disable_previous) == -1:
            driver.find_element_by_id("orders_table_next").click()
            time.sleep(1)
            actual_current_page_color = driver.find_element_by_link_text("2").value_of_css_property("background-color")
            assert expected_current_page_color in actual_current_page_color
            # The current page number is highlighted
            driver.find_element_by_id("orders_table_previous").click()
            time.sleep(1)
            actual_current_page_color = driver.find_element_by_link_text("1").value_of_css_property("background-color")
            assert expected_current_page_color in actual_current_page_color

    # ==================================C103==========02 Feb =============================================

    def test_SalesVerifyChangeColumnFunctionality_Orders_Bookmarks_C103(self, impersonate_sales):
        driver = impersonate_sales['webdriver']
        # Verify page load
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Verify Change column functionality in Orders/BookMarks page.
        # Click on order tab
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        driver.find_element_by_css_selector(".fa.fa-bookmark-o.fa-fw").click()      #Click on Bookmark

        #Verify Bookmarks page is displayed.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        actualtitle=driver.find_element_by_id("content-header").text
        expectedtitle= "Bookmarks"
        assert expectedtitle in actualtitle
        wait.until(EC.visibility_of_element_located((By.ID,'orders_table_previous')))

        driver.find_element_by_id("orders_table_wrapper").find_element_by_class_name("ColVis_MasterButton").click()
        time.sleep(1)
        actual=driver.find_element_by_class_name("ColVis_collection").text
        for tr in driver.find_elements_by_id('orders_table'):
            ths=tr.find_elements_by_tag_name('th')
            if ths:
                data= [th.text for th in ths]
        array = actual.split("\n")
        size=len(data)
        for i in range(size):
            assert data[i] in array

    # ==================================C96==========02 Feb =============================================

    def test_Sales_Verify_Sorting_functionality_in_Orders_Orders_Search_C96(self, impersonate_sales):
        driver = impersonate_sales['webdriver']
        # Verify page load
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Verify pagination functionality in Orders/Order search page.
        # Click on order tab
        driver.find_element_by_link_text("Orders").click()
        # Click on 'Order Search'.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Order Search')))
        driver.find_element_by_link_text("Order Search").click()
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID,'gen_search')))
        actualtitle=driver.find_element_by_id("content-header").text
        expectedtitle= "Order Search"
        assert expectedtitle in actualtitle
        #driver.find_element_by_id("toggle").click()
        driver.find_element_by_id("gen_search").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'col-id')))
        time.sleep(1)

        # Verify ascending and descending order for 'Id' column on 'Order Search' page.
        expected_Ascending_order="ascending"
        expected_Descending_order="descending"

        actual_order = driver.find_element_by_id("orders_table").find_element_by_class_name("col-id").get_attribute("aria-sort")
        print(actual_order)
        assert actual_order in expected_Ascending_order
        driver.find_element_by_class_name("col-id").click()
        time.sleep(1)
        actual_order=driver.find_element_by_class_name("col-id").get_attribute("aria-sort")
        assert actual_order in expected_Descending_order

        # Verify ascending and descending order for 'Client Name' column on 'Order Search' page.
        a=driver.find_elements_by_class_name("col-client-name")
        a[0].click()
        time.sleep(1)
        actual_order = driver.find_element_by_id("orders_table").find_element_by_class_name("col-client-name").get_attribute("aria-sort")
        assert  actual_order in expected_Ascending_order
        a=driver.find_element_by_class_name("col-client-name")
        a.click()
        time.sleep(1)
        actual_order=a.get_attribute("aria-sort")
        assert actual_order in expected_Descending_order

        # Verify ascending and descending order for 'Status' column on 'Order Search' page.
        a=driver.find_elements_by_class_name("col-status")
        a[0].click()
        time.sleep(1)
        actual_order = driver.find_element_by_id("orders_table").find_element_by_class_name("col-status").get_attribute("aria-sort")
        assert  actual_order in expected_Ascending_order
        a=driver.find_element_by_class_name("col-status")
        a.click()
        time.sleep(1)
        actual_order=a.get_attribute("aria-sort")
        assert actual_order in expected_Descending_order

        # Verify ascending and descending order for 'Date Submitted' column on 'Order Search' page.
        a=driver.find_elements_by_class_name("col-date-submitted")
        a[0].click()
        time.sleep(1)
        actual_order = driver.find_element_by_id("orders_table").find_element_by_class_name("col-date-submitted").get_attribute("aria-sort")
        assert  actual_order in expected_Ascending_order
        a=driver.find_element_by_class_name("col-date-submitted")
        a.click()
        time.sleep(1)
        actual_order=a.get_attribute("aria-sort")
        assert actual_order in expected_Descending_order

        # Verify ascending and descending order for 'Hands Date' column on 'Order Search' page.
        a=driver.find_elements_by_class_name("col-in-hands-date")
        a[0].click()
        time.sleep(1)
        actual_order = driver.find_element_by_id("orders_table").find_element_by_class_name("col-in-hands-date").get_attribute("aria-sort")
        assert  actual_order in expected_Ascending_order
        a=driver.find_element_by_class_name("col-in-hands-date")
        a.click()
        time.sleep(1)
        actual_order=a.get_attribute("aria-sort")
        assert actual_order in expected_Descending_order

        # Verify ascending and descending order for 'PO' column on 'Order Search' page.
        a=driver.find_elements_by_class_name("col-po")
        a[0].click()
        time.sleep(1)
        actual_order = driver.find_element_by_id("orders_table").find_element_by_class_name("col-po").get_attribute("aria-sort")
        assert  actual_order in expected_Ascending_order
        a=driver.find_element_by_class_name("col-po")
        a.click()
        time.sleep(1)
        actual_order=a.get_attribute("aria-sort")
        assert actual_order in expected_Descending_order

        # Verify ascending and descending order for 'Art Title' column on 'Order Search' page.
        a=driver.find_elements_by_class_name("col-art-title")
        a[0].click()
        time.sleep(1)
        actual_order = driver.find_element_by_id("orders_table").find_element_by_class_name("col-art-title").get_attribute("aria-sort")
        assert  actual_order in expected_Ascending_order
        a=driver.find_element_by_class_name("col-art-title")
        a.click()
        time.sleep(1)
        actual_order=a.get_attribute("aria-sort")
        assert actual_order in expected_Descending_order

        # Verify ascending and descending order for 'Ship to name' column on bookmarks page.
        a=driver.find_elements_by_class_name("col-shipto-name")
        a[0].click()
        time.sleep(1)
        actual_order = driver.find_element_by_id("orders_table").find_element_by_class_name("col-shipto-name").get_attribute("aria-sort")
        assert  actual_order in expected_Ascending_order
        a=driver.find_element_by_class_name("col-shipto-name")
        a.click()
        time.sleep(1)
        actual_order=a.get_attribute("aria-sort")
        assert actual_order in expected_Descending_order

        # Verify ascending and descending order for 'Type' column on 'Order Search' page.
        a=driver.find_elements_by_class_name("col-type")
        a[0].click()
        time.sleep(1)
        actual_order = driver.find_element_by_id("orders_table").find_element_by_class_name("col-type").get_attribute("aria-sort")
        assert  actual_order in expected_Ascending_order
        a=driver.find_element_by_class_name("col-type")
        a.click()
        time.sleep(1)
        actual_order=a.get_attribute("aria-sort")
        assert actual_order in expected_Descending_order

    # ===========================115======================================08 Feb========================================

    def test_SalesReportAccountReceivable_VerifyBlankFieldSubscriptionNotSubmitted_C115(self, impersonate_sales):
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)

        # Verify application not allowed to submit subscription with blank data fields.
        #Click on Reports tab.
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Personal')))
        driver.find_element_by_link_text("Personal").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Accounts Receivable')))
        driver.find_element_by_link_text("Accounts Receivable").click()

        # By default user is selected in the drop down.
        wait.until(EC.visibility_of_element_located((By.ID, 'selector')))
        actual_user_name = driver.find_element_by_id("selector").text
        expected_user_name = "Schulman, Anne"
        assert expected_user_name in actual_user_name

        #Click on make a subscription button.
        driver.find_element_by_id("subscription_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'modal-title')))

        # Click on submit button and Verify Subscription form remain displaying.
        wait.until(EC.visibility_of_element_located((By.ID,'next_btn')))
        driver.find_element_by_id("next_btn").click()
        assert driver.find_element_by_id("myModalLabel").is_displayed()
        # Note : Error message 'error message " Please fill out this field".' is not verified because id is not found.

    # ===========================121=================================08 feb=============================================

    def test_SalesReportOpenOrder_VerifyPaginationfunctionalityInGeneratedReport_C121(self, impersonate_sales):
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)

        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Personal')))
        driver.find_element_by_link_text("Personal").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Open Orders')))
        driver.find_element_by_link_text("Open Orders").click()

        # Heading displayed " Report: Open Orders".
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_open_order_header = driver.find_element_by_id("content-header").text
        expected_open_order_header = "Open Orders Report"
        assert expected_open_order_header in actual_open_order_header

        # Generate Report(button)
        wait.until(EC.visibility_of_element_located((By.ID, 'sub_btn')))
        driver.find_element_by_id("sub_btn").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'dataTable_previous')))

        # Verify by default previous button is displayed as disabled.
        expected_disable_previous = "disabled"
        actual_disable_previous = driver.find_element_by_id("dataTable_previous").get_attribute("class")
        assert expected_disable_previous in actual_disable_previous
        expected_current_page_color = "rgba(229, 65, 45, 1)"

        # Verify link '2' is displayed, if displayed then click and verify pagination functionality.
        if driver.find_element_by_link_text("2").is_displayed():
            next_Button = driver.find_element_by_id("dataTable_next").get_attribute("class")
            assert expected_disable_previous not in next_Button
            driver.find_element_by_link_text("2").click()
            time.sleep(1)
            actual_disable_previous = driver.find_element_by_id("dataTable_previous").get_attribute("class")
            assert expected_disable_previous not in actual_disable_previous
            actual_current_page_color = driver.find_element_by_link_text("2").value_of_css_property("background-color")
            assert expected_current_page_color in actual_current_page_color

        # Click on '1' link and verify the pagination functionality.
        driver.find_element_by_link_text("1").click()
        time.sleep(1)
        actual_current_page_color = driver.find_element_by_link_text("1").value_of_css_property("background-color")
        assert expected_current_page_color in actual_current_page_color

    # ===========================139=====================================08 feb=======================================

    def test_SalesReportSalesOrderByDollarValue_VerifyPaginationfunctionalityInGeneratedReport_C139(self, impersonate_sales):
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Navigates to the 'Sales Order By Dollar Value' page.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Personal')))
        driver.find_element_by_link_text("Personal").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Sales Order by Dollar Value')))
        driver.find_element_by_link_text("Sales Order by Dollar Value").click()

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

        # Click on Generate report button
        driver.find_element_by_id("sub_btn").click()
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(5)

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

    # ===========================148=====================================16 feb=======================================

    def test_SalesOrderByDollarValue_VerifyStartdate_Enddate_C148(self, impersonate_sales):
        # Verify Start date is not greater than End date in Reports/Sales Order by Dollar Value page
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Personal')))
        driver.find_element_by_link_text("Personal").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Sales Order by Dollar Value')))
        driver.find_element_by_link_text("Sales Order by Dollar Value").click()

        wait.until(EC.visibility_of_element_located((By.ID, 'form_criteria')))

        # Validate Start date higher than end date resets
        wait.until(EC.visibility_of_element_located((By.NAME,'daterange')))
        driver.find_element_by_name("daterange").click()
        time.sleep(1)

        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("02/24/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("02/23/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        time.sleep(1)
        sd = driver.find_element_by_name("daterangepicker_start").get_attribute("value")
        ed = driver.find_element_by_name("daterangepicker_end").get_attribute("value")
        # Verify both dates are set to equal automatically
        assert sd == ed
        time.sleep(1)
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()

    # ===========================135===================================16 feb=========================================

    def test_SalesOrderByDollarValue_VerifyreportSearch_C135(self, impersonate_sales):
        # Verify Search functionality in Reports/Sales Order by Dollar Value page.
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Personal')))
        driver.find_element_by_link_text("Personal").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Sales Order by Dollar Value')))
        driver.find_element_by_link_text("Sales Order by Dollar Value").click()
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.ID, 'form_criteria')))
        # Enter Start date higher than end date
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
        # Click on Generate Report button.
        driver.find_element_by_id("sub_btn").click()
        # Report should be generated successfully on the same page.
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(5)
        # enter Sales Rep code "AS" to search
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl00").send_keys("AS")
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

    # ==============================================================17 feb=========================================

    def test_salesuser_OrderSearch_AddRemove_bookmarks_C94(self, impersonate_sales):
        # Verify the bookmark functionality in search results section in Orders/Orders
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Verify Orders tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
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
            driver.find_element_by_class_name("sub-nav").find_element_by_link_text("Order Search").click()
            time.sleep(1)
            # Click on advance filter button
            # driver.find_element_by_id("toggle").click()
            # time.sleep(1)
            # Click on Search button
            wait.until(EC.visibility_of_element_located((By.ID,'gen_search')))
            driver.find_element_by_id("gen_search").click()
            # Filter same orderid
            driver.find_element_by_id("orders_table_filter").find_element_by_class_name("input-sm").send_keys(v_orderid)
            time.sleep(4)
            # Click on bookmark icon to remove bookmark
            driver.find_element_by_class_name('glyphicon-bookmark').click()
            time.sleep(4)
            # Open Bookmarks page and Search for orderid that no longer has bookmark
            driver.find_element_by_css_selector(".fa.fa-bookmark-o.fa-fw").click()
            time.sleep(1)
            # Search for Orderid in Bookmarks table class input-sm
            driver.find_element_by_id("orders_table_filter").find_element_by_class_name("input-sm").send_keys(v_orderid)
            time.sleep(4)
            # Check row count displayed orders_table_info  Showing 0 to 0 of 0 entries
            srch_text = driver.find_element_by_id('orders_table_info').text
            assert srch_text == 'Showing 0 to 0 of 0 entries'
            time.sleep(1)

    # ==============================95============================17 feb=========================================

    def test_sales_verify_Ordersearch_Pagefilters_C95(self, impersonate_sales):
        # Verify 'Showing 1 to 'xx' of 'xxx' entries functionality in search results section - Orders/Orders Search page
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Verify Orders tab visibility
        # Click on order tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        # Click on Order Search
        driver.find_element_by_class_name("sub-nav").find_element_by_link_text("Order Search").click()
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        time.sleep(1)
        # Click on Search button
        driver.find_element_by_id("gen_search").click()
        time.sleep(10)
        # Select 25 entries orders_table_length
        entry_sel = driver.find_element_by_id("orders_table_length")
        v_optsel = "25"
        for opt in entry_sel.find_elements_by_tag_name("option"):
            if opt.text == v_optsel:
                opt.click()
                break
        # Check row count displayed orders_table_info Showing 1 to xx of yy entries orders_table_info
        time.sleep(3)
        srch_text = driver.find_element_by_id('orders_table_info').text
        time.sleep(3)
        assert 'Showing 1 to 25' in srch_text

        # Select 10 entries orders_table_length
        entry_sel = driver.find_element_by_id("orders_table_length")
        v_optsel = "10"
        for opt in entry_sel.find_elements_by_tag_name("option"):
            if opt.text == v_optsel:
                opt.click()
                break
        # Check row count displayed orders_table_info  Showing 1 to xx of yy entries orders_table_info
        time.sleep(3)
        srch_text = driver.find_element_by_id('orders_table_info').text
        time.sleep(3)
        assert 'Showing 1 to 10' in srch_text

        # Select 50 entries orders_table_length
        entry_sel = driver.find_element_by_id("orders_table_length")
        v_optsel = "50"
        for opt in entry_sel.find_elements_by_tag_name("option"):
            if opt.text == v_optsel:
                opt.click()
                break
        # Check row count displayed orders_table_info  Showing 1 to xx of yy entries orders_table_info
        time.sleep(3)
        srch_text = driver.find_element_by_id('orders_table_info').text
        time.sleep(3)
        assert 'Showing 1 to 50' in srch_text
        time.sleep(1)

        # Select 100 entries orders_table_length
        entry_sel = driver.find_element_by_id("orders_table_length")
        v_optsel = "100"
        for opt in entry_sel.find_elements_by_tag_name("option"):
            if opt.text == v_optsel:
                opt.click()
                break
        # Check row count displayed orders_table_info  Showing 1 to xx of yy entries orders_table_info
        time.sleep(3)
        srch_text = driver.find_element_by_id('orders_table_info').text
        time.sleep(3)
        assert 'Showing 1 to 100' in srch_text
        time.sleep(1)

    # ==============================================================17 feb=========================================

    def test_salesuser_verify_orders_bookmark_filters_C104(self, impersonate_sales):
        # Verify the filter functionality in Orders/Bookmarks Page.
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Wait for Orders link to show up
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
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
        assert driver.find_element_by_class_name("input-sm").is_displayed()
        # Verify valid entry and search for same    glyphicon glyphicon-bookmark pull-left bookmarked
        # Check valid bookmark id glyphicon-bookmark , check Previous button displayed to ensure records exist
        if len(driver.find_element_by_id('orders_table').find_elements_by_tag_name('tr')) > 1:
            v_orderid = driver.find_element_by_class_name('glyphicon-bookmark').get_attribute('data-order-id')
            driver.find_element_by_id("orders_table_filter").find_element_by_class_name("input-sm").send_keys(v_orderid)
            time.sleep(4)
            v_clsname  = driver.find_element_by_class_name('glyphicon-bookmark').get_attribute('class')
            if v_clsname == 'glyphicon glyphicon-bookmark pull-left bookmarked':
                # goto bookmark
                bm_flag = 1
            else:
                #Click on bookmark for record if already not bookmarked
                driver.find_element_by_class_name('glyphicon-bookmark').click()
                time.sleep(1)

            # Refresh Bookmark page and search for bookmarked order
            driver.find_element_by_css_selector(".fa.fa-bookmark-o.fa-fw").click()
            time.sleep(1)
            # Search for Orderid in Bookmarks table class input-sm
            driver.find_element_by_id("orders_table_filter").find_element_by_class_name("input-sm").send_keys(v_orderid)
            time.sleep(4)
            # Check row count displayed orders_table_info  Showing 1 to 1 of 1 entries
            rc_text = driver.find_element_by_id('orders_table_info').text
            assert rc_text == 'Showing 1 to 1 of 1 entries'
            time.sleep(1)
            # Bookmark
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


    # ==============================================================17 feb=========================================

    def test_salesuser_verify_orders_bookmark_functionality_C105(self, impersonate_sales):
        # Verify the bookmark functionality in Orders/Bookmarks Page.
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Wait for Orders link to show up
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Orders')))
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        # Bookmark Link
        driver.find_element_by_css_selector(".fa.fa-bookmark-o.fa-fw").click()
        time.sleep(1)

        # Verify Bookmarks page is displayed.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        time.sleep(1)
        actualtitle = driver.find_element_by_id("content-header").text
        expectedtitle = "Bookmarks"
        assert expectedtitle in actualtitle
        time.sleep(1)

        # Verify error message from orders table if no Bookmark
        wait.until(EC.visibility_of_element_located((By.ID,'panel_body')))
        ord_tab_content = driver.find_element_by_id("panel_body").text
        no_data_message = "No Orders Bookmarked"
        if no_data_message in ord_tab_content:
            flag = 2
        else:
            # data exists
            flag = 1
        # Go to Page 1 if bookmarks exist
        if int(flag) == 1:
            # Count Bookmark
            bc = len(driver.find_element_by_id('orders_table').find_elements_by_tag_name("tr"))
            # Fetch Order Id dynamically for Valid search criteria
            v_orderid = driver.find_element_by_class_name('glyphicon-bookmark').get_attribute('data-order-id')
            # filter order id
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
            time.sleep(4)

            # Verify error message from orders table if no Bookmark
            wait.until(EC.visibility_of_element_located((By.ID,'content-container')))
            ord_tab_content = driver.find_element_by_id("content-container").text
            no_data_message = "No Orders Bookmarked"

            if no_data_message in ord_tab_content:
                flag = 2
                bk_count=0
            else:
                # data rows exist
                flag = 1

            # Go to Bookmarks page if bookmarks exist and confirm  removed bookmark order
            if int(flag) == 1:
                driver.find_element_by_id("orders_table_filter").find_element_by_class_name("input-sm").send_keys(v_orderid)
                time.sleep(4)
                # Check row count displayed orders_table_info  Showing 0 to 0 of 0 entries
                rc_text = driver.find_element_by_id('orders_table_info').text
                time.sleep(1)
                assert 'Showing 0 to 0 of 0 entries' in rc_text
                time.sleep(1)


            # Click on Order Search link to view all orders
            driver.find_element_by_class_name("sub-nav").find_element_by_link_text("Order Search").click()
            time.sleep(1)
            # Click on Search button
            wait.until(EC.visibility_of_element_located((By.ID,'gen_search')))
            driver.find_element_by_id("gen_search").click()

            # Wait orders_table_info
            wait.until(EC.visibility_of_element_located((By.ID,'orders_table_info')))
            time.sleep(1)
            if driver.find_element_by_link_text('1').is_displayed():
                if '-' in v_orderid:
                    v_orderidnew = v_orderid.split("-")
                    v_orderid = v_orderidnew[0]
                driver.find_element_by_id("orders_table_filter").find_element_by_class_name("input-sm").send_keys(v_orderid)
                time.sleep(8)
                # Bookmark the record
                driver.find_element_by_class_name('glyphicon-bookmark').click()
                time.sleep(4)
                driver.refresh()
                # Check bookmarks badges count
                badge_pagesnew = driver.find_element_by_class_name('badge').text
                time.sleep(1)
                # Check prev and new bookmark values
                assert bc != badge_pagesnew

    # ==============================================================17 feb=========================================

    def test_salesuser_verify_orders_bookmark_countchange_C109(self, impersonate_sales):
        # Verify the count of bookmarks in Orders/Bookmarks Page..
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Wait for Orders link to show up
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
        # Get bookmark count
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
        # Check if Page 1 is visible to see bookmarks exist
        if int(flag) == 1:
            badge_pages_prev = driver.find_element_by_class_name('badge').text
            time.sleep(1)
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
            # Check bookmarks badges count if bookmarks exist
            # Verify error message from orders table if no Bookmark
            wait.until(EC.visibility_of_element_located((By.ID,'panel_body')))
            ord_tab_content = driver.find_element_by_id("panel_body").text
            no_data_message = "No Orders Bookmarked"
            if no_data_message in ord_tab_content:
                flag = 2
            else:
                # data exists
                badge_pagesnew = driver.find_element_by_class_name('badge').text
                time.sleep(1)
                # Check prev and new bookmark values
                assert badge_pages_prev != badge_pagesnew

    # ===========================================142===================18 feb=========================================

    def test_salesuser_verify_supplier_diversity_pagecontent_C142(self, impersonate_sales):
        # Verify the contents on Supplier Diversity page.
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Personal')))
        driver.find_element_by_link_text("Personal").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Supplier Diversity')))
        driver.find_element_by_link_text("Supplier Diversity").click()
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actualtitle = driver.find_element_by_id("content-header").text
        expectedtitle = "Supplier Diversity Report"
        assert expectedtitle in actualtitle

        # Make a Subscription button.
        assert driver.find_element_by_class_name("btn-primary").is_displayed()
        # Criteria Label
        vc = driver.find_element_by_id("criteria").text
        assert "Report: Supplier Diversity" in vc
        #Custno Dropdown
        time.sleep(1)
        assert driver.find_element_by_id("custno").is_displayed()
        #PoStartDate  PoEndDate
        assert driver.find_element_by_name("daterange").is_displayed()

        # Generate Report(button) visibility
        assert driver.find_element_by_id("sub_btn").is_displayed()

    # ============================783===========================19 feb=========================================

    def test_salesuser_verify_OrderDetails_Pagecontent_C783(self, impersonate_sales):
        # My open orders/Order Id - Verify the contents on order id page.
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Orders tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Orders')))
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        driver.find_element_by_link_text("My Open Orders").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))

        # Click Order Id
        v_orderidfull = driver.find_element_by_id("order-table").find_element_by_class_name("odd").text
        print(v_orderidfull)
        # Split order id based on -
        v_orderidsp1 = v_orderidfull.split(" ")
        v_orderidsp2 = str(v_orderidsp1[0])
        v_orderidsp3 = v_orderidsp2.split("-")
        v_orderid = v_orderidsp3[1]
        # Click on first Order Id
        driver.find_element_by_link_text(v_orderidsp2).click()
        time.sleep(3)
        # Verify Order Id page header
        actualTitle = driver.find_element_by_id("content-header").text
        assert v_orderidsp2 in actualTitle
        time.sleep(1)
        # Verify Elements on Order Details Page
        assert driver.find_element_by_id('bookmark').is_displayed()
        assert driver.find_element_by_link_text('Details').is_displayed()
        assert driver.find_element_by_link_text('Decoration').is_displayed()
        assert driver.find_element_by_partial_link_text('Deposits').is_displayed()
        assert driver.find_element_by_partial_link_text('Purchase Orders').is_displayed()
        assert driver.find_element_by_partial_link_text('Shipments').is_displayed()
        assert driver.find_element_by_partial_link_text('Invoices').is_displayed()
        assert driver.find_element_by_partial_link_text('Order History').is_displayed()
        assert driver.find_element_by_class_name('btn-info').is_displayed()
        assert driver.find_element_by_class_name('btn-success').is_displayed()
        assert driver.find_element_by_id('wrap_text_area').is_displayed()


    # ============================106=======================19 feb=========================================

    def test_salesuser_verify_Orders_bookmark_Pagefilters_C106(self, impersonate_sales):
        # Verify 'Showing 1 to 'xx'of 'xxx' entries functionality in Orders/Bookmarks Page.
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        #Verify the count of bookmarks in Orders/Bookmarks Page.
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
        # Get bookmark count
        # Verify error message from orders table if no Bookmark
        wait.until(EC.visibility_of_element_located((By.ID,'panel_body')))
        ord_tab_content = driver.find_element_by_id("panel_body").text
        no_data_message = "No Orders Bookmarked"
        if no_data_message in ord_tab_content:
            flag = 2
            badge_pages = 0
        else:
            # data exists
            flag = 1
            badge_pages = driver.find_element_by_class_name('badge').text

        # Check if Page 1 is visible to see bookmarks exist
        if int(badge_pages) >= 10:
            # Verify  Bookmarks dropdowns 10,25,50,100
            if int(badge_pages) >= 100:
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
            if int(badge_pages) >= 50:
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
            if int(badge_pages) >= 25:
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
            if int(badge_pages) >= 10:
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

    # ============================133================================19 feb=========================================

    def test_salesuser_verify_modify_subscription_C133(self, impersonate_sales):
        # To verify the save subscription functionality in modify Subscription for: Personal AR Report pop up.
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Subscriptions')))
        driver.find_element_by_link_text("Subscriptions").click()
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actualtitle = driver.find_element_by_id("content-header").text
        expectedtitle = "Subscriptions"
        assert expectedtitle in actualtitle

        # Check Records exist i.e. Modify link exists
        if driver.find_element_by_link_text('Modify').is_displayed():
            driver.find_element_by_link_text('Modify').click()
            # Proceed with modification and save
            wait.until(EC.visibility_of_element_located((By.ID, 'myModalLabel')))
            time.sleep(1)
            # Modify Name
            wait.until(EC.visibility_of_element_located((By.ID, 'sub_name')))
            driver.find_element_by_id('sub_name').clear()
            driver.find_element_by_id('sub_name').send_keys('TestSub12345')
            # Save Subscription
            driver.find_element_by_id('next_btn').click()
            time.sleep(4)
            driver.find_element_by_link_text("Subscriptions").click()
            time.sleep(1)

            # Verify saved Name content-container
            cnt = driver.find_element_by_id('content-container').text
            time.sleep(1)
            # check new subscription name is displayed in table
            assert 'TestSub12345' in cnt
            time.sleep(1)

    #==============================================81===========================================================

    def test_SalesProfileVerifyRemoveUserFunctionality_C81(self, impersonate_sales):
        # Verify sales impersonation
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Orders')))
    #==============================================83===========================================================

    def test_SalesProfileVerifyPagenation_C83(self, impersonate_sales):
        #Verify the contents in Orders/My Open Orders.
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Orders')))
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        driver.find_element_by_link_text("My Open Orders").click()
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'input-sm')))
        time.sleep(1)
        # Select 10 entries
        user_dropdown = driver.find_element_by_class_name('input-sm')
        option_text="10"
        for option in user_dropdown.find_elements_by_tag_name('option'):
            if option.text == option_text:
                option.click()
                break
        driver.implicitly_wait(10)
        actual_message=driver.find_element_by_id('order-table_info').text
        open_orders=driver.find_elements_by_xpath("//tbody/tr")
        number_of_open_orders=len(open_orders)
        expected_message="Showing 1 to "+number_of_open_orders.__str__()
        assert expected_message in actual_message
        # Select 25 entries
        user_dropdown=driver.find_element_by_class_name('input-sm')
        option_text="25"
        for option in user_dropdown.find_elements_by_tag_name('option'):
            if option.text == option_text:
                option.click()
                break
        driver.implicitly_wait(10)
        actual_message=driver.find_element_by_id('order-table_info').text
        open_orders=driver.find_elements_by_xpath("//tbody/tr")
        number_of_open_orders=len(open_orders)
        expected_message="Showing 1 to "+number_of_open_orders.__str__()
        assert expected_message in actual_message

        # Select 50 entries
        user_dropdown=driver.find_element_by_class_name('input-sm')
        option_text="50"
        for option in user_dropdown.find_elements_by_tag_name('option'):
            if option.text == option_text:
                option.click()
                break
        driver.implicitly_wait(10)
        actual_message=driver.find_element_by_id('order-table_info').text
        open_orders=driver.find_elements_by_xpath("//tbody/tr")
        number_of_open_orders=len(open_orders)
        expected_message="Showing 1 to " + number_of_open_orders.__str__()
        assert expected_message in actual_message

        # Select 100 entries
        user_dropdown=driver.find_element_by_class_name('input-sm')
        option_text="100"
        for option in user_dropdown.find_elements_by_tag_name('option'):
            if option.text == option_text:
                option.click()
                break
        driver.implicitly_wait(10)
        actual_message=driver.find_element_by_id('order-table_info').text
        open_orders=driver.find_elements_by_xpath("//tbody/tr")
        number_of_open_orders=len(open_orders)
        expected_message="Showing 1 to "+number_of_open_orders.__str__()
        assert expected_message in actual_message

    # ============================144===========================22 feb=========================================

    def test_salesuser_verify_GenerateReport_supplierDiversity_C144(self, impersonate_sales):
        #  Reports/Supplier Diversity - Verify the generate report functionality on Reports/Supplier Diversity page.
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        time.sleep(1)
        # Click on Personal tab.
        operations = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Personal')))
        operations.click()
        time.sleep(1)
        # Click on Supplier Diversity tab.
        supplier_diversity = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Supplier Diversity')))
        supplier_diversity.click()
        time.sleep(1)
        # Verify the contents on reports / Personal / Supplier Diversity page.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'panel-heading')))
        expected_header = "Report: Supplier Diversity"
        actual_header = driver.find_element_by_class_name("panel-heading").text
        assert expected_header in actual_header
        # Drop down with multiple clients
        expected_clients = "select"
        actual_clients = driver.find_element_by_id("custno").tag_name
        assert expected_clients in actual_clients
        # Generate Report button
        assert driver.find_element_by_id("sub_btn").is_displayed()
        # Make a Subscription button
        assert driver.find_element_by_class_name("btn-primary").is_displayed()
        # PO Start
        assert driver.find_element_by_name("daterange").is_displayed()

        # Select dropdown value
        mySelect = Select(driver.find_element_by_id("custno"))
        mySelect.select_by_index(4)
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
        mySelect = Select(driver.find_element_by_id("custno"))
        mySelect.select_by_index(3)
        #Generate report
        driver.find_element_by_class_name('btn-success').click()
        # Switch to Report Frame
        driver.switch_to_frame("report_src")
        time.sleep(1)
        # ReportViewerControl_fixedTable  ReportViewerForm
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerForm')))
        time.sleep(5)

    # ============================796===========================22 feb=========================================

    def test_salesuser_verify_icontooltips_orderdetailspage_C796(self, impersonate_sales):
        # My open orders/Order Id - Verify the tooltip text in details page in order id page.
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Orders tab.
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        driver.find_element_by_link_text("My Open Orders").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))

        # Click Order Id
        v_orderidfull = driver.find_element_by_id("order-table").find_element_by_class_name("odd").text
        # Split order id based on
        v_orderidsp1 = v_orderidfull.split(" ")
        v_orderidsp2 = str(v_orderidsp1[0])

        # Click on first Order Id
        driver.find_element_by_link_text(v_orderidsp2).click()
        time.sleep(3)
        # Verify Order Id page header
        actualTitle = driver.find_element_by_id("content-header").text
        assert v_orderidsp2 in actualTitle
        time.sleep(1)
        # Verify Element on Order Details Page
        assert driver.find_element_by_id('bookmark').is_displayed()
        # Verify all action icons exist
        # icon_forms_submitted,icon_po_issued, icon_po_received, icon_shipped,icon_invoice_generated,icon_invoice_paid
        assert driver.find_element_by_id('icon_forms_submitted').is_displayed()
        assert driver.find_element_by_id('icon_po_issued').is_displayed()
        assert driver.find_element_by_id('icon_po_received').is_displayed()
        assert driver.find_element_by_id('icon_shipped').is_displayed()
        assert driver.find_element_by_id('icon_invoice_generated').is_displayed()
        assert driver.find_element_by_id('icon_invoice_paid').is_displayed()

        # Move to icon forms_submitted
        element = driver.find_element_by_id('icon_forms_submitted')
        hov = ActionChains(driver).move_to_element(element)
        hov.perform()
        time.sleep(1)
        hovertext = driver.find_element_by_class_name('flag-popover').get_attribute("aria-describedby")
        assert hovertext != ""

        # Move to icon po_issued
        element = driver.find_element_by_id('icon_po_issued')
        hov = ActionChains(driver).move_to_element(element)
        hov.perform()
        time.sleep(1)
        hovertext = driver.find_element_by_class_name('flag-popover').get_attribute("aria-describedby")
        assert hovertext != ""

        # Move to icon po_received
        element = driver.find_element_by_id('icon_po_received')
        hov = ActionChains(driver).move_to_element(element)
        hov.perform()
        time.sleep(1)
        hovertext = driver.find_element_by_class_name('flag-popover').get_attribute("aria-describedby")
        assert hovertext != ""

        # Move to icon shipped   icon_shipped,,icon_invoice_paid
        element = driver.find_element_by_id('icon_shipped')
        hov = ActionChains(driver).move_to_element(element)
        hov.perform()
        time.sleep(1)
        hovertext = driver.find_element_by_class_name('flag-popover').get_attribute("aria-describedby")
        assert hovertext != ""

        # Move to icon invoice_generated
        element = driver.find_element_by_id('icon_invoice_generated')
        hov = ActionChains(driver).move_to_element(element)
        hov.perform()
        time.sleep(1)
        hovertext = driver.find_element_by_class_name('flag-popover').get_attribute("aria-describedby")
        assert hovertext != ""

        # Move to icon invoice_paid
        element = driver.find_element_by_id('icon_invoice_paid')
        hov = ActionChains(driver).move_to_element(element)
        hov.perform()
        time.sleep(1)
        hovertext = driver.find_element_by_class_name('flag-popover').get_attribute("aria-describedby")
        assert hovertext != ""

    # ============================794===========================22 feb=========================================

    def test_salesuser_verify_Orderhistory_orderdetailspage_C794(self, impersonate_sales):
        # My open orders/Order Id - Verify the contents on Order History page in Order details page.
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Orders tab.
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        driver.find_element_by_link_text("My Open Orders").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))

        # Get Order id and Click Order Id
        v_orderidfull = driver.find_element_by_id("order-table").find_element_by_class_name("odd").text
        # Split order id based on
        v_orderidsp1 = v_orderidfull.split(" ")
        v_orderidsp2 = str(v_orderidsp1[0])

        # Click on first Order Id
        driver.find_element_by_link_text(v_orderidsp2).click()
        time.sleep(3)
        # Verify Order Id page header
        actualTitle = driver.find_element_by_id("content-header").text
        assert v_orderidsp2 in actualTitle
        time.sleep(1)
        # Verify Element on Order Details Page
        assert driver.find_element_by_id('bookmark').is_displayed()

        # Click Order History tab
        driver.find_element_by_partial_link_text('Order History').click()
        time.sleep(1)
        clsdet = driver.find_element_by_id("history").text
        # Verify Contents
        assert 'Date' in clsdet
        assert 'Order History Details' in clsdet
        assert 'User' in clsdet
        assert 'Action' in clsdet
        assert 'Details' in clsdet

    # ============================795===========================22 feb=========================================

    def test_salesuser_verify_Orderdetails_bookmark_C795(self, impersonate_sales):
        # My open orders/Order Id - Verify the bookmark functionality in order id page.
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Orders tab.
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        driver.find_element_by_link_text("My Open Orders").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))

        # Click Order Id
        v_orderidfull = driver.find_element_by_id("order-table").find_element_by_class_name("odd").text
        print(v_orderidfull)
        # Split order id based on space
        v_orderidsp1 = v_orderidfull.split(" ")
        v_orderidsp2 = str(v_orderidsp1[0])
        v_orderidsp3 = v_orderidsp2.split("-")
        v_orderid = v_orderidsp3[1]

        # Click on first Order Id
        driver.find_element_by_link_text(v_orderidsp2).click()
        time.sleep(3)
        # Verify Order Id page header
        actualTitle = driver.find_element_by_id("content-header").text
        assert v_orderidsp2 in actualTitle
        time.sleep(1)
        # Verify Element on Order Details Page
        assert driver.find_element_by_id('bookmark').is_displayed()

        # Check order is not bookmarked
        cls = driver.find_element_by_id('bookmark').get_attribute("class")
        if cls == 'btn btn-default':
            driver.find_element_by_id('bookmark').click()
        # Open Book marks section from Orders
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        driver.find_element_by_link_text("Orders").click()
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

    # ============================784===========================24 feb=========================================

    def test_salesuser_verify_OrderDetails_tabcontent_C784(self, impersonate_sales):
        # My Open Orders/Order Id - Verify the contents on details Tab in order details page.
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Orders tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Orders')))
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        driver.find_element_by_link_text("My Open Orders").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))

        # Get Order Id dynamically
        v_orderidfull = driver.find_element_by_id("order-table").find_element_by_class_name("odd").text
        # Split order id based on -
        v_orderidsp1 = v_orderidfull.split(" ")
        v_orderidsp2 = str(v_orderidsp1[0])
        v_orderidsp3 = v_orderidsp2.split("-")
        v_orderid = v_orderidsp3[1]
        # Click on first Order Id
        driver.find_element_by_link_text(v_orderidsp2).click()
        time.sleep(3)
        # Verify Order Id page header
        actualTitle = driver.find_element_by_id("content-header").text
        assert v_orderidsp2 in actualTitle
        time.sleep(1)
        # Verify Elements on Order Details Page
        assert driver.find_element_by_id('bookmark').is_displayed()
        assert driver.find_element_by_link_text('Details').is_displayed()

        # Verify content for Order Details tab
        cnt_text = driver.find_element_by_id('details').text
        time.sleep(1)
        assert "Order Information" in cnt_text
        assert "Client PO:" in cnt_text
        assert "Status" in cnt_text
        assert "Submitted" in cnt_text
        assert "Order Type:" in cnt_text
        assert "Date Placed:" in cnt_text
        assert "Planned Production Date:" in cnt_text
        assert "Ship by Date:" in cnt_text
        assert "In-Hands Date:" in cnt_text
        assert "Payment Terms:" in cnt_text
        assert "Order Information" in cnt_text
        assert "Sales Rep:" in cnt_text

        assert "Address Information" in cnt_text
        assert "Bill to:" in cnt_text
        assert "US" in cnt_text
        assert "Ship to:" in cnt_text
        assert "Items in Order" in cnt_text
        assert "Item SKU #1" in cnt_text
        assert "Item SKU #2" in cnt_text
        assert "Description" in cnt_text
        assert "Quantity" in cnt_text
        assert "Weight" in cnt_text
        assert "Price/Unit" in cnt_text
        assert "Discount" in cnt_text
        assert "Workflow Status" in cnt_text

        # Check Item Table displayed
        assert driver.find_element_by_class_name('table-hover').is_displayed()
        # Check table row count > 0
        tr = driver.find_element_by_class_name('table-hover').find_elements_by_tag_name('tr')
        trc = len(tr)
        assert int(trc) >= 1

    # ============================792===========================24 feb=========================================

    def test_salesuser_verify_OrderDetails_PurchaseOrderstabcontent_C792(self, impersonate_sales):
        # My open orders/Order Id - Verify the contents on Purchase Orders page in order id page.
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Orders tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Orders')))
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        driver.find_element_by_link_text("My Open Orders").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))

        # Get Order Id dynamically
        v_orderidfull = driver.find_element_by_id("order-table").find_element_by_class_name("odd").text
        # Split order id based on -
        v_orderidsp1 = v_orderidfull.split(" ")
        v_orderidsp2 = str(v_orderidsp1[0])
        v_orderidsp3 = v_orderidsp2.split("-")
        v_orderid = v_orderidsp3[1]
        # Click on first Order Id
        driver.find_element_by_link_text(v_orderidsp2).click()
        time.sleep(3)
        # Verify Order Id page header
        actualTitle = driver.find_element_by_id("content-header").text
        assert v_orderidsp2 in actualTitle
        time.sleep(1)
        # Verify Elements on Order Details Page
        assert driver.find_element_by_id('bookmark').is_displayed()
        assert driver.find_element_by_link_text('Details').is_displayed()

        #nav_elements = driver.find_elements_by_class_name('nav-tabs')
        time.sleep(1)
        driver.find_element_by_partial_link_text('Purchase Orders').click()
        wait.until(EC.visibility_of_element_located((By.ID, 'purchases')))
        # Verify content
        cnt_text = driver.find_element_by_id('purchases').text
        time.sleep(1)

        # If purchase order exists
        if cnt_text.find("Purchase Order 1"):
            assert "Purchase Order 1" in cnt_text
            assert "Special Instructions" in cnt_text
            assert "Click Edit to Update" in cnt_text
            assert "Save" in cnt_text
            assert "Edit" in cnt_text
            assert "Status:" in cnt_text
            assert "Vendor:" in cnt_text
            assert "Create Date:" in cnt_text
            assert "Ship Method:" in cnt_text
            assert "Payment Terms:" in cnt_text
            assert "Items for this Purchase Order" in cnt_text
            assert "SKU" in cnt_text

            assert "Description" in cnt_text
            assert "Qty Ordered" in cnt_text
            assert "Qty Received" in cnt_text
            assert "Cost" in cnt_text
            assert "Notes" in cnt_text

            # Check Items for Purchase Order displayed in Table
            assert driver.find_element_by_class_name('table-hover').is_displayed()
            # Check table row count > 0
            tr = driver.find_element_by_class_name('table-hover').find_elements_by_tag_name('tr')
            trc = len(tr)
            assert int(trc) >= 1

    # ============================791===========================24 feb=========================================

    def test_salesuser_verify_OrderDetails_invoicetabcontent_C791(self, impersonate_sales):
        # My open orders/Order Id - Verify the contents on invoices page in order id page.
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Orders tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Orders')))
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        driver.find_element_by_link_text("My Open Orders").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        # Select 100 entries from dropdown
        option_text = "100"
        user_dropdown = driver.find_element_by_id("order-table_length").find_element_by_class_name("input-sm")
        for option in user_dropdown.find_elements_by_tag_name('option'):
            if option.text == option_text:
                option.click()
                break
        time.sleep(1)
        # Get Order Id dynamically
        v_orderidfull = driver.find_element_by_id("order-table").find_element_by_class_name("odd").text
        # Split order id based on space
        v_orderidsp1 = v_orderidfull.split(" ")
        v_orderidsp2 = str(v_orderidsp1[0])

        # Click on first Order Id
        driver.find_element_by_link_text(v_orderidsp2).click()
        time.sleep(3)
        # Verify Order Id page header
        actualTitle = driver.find_element_by_id("content-header").text
        assert v_orderidsp2 in actualTitle
        time.sleep(1)
        # Verify Elements on Order Details Page
        assert driver.find_element_by_id('bookmark').is_displayed()
        assert driver.find_element_by_link_text('Details').is_displayed()

        time.sleep(1)
        driver.find_element_by_partial_link_text('Invoices').click()
        wait.until(EC.visibility_of_element_located((By.ID, 'invoices')))
        # Verify content
        cnt_text = driver.find_element_by_id('invoices').text
        time.sleep(1)
        # If Invoice exists
        if not cnt_text.find("No invoices found.") == 0:
            assert "Date:" in cnt_text
            assert "Items in this Invoice" in cnt_text
            assert "SKU" in cnt_text
            assert "Description" in cnt_text
            assert "Qty Ordered" in cnt_text
            assert "Price" in cnt_text

            assert "Sales Representative: " in cnt_text
            assert "Payment Terms:" in cnt_text
            assert "Tax Rate:" in cnt_text
            assert "Total Amount:" in cnt_text
            assert "Amount Paid:" in cnt_text
            assert "Balance:" in cnt_text
            assert "Paid Date:" in cnt_text

            # Check Items for Purchase Order displayed in Table
            assert driver.find_element_by_class_name('table-hover').is_displayed()
            # Check table row count > 0
            tr = driver.find_element_by_class_name('table-hover').find_elements_by_tag_name('tr')
            trc = len(tr)
            assert int(trc) >= 1
        else:
            print("No Invoice Exist for this order")

    # ============================802===========================24 feb=========================================

    def test_salesuser_verify_OrderDetails_Decorationtabcontent_C802(self, impersonate_sales):
        # My open orders/Order Id - Verify the contents on decoration page in order id page.
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Orders tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Orders')))
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        driver.find_element_by_link_text("My Open Orders").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        # Select 100 entries
        option_text = "100"
        user_dropdown = driver.find_element_by_id("order-table_length").find_element_by_class_name("input-sm")
        for option in user_dropdown.find_elements_by_tag_name('option'):
            if option.text == option_text:
                option.click()
                break
        time.sleep(1)
        # Get Order Id dynamically
        v_orderidfull = driver.find_element_by_id("order-table").find_element_by_class_name("odd").text
        # Split order id based on space
        v_orderidsp1 = v_orderidfull.split(" ")
        v_orderidsp2 = str(v_orderidsp1[0])

        # Click on first Order Id
        driver.find_element_by_link_text(v_orderidsp2).click()
        time.sleep(3)
        # Verify Order Id page header
        actualTitle = driver.find_element_by_id("content-header").text
        assert v_orderidsp2 in actualTitle
        time.sleep(1)
        # Verify Elements on Order Details Page
        assert driver.find_element_by_id('bookmark').is_displayed()
        assert driver.find_element_by_link_text('Details').is_displayed()

        time.sleep(1)
        driver.find_element_by_partial_link_text('Decoration').click()
        wait.until(EC.visibility_of_element_located((By.ID, 'decoration')))
        # Verify content
        cnt_text = driver.find_element_by_id('decoration').text
        time.sleep(1)
        # If decoration content exists
        if cnt_text.find("Artwork Information") == 0:
            print("Hello")
            assert "Art ID: " in cnt_text
            assert "Artwork Title:" in cnt_text
            assert "Art Hours:" in cnt_text
            assert "Artist:" in cnt_text
            assert "Screens:" in cnt_text
            assert "Artwork Preview" in cnt_text
            #Some elements are not visible currently , so assertion not applied to all elements
        else:
            print("No Decoration Content exists for this order")

    # ==============================1437===============================26 feb====================================
    def test_Salesuser_VerifyGeneratedReportedFunctionality_C1437(self, impersonate_sales):
        driver = impersonate_sales['webdriver']
        # Verify generated report functionality on 'Supplier Diversity' page.
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        time.sleep(1)
        # Click on Personal tab.
        personal = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Personal')))
        personal.click()
        time.sleep(1)
        # Click on Supplier Diversity tab.
        supplier_diversity = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Supplier Diversity')))
        supplier_diversity.click()
        time.sleep(1)
        # Select the client from the drop down
        # Selecting by Xpath for partial text
        driver.find_element_by_id('custno').find_element_by_xpath("//option[contains(text(),'ACVS')]").click()
        # Select the ship Start date  and ship end date
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
        # Click on Generate report button.
        driver.find_element_by_class_name("btn-success").click()
        # Switch to report
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(3)
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_displayed()
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()
    
    # ============================3March==============793=================================================

    def test_salesuser_verify_OrderDetails_depositstabcontent_C793(self, impersonate_sales):
        # My open orders/Order Id - Verify the contents on Deposits page in order id page.
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Orders tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Orders')))
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        driver.find_element_by_link_text("My Open Orders").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        # Select 100 entries from dropdown
        option_text = "100"
        user_dropdown = driver.find_element_by_id("order-table_length").find_element_by_class_name("input-sm")
        for option in user_dropdown.find_elements_by_tag_name('option'):
            if option.text == option_text:
                option.click()
                break
        time.sleep(1)
        # Get Order Id dynamically
        v_orderidfull = driver.find_element_by_id("order-table").find_element_by_class_name("odd").text
        # Split order id based on space
        v_orderidsp1 = v_orderidfull.split(" ")
        v_orderidsp2 = str(v_orderidsp1[0])

        # Click on first Order Id
        driver.find_element_by_link_text(v_orderidsp2).click()
        time.sleep(3)
        # Verify Order Id page header
        actualTitle = driver.find_element_by_id("content-header").text
        assert v_orderidsp2 in actualTitle
        time.sleep(1)
        # Verify Elements on Order Details Page
        assert driver.find_element_by_id('bookmark').is_displayed()
        assert driver.find_element_by_link_text('Details').is_displayed()

        time.sleep(1)
        driver.find_element_by_partial_link_text('Deposits').click()
        wait.until(EC.visibility_of_element_located((By.ID, 'deposits')))
        # Verify content
        cnt_text = driver.find_element_by_id('deposits').text
        time.sleep(1)
        # If Deposits exists
        if not cnt_text.find("No deposits found.") == 0:
            assert "Date:" in cnt_text
            assert "Invoice" in cnt_text
            assert "Sales Representative:" in cnt_text
            assert "Payment Terms:" in cnt_text
            assert "Tax Rate:" in cnt_text
            assert "Total Amount:" in cnt_text
            assert "Amount Paid:" in cnt_text
            assert "Balance:" in cnt_text
        else:
            print("No Deposits Exist for this order")

    # ==========================77============================4March=================================================

    def test_salesuser_dashboard_chartContent_C77(self, impersonate_sales):
        # Dashboard - Verify the chart data in User profile Dashboard page for Open Orders, Invoiced Sales, Paid Sales.
        driver = impersonate_sales['webdriver']
        # Verify page load
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text('Dashboard').click()
        time.sleep(5)
        # These are the 5 widgets that are expected on page
        expected_widgets = [
            'Open Orders',
            'Paid Sales for the Past 12 Months',
            'Invoiced Sales for the Past 12 Months',
            'Top 5 Clients by Invoiced Sales ',
            'Invoiced Sales Table']
        # First, collect all the widgets on the page
        widgets = driver.find_elements_by_class_name('widget')
        # Verify actual vs. expected widget count
        assert len(expected_widgets) == len(widgets)
        # Verify Widgets Display
        src = driver.page_source
        text_found1 = re.search(r'Open Orders', src)
        text_found2 = re.search(r'Paid Sales for the Past 12 Months', src)
        text_found3 = re.search(r'Invoiced Sales for the Past 12 Months', src)
        # Verify Dashboard chart Hover text
        # Hover to Open Orders, Invoiced Sales, Paid Sales Widget 'dash-size'
        hv_class_size = len(driver.find_elements_by_class_name('dash-size'))
        hv_classes = driver.find_elements_by_class_name('dash-size')
        for j in range(1, hv_class_size):
            hov = ActionChains(driver).move_to_element(hv_classes[j])
            hov.perform()
            time.sleep(1)
            cls1arr = driver.find_elements_by_class_name('morris-hover-point')
            newarr = []
            # copy class objects text values to an array
            for r in range(len(cls1arr)):
                objval = cls1arr[r].text
                newarr.append(objval)
            # convert array to create single string
            txt1str = ' '.join(newarr)
            print(txt1str)
            exp_val = ['ASI:','Embroidery:','Screen:','Mixed:','Total:']
            size = len(exp_val)
            for i in range(size):
                assert exp_val[i] in txt1str
            time.sleep(1)

    # ============================================80==========================================================

    def test_SalesProfileVerifySubmitSharingpage_C80(self, impersonate_sales):
        # Verify the submit functionality in sharing page in User profile Dashboard page.
        driver = impersonate_sales['webdriver']
        wait = WebDriverWait(driver, 90)
        # Verify Dashboard tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Dashboard')))
        # Click on Sharing link
        driver.find_element_by_id("nav_dropdown").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Sharing')))
        driver.find_element_by_link_text("Sharing").click()
        # Wait for Delegation select drop down
        wait.until(EC.visibility_of_element_located((By.NAME,'new_delegation')))
        time.sleep(1)
        # Check if not shared
        sh = driver.find_element_by_class_name('panel-body').text
        tx = "You have not shared your orders"
        time.sleep(1)
        if tx in sh:
            # Select any drop down value
            entry_sel = Select(driver.find_element_by_name("new_delegation"))
            entry_sel.select_by_index(2)
            # Click Submit
            driver.find_element_by_class_name('btn-default').click()
            time.sleep(1)
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'btn-danger')))
            time.sleep(1)

        # Verify Orders shared with user
        panel_data = driver.find_element_by_class_name('panel-body').text
        time.sleep(1)
        your_order_shared_expected = "Your orders are shared with:"
        # Verify text in table
        assert your_order_shared_expected in panel_data
        assert "User" in panel_data
        assert "Added On" in panel_data
        assert driver.find_element_by_link_text("Remove").is_displayed()
        time.sleep(1)

        # Verify Dashboard tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Dashboard')))
        driver.find_element_by_link_text('Dashboard').click()
        # Verify that dashboard page shows Sales Dashboard for user
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        time.sleep(1)

    # ====================================803==================11 march============================================

    def test_salesuser_dashboard_VerifyContentOnShipmentTabOnOrderPage_C803(self, impersonate_sales):
        driver = impersonate_sales['webdriver']
        # Verify the contents on shipments page in order id page.
        wait = WebDriverWait(driver, 90)
        # Click on Orders tab.
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        driver.find_element_by_link_text("My Open Orders").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))

        # Get Order id and Click Order Id
        v_orderidfull = driver.find_element_by_id("order-table").find_element_by_class_name("odd").text
        # Split order id based on
        v_orderidsp1 = v_orderidfull.split(" ")
        v_orderidsp2 = str(v_orderidsp1[0])

        # Click on first Order Id
        driver.find_element_by_link_text(v_orderidsp2).click()
        time.sleep(3)
        # Verify Order Id page header
        actualTitle = driver.find_element_by_id("content-header").text
        assert v_orderidsp2 in actualTitle
        time.sleep(1)
        # Verify Element on Order Details Page
        assert driver.find_element_by_id('bookmark').is_displayed()

        # Click shipments tab
        driver.find_element_by_partial_link_text('Shipments').click()
        time.sleep(1)

        shipmentValue = driver.find_element_by_id("shipments").text

        if "No shipments found." not in shipmentValue:
            clsdet = driver.find_element_by_id("shipping").text
            # Verify Contents
            assert 'Method:' in clsdet
            assert 'Time created:' in clsdet
            assert 'Tracking:' in clsdet

    # =====================================================================================