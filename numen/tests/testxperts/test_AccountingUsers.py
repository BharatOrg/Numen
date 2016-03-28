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

class TestAccountingUsers:
    # ====================================1360==================15 march==========================================

    def test_AccountingUser_PersonalAccountReeceivable_VerifyContentOnSubscription_C1360(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify the content in Subscription for: Personal Accounts Receivable page.
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        time.sleep(1)
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Personal
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Personal')))
        driver.find_element_by_link_text("Personal").click()
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Accounts Receivable')))
        driver.find_element_by_link_text("Accounts Receivable").click()
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header = "Personal Accounts Receivable Report"
        actual_header = driver.find_element_by_id("content-header").text
        # Verify Job Header
        assert expected_header in actual_header

        # Click on Make a subscription button right side of the page.
        driver.find_element_by_class_name("btn-primary").click()
        # Verify the content on the subscription form
        # Verify Subscription Name
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
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
        actual_days = driver.find_elements_by_class_name("checkbox")
        time.sleep(1)
        for day in actual_days:
            name = day.text
            assert name in expected_days
        # Verify back button
        assert driver.find_element_by_class_name("btn-default").is_displayed()
        # Verify save Subscription button
        assert driver.find_element_by_id("next_btn").is_displayed()
        driver.find_element_by_class_name("btn-default").click()

    # ====================================1359==================14 march============================================

    def test_AccountingUser_PersonalAccountReeceivable_VerifyContent_C1359(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify the content on "Personal Accounts Receivable Report" page.
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        time.sleep(1)
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Personal
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Personal')))
        driver.find_element_by_link_text("Personal").click()
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Accounts Receivable')))
        driver.find_element_by_link_text("Accounts Receivable").click()
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header = "Personal Accounts Receivable Report"
        actual_header = driver.find_element_by_id("content-header").text
        # Verify Create a Presort Job Header
        assert expected_header in actual_header

        # Click Advanced filters button
        driver.find_element_by_class_name("btn-primary").is_displayed()
        driver.find_element_by_class_name("btn-success").is_displayed()

        driver.find_element_by_id("selector").is_displayed()

    # ====================================1177==================14 march============================================

    def test_AccountingUser_DivisionAccountReeceivable_VerifyContent_C1177(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify the content on "Division Accounts Receivable Report " page.
        wait = WebDriverWait(driver, 90)
        # Click on Reports
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        time.sleep(1)
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Division tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Division')))
        driver.find_element_by_link_text("Division").click()
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Accounts Receivable')))
        driver.find_element_by_link_text("Accounts Receivable").click()
        time.sleep(1)


        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header = "Division Accounts Receivable Report"
        actual_header = driver.find_element_by_id("content-header").text
        # Verify Job Header.
        assert expected_header in actual_header

        # Click Advanced filters button
        driver.find_element_by_class_name("btn-primary").is_displayed()
        driver.find_element_by_class_name("btn-success").is_displayed()

        driver.find_element_by_id("selector").is_displayed()

    # ====================================1480==================14 march============================================

    def test_AccountingUser_OrderSearch_VerifyContentInSearchField_C1480(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify the contents headers in Order Search output table
        wait = WebDriverWait(driver, 90)
        # Click on Orders tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        driver.find_element_by_link_text("Orders").click()
        # Click on Order Search
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Order Search')))
        driver.find_element_by_link_text("Order Search").click()

        # Click Search button
        wait.until(EC.visibility_of_element_located((By.ID,'gen_search')))
        driver.find_element_by_id("gen_search").click()
        # Verify table loaded
        wait.until(EC.visibility_of_element_located((By.ID,'orders_table_length')))
        assert driver.find_element_by_id("orders_table_length").is_displayed()
        # Verify search
        driver.find_element_by_id("search_input_toggle").click()
        time.sleep(1)

        actual = driver.find_element_by_id('orders_table').find_elements_by_tag_name('th')
        expected_OrdTable = ['ID','Client Name','Status','Sales Rep','Client PO','Date Submitted','Production Date', 'Ship-by Date', 'Paid Date','Invoice Create Date', 'Type', 'In Hands Date',
            'PO #','Tracking #' ,'Invoice #','Art Title','Ship-to Name','Order Origin']
        size = len(actual)
        if int(size) > 0:
            for i in range(size):
                assert actual[i].text in expected_OrdTable
        time.sleep(1)

    # ====================================1187==================14 march============================================

    def test_AccountingUser_DivisionAccountReeceivable_VerifyBackButtonOnSubscription_C1187(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify the back button functionality in Subscription for: Division Accounts Receivable form.
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        time.sleep(1)
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Division
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Division')))
        driver.find_element_by_link_text("Division").click()
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Accounts Receivable')))
        driver.find_element_by_link_text("Accounts Receivable").click()
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header = "Division Accounts Receivable Report"
        actual_header = driver.find_element_by_id("content-header").text
        # Verify Job Header
        assert expected_header in actual_header

        # Click on Make a subscription button right side of the page.
        driver.find_element_by_class_name("btn-primary").click()
        # Verify the content on the subscription form
        time.sleep(1)
        random_number = str(randint(10, 999))
        name = "TestgSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        # Click on Back button at the bottom of the page.
        driver.find_element_by_class_name("btn-default").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        # User should redirect Report page.
        expected_header = "Division Accounts Receivable Report"
        actual_header = driver.find_element_by_id("content-header").text
        assert expected_header in actual_header
        assert driver.find_element_by_id("sub_name").is_displayed() == 0

    # ====================================1189==================14 march============================================

    def test_AccountingUser_DivisionAccountReeceivable_VerifyDefaultEmailIDOnSubscription_C1189(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify user Email Id display by default  in subscription form.
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        time.sleep(1)
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Division
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Division')))
        driver.find_element_by_link_text("Division").click()
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Accounts Receivable')))
        driver.find_element_by_link_text("Accounts Receivable").click()
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header = "Division Accounts Receivable Report"
        actual_header = driver.find_element_by_id("content-header").text
        # Verify Job Header
        assert expected_header in actual_header

        # Click on Make a subscription button right side of the page.
        driver.find_element_by_class_name("btn-primary").click()
        # Verify the content on the subscription form
        time.sleep(1)
        expectedEmail  = "jstorey@ggoutfitters.com"
        actualEmail = driver.find_element_by_id("email").get_attribute("value")
        # Click on Back button at the bottom of the page.
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header = driver.find_element_by_id("content-header").text
        assert expectedEmail == actualEmail
        driver.find_element_by_class_name("btn-default").click()

    # ====================================1190==================14 march============================================
    def test_AccountingUser_DivisionAccountReeceivable_VerifyBlankFieldNotSubmittedOnSubscription_C1190(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify with blank fields subscription form not submitted.
        wait = WebDriverWait(driver, 90)
        # Click on Orders tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        time.sleep(1)
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Order Search
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Division')))
        driver.find_element_by_link_text("Division").click()
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Accounts Receivable')))
        driver.find_element_by_link_text("Accounts Receivable").click()
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header = "Division Accounts Receivable Report"
        actual_header = driver.find_element_by_id("content-header").text
        # Verify Job Header
        assert expected_header in actual_header

        # Click on Make a subscription button right side of the page.
        driver.find_element_by_class_name("btn-primary").click()
        # Verify the content on the subscription form
        time.sleep(1)

        # Click on submit button and Verify Subscription form remain displaying.
        wait.until(EC.visibility_of_element_located((By.ID,'next_btn')))
        driver.find_element_by_id("next_btn").click()
        time.sleep(1)
        assert driver.find_element_by_id("myModalLabel").is_displayed()
        # Note : Error message 'error message " Please fill out this field".' is not verified because id is not found.

    # ====================================1186==================14 march==========================================

    def test_AccountingUser_DivisionAccountReeceivable_VerifyContentOnSubscription_C1186(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        #  Verify the content in Subscription for: Division Accounts Receivable page.
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        time.sleep(1)
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Division tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Division')))
        driver.find_element_by_link_text("Division").click()
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Accounts Receivable')))
        driver.find_element_by_link_text("Accounts Receivable").click()
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header = "Division Accounts Receivable Report"
        actual_header = driver.find_element_by_id("content-header").text
        # Verify Job Header.
        assert expected_header in actual_header

        # Click on Make a subscription button right side of the page.
        driver.find_element_by_class_name("btn-primary").click()
        # Verify the content on the subscription form
        # Verify Subscription Name
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
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
        actual_days = driver.find_elements_by_class_name("checkbox")
        time.sleep(1)
        for day in actual_days:
            name = day.text
            assert name in expected_days
        # Verify back button
        assert driver.find_element_by_class_name("btn-default").is_displayed()
        # Verify save Subscription button
        assert driver.find_element_by_id("next_btn").is_displayed()
        driver.find_element_by_class_name("btn-default").click()


    # ====================================16499==================15 march===========================================

    def test_AccountingUser_BookMarks_VerifyContent_C16499(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify the contents on Bookmarks page.
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
        print(flag)
        # Go to Bookmarks page if bookmarks exist and confirm  removed bookmark order
        if int(flag) == 1:
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

    # ====================================16500==================15 march===========================================

    def test_AccountingUser_BookMarks_VerifyFilterFunctionality_C164500(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        #  Verify the filter functionality on Bookmarks page.
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

        if int(flag) == 1:
            # Check if Page 1 is visible to see bookmarks exist
            if driver.find_element_by_link_text('1').is_enabled():
                # Fetch Order Id dynamically for Valid search criteria
                v_orderid = driver.find_element_by_class_name('glyphicon-bookmark').get_attribute('data-order-id')
                v_orderidfull = driver.find_element_by_class_name('glyphicon-bookmark').get_attribute('data-order-id')
                # Split order id based on '-' to get orderid
                v_orderidsp = v_orderidfull.split('-')
                v_orderid = v_orderidsp[1]
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

    # ====================================16501==================15 march===========================================

    def test_AccountingUser_BookMarks_VerifyBookmarkFunctionality_C16501(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify the bookmark functionality on Bookmarks page.
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
        print(ord_tab_content)
        if no_data_message in ord_tab_content:
            flag = 2
        else:
            # data exists
            flag = 1
        print(flag)
        # Go to Page 1 if bookmarks exist
        if int(flag) == 1:
            # Count Bookmark
            bc = len(driver.find_element_by_id('orders_table').find_elements_by_tag_name("tr"))
            # Fetch Order Id dynamically for Valid search criteria
            v_orderidfull = driver.find_element_by_class_name('glyphicon-bookmark').get_attribute('data-order-id')
            # Split order id based on '-' to get orderid
            if '-' in v_orderidfull:
                v_orderidsp = v_orderidfull.split('-')
                v_orderid = v_orderidsp[1]
            else:
                v_orderid = v_orderidfull
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
                driver.find_element_by_id("orders_table_filter").find_element_by_class_name("input-sm").send_keys(v_orderidfull)
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
                driver.find_element_by_id("orders_table_filter").find_element_by_class_name("input-sm").send_keys(v_orderid)
                time.sleep(1)
                # Bookmark the record
                driver.find_element_by_class_name('glyphicon-bookmark').click()
                time.sleep(4)
                driver.refresh()
                # Check bookmarks badges count
                badge_pagesnew = driver.find_element_by_class_name('badge').text
                time.sleep(1)
                # Check prev and new bookmark values
                assert bc != badge_pagesnew

    # ====================================16502==================15 march===========================================

    def test_AccountingUser_BookMarks_VerifyEntriesFunctionality_C16502(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify 'Showing 1 to 'xx'of 'xxx' entries functionality on Bookmarks page.
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

    # ====================================16503==================15 march===========================================

    def test_AccountingUser_BookMarks_VerifySortingFunctionality_C16503(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify sorting functionality on Bookmarks page.
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

    # ====================================16504==================15 march===========================================

    def test_AccountingUser_BookMarks_VerifyPaginationFunctionality_C16504(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify pagination functionality on Bookmarks page.
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

        if int(flag) == 1:
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

    # ====================================16505==================15 march===========================================

    def test_AccountingUser_BookMarks_VerifyCountOfBookMark_C16505(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify the count of bookmarks in Orders/Bookmarks Page.
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
            v_orderidfull = driver.find_element_by_class_name('glyphicon-bookmark').get_attribute('data-order-id')
            # Split order id based on '-' to get orderid
            v_orderidsp = v_orderidfull.split('-')
            v_orderid = v_orderidsp[1]
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

    # ====================================16506==================15 march===========================================

    def test_AccountingUser_BookMarks_VerifyChangeColumnFunctionality_C16506(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify the change column functionality in Orders/Bookmarks Page.
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

        if int(flag) == 1:
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

    # ====================================1460==================16 march===========================================

    def test_AccountingUser_Shipping_VerifyContent_C1460(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify the content in the Shipping report page.
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Shipping')))
        time.sleep(1)
        driver.find_element_by_link_text("Shipping").click()
        time.sleep(1)
        expected_header_Shipping_Report = "Shipping Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Shipping_Report = driver.find_element_by_id("content-header").text
        # Verify Header
        assert expected_header_Shipping_Report in actual_header_Shipping_Report

        assert driver.find_element_by_id("client_id").is_displayed()
        assert driver.find_element_by_name("daterange").is_displayed()
        assert driver.find_element_by_class_name("btn-success").is_displayed()

    # ====================================1461==================16 march===========================================

    def test_AccountingUser_Shipping_VerifyGeneratedReport_C1461(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify that report is generated for Shipping page.
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Shipping')))
        time.sleep(1)
        driver.find_element_by_link_text("Shipping").click()
        time.sleep(1)
        expected_header_Shipping_Report = "Shipping Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Shipping_Report = driver.find_element_by_id("content-header").text
        # Verify Header
        assert expected_header_Shipping_Report in actual_header_Shipping_Report

        # Select the client from the drop down
        clients = driver.find_element_by_id("client_id")
        client_option = "AFNAVY"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Select the Ship Start  and ship end date
        driver.find_element_by_name("daterange").click()
        time.sleep(1)

        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("03/11/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("03/12/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)
        # Click on Generate report button.
        driver.find_element_by_class_name("btn-success").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
        time.sleep(1)
        assert driver.find_element_by_id("table_report").is_displayed()

    # ====================================1462==================16 march===========================================

    def test_AccountingUser_Shipping_VerifymakeSubscriptionFunctionality_C1462(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify the functionality of make a subscription button for the generated report on Shipping page.
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Shipping')))
        time.sleep(1)
        driver.find_element_by_link_text("Shipping").click()
        time.sleep(1)
        expected_header_Shipping_Report = "Shipping Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Shipping_Report = driver.find_element_by_id("content-header").text
        # Verify Header
        assert expected_header_Shipping_Report in actual_header_Shipping_Report

        # Select the client from the drop down
        clients = driver.find_element_by_id("client_id")
        client_option = "ARA"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Select the Ship Start  and ship end date
        driver.find_element_by_name("daterange").click()
        time.sleep(1)

        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("03/11/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("03/12/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)
        # Click on Generate report button.
        driver.find_element_by_class_name("btn-success").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
        time.sleep(1)
        assert driver.find_element_by_id("table_report").is_displayed()
        # Click Subscription
        driver.find_element_by_id("table_report").find_element_by_class_name("btn-primary").click()
        time.sleep(1)

        expected_header = "Subscription for: ARA Shipping Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'subscriptionsModalLabel')))
        actual_header = driver.find_element_by_id("subscriptionsModalLabel").text
        # Verify Header
        assert expected_header in actual_header
        # Click Back
        driver.find_element_by_class_name('btn-default').click()
        time.sleep(1)

    # ====================================1464==================16 march===========================================

    def test_AccountingUser_Shipping_VerifyContentOnGeneratedreport_C1464(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify the content of report generated for Shipping page.
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Shipping')))
        time.sleep(1)
        driver.find_element_by_link_text("Shipping").click()
        time.sleep(1)
        expected_header_Shipping_Report = "Shipping Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Shipping_Report = driver.find_element_by_id("content-header").text
        # Verify Header
        assert expected_header_Shipping_Report in actual_header_Shipping_Report

        # Select the client from the drop down
        clients = driver.find_element_by_id("client_id")
        client_option = "ARA"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Select the Ship Start  and ship end date
        driver.find_element_by_name("daterange").click()
        time.sleep(1)

        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("03/11/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("03/12/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)
        # Click on Generate report button.
        driver.find_element_by_class_name("btn-success").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
        time.sleep(3)
        assert driver.find_element_by_id("table_report").is_displayed()

        actual = driver.find_element_by_class_name('table-striped').find_elements_by_tag_name('th')
        expected_OrdTable = ['List Freight','Company','Attention','Addr1','Addr2','City','State','Zip','SS Order Nbr','Client PO','Tracking','Freight','Ship Date'
            'Ship Method','SKUs']
        size = len(actual)
        arr = []
        for i in range(size):
            ar1 = actual[i].text
            arr.append(ar1)
        # Convert array to create single string
        txt1str = ' '.join(expected_OrdTable)

        size = len(arr)
        if int(size) > 0:
            for i in range(size):
                assert arr[i] in txt1str
        time.sleep(1)

        assert driver.find_element_by_name("dataTable_length").is_displayed()
        assert driver.find_element_by_id("dataTable_filter").find_element_by_class_name("input-sm").is_displayed()
        assert driver.find_element_by_class_name("btn-primary").is_displayed()
        assert driver.find_element_by_id("dataTable_info").is_displayed()

    # ====================================1469==================16 march===========================================

    def test_AccountingUser_Shipping_VerifyContentOnSubscription_C1469(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify the content in Subscription for: Client name Shipping pop up in KKohn- Reports/Ad-hoc/Shipping page.
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Shipping')))
        time.sleep(1)
        driver.find_element_by_link_text("Shipping").click()
        time.sleep(1)
        expected_header_Shipping_Report = "Shipping Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Shipping_Report = driver.find_element_by_id("content-header").text
        # Verify Header
        assert expected_header_Shipping_Report in actual_header_Shipping_Report

        # Select the client from the drop down
        clients = driver.find_element_by_id("client_id")
        client_option = "ARA"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Select the Ship Start  and ship end date
        driver.find_element_by_name("daterange").click()
        time.sleep(1)

        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("03/11/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("03/12/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)
        # Click on Generate report button.
        driver.find_element_by_class_name("btn-success").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
        time.sleep(1)
        assert driver.find_element_by_id("table_report").is_displayed()

        driver.find_element_by_id("table_report").find_element_by_class_name("btn-primary").click()
        time.sleep(1)

        expected_header = "Subscription for: ARA Shipping Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'subscriptionsModalLabel')))
        actual_header = driver.find_element_by_id("subscriptionsModalLabel").text
        # Verify Header
        assert expected_header in actual_header

        # Verify Subscription Name
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
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
        actual_days = driver.find_elements_by_class_name("checkbox")
        time.sleep(1)
        for day in actual_days:
            name = day.text
            assert name in expected_days
        # Verify back button
        assert driver.find_element_by_class_name("btn-default").is_displayed()
        # Verify save Subscription button
        assert driver.find_element_by_id("next_btn").is_displayed()
        driver.find_element_by_class_name("btn-default").click()

    # ====================================16507==================16 march===========================================

    def test_AccountingUser_Kitting_VerifyContent_C16507(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify the content in the Kitting report page.
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        time.sleep(1)
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Kitting')))
        driver.find_element_by_link_text("Kitting").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Kitting_Report = "Kitting Report"
        time.sleep(1)
        actual_header_Kitting_Report = driver.find_element_by_id("content-header").text
        # Verify  Header
        assert expected_header_Kitting_Report in actual_header_Kitting_Report

        assert driver.find_element_by_id("client_id").is_displayed()
        assert driver.find_element_by_name("daterange").is_displayed()
        assert driver.find_element_by_class_name("btn-success").is_displayed()

    # ====================================16508==================16 march===========================================

    def test_AccountingUser_Kitting_VerifyGeneratedReport_C16508(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify that report is generated for Kitting page.
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Kitting')))
        driver.find_element_by_link_text("Kitting").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Kitting_Report = "Kitting Report"
        time.sleep(1)
        actual_header_Kitting_Report = driver.find_element_by_id("content-header").text
        # Verify  Header
        assert expected_header_Kitting_Report in actual_header_Kitting_Report

        # Select the client from the drop down
        clients = driver.find_element_by_id("client_id")
        client_option = "ARA"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Select the Ship Start  and ship end date
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
        driver.find_element_by_class_name("btn-success").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
        time.sleep(5)

        assert driver.find_element_by_id("table_report").is_displayed()

    # ====================================16509==================16 march===========================================

    def test_AccountingUser_Kitting_VerifyMakeSubscriptionFunctionality_C16509(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify the functionality of make a subscription button for the generated report on Kitting page.
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Kitting')))
        driver.find_element_by_link_text("Kitting").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Kitting_Report = "Kitting Report"
        time.sleep(1)
        actual_header_Kitting_Report = driver.find_element_by_id("content-header").text
        # Verify  Header
        assert expected_header_Kitting_Report in actual_header_Kitting_Report

        # Select the client from the drop down
        clients = driver.find_element_by_id("client_id")
        client_option = "ARA"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Select the Ship Start  and ship end date
        driver.find_element_by_name("daterange").click()
        #driver.find_element_by_name('daterangepicker_start').send_keys()
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
        driver.find_element_by_class_name("btn-success").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
        time.sleep(5)

        assert driver.find_element_by_id("table_report").is_displayed()

        driver.find_element_by_id("table_report").find_element_by_class_name("btn-primary").click()
        time.sleep(1)

        expected_header = "Subscription for: ARA Kitting Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'subscriptionsModalLabel')))
        actual_header = driver.find_element_by_id("subscriptionsModalLabel").text
        # Verify Header
        assert expected_header in actual_header

    # ====================================16511==================16 march===========================================

    def test_AccountingUser_Kitting_VerifyContentOnReport_C16511(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify the content of report generated for Kitting page.
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Kitting')))
        driver.find_element_by_link_text("Kitting").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Kitting_Report = "Kitting Report"
        time.sleep(1)
        actual_header_Kitting_Report = driver.find_element_by_id("content-header").text
        # Verify  Header
        assert expected_header_Kitting_Report in actual_header_Kitting_Report

        # Select the client from the drop down
        clients = driver.find_element_by_id("client_id")
        client_option = "ARA"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Select the Ship Start  and ship end date
        driver.find_element_by_name("daterange").click()
        #driver.find_element_by_name('daterangepicker_start').send_keys()
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
        driver.find_element_by_class_name("btn-success").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
        time.sleep(5)

        assert driver.find_element_by_id("table_report").is_displayed()

        actual = driver.find_element_by_class_name('table-striped').find_elements_by_tag_name('th')
        expected_OrdTable = ['packslip','product','quantity']
        print(expected_OrdTable)
        size = len(actual)
        print(size)
        if int(size) > 0:
            for i in range(size):
                print(actual[i].text)
                assert actual[i].text in expected_OrdTable
        time.sleep(1)

        assert driver.find_element_by_name("dataTable_length").is_displayed()
        assert driver.find_element_by_id("dataTable_filter").find_element_by_class_name("input-sm").is_displayed()
        assert driver.find_element_by_class_name("btn-primary").is_displayed()
        assert driver.find_element_by_id("dataTable_info").is_displayed()

    # ====================================16516==================16 march===========================================

    def test_AccountingUser_Kitting_VerifyContentOnSubscription_C16516(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify the content in Subscription for: Client name Kitting pop up in KKohn- Reports/Ad-hoc/Kitting page.
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Kitting')))
        driver.find_element_by_link_text("Kitting").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Kitting_Report = "Kitting Report"
        time.sleep(1)
        actual_header_Kitting_Report = driver.find_element_by_id("content-header").text
        # Verify  Header
        assert expected_header_Kitting_Report in actual_header_Kitting_Report

        # Select the client from the drop down
        clients = driver.find_element_by_id("client_id")
        client_option = "ARA"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Select the Ship Start  and ship end date
        driver.find_element_by_name("daterange").click()
        #driver.find_element_by_name('daterangepicker_start').send_keys()
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
        driver.find_element_by_class_name("btn-success").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
        time.sleep(5)

        assert driver.find_element_by_id("table_report").is_displayed()

        driver.find_element_by_id("table_report").find_element_by_class_name("btn-primary").click()
        time.sleep(1)

        expected_header = "Subscription for: ARA Kitting Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'subscriptionsModalLabel')))
        actual_header = driver.find_element_by_id("subscriptionsModalLabel").text
        # Verify Header
        assert expected_header in actual_header

        # Verify Subscription Name
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
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
        actual_days = driver.find_elements_by_class_name("checkbox")
        time.sleep(1)
        for day in actual_days:
            name = day.text
            assert name in expected_days
        # Verify back button
        assert driver.find_element_by_class_name("btn-default").is_displayed()
        # Verify save Subscription button
        assert driver.find_element_by_id("next_btn").is_displayed()
        driver.find_element_by_class_name("btn-default").click()

    # ====================================1463==================17march===========================================

    def test_AccountingUser_Shipping_verifyExcelandSubscriptionButton_C1463(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # [Reports/Ad-hoc/Shipping] - Verify the visibility of Excel button on the report generated for Shipping page.
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Shipping')))
        time.sleep(1)
        driver.find_element_by_link_text("Shipping").click()
        time.sleep(1)
        expected_header_Shipping_Report = "Shipping Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Shipping_Report = driver.find_element_by_id("content-header").text
        # Verify Header
        assert expected_header_Shipping_Report in actual_header_Shipping_Report

        # Select the client from the drop down
        clients = driver.find_element_by_id("client_id")
        client_option = "ARA"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Select the Ship Start  and ship end date
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
        driver.find_element_by_class_name("btn-success").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
        time.sleep(5)
        # Verify Make a Subscription and Excel button displayed on the report
        assert driver.find_element_by_id("table_report").find_element_by_class_name("btn-primary").is_displayed()
        assert driver.find_element_by_id("table_report").find_element_by_id("xls_btn").is_displayed()

    # ====================================1471==================17 march===========================================

    def test_AccountingUser_Shipping_VerifyBackButtonFunctionalityInSubscription_C1471(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify the back button functionality in Subscription in KKohn- Reports/Ad-hoc/Shipping page.
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Shipping')))
        time.sleep(1)
        driver.find_element_by_link_text("Shipping").click()
        time.sleep(1)
        expected_header_Shipping_Report = "Shipping Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Shipping_Report = driver.find_element_by_id("content-header").text
        # Verify Header
        assert expected_header_Shipping_Report in actual_header_Shipping_Report

        # Select the client from the drop down
        clients = driver.find_element_by_id("client_id")
        client_option = "ARA"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Select the Ship Start  and ship end date
        driver.find_element_by_name("daterange").click()
        time.sleep(1)

        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("03/11/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("03/12/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)
        # Click on Generate report button.
        driver.find_element_by_class_name("btn-success").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
        time.sleep(1)
        assert driver.find_element_by_id("table_report").is_displayed()
        # Open Subscription
        driver.find_element_by_id("table_report").find_element_by_class_name("btn-primary").click()
        time.sleep(1)

        expected_header = "Subscription for: ARA Shipping Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'subscriptionsModalLabel')))
        actual_header = driver.find_element_by_id("subscriptionsModalLabel").text
        # Verify Header
        assert expected_header in actual_header
        time.sleep(1)

        random_number = str(randint(10, 999))
        name = "TestSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        # Click on Back button at the bottom of the page.
        driver.find_element_by_class_name("btn-default").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        # User should redirect Report page.
        expected_header = "Shipping Report"
        actual_header = driver.find_element_by_id("content-header").text
        assert expected_header in actual_header
        assert driver.find_element_by_id("sub_name").is_displayed() == 0

    # ====================================1470==================17 march===========================================

    def test_AccountingUser_Shipping_VerifySaveButtonFunctionalityInSubscription_C1470(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify the save Subscription functionality in Subscription in KKohn- Reports/Ad-hoc/Shipping page.
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Shipping')))
        time.sleep(1)
        driver.find_element_by_link_text("Shipping").click()
        time.sleep(1)
        expected_header_Shipping_Report = "Shipping Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Shipping_Report = driver.find_element_by_id("content-header").text
        # Verify Header
        assert expected_header_Shipping_Report in actual_header_Shipping_Report

        # Select the client from the drop down
        clients = driver.find_element_by_id("client_id")
        client_option = "ARA"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Select the Ship Start  and ship end date
        driver.find_element_by_name("daterange").click()
        time.sleep(1)

        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("03/11/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("03/12/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)
        # Click on Generate report button.
        driver.find_element_by_class_name("btn-success").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
        time.sleep(1)
        assert driver.find_element_by_id("table_report").is_displayed()

        driver.find_element_by_id("table_report").find_element_by_class_name("btn-primary").click()
        time.sleep(1)

        expected_header = "Subscription for: ARA Shipping Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'subscriptionsModalLabel')))
        actual_header = driver.find_element_by_id("subscriptionsModalLabel").text
        # Verify Header
        assert expected_header in actual_header

        time.sleep(1)
        random_number = str(randint(10, 999))
        name = "TestSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        # Click on Back button at the bottom of the page.
        driver.find_element_by_id("next_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'noty_text')))
        # Subscription form submitted successfully and display message Subscription Saved.
        expected_message = "Subscription saved."
        actual_message = driver.find_element_by_class_name("noty_text").text
        assert expected_message in actual_message
        # Subscription should be display in subscriptions page with correct data.
        driver.find_element_by_link_text("Subscriptions").click()
        time.sleep(1)
        NameNew_value = driver.find_element_by_id("jobs_table").text
        assert name in NameNew_value

    # ====================================16519==================17 march===========================================

    def test_AccountingUser_Settlement_VerifyContent_C16519(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify the content in the Settlement report page.
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        time.sleep(1)
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Settlement')))
        driver.find_element_by_link_text("Settlement").click()
        time.sleep(1)
        expected_header_Settlement_Report = "Settlement Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Settlement_Report = driver.find_element_by_id("content-header").text
        time.sleep(1)
        # Verify  Header
        assert expected_header_Settlement_Report in actual_header_Settlement_Report

        assert driver.find_element_by_id("client_id").is_displayed()
        assert driver.find_element_by_name("daterange").is_displayed()
        assert driver.find_element_by_class_name("btn-success").is_displayed()

    # ====================================16520==================17 march===========================================

    def test_AccountingUser_Settlement_VerifyGeneratedReport_C16520(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify that report is generated for Settlement page.
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Settlement')))
        driver.find_element_by_link_text("Settlement").click()
        time.sleep(1)
        expected_header_Settlement_Report = "Settlement Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Settlement_Report = driver.find_element_by_id("content-header").text
        time.sleep(1)
        # Verify  Header
        assert expected_header_Settlement_Report in actual_header_Settlement_Report

        # Select the client from the drop down
        clients = driver.find_element_by_id("client_id")
        client_option = "ARA"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Select the Ship Start  and ship end date
        driver.find_element_by_name("daterange").click()
        #driver.find_element_by_name('daterangepicker_start').send_keys()
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
        driver.find_element_by_class_name("btn-success").click()

        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
        time.sleep(5)

        assert driver.find_element_by_id("table_report").is_displayed()

    # ====================================16531==================17 march===========================================

    def test_AccountingUser_SatoriBulkMailing_VerifyContent_C16531(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify the content in Reports/Ad-hoc/Satori Bulk Mailing page.
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Satori Bulk Mailing')))
        driver.find_element_by_link_text("Satori Bulk Mailing").click()
        time.sleep(1)
        expected_header_Satori_Bulk_Mailing = "Satori Bulk Mailing Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Satori_Bulk_Mailing = driver.find_element_by_id("content-header").text
        time.sleep(1)
        # Verify  Header
        assert expected_header_Satori_Bulk_Mailing in actual_header_Satori_Bulk_Mailing

        assert driver.find_element_by_id("client_id").is_displayed()
        assert driver.find_element_by_class_name("btn-success").is_displayed()

    # ====================================16510==================17 march===========================================

    def test_AccountingUser_Kitting_verifyExcelandSubscriptionButton_C16510(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # [Reports/Ad-hoc/Kitting] - Verify the visibility of Excel/Make Subscription button on the report generated.
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Kitting')))
        driver.find_element_by_link_text("Kitting").click()

        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Kitting_Report = "Kitting Report"
        time.sleep(1)
        actual_header_Kitting_Report = driver.find_element_by_id("content-header").text
        # Verify  Header
        assert expected_header_Kitting_Report in actual_header_Kitting_Report

        # Select the client from the drop down
        clients = driver.find_element_by_id("client_id")
        client_option = "ARA"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Select the Ship Start  and ship end date
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
        driver.find_element_by_class_name("btn-success").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
        time.sleep(5)
        # Verify Make a Subscription and Excel button displayed on the report
        assert driver.find_element_by_id("table_report").find_element_by_class_name("btn-primary").is_displayed()
        assert driver.find_element_by_id("table_report").find_element_by_id("xls_btn").is_displayed()

    # ====================================16493==================18 march===========================================

    def test_AccountingUser_OrderSearch_VerifyResetFunctionality_C16493(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify the reset functionality in Orders/Orders Search page.
        wait = WebDriverWait(driver, 90)
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
        driver.find_element_by_id("reset").click()
        time.sleep(1)
        act_orderid = driver.find_element_by_id("orderid").get_attribute("value")
        act_invoice = driver.find_element_by_id("invoice_nbr").get_attribute("value")
        assert orderid_number is not act_orderid
        assert invoice_number is not act_invoice

    # ====================================16497==================18 march===========================================

    def test_AccountingUser_OrderSearch_VerifyContent_C16497(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify the contents on Order Search page.
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
        arr = ['ID / SO #:','Client PO #:','Order Status:','Date Submitted:','Order Type:','Production Date:','Client # / Client Name:'
               ,'Order Origin:','Ship by Date:','Tracking #:','Sales Rep:','In Hands Date:','Invoice #:','Flags:','Paid Date:','Art Title:','Invoice Create Date:','Ship to Name:']

        for i in range(len(arr)):
            assert arr[i] in lblgroup

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

    # ====================================1188==================18 march===========================================

    def test_AccountingUser_DivisionAccountReeceivable_VerifySubscriptionAcceptOnlyNumberAndLetter_C1188(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify in "Subscription Name" text box only letters and numbers are allowed.
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        time.sleep(1)
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Order Search
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Division')))
        driver.find_element_by_link_text("Division").click()
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Accounts Receivable')))
        driver.find_element_by_link_text("Accounts Receivable").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header = "Division Accounts Receivable Report"
        actual_header = driver.find_element_by_id("content-header").text
        # Verify Create a Presort Job Header
        assert expected_header in actual_header

        # Click on Make a subscription button right side of the page.
        driver.find_element_by_class_name("btn-primary").click()
        # Verify the content on the subscription form
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

    # ====================================1190==================18 march===========================================

    def test_AccountingUser_DivisionAccountReceivable_VerifySubscriptionNotSubmittedWithBlankField_C1190(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify with blank fields subscription form not submitted.
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        time.sleep(1)
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Order Search
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Division')))
        driver.find_element_by_link_text("Division").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Accounts Receivable')))
        driver.find_element_by_link_text("Accounts Receivable").click()
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_presort_job = "Division Accounts Receivable Report"
        actual_header_presort_job = driver.find_element_by_id("content-header").text
        # Verify Create a Presort Job Header
        assert expected_header_presort_job in actual_header_presort_job

        # Click Advanced filters button
        # Click on Make a subscription button right side of the page.
        driver.find_element_by_class_name("btn-primary").click()
        # Verify the content on the subscription form
        # Click on submit button and Verify Subscription form remain displaying.
        wait.until(EC.visibility_of_element_located((By.ID,'next_btn')))
        driver.find_element_by_id("next_btn").click()
        assert driver.find_element_by_id("myModalLabel").is_displayed()
        # Note : Error message 'error message " Please fill out this field".' is not verified because id is not found.

    # ====================================1191==================18 march===========================================

    def test_AccountingUser_DivisionAccountReceivable_VerifySaveSubscriptionFunctionality_C1191(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify the save Subscription functionality in Subscription for: Division Accounts Receivable form.
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        time.sleep(1)
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Order Search
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Division')))
        driver.find_element_by_link_text("Division").click()
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Accounts Receivable')))
        driver.find_element_by_link_text("Accounts Receivable").click()
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_presort_job = "Division Accounts Receivable Report"
        actual_header_presort_job = driver.find_element_by_id("content-header").text
        # Verify Create a Presort Job Header
        assert expected_header_presort_job in actual_header_presort_job

        # Click Advanced filters button
        # Click on Make a subscription button right side of the page.
        driver.find_element_by_class_name("btn-primary").click()
        # Verify the content on the subscription form
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
        # Subscription should be display in subscriptions page with correct data.
        driver.find_element_by_link_text("Subscriptions").click()
        time.sleep(1)
        NameNew_value = driver.find_element_by_id("jobs_table").text
        assert name in NameNew_value

    # ====================================1192==================18 march===========================================

    def test_AccountingUser_DivisionAccountReeceivable_VerifyMakeSubscriptionFunctionality_C1192(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify the make a subscription button functionality.
        wait = WebDriverWait(driver, 90)
        # Click on Orders tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        time.sleep(1)
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Order Search
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Division')))
        driver.find_element_by_link_text("Division").click()
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Accounts Receivable')))
        driver.find_element_by_link_text("Accounts Receivable").click()
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header = "Division Accounts Receivable Report"
        actual_header = driver.find_element_by_id("content-header").text
        # Verify Create a Presort Job Header
        assert expected_header in actual_header

        # Click on Make a subscription button right side of the page.
        driver.find_element_by_class_name("btn-primary").click()
        time.sleep(1)
        # Verify the content on the subscription form
        expected_header = "Subscription for: Division Accounts Receivable"
        actual_header = driver.find_element_by_id("myModalLabel").text
        assert expected_header in actual_header

    # ====================================1197==================18 march===========================================

    def test_AccountingUser_DivisionAccountReeceivable_VerifyModifyAndDelete_C1197(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify submitted subscription show in the "subscription"page.
        wait = WebDriverWait(driver, 90)
        # Click on Orders tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        time.sleep(1)
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Order Search
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Division')))
        driver.find_element_by_link_text("Division").click()
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Accounts Receivable')))
        driver.find_element_by_link_text("Accounts Receivable").click()
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_presort_job = "Division Accounts Receivable Report"
        actual_header_presort_job = driver.find_element_by_id("content-header").text
        # Verify Create a Presort Job Header
        assert expected_header_presort_job in actual_header_presort_job

        # Click on Make a subscription button right side of the page.
        driver.find_element_by_class_name("btn-primary").click()
        # Verify the content on the subscription form
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
        # Subscription should be display in subscriptions page with correct data.
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

    # ====================================1361==================18 march===========================================

    def test_AccountingUser_PersonalAccountReeceivable_VerifyBackButtonFunctionality_C1361(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify the back button functionality in Subscription for: Division Accounts Receivable form.
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        time.sleep(1)
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Order Search
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Personal')))
        driver.find_element_by_link_text("Personal").click()
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Accounts Receivable')))
        driver.find_element_by_link_text("Accounts Receivable").click()
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_presort_job = "Personal Accounts Receivable Report"
        actual_header_presort_job = driver.find_element_by_id("content-header").text
        # Verify Create a Presort Job Header
        assert expected_header_presort_job in actual_header_presort_job

        # Click Advanced filters button
        # Click on Make a subscription button right side of the page.
        driver.find_element_by_class_name("btn-primary").click()
        # Verify the content on the subscription form
        time.sleep(1)
        random_number = str(randint(10, 999))
        name = "TestSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        # Click on Back button at the bottom of the page.
        driver.find_element_by_class_name("btn-default").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        # User should redirect Report page.
        expected_header = "Personal Accounts Receivable Report"
        actual_header = driver.find_element_by_id("content-header").text
        assert expected_header in actual_header
        assert driver.find_element_by_id("sub_name").is_displayed() == 0

    # ====================================1362==================18 march===========================================

    def test_AccountingUser_PersonalAccountReeceivable_VerifySubscriptionAcceptOnlyNumberAndLetter_C1362(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify in "Subscription Name" text box only letters and numbers are allowed.
        wait = WebDriverWait(driver, 90)
        # Click on Orders tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        time.sleep(1)
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Order Search
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Personal')))
        driver.find_element_by_link_text("Personal").click()
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Accounts Receivable')))
        driver.find_element_by_link_text("Accounts Receivable").click()
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_presort_job = "Personal Accounts Receivable Report"
        actual_header_presort_job = driver.find_element_by_id("content-header").text
        # Verify Create a Presort Job Header
        assert expected_header_presort_job in actual_header_presort_job

        # Click on Make a subscription button right side of the page.
        driver.find_element_by_id("subscription_btn").click()
        wait.until(EC.visibility_of_element_located((By.ID,'sub_name')))
        driver.find_element_by_id("sub_name").send_keys("*%&")
        driver.find_element_by_id("next_btn").click()
        wait.until(EC.visibility_of_element_located((By.ID,'sub_name')))

        # Verify the warning message.
        expected_message="Only use letters and numbers."
        actual_message=driver.find_element_by_id("sub_name").get_attribute("title")
        assert expected_message in actual_message

    # ====================================1375==================18 march===========================================

    def test_AccountingUser_PersonalAccountReeceivable_VerifyDefualtEmailIDInSubscription_C1375(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify user Email Id display by default  in subscription form.
        wait = WebDriverWait(driver, 90)
        # Click on Orders tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        time.sleep(1)
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Order Search
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Personal')))
        driver.find_element_by_link_text("Personal").click()
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Accounts Receivable')))
        driver.find_element_by_link_text("Accounts Receivable").click()
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_presort_job = "Personal Accounts Receivable Report"
        actual_header_presort_job = driver.find_element_by_id("content-header").text
        # Verify Create a Presort Job Header
        assert expected_header_presort_job in actual_header_presort_job

        # Click Advanced filters button
        # Click on Make a subscription button right side of the page.
        driver.find_element_by_class_name("btn-primary").click()
        # Verify the content on the subscription form
        time.sleep(1)
        expectedEmail  = "jstorey@ggoutfitters.com"
        actualEmail = driver.find_element_by_id("email").get_attribute("value")
        # Click on Back button at the bottom of the page.
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header = driver.find_element_by_id("content-header").text
        assert expectedEmail == actualEmail

        driver.find_element_by_class_name("btn-default").click()

    # ====================================1465==================21 March===========================================

    def test_AccountingUser_VerifyAdhocShipping_ReportSearchFunctionality_C1465(self, impersonate_accounting):
        # Reports/Ad-hoc/Shipping - Verify the search functionality in Reports.
        driver = impersonate_accounting['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Shipping')))
        time.sleep(1)
        driver.find_element_by_link_text("Shipping").click()
        time.sleep(1)
        expected_header_Shipping_Report = "Shipping Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Shipping_Report = driver.find_element_by_id("content-header").text
        # Verify Header
        assert expected_header_Shipping_Report in actual_header_Shipping_Report

        # Select the client from the drop down
        clients = driver.find_element_by_id("client_id")
        client_option = "AFNAVY"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Select the Ship Start  and ship end date
        driver.find_element_by_name("daterange").click()
        time.sleep(1)

        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("03/07/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("03/25/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)
        # Click on Generate report button.
        driver.find_element_by_class_name("btn-success").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
        time.sleep(3)
        # Wait until table is displayed dataTable
        wait.until(EC.presence_of_element_located((By.ID, 'dataTable')))
        # Count table rows
        rc = len(driver.find_element_by_id('dataTable').find_elements_by_tag_name('tr'))
        if int(rc) > 0:
            # Get first row First column value for filter
            trval = driver.find_element_by_id('dataTable').find_elements_by_class_name('sorting_1')
            assert driver.find_element_by_id("dataTable_filter").find_element_by_class_name("input-sm").is_displayed()
            driver.find_element_by_id("dataTable_filter").find_element_by_class_name("input-sm").send_keys(trval[0].text)
            time.sleep(2)
            filterInfo = driver.find_element_by_id('dataTable_info').text
            assert 'Showing 1 to 1' in filterInfo
            # Check no Matching in case of Failed search
            driver.find_element_by_id("dataTable_filter").find_element_by_class_name("input-sm").send_keys("Test123")
            time.sleep(2)
            Incorrectfiltermsg = driver.find_element_by_id('table_report').text
            assert 'No matching records found' in Incorrectfiltermsg

    # ====================================1466==================21 March===========================================

    def test_AccountingUser_VerifyAdhocShipping_Report_DisplayRecordFilters_C1466(self, impersonate_accounting):
        # Reports/Ad-hoc/Shipping-  Verify Displayed records filters 'Showing 1 to 'xx' of 'xxx' entries functionality
        driver = impersonate_accounting['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Shipping')))
        time.sleep(1)
        driver.find_element_by_link_text("Shipping").click()
        time.sleep(1)
        expected_header_Shipping_Report = "Shipping Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Shipping_Report = driver.find_element_by_id("content-header").text
        # Verify Header
        assert expected_header_Shipping_Report in actual_header_Shipping_Report

        # Select the client from the drop down
        clients = driver.find_element_by_id("client_id")
        client_option = "AFNAVY"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Select the Ship Start  and ship end date
        driver.find_element_by_name("daterange").click()
        time.sleep(1)

        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("03/07/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("03/25/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)
        # Click on Generate report button.
        driver.find_element_by_class_name("btn-success").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
        time.sleep(3)
        # Wait until table is displayed dataTable
        wait.until(EC.presence_of_element_located((By.ID, 'dataTable')))
        # Count table rows
        orderCount = len(driver.find_element_by_id('dataTable').find_elements_by_tag_name('tr'))
        if int(orderCount) > 0:
            # Check records Filters for All, 10,25,50,100
            if int(orderCount) >= 100:
                # Select 100 entries orders_table_length
                entry_sel = driver.find_element_by_name("dataTable_length")
                v_optsel = "100"
                for opt in entry_sel.find_elements_by_tag_name("option"):
                    if opt.text == v_optsel:
                        opt.click()
                        break
                time.sleep(3)
                srch_text = driver.find_element_by_id('dataTable_info').text
                time.sleep(1)
                assert 'Showing 1 to 100' in srch_text
            if int(orderCount) >= 50:
                # Select 50 entries orders_table_length
                entry_sel = driver.find_element_by_name("dataTable_length")
                v_optsel = "50"
                for opt in entry_sel.find_elements_by_tag_name("option"):
                    if opt.text == v_optsel:
                        opt.click()
                        break
                time.sleep(3)
                srch_text = driver.find_element_by_id('dataTable_info').text
                time.sleep(1)
                assert 'Showing 1 to 50' in srch_text
            if int(orderCount) >= 25:
                # Select 25 entries orders_table_length
                entry_sel = driver.find_element_by_name("dataTable_length")
                v_optsel = "25"
                for opt in entry_sel.find_elements_by_tag_name("option"):
                    if opt.text == v_optsel:
                        opt.click()
                        break
                time.sleep(3)
                srch_text = driver.find_element_by_id('dataTable_info').text
                time.sleep(1)
                assert 'Showing 1 to 25' in srch_text
            if int(orderCount) >= 10:
                # Select 10 entries orders_table_length
                entry_sel = driver.find_element_by_name("dataTable_length")
                v_optsel = "10"
                for opt in entry_sel.find_elements_by_tag_name("option"):
                    if opt.text == v_optsel:
                        opt.click()
                        break
                time.sleep(3)
                srch_text = driver.find_element_by_id('dataTable_info').text
                time.sleep(1)
                assert 'Showing 1 to 10' in srch_text
                # Select ALL entries orders_table_length
                entry_sel = driver.find_element_by_name("dataTable_length")
                v_optsel = "All"
                for opt in entry_sel.find_elements_by_tag_name("option"):
                    if opt.text == v_optsel:
                        opt.click()
                        break
                time.sleep(3)
                srch_text = driver.find_element_by_id('dataTable_info').text
                time.sleep(1)
                Sprecs = srch_text.split(" ")
                # Check 4th and 6th values are same for All option
                assert Sprecs[3] == Sprecs[5]
        else:
                print("Insufficient records  to validate filters")

    # ====================================1382==================21 march===========================================
    def test_AccountingUser_CollectionLog_VerifygeneratedReportFunctionality_C1382(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify the generate report button functionality.
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        time.sleep(2)
        driver.find_element_by_link_text("Reports").click()
        time.sleep(2)
        # Click on Personal
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Personal')))
        driver.find_element_by_link_text("Personal").click()
        time.sleep(2)

        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Collections Log')))
        driver.find_element_by_link_text("Collections Log").click()
        time.sleep(2)

        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header = "Collections Log"
        actual_header = driver.find_element_by_id("content-header").text
        # Verify Header.
        assert expected_header in actual_header

        # Select the client from the drop down
        wait.until(EC.visibility_of_element_located((By.ID, 'sales_rep')))
        clients = driver.find_element_by_id("sales_rep")
        client_option = "Gibson, Monica"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break

        # Click on Make a subscription button right side of the page.
        driver.find_element_by_id("sub_btn").click()
        time.sleep(3)
        wait.until(EC.visibility_of_element_located((By.ID, 'table_report')))
        assert driver.find_element_by_id("table_report").is_displayed()

    # ====================================1383==================21 march===========================================
    def test_AccountingUser_CollectionLog_VerifymakeSubscriptionFunctionality_C1383(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify the make a subscription button functionality.
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        time.sleep(2)
        driver.find_element_by_link_text("Reports").click()
        time.sleep(2)
        # Click on Personal
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Personal')))
        driver.find_element_by_link_text("Personal").click()
        time.sleep(2)

        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Collections Log')))
        driver.find_element_by_link_text("Collections Log").click()
        time.sleep(2)

        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header = "Collections Log"
        actual_header = driver.find_element_by_id("content-header").text
        # Verify Header.
        assert expected_header in actual_header

        # Select the client from the drop down
        wait.until(EC.visibility_of_element_located((By.ID, 'sales_rep')))
        clients = driver.find_element_by_id("sales_rep")
        client_option = "Gibson, Monica"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break

        # Click on Make a subscription button right side of the page.
        driver.find_element_by_id("sub_btn").click()
        time.sleep(3)
        wait.until(EC.visibility_of_element_located((By.ID, 'table_report')))
        assert driver.find_element_by_id("table_report").is_displayed()
        # Click Subscription
        driver.find_element_by_id("table_report").find_element_by_class_name("btn-primary").click()
        time.sleep(2)

        expected_header = "Subscription for: Collections Log"
        wait.until(EC.visibility_of_element_located((By.ID, 'subscriptionsModalLabel')))
        actual_header = driver.find_element_by_id("subscriptionsModalLabel").text
        # Verify Header
        assert expected_header in actual_header
        # Click Back
        driver.find_element_by_class_name('btn-default').click()
        time.sleep(1)

    # ====================================1384==================21March===========================================

    def test_AccountingUser_CollectionLog_VerifyContentInSubscription_C1384(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify the content in Subscription for: Collections Log pop up.
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        time.sleep(2)
        driver.find_element_by_link_text("Reports").click()
        time.sleep(2)
        # Click on Personal
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Personal')))
        driver.find_element_by_link_text("Personal").click()
        time.sleep(2)

        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Collections Log')))
        driver.find_element_by_link_text("Collections Log").click()
        time.sleep(2)

        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header = "Collections Log"
        actual_header = driver.find_element_by_id("content-header").text
        # Verify Header.
        assert expected_header in actual_header

        # Select the client from the drop down
        wait.until(EC.visibility_of_element_located((By.ID, 'sales_rep')))
        clients = driver.find_element_by_id("sales_rep")
        client_option = "Gibson, Monica"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break

        # Click on Make a subscription button right side of the page.
        driver.find_element_by_id("sub_btn").click()
        time.sleep(3)
        wait.until(EC.visibility_of_element_located((By.ID, 'table_report')))
        assert driver.find_element_by_id("table_report").is_displayed()

        driver.find_element_by_id("table_report").find_element_by_class_name("btn-primary").click()
        time.sleep(2)

        expected_header = "Subscription for: Collections Log"
        wait.until(EC.visibility_of_element_located((By.ID, 'subscriptionsModalLabel')))
        actual_header = driver.find_element_by_id("subscriptionsModalLabel").text
        # Verify Header
        assert expected_header in actual_header

        # Verify Subscription Name
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
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
        actual_days = driver.find_elements_by_class_name("checkbox")
        time.sleep(2)
        for day in actual_days:
            name = day.text
            assert name in expected_days
        # Verify back button
        assert driver.find_element_by_class_name("btn-default").is_displayed()
        # Verify save Subscription button
        assert driver.find_element_by_id("next_btn").is_displayed()
        driver.find_element_by_class_name("btn-default").click()

    # ====================================1385==================21 march===========================================
    def test_AccountingUser_CollectionLog_VerifySaveSubscriptionFuntionality_C1385(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        #  Verify the save Subscription functionality in Subscription for: Collections Log pop up.
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        time.sleep(2)
        driver.find_element_by_link_text("Reports").click()
        time.sleep(2)
        # Click on Personal
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Personal')))
        driver.find_element_by_link_text("Personal").click()
        time.sleep(2)

        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Collections Log')))
        driver.find_element_by_link_text("Collections Log").click()
        time.sleep(2)

        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header = "Collections Log"
        actual_header = driver.find_element_by_id("content-header").text
        # Verify Header.
        assert expected_header in actual_header

        # Select the client from the drop down
        wait.until(EC.visibility_of_element_located((By.ID, 'sales_rep')))
        clients = driver.find_element_by_id("sales_rep")
        client_option = "Gibson, Monica"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break

        # Click on Make a subscription button right side of the page.
        driver.find_element_by_id("sub_btn").click()
        time.sleep(3)
        wait.until(EC.visibility_of_element_located((By.ID, 'table_report')))
        assert driver.find_element_by_id("table_report").is_displayed()

        driver.find_element_by_id("table_report").find_element_by_class_name("btn-primary").click()
        time.sleep(2)

        expected_header = "Subscription for: Collections Log"
        wait.until(EC.visibility_of_element_located((By.ID, 'subscriptionsModalLabel')))
        actual_header = driver.find_element_by_id("subscriptionsModalLabel").text
        # Verify Header
        assert expected_header in actual_header

        time.sleep(2)
        random_number = str(randint(10, 999))
        name = "TTSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        # Click on Back button at the bottom of the page.
        driver.find_element_by_id("next_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'noty_text')))
        # Subscription form submitted successfully and display message Subscription Saved.
        expected_message = "Subscription saved."
        actual_message = driver.find_element_by_class_name("noty_text").text
        assert expected_message in actual_message
        # Subscription should be display in subscriptions page with correct data.
        driver.find_element_by_link_text("Subscriptions").click()
        time.sleep(2)
        NameNew_value = driver.find_element_by_id("jobs_table").text
        assert name in NameNew_value

    # ====================================1386==================21 march===========================================
    def test_AccountingUser_CollectionLog_VerifyBackButtonFunctionalityInSubscription_C1386(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify the back button functionality in Subscription for: Collections Log pop up.
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        time.sleep(2)
        driver.find_element_by_link_text("Reports").click()
        time.sleep(2)
        # Click on Personal
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Personal')))
        driver.find_element_by_link_text("Personal").click()
        time.sleep(2)

        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Collections Log')))
        driver.find_element_by_link_text("Collections Log").click()
        time.sleep(2)


        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header = "Collections Log"
        actual_header = driver.find_element_by_id("content-header").text
        # Verify Header.
        assert expected_header in actual_header

        # Select the client from the drop down
        wait.until(EC.visibility_of_element_located((By.ID, 'sales_rep')))
        clients = driver.find_element_by_id("sales_rep")
        client_option = "Gibson, Monica"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break

        # Click on Make a subscription button right side of the page.
        driver.find_element_by_id("sub_btn").click()
        time.sleep(3)
        wait.until(EC.visibility_of_element_located((By.ID, 'table_report')))
        assert driver.find_element_by_id("table_report").is_displayed()

        driver.find_element_by_id("table_report").find_element_by_class_name("btn-primary").click()
        time.sleep(2)

        expected_header = "Subscription for: Collections Log"
        wait.until(EC.visibility_of_element_located((By.ID, 'subscriptionsModalLabel')))
        actual_header = driver.find_element_by_id("subscriptionsModalLabel").text
        # Verify Header
        assert expected_header in actual_header

        time.sleep(2)
        random_number = str(randint(10, 999))
        name = "TTSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        # Click on Back button at the bottom of the page.
        driver.find_element_by_class_name("btn-default").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        # User should redirect Report page.
        expected_header = "Collections Log"
        actual_header = driver.find_element_by_id("content-header").text
        assert expected_header in actual_header
        assert driver.find_element_by_id("sub_name").is_displayed() == 0

    # ====================================1388==================21March===========================================

    def test_AccountingUser_CollectionLog_VerifyBlankFieldNotSubmittedInSubscription_C1388(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify with blank fields subscription form not submitted.
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        time.sleep(2)
        driver.find_element_by_link_text("Reports").click()
        time.sleep(2)
        # Click on Personal
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Personal')))
        driver.find_element_by_link_text("Personal").click()
        time.sleep(2)

        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Collections Log')))
        driver.find_element_by_link_text("Collections Log").click()
        time.sleep(2)

        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header = "Collections Log"
        actual_header = driver.find_element_by_id("content-header").text
        # Verify Header.
        assert expected_header in actual_header

        # Select the client from the drop down
        wait.until(EC.visibility_of_element_located((By.ID, 'sales_rep')))
        clients = driver.find_element_by_id("sales_rep")
        client_option = "Gibson, Monica"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break

        # Click on Make a subscription button right side of the page.
        driver.find_element_by_id("sub_btn").click()
        time.sleep(3)
        wait.until(EC.visibility_of_element_located((By.ID, 'table_report')))
        assert driver.find_element_by_id("table_report").is_displayed()

        driver.find_element_by_id("table_report").find_element_by_class_name("btn-primary").click()
        time.sleep(2)

        expected_header = "Subscription for: Collections Log"
        wait.until(EC.visibility_of_element_located((By.ID, 'subscriptionsModalLabel')))
        actual_header = driver.find_element_by_id("subscriptionsModalLabel").text
        # Verify Header
        assert expected_header in actual_header

        # Click on Back button at the bottom of the page.
        driver.find_element_by_id("next_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'noty_text')))
        # Subscription form submitted successfully and display message Subscription Saved.
        expected_message = "Please Fill Out Fields Properly"
        actual_message = driver.find_element_by_class_name("noty_text").text
        assert expected_message in actual_message

    # ====================================1387==================21 march===========================================

    def test_AccountingUser_CollectionLog_VerifyContentInReport_C1387(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify the content of generated report.
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        time.sleep(2)
        driver.find_element_by_link_text("Reports").click()
        time.sleep(2)
        # Click on Personal
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Personal')))
        driver.find_element_by_link_text("Personal").click()
        time.sleep(2)

        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Collections Log')))
        driver.find_element_by_link_text("Collections Log").click()
        time.sleep(2)

        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header = "Collections Log"
        actual_header = driver.find_element_by_id("content-header").text
        # Verify Header.
        assert expected_header in actual_header

        # Select the client from the drop down
        wait.until(EC.visibility_of_element_located((By.ID, 'sales_rep')))
        clients = driver.find_element_by_id("sales_rep")
        client_option = "Gibson, Monica"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break

        # Click on Make a subscription button right side of the page.
        driver.find_element_by_id("sub_btn").click()
        time.sleep(3)
        wait.until(EC.visibility_of_element_located((By.ID, 'table_report')))
        assert driver.find_element_by_id("table_report").is_displayed()

        # Select the client from the drop down
        actual = driver.find_element_by_class_name('table-striped').find_elements_by_tag_name('th')
        expected_OrdTable = ['Company Name','Company No.','PRO01 Invoice','PRO01 Balance','PRO06 Invoice','PRO06 Balance','PRO10 Invoice','PRO10 Balance','Most Recent Note','Author','Text']
        size = len(actual)
        if int(size) > 0:
            for i in range(size):
                print(actual[i].text)
                assert actual[i].text in expected_OrdTable
        time.sleep(1)

        assert driver.find_element_by_name("dataTable_length").is_displayed()
        assert driver.find_element_by_id("dataTable_filter").find_element_by_class_name("input-sm").is_displayed()
        assert driver.find_element_by_class_name("btn-primary").is_displayed()
        assert driver.find_element_by_id("dataTable_info").is_displayed()

    # ====================================1380==================21 march===========================================

    def test_AccountingUser_CollectionLog_VerifyContent_C1380(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify the content on "Collections log " page.
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        time.sleep(2)
        driver.find_element_by_link_text("Reports").click()
        time.sleep(2)
        # Click on Personal
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Personal')))
        driver.find_element_by_link_text("Personal").click()
        time.sleep(2)

        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Collections Log')))
        driver.find_element_by_link_text("Collections Log").click()
        time.sleep(2)

        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header = "Collections Log"
        actual_header = driver.find_element_by_id("content-header").text
        # Verify Header.
        assert expected_header in actual_header

        assert driver.find_element_by_id("requested_invoice_age").is_displayed()
        assert driver.find_element_by_id("sales_rep").is_displayed()
        assert driver.find_element_by_class_name("btn-info").is_displayed()
        assert driver.find_element_by_id("sub_btn").is_displayed()


    # ====================================1467==================22 March===========================================

    def test_AccountingUser_VerifyAdhocShipping_ReportSortFunctionality_C1467(self, impersonate_accounting):
        # Reports/Ad-hoc/Shipping - Verify the sorting functionality in report generated
        driver = impersonate_accounting['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Shipping')))
        time.sleep(1)
        driver.find_element_by_link_text("Shipping").click()
        time.sleep(1)
        expected_header_Shipping_Report = "Shipping Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Shipping_Report = driver.find_element_by_id("content-header").text
        # Verify Header
        assert expected_header_Shipping_Report in actual_header_Shipping_Report

        # Select the client from the drop down
        clients = driver.find_element_by_id("client_id")
        client_option = "AFNAVY"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Select the Ship Start  and ship end date
        driver.find_element_by_name("daterange").click()
        time.sleep(1)

        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("03/07/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("03/25/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)
        # Click on Generate report button.
        driver.find_element_by_class_name("btn-success").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
        time.sleep(3)
        # Wait until table is displayed dataTable
        wait.until(EC.presence_of_element_located((By.ID, 'dataTable')))
        # Count table rows
        orderCount = len(driver.find_element_by_id('dataTable').find_elements_by_tag_name('tr'))
        if int(orderCount) > 0:
            # Get Headers  of displayed columns data-column-index
            testhdrs = driver.find_element_by_class_name('dataTable').find_elements_by_tag_name('th')
            # Verify sorting for 10 Columns
            for i in range(0, 10):
                time.sleep(1)
                # Ascending Order check
                if int(i) > 0:
                    testhdrs[i].click()
                    time.sleep(1)
                asc_order = testhdrs[i].get_attribute("aria-sort")
                assert asc_order in "ascending"
                # Descending check
                testhdrs[i].click()
                time.sleep(1)
                desc_order = testhdrs[i].get_attribute("aria-sort")
                assert desc_order in "descending"

    # ====================================1468==================22 March===========================================

    def test_AccountingUser_VerifyAdhocShipping_ReportPaginationFunctionality_C1468(self, impersonate_accounting):
        # Reports/Ad-hoc/Shipping - Verify the pagination functionality
        driver = impersonate_accounting['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Shipping')))
        time.sleep(1)
        driver.find_element_by_link_text("Shipping").click()
        time.sleep(1)
        expected_header_Shipping_Report = "Shipping Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Shipping_Report = driver.find_element_by_id("content-header").text
        # Verify Header
        assert expected_header_Shipping_Report in actual_header_Shipping_Report

        # Select the client from the drop down
        clients = driver.find_element_by_id("client_id")
        client_option = "AFNAVY"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Select the Ship Start  and ship end date
        driver.find_element_by_name("daterange").click()
        time.sleep(1)

        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("03/07/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("03/25/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)
        # Click on Generate report button.
        driver.find_element_by_class_name("btn-success").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
        time.sleep(3)
        # Wait until table is displayed dataTable
        wait.until(EC.presence_of_element_located((By.ID, 'dataTable')))
        # Count table rows
        orderCount = len(driver.find_element_by_id('dataTable').find_elements_by_tag_name('tr'))
        if int(orderCount) > 0:
            # Verify Pagination controls Previous Button, current page
            print(int(orderCount))
            disabled_prev = driver.find_element_by_id("dataTable_previous").get_attribute("class")
            assert disabled_prev == "paginate_button previous disabled"
            # verify current page
            btn_elem = driver.find_elements_by_class_name('paginate_button')
            print(btn_elem[1].text)
            assert btn_elem[1].text == '1'
            # Click Next paginate_button next
            if driver.find_element_by_link_text('Next').is_enabled():
                driver.find_element_by_link_text('Next').click()
                time.sleep(2)
                # Check active page number after clicking Next
                btn_elem = driver.find_elements_by_class_name('paginate_button')
                bt_new = btn_elem[2].get_attribute("class")
                assert bt_new == 'paginate_button active'
                # Go to last page and check Next is disabled - keep clicking next until disabled
                cls_btn_next = driver.find_element_by_id("dataTable_next").get_attribute("class")
                while cls_btn_next == "paginate_button next":
                    driver.find_element_by_link_text('Next').click()
                    time.sleep(2)
                    cls_btn_next = driver.find_element_by_id("dataTable_next").get_attribute("class")
                # Verify Next is disabled
                assert cls_btn_next == "paginate_button next disabled"
                time.sleep(1)

    # ====================================16512==================22March===========================================

    def test_AccountingUser_VerifyAdhocKitting_ReportSearchFunctionality_C16512(self, impersonate_accounting):
        # Reports/Ad-hoc/Kitting - Verify the search functionality in Reports.
        driver = impersonate_accounting['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Kitting')))
        time.sleep(1)
        driver.find_element_by_link_text("Kitting").click()
        time.sleep(1)
        expected_header_Kitting_Report = "Kitting Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Kitting_Report = driver.find_element_by_id("content-header").text
        # Verify Header
        assert expected_header_Kitting_Report in actual_header_Kitting_Report

        # Select the client from the drop down
        clients = driver.find_element_by_id("client_id")
        client_option = "AFNAVY"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Select the Ship Start  and ship end date
        driver.find_element_by_name("daterange").click()
        time.sleep(1)

        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("03/07/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("03/25/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)
        # Click on Generate report button.
        driver.find_element_by_class_name("btn-success").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
        time.sleep(3)
        # Wait until table is displayed dataTable
        wait.until(EC.presence_of_element_located((By.ID, 'dataTable')))
        # Count table rows
        rc = len(driver.find_element_by_id('dataTable').find_elements_by_tag_name('tr'))
        # if no records exist - rowcount is 2
        if int(rc) > 2:
            # Get first row First column value for filter
            trval = driver.find_element_by_id('dataTable').find_elements_by_class_name('sorting_1')
            assert driver.find_element_by_id("dataTable_filter").find_element_by_class_name("input-sm").is_displayed()
            driver.find_element_by_id("dataTable_filter").find_element_by_class_name("input-sm").send_keys(trval[0].text)
            time.sleep(2)
            filterInfo = driver.find_element_by_id('dataTable_info').text
            assert 'Showing 1 to 1' in filterInfo
            # Check no Matching in case of Failed search
            driver.find_element_by_id("dataTable_filter").find_element_by_class_name("input-sm").send_keys("Test123")
            time.sleep(2)
            Incorrectfiltermsg = driver.find_element_by_id('table_report').text
            assert 'No matching records found' in Incorrectfiltermsg

    # ====================================16513==================22March===========================================

    def test_AccountingUser_VerifyAdhocKitting_Report_DisplayRecordFilters_C16513(self, impersonate_accounting):
        # Reports/Ad-hoc/Kitting-  Verify Displayed records filters 'Showing 1 to 'xx' of 'xxx' entries functionality
        driver = impersonate_accounting['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Kitting')))
        time.sleep(1)
        driver.find_element_by_link_text("Kitting").click()
        time.sleep(1)
        expected_header_Kitting_Report = "Kitting Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Kitting_Report = driver.find_element_by_id("content-header").text
        # Verify Header
        assert expected_header_Kitting_Report in actual_header_Kitting_Report

        # Select the client from the drop down
        clients = driver.find_element_by_id("client_id")
        client_option = "AFNAVY"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Select the Ship Start  and ship end date
        driver.find_element_by_name("daterange").click()
        time.sleep(1)

        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("03/07/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("03/25/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)
        # Click on Generate report button.
        driver.find_element_by_class_name("btn-success").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
        time.sleep(3)
        # Wait until table is displayed dataTable
        wait.until(EC.presence_of_element_located((By.ID, 'dataTable')))
        # Count table rows
        orderCount = len(driver.find_element_by_id('dataTable').find_elements_by_tag_name('tr'))
        if int(orderCount) > 2:
            # Check records Filters for All, 10,25,50,100
            if int(orderCount) > 100:
                # Select 100 entries orders_table_length
                entry_sel = driver.find_element_by_name("dataTable_length")
                v_optsel = "100"
                for opt in entry_sel.find_elements_by_tag_name("option"):
                    if opt.text == v_optsel:
                        opt.click()
                        break
                time.sleep(3)
                srch_text = driver.find_element_by_id('dataTable_info').text
                time.sleep(1)
                assert 'Showing 1 to 100' in srch_text
            if int(orderCount) > 50:
                # Select 50 entries orders_table_length
                entry_sel = driver.find_element_by_name("dataTable_length")
                v_optsel = "50"
                for opt in entry_sel.find_elements_by_tag_name("option"):
                    if opt.text == v_optsel:
                        opt.click()
                        break
                time.sleep(3)
                srch_text = driver.find_element_by_id('dataTable_info').text
                time.sleep(1)
                assert 'Showing 1 to 50' in srch_text
            if int(orderCount) > 25:
                # Select 25 entries orders_table_length
                entry_sel = driver.find_element_by_name("dataTable_length")
                v_optsel = "25"
                for opt in entry_sel.find_elements_by_tag_name("option"):
                    if opt.text == v_optsel:
                        opt.click()
                        break
                time.sleep(3)
                srch_text = driver.find_element_by_id('dataTable_info').text
                time.sleep(1)
                assert 'Showing 1 to 25' in srch_text
            if int(orderCount) > 10:
                # Select 10 entries orders_table_length
                entry_sel = driver.find_element_by_name("dataTable_length")
                v_optsel = "10"
                for opt in entry_sel.find_elements_by_tag_name("option"):
                    if opt.text == v_optsel:
                        opt.click()
                        break
                time.sleep(3)
                srch_text = driver.find_element_by_id('dataTable_info').text
                time.sleep(1)
                assert 'Showing 1 to 10' in srch_text
                # Select ALL entries orders_table_length
                entry_sel = driver.find_element_by_name("dataTable_length")
                v_optsel = "All"
                for opt in entry_sel.find_elements_by_tag_name("option"):
                    if opt.text == v_optsel:
                        opt.click()
                        break
                time.sleep(3)
                srch_text = driver.find_element_by_id('dataTable_info').text
                time.sleep(1)
                Sprecs = srch_text.split(" ")
                # Check 4th and 6th values are same for All option
                assert Sprecs[3] == Sprecs[5]
        else:
                print("Insufficient records  to validate filters")


    # ====================================16514==================22 March===========================================

    def test_AccountingUser_VerifyAdhocKitting_ReportSortFunctionality_C16514(self, impersonate_accounting):
        # Reports/Ad-hoc/Kitting - Verify the sorting functionality in report generated
        driver = impersonate_accounting['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Kitting')))
        time.sleep(1)
        driver.find_element_by_link_text("Kitting").click()
        time.sleep(1)
        expected_header_Kitting_Report = "Kitting Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Kitting_Report = driver.find_element_by_id("content-header").text
        # Verify Header
        assert expected_header_Kitting_Report in actual_header_Kitting_Report

        # Select the client from the drop down
        clients = driver.find_element_by_id("client_id")
        client_option = "AFNAVY"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Select the Ship Start  and ship end date
        driver.find_element_by_name("daterange").click()
        time.sleep(1)

        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("03/07/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("03/25/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)
        # Click on Generate report button.
        driver.find_element_by_class_name("btn-success").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
        time.sleep(3)
        # Wait until table is displayed dataTable
        wait.until(EC.presence_of_element_located((By.ID, 'dataTable')))
        # Count table rows
        orderCount = len(driver.find_element_by_id('dataTable').find_elements_by_tag_name('tr'))
        if int(orderCount) > 1:
            # Get Headers  of displayed columns data-column-index
            testhdrs = driver.find_element_by_class_name('dataTable').find_elements_by_tag_name('th')
            # Verify sorting for 3 Columns
            for i in range(0, 3):
                time.sleep(1)
                # Ascending Order check
                if int(i) > 0:
                    testhdrs[i].click()
                    time.sleep(1)
                asc_order = testhdrs[i].get_attribute("aria-sort")
                assert asc_order in "ascending"
                # Descending check
                testhdrs[i].click()
                time.sleep(1)
                desc_order = testhdrs[i].get_attribute("aria-sort")
                assert desc_order in "descending"

    # ====================================16515==================22 March===========================================

    def test_AccountingUser_VerifyAdhocKitting_ReportPaginationFunctionality_C16515(self, impersonate_accounting):
        # Reports/Ad-hoc/Kitting - Verify the pagination functionality
        driver = impersonate_accounting['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Kitting')))
        time.sleep(1)
        driver.find_element_by_link_text("Kitting").click()
        time.sleep(1)
        expected_header_Kitting_Report = "Kitting Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Kitting_Report = driver.find_element_by_id("content-header").text
        # Verify Header
        assert expected_header_Kitting_Report in actual_header_Kitting_Report

        # Select the client from the drop down
        clients = driver.find_element_by_id("client_id")
        client_option = "AFNAVY"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Select the Ship Start  and ship end date
        driver.find_element_by_name("daterange").click()
        time.sleep(1)

        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("03/07/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("03/25/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)
        # Click on Generate report button.
        driver.find_element_by_class_name("btn-success").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
        time.sleep(3)
        # Wait until table is displayed dataTable
        wait.until(EC.presence_of_element_located((By.ID, 'dataTable')))
        # Count table rows
        orderCount = len(driver.find_element_by_id('dataTable').find_elements_by_tag_name('tr'))
        # if record count is more than 2 , data exists
        if int(orderCount) > 2:
            # Verify Pagination controls Previous Button, current page
            print(int(orderCount))
            disabled_prev = driver.find_element_by_id("dataTable_previous").get_attribute("class")
            assert disabled_prev == "paginate_button previous disabled"
            # verify current page
            btn_elem = driver.find_elements_by_class_name('paginate_button')
            print(btn_elem[1].text)
            assert btn_elem[1].text == '1'
            # Click Next paginate_button next
            if driver.find_element_by_link_text('Next').is_enabled():
                driver.find_element_by_link_text('Next').click()
                time.sleep(2)
                # Check active page number after clicking Next
                btn_elem = driver.find_elements_by_class_name('paginate_button')
                bt_new = btn_elem[2].get_attribute("class")
                assert bt_new == 'paginate_button active'
                # Go to last page and check Next is disabled - keep clicking next until disabled
                cls_btn_next = driver.find_element_by_id("dataTable_next").get_attribute("class")
                while cls_btn_next == "paginate_button next":
                    driver.find_element_by_link_text('Next').click()
                    time.sleep(2)
                    cls_btn_next = driver.find_element_by_id("dataTable_next").get_attribute("class")
                # Verify Next is disabled
                assert cls_btn_next == "paginate_button next disabled"
                time.sleep(1)

    # ====================================16517==================22march===========================================

    def test_AccountingUser_Kitting_VerifySaveButtonFunctionalityInSubscription_C16517(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Reports/Ad-hoc/Kitting- Verify the save Subscription functionality in Subscription for: Client name Kitting pop up.
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Kitting')))
        time.sleep(1)
        driver.find_element_by_link_text("Kitting").click()
        time.sleep(1)
        expected_header_Kitting_Report = "Kitting Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Kitting_Report = driver.find_element_by_id("content-header").text
        # Verify Header
        assert expected_header_Kitting_Report in actual_header_Kitting_Report

        # Select the client from the drop down
        clients = driver.find_element_by_id("client_id")
        client_option = "ARA"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Select the Ship Start  and ship end date
        driver.find_element_by_name("daterange").click()
        time.sleep(1)

        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("03/11/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("03/25/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)
        # Click on Generate report button.
        driver.find_element_by_class_name("btn-success").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
        time.sleep(1)
        assert driver.find_element_by_id("table_report").is_displayed()
        # Open Subscription
        driver.find_element_by_id("table_report").find_element_by_class_name("btn-primary").click()
        time.sleep(1)

        expected_header = "Subscription for: ARA Kitting Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'subscriptionsModalLabel')))
        actual_header = driver.find_element_by_id("subscriptionsModalLabel").text
        # Verify Header
        assert expected_header in actual_header

        time.sleep(1)
        random_number = str(randint(10, 999))
        name = "TestSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        # Click on Back button at the bottom of the page.
        driver.find_element_by_id("next_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'noty_text')))
        # Subscription form submitted successfully and display message Subscription Saved.
        expected_message = "Subscription saved."
        actual_message = driver.find_element_by_class_name("noty_text").text
        assert expected_message in actual_message
        # Subscription should be display in subscriptions page with correct data.
        driver.find_element_by_link_text("Subscriptions").click()
        time.sleep(1)
        NameNew_value = driver.find_element_by_id("jobs_table").text
        assert name in NameNew_value

    # ====================================16518======================22March===========================================

    def test_AccountingUser_Kitting_VerifyBackButtonFunctionalityInSubscription_C16518(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Reports/Ad-hoc/Kitting -Verify the back button functionality in Subscription for: Client name Kitting pop up should be displayed.
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Kitting')))
        time.sleep(1)
        driver.find_element_by_link_text("Kitting").click()
        time.sleep(1)
        expected_header_Kitting_Report = "Kitting Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Kitting_Report = driver.find_element_by_id("content-header").text
        # Verify Header
        assert expected_header_Kitting_Report in actual_header_Kitting_Report

        # Select the client from the drop down
        clients = driver.find_element_by_id("client_id")
        client_option = "AFNAVY"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Select the Ship Start  and ship end date
        driver.find_element_by_name("daterange").click()
        time.sleep(1)

        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("03/11/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("03/12/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)
        # Click on Generate report button.
        driver.find_element_by_class_name("btn-success").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
        time.sleep(1)
        assert driver.find_element_by_id("table_report").is_displayed()
        # Open Subscription
        driver.find_element_by_id("table_report").find_element_by_class_name("btn-primary").click()
        time.sleep(1)

        expected_header = "Subscription for: AFNAVY Kitting Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'subscriptionsModalLabel')))
        actual_header = driver.find_element_by_id("subscriptionsModalLabel").text
        # Verify Header
        assert expected_header in actual_header
        time.sleep(1)

        random_number = str(randint(10, 999))
        name = "TestSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        # Click on Back button at the bottom of the page.
        driver.find_element_by_class_name("btn-default").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        # User should redirect Report page.
        expected_header = "Kitting Report"
        actual_header = driver.find_element_by_id("content-header").text
        assert expected_header in actual_header
        assert driver.find_element_by_id("sub_name").is_displayed() == 0

    # ====================================16521==================22March===========================================

    def test_AccountingUser_Settlement_VerifyMakeSubscriptionFunctionality_C16521(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Reports/Ad-hoc/Settlement - Verify the functionality of make a subscription button for the generated report on Settlement page.
        wait = WebDriverWait(driver, 90)
        # Verify Report Tab Visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Settlement')))
        driver.find_element_by_link_text("Settlement").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Settlement_Report = "Settlement Report"
        time.sleep(1)
        actual_header_Settlement_Report = driver.find_element_by_id("content-header").text
        # Verify  Header
        assert expected_header_Settlement_Report in actual_header_Settlement_Report

        # Select the client from the drop down
        clients = driver.find_element_by_id("client_id")
        client_option = "AFNAVY"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Select the Ship Start  and ship end date
        driver.find_element_by_name("daterange").click()
        #driver.find_element_by_name('daterangepicker_start').send_keys()
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
        driver.find_element_by_class_name("btn-success").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
        time.sleep(2)

        assert driver.find_element_by_id("table_report").is_displayed()
        # Click Subscription
        driver.find_element_by_id("table_report").find_element_by_class_name("btn-primary").click()
        time.sleep(1)

        expected_header = "Subscription for: AFNAVY Settlement Summary Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'subscriptionsModalLabel')))
        actual_header = driver.find_element_by_id("subscriptionsModalLabel").text
        # Verify Header
        assert expected_header in actual_header
        # Click Back
        driver.find_element_by_class_name('btn-default').click()
        time.sleep(1)

    # ====================================16522==================22March===========================================

    def test_AccountingUser_Settlement_verifyExcelandSubscriptionButton_C16522(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Reports/Ad-hoc/Settlement - Verify the visibility of Excel/Make Subscription button on the report generated.
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Settlement')))
        driver.find_element_by_link_text("Settlement").click()

        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Settlement_Report = "Settlement Report"
        time.sleep(1)
        actual_header_Settlement_Report = driver.find_element_by_id("content-header").text
        # Verify  Header
        assert expected_header_Settlement_Report in actual_header_Settlement_Report

        # Select the client from the drop down
        clients = driver.find_element_by_id("client_id")
        client_option = "AFNAVY"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Select the date range
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
        driver.find_element_by_class_name("btn-success").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
        time.sleep(2)

        # Verify Make a Subscription and Excel button displayed on the report
        assert driver.find_element_by_id("table_report").find_element_by_class_name("btn-primary").is_displayed()
        assert driver.find_element_by_id("table_report").find_element_by_id("xls_btn").is_displayed()

    # ====================================16524==================23March===========================================

    def test_AccountingUser_VerifyAdhocSettlement_ReportSearchFunctionality_C16524(self, impersonate_accounting):
        # Reports/Ad-hoc/Settlement - Verify the search functionality in Reports.
        driver = impersonate_accounting['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Settlement')))
        time.sleep(1)
        driver.find_element_by_link_text("Settlement").click()
        time.sleep(1)
        expected_header_Settlement_Report = "Settlement Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Settlement_Report = driver.find_element_by_id("content-header").text
        # Verify Header
        assert expected_header_Settlement_Report in actual_header_Settlement_Report

        # Select the client from the drop down
        clients = driver.find_element_by_id("client_id")
        client_option = "AFNAVY"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Select the Ship Start  and ship end date
        driver.find_element_by_name("daterange").click()
        time.sleep(1)

        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("03/07/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("03/25/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)
        # Click on Generate report button.
        driver.find_element_by_class_name("btn-success").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
        time.sleep(3)
        # Wait until table is displayed dataTable
        wait.until(EC.presence_of_element_located((By.ID, 'dataTable')))
        # Count table rows
        rc = len(driver.find_element_by_id('dataTable').find_elements_by_tag_name('tr'))
        # if no records exist - rowcount is more than 3
        if int(rc) > 3:
            # Get first row First column value for filter
            trval = driver.find_element_by_id('dataTable').find_elements_by_class_name('sorting_1')
            assert driver.find_element_by_id("dataTable_filter").find_element_by_class_name("input-sm").is_displayed()
            driver.find_element_by_id("dataTable_filter").find_element_by_class_name("input-sm").send_keys(trval[0].text)
            time.sleep(2)
            filterInfo = driver.find_element_by_id('dataTable_info').text
            assert 'Showing 1 to 1' in filterInfo
            # Check no Matching in case of Failed search
            driver.find_element_by_id("dataTable_filter").find_element_by_class_name("input-sm").send_keys("Test123")
            time.sleep(2)
            Incorrectfiltermsg = driver.find_element_by_id('table_report').text
            assert 'No matching records found' in Incorrectfiltermsg

    # ====================================16525==================23March===========================================

    def test_AccountingUser_VerifyAdhocSettlement_Report_DisplayRecordFilters_C16525(self, impersonate_accounting):
        # Reports/Ad-hoc/Settlement-  Verify Displayed records filters 'Showing 1 to 'xx' of 'xxx' entries functionality
        driver = impersonate_accounting['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Settlement')))
        time.sleep(1)
        driver.find_element_by_link_text("Settlement").click()
        time.sleep(1)
        expected_header_Settlement_Report = "Settlement Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Settlement_Report = driver.find_element_by_id("content-header").text
        # Verify Header
        assert expected_header_Settlement_Report in actual_header_Settlement_Report

        # Select the client from the drop down
        clients = driver.find_element_by_id("client_id")
        client_option = "AFNAVY"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Select the Ship Start  and ship end date
        driver.find_element_by_name("daterange").click()
        time.sleep(1)

        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("03/07/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("03/25/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)
        # Click on Generate report button.
        driver.find_element_by_class_name("btn-success").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
        time.sleep(3)
        # Wait until table is displayed dataTable
        wait.until(EC.presence_of_element_located((By.ID, 'dataTable')))
        # Count table rows
        orderCount = len(driver.find_element_by_id('dataTable').find_elements_by_tag_name('tr'))
        if int(orderCount) > 3:
            # Check records Filters for All, 10,25,50,100
            if int(orderCount) > 100:
                # Select 100 entries orders_table_length
                entry_sel = driver.find_element_by_name("dataTable_length")
                v_optsel = "100"
                for opt in entry_sel.find_elements_by_tag_name("option"):
                    if opt.text == v_optsel:
                        opt.click()
                        break
                time.sleep(3)
                srch_text = driver.find_element_by_id('dataTable_info').text
                time.sleep(1)
                assert 'Showing 1 to 100' in srch_text
            if int(orderCount) > 50:
                # Select 50 entries orders_table_length
                entry_sel = driver.find_element_by_name("dataTable_length")
                v_optsel = "50"
                for opt in entry_sel.find_elements_by_tag_name("option"):
                    if opt.text == v_optsel:
                        opt.click()
                        break
                time.sleep(3)
                srch_text = driver.find_element_by_id('dataTable_info').text
                time.sleep(1)
                assert 'Showing 1 to 50' in srch_text
            if int(orderCount) > 25:
                # Select 25 entries orders_table_length
                entry_sel = driver.find_element_by_name("dataTable_length")
                v_optsel = "25"
                for opt in entry_sel.find_elements_by_tag_name("option"):
                    if opt.text == v_optsel:
                        opt.click()
                        break
                time.sleep(3)
                srch_text = driver.find_element_by_id('dataTable_info').text
                time.sleep(1)
                assert 'Showing 1 to 25' in srch_text
            if int(orderCount) > 10:
                # Select 10 entries orders_table_length
                entry_sel = driver.find_element_by_name("dataTable_length")
                v_optsel = "10"
                for opt in entry_sel.find_elements_by_tag_name("option"):
                    if opt.text == v_optsel:
                        opt.click()
                        break
                time.sleep(3)
                srch_text = driver.find_element_by_id('dataTable_info').text
                time.sleep(1)
                assert 'Showing 1 to 10' in srch_text
                # Select ALL entries orders_table_length
                entry_sel = driver.find_element_by_name("dataTable_length")
                v_optsel = "All"
                for opt in entry_sel.find_elements_by_tag_name("option"):
                    if opt.text == v_optsel:
                        opt.click()
                        break
                time.sleep(3)
                srch_text = driver.find_element_by_id('dataTable_info').text
                time.sleep(1)
                Sprecs = srch_text.split(" ")
                # Check 4th and 6th values are same for All option
                assert Sprecs[3] == Sprecs[5]
        else:
                print("Insufficient records  to validate filters")

    # ====================================16526==================23March===========================================

    def test_AccountingUser_VerifyAdhocSettlement_ReportSortFunctionality_C16526(self, impersonate_accounting):
        # Reports/Ad-hoc/Settlement - Verify the sorting functionality in report generated
        driver = impersonate_accounting['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Settlement')))
        time.sleep(1)
        driver.find_element_by_link_text("Settlement").click()
        time.sleep(1)
        expected_header_Settlement_Report = "Settlement Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Settlement_Report = driver.find_element_by_id("content-header").text
        # Verify Header
        assert expected_header_Settlement_Report in actual_header_Settlement_Report

        # Select the client from the drop down
        clients = driver.find_element_by_id("client_id")
        client_option = "AFNAVY"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Select the Ship Start  and ship end date
        driver.find_element_by_name("daterange").click()
        time.sleep(1)

        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("03/07/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("03/25/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)
        # Click on Generate report button.
        driver.find_element_by_class_name("btn-success").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
        time.sleep(3)
        # Wait until table is displayed dataTable
        wait.until(EC.presence_of_element_located((By.ID, 'dataTable')))
        # Count table rows
        orderCount = len(driver.find_element_by_id('dataTable').find_elements_by_tag_name('tr'))
        if int(orderCount) > 3:
            # Get Headers  of displayed columns data-column-index
            testhdrs = driver.find_element_by_class_name('dataTable').find_elements_by_tag_name('th')
            # Verify sorting for 5 Columns
            for i in range(0, 5):
                time.sleep(1)
                # Ascending Order check
                if int(i) > 0:
                    testhdrs[i].click()
                    time.sleep(1)
                asc_order = testhdrs[i].get_attribute("aria-sort")
                assert asc_order in "ascending"
                # Descending check
                testhdrs[i].click()
                time.sleep(1)
                desc_order = testhdrs[i].get_attribute("aria-sort")
                assert desc_order in "descending"

    # ====================================16527==================23March===========================================

    def test_AccountingUser_VerifyAdhocSettlement_ReportPaginationFunctionality_C16527(self, impersonate_accounting):
        # Reports/Ad-hoc/Settlement - Verify the pagination functionality
        driver = impersonate_accounting['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Settlement')))
        time.sleep(1)
        driver.find_element_by_link_text("Settlement").click()
        time.sleep(1)
        expected_header_Settlement_Report = "Settlement Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Settlement_Report = driver.find_element_by_id("content-header").text
        # Verify Header
        assert expected_header_Settlement_Report in actual_header_Settlement_Report

        # Select the client from the drop down
        clients = driver.find_element_by_id("client_id")
        client_option = "AFNAVY"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Select the Ship Start  and ship end date
        driver.find_element_by_name("daterange").click()
        time.sleep(1)

        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("03/07/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("03/25/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)
        # Click on Generate report button.
        driver.find_element_by_class_name("btn-success").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
        time.sleep(3)
        # Wait until table is displayed dataTable
        wait.until(EC.presence_of_element_located((By.ID, 'dataTable')))
        # Count table rows
        orderCount = len(driver.find_element_by_id('dataTable').find_elements_by_tag_name('tr'))
        # if record count is more than 3 , data exists
        if int(orderCount) > 3:
            # Verify Pagination controls Previous Button, current page
            print(int(orderCount))
            disabled_prev = driver.find_element_by_id("dataTable_previous").get_attribute("class")
            assert disabled_prev == "paginate_button previous disabled"
            # verify current page
            btn_elem = driver.find_elements_by_class_name('paginate_button')
            print(btn_elem[1].text)
            assert btn_elem[1].text == '1'
            # Click Next paginate_button next
            if driver.find_element_by_link_text('Next').is_enabled():
                driver.find_element_by_link_text('Next').click()
                time.sleep(2)
                # Check active page number after clicking Next
                btn_elem = driver.find_elements_by_class_name('paginate_button')
                bt_new = btn_elem[2].get_attribute("class")
                assert bt_new == 'paginate_button active'
                # Go to last page and check Next is disabled - keep clicking next until disabled
                cls_btn_next = driver.find_element_by_id("dataTable_next").get_attribute("class")
                while cls_btn_next == "paginate_button next":
                    driver.find_element_by_link_text('Next').click()
                    time.sleep(2)
                    cls_btn_next = driver.find_element_by_id("dataTable_next").get_attribute("class")
                # Verify Next is disabled
                assert cls_btn_next == "paginate_button next disabled"
                time.sleep(1)

    # ===================================16528==================23march===========================================

    def test_AccountingUser_Settlement_VerifyContentOnSubscription_C16528(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify the content in Subscription for: Client name Settlement pop up in KKohn- Reports/Ad-hoc/Settlement page.
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Settlement')))
        driver.find_element_by_link_text("Settlement").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Settlement_Report = "Settlement Report"
        time.sleep(1)
        actual_header_Settlement_Report = driver.find_element_by_id("content-header").text
        # Verify  Header
        assert expected_header_Settlement_Report in actual_header_Settlement_Report

        # Select the client from the drop down
        clients = driver.find_element_by_id("client_id")
        client_option = "ARA"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Select the Ship Start  and ship end date
        driver.find_element_by_name("daterange").click()
        #driver.find_element_by_name('daterangepicker_start').send_keys()
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
        driver.find_element_by_class_name("btn-success").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
        time.sleep(5)

        assert driver.find_element_by_id("table_report").is_displayed()

        driver.find_element_by_id("table_report").find_element_by_class_name("btn-primary").click()
        time.sleep(1)

        expected_header = "Subscription for: ARA Settlement Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'subscriptionsModalLabel')))
        actual_header = driver.find_element_by_id("subscriptionsModalLabel").text
        # Verify Header
        assert expected_header in actual_header

        # Verify Subscription Name
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
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
        actual_days = driver.find_elements_by_class_name("checkbox")
        time.sleep(1)
        for day in actual_days:
            name = day.text
            assert name in expected_days
        # Verify back button
        assert driver.find_element_by_class_name("btn-default").is_displayed()
        # Verify save Subscription button
        assert driver.find_element_by_id("next_btn").is_displayed()
        driver.find_element_by_class_name("btn-default").click()

    # ====================================16529==================23March===========================================

    def test_AccountingUser_Settlement_VerifySaveButtonFunctionalityInSubscription_C16529(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Reports/Ad-hoc/Settlement- Verify the save Subscription functionality in Subscription for: Client name Settlement pop up.
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Settlement')))
        time.sleep(1)
        driver.find_element_by_link_text("Settlement").click()
        time.sleep(1)
        expected_header_Settlement_Report = "Settlement Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Settlement_Report = driver.find_element_by_id("content-header").text
        # Verify Header
        assert expected_header_Settlement_Report in actual_header_Settlement_Report

        # Select the client from the drop down
        clients = driver.find_element_by_id("client_id")
        client_option = "ARA"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Select the Ship Start  and ship end date
        driver.find_element_by_name("daterange").click()
        time.sleep(1)

        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("03/11/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("03/25/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)
        # Click on Generate report button.
        driver.find_element_by_class_name("btn-success").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
        time.sleep(1)
        assert driver.find_element_by_id("table_report").is_displayed()
        # Open Subscription
        driver.find_element_by_id("table_report").find_element_by_class_name("btn-primary").click()
        time.sleep(1)

        expected_header = "Subscription for: ARA Settlement Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'subscriptionsModalLabel')))
        actual_header = driver.find_element_by_id("subscriptionsModalLabel").text
        # Verify Header
        assert expected_header in actual_header

        time.sleep(1)
        random_number = str(randint(10, 999))
        name = "TestSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        # Click on Back button at the bottom of the page.
        driver.find_element_by_id("next_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'noty_text')))
        # Subscription form submitted successfully and display message Subscription Saved.
        expected_message = "Subscription saved."
        actual_message = driver.find_element_by_class_name("noty_text").text
        assert expected_message in actual_message
        # Subscription should be display in subscriptions page with correct data.
        driver.find_element_by_link_text("Subscriptions").click()
        time.sleep(1)
        NameNew_value = driver.find_element_by_id("jobs_table").text
        assert name in NameNew_value

    # ====================================16530======================23March===========================================

    def test_AccountingUser_Settlement_VerifyBackButtonFunctionalityInSubscription_C16530(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Reports/Ad-hoc/Settlement -Verify the back button functionality in Subscription for: Client name Settlement pop up
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Settlement')))
        time.sleep(1)
        driver.find_element_by_link_text("Settlement").click()
        time.sleep(1)
        expected_header_Settlement_Report = "Settlement Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Settlement_Report = driver.find_element_by_id("content-header").text
        # Verify Header
        assert expected_header_Settlement_Report in actual_header_Settlement_Report

        # Select the client from the drop down
        clients = driver.find_element_by_id("client_id")
        client_option = "AFNAVY"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Select the Ship Start  and ship end date
        driver.find_element_by_name("daterange").click()
        time.sleep(1)

        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("03/11/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("03/12/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)
        # Click on Generate report button.
        driver.find_element_by_class_name("btn-success").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
        time.sleep(1)
        assert driver.find_element_by_id("table_report").is_displayed()
        # Open Subscription
        driver.find_element_by_id("table_report").find_element_by_class_name("btn-primary").click()
        time.sleep(1)

        expected_header = "Subscription for: AFNAVY Settlement Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'subscriptionsModalLabel')))
        actual_header = driver.find_element_by_id("subscriptionsModalLabel").text
        # Verify Header
        assert expected_header in actual_header
        time.sleep(1)

        random_number = str(randint(10, 999))
        name = "TestSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        # Click on Back button at the bottom of the page.
        driver.find_element_by_class_name("btn-default").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        # User should redirect Report page.
        expected_header = "Settlement Report"
        actual_header = driver.find_element_by_id("content-header").text
        assert expected_header in actual_header
        assert driver.find_element_by_id("sub_name").is_displayed() == 0

    # ====================================16532==================23March===========================================

    def test_AccountingUser_SatoriBulkMailing_VerifyGeneratedReport_C16532(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Verify that report is generated for Satori Bulk Mailing page.
        wait = WebDriverWait(driver, 90)
        # Wait for Report Tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Satori Bulk Mailing')))
        driver.find_element_by_link_text("Satori Bulk Mailing").click()
        time.sleep(1)
        expected_header_SBM_Report = "Satori Bulk Mailing Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_SBM_Report = driver.find_element_by_id("content-header").text
        time.sleep(1)
        # Verify  Header
        assert expected_header_SBM_Report in actual_header_SBM_Report

        # Select the client from the drop down
        clients = driver.find_element_by_id("client_id")
        client_option = "ARA"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        time.sleep(1)
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)
        # Click on Generate report button.
        driver.find_element_by_class_name("btn-success").click()

        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
        time.sleep(1)
        # Check Table heading displayed
        assert driver.find_element_by_class_name("dataTables_scrollHead").is_displayed()

    # ====================================16533==================23March===========================================

    def test_AccountingUser_SatoriBulkMailing_VerifyMakeSubscriptionFunctionality_C16533(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Reports/Ad-hoc/Satori Bulk Mailing - Verify the functionality of make a subscription button for the generated report
        wait = WebDriverWait(driver, 90)
        # Verify Report Tab Visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Satori Bulk Mailing')))
        driver.find_element_by_link_text("Satori Bulk Mailing").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Sbm_Report = "Satori Bulk Mailing Report"
        time.sleep(1)
        actual_header_Sbm_Report = driver.find_element_by_id("content-header").text
        # Verify  Header
        assert expected_header_Sbm_Report in actual_header_Sbm_Report

        # Select the client from the drop down
        clients = driver.find_element_by_id("client_id")
        client_option = "AFNAVY"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        time.sleep(1)
        # Click on Generate report button.
        driver.find_element_by_class_name("btn-success").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
        time.sleep(2)

        assert driver.find_element_by_id("table_report").is_displayed()
        # Click Subscription
        driver.find_element_by_id("table_report").find_element_by_class_name("btn-primary").click()
        time.sleep(1)

        expected_header = "Subscription for: AFNAVY Satori Bulk Mail Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'subscriptionsModalLabel')))
        actual_header = driver.find_element_by_id("subscriptionsModalLabel").text
        # Verify Header
        assert expected_header in actual_header
        # Click Back
        driver.find_element_by_class_name('btn-default').click()
        time.sleep(1)

    # ====================================16534==================23March===========================================

    def test_AccountingUser_SatoriBulkMailing_verifyExcelandSubscriptionButton_C16534(self, impersonate_accounting):
        driver = impersonate_accounting['webdriver']
        # Reports/Ad-hoc/Satori Bulk Mailing - Verify the visibility of Excel/Make Subscription button on the report generated.
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Satori Bulk Mailing')))
        driver.find_element_by_link_text("Satori Bulk Mailing").click()

        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Sbm_Report = "Satori Bulk Mailing Report"
        time.sleep(1)
        actual_header_sbm_Report = driver.find_element_by_id("content-header").text
        # Verify  Header
        assert expected_header_Sbm_Report in actual_header_sbm_Report

        # Select the client from the drop down
        clients = driver.find_element_by_id("client_id")
        client_option = "AFNAVY"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        time.sleep(1)
        # Click on Generate report button.
        driver.find_element_by_class_name("btn-success").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
        time.sleep(2)

        # Verify Make a Subscription and Excel button displayed on the report
        assert driver.find_element_by_id("table_report").find_element_by_class_name("btn-primary").is_displayed()
        assert driver.find_element_by_id("table_report").find_element_by_id("xls_btn").is_displayed()

    # =================================================================================================
