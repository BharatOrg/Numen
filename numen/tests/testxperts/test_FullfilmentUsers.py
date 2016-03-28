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

class TestFullfilmentUsers:
    # ==================================21 Dec=======c689===============================

    def test_FulfilmentVerifyImpersonateFunctionality_C689(self, impersonate_fullfilment):
        # User profile impersonate
        assert True

    # ==================================C751=====================================14 march================
    def test_FulfilmentVerifyDateTimeGeneratedReport_C751(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify Date and Time of generated report
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
        # Click on Out of Stock.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Out of Stock')))
        driver.find_element_by_link_text("Out of Stock").click()
        time.sleep(1)
        # Select the client from the drop down
        wait.until(EC.visibility_of_element_located((By.ID, 'CustomerNumber')))
        clients = driver.find_element_by_id("CustomerNumber")
        client_option = "AFNAVY"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Click on Generate report button
        driver.find_element_by_id("sub_btn").click()
        # Verify the Date and Time of the generated report
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(4)
        actual_dateTime = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        exp_dateTime = "Report Created On"
        exp_dateTime1 = "AM"
        exp_dateTime2 = "PM"
        exp_dateTime3 = ":"
        assert exp_dateTime in actual_dateTime
        assert ((exp_dateTime1 in actual_dateTime) | (exp_dateTime2 in actual_dateTime)) & (exp_dateTime3 in actual_dateTime)

    # ===========================================================C691=============================================

    def test_FulfilmentVerifyHomeButtonFunctionality_C691(self, impersonate_fullfilment):
        # Verify home button functionality in all the pages in vlucero
        driver = impersonate_fullfilment['webdriver']
        # Verify Date and Time of generated report
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # ====================My Work=Fulfillment=Presort Jobs=================================================
        expected_header_home = "Welcome"
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'My Work')))
        driver.find_element_by_link_text("My Work").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Fulfillment')))
        driver.find_element_by_link_text("Fulfillment").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Presort Jobs')))
        driver.find_element_by_link_text("Presort Jobs").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_presort_job = "Create a Presort Job"
        actual_header_presort_job = driver.find_element_by_id("content-header").text
        # Verify Create a Presort Job Header
        assert expected_header_presort_job in actual_header_presort_job
        driver.find_element_by_link_text("Home").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_home = driver.find_element_by_id("content-header").text
        # Verify Home Button Functionality
        assert expected_header_home in actual_header_home

        # ====================My Work=Fulfillment=View Jobs=Active===============
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'My Work')))
        driver.find_element_by_link_text("My Work").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Fulfillment')))
        driver.find_element_by_link_text("Fulfillment").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'View Jobs')))
        driver.find_element_by_link_text("View Jobs").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Active')))
        driver.find_element_by_link_text("Active").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_active = "View Active Jobs"
        actual_header_active = driver.find_element_by_id("content-header").text
        # Verify View Active Jobs Header
        assert expected_header_active in actual_header_active
        driver.find_element_by_link_text("Home").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_home = driver.find_element_by_id("content-header").text
        # Verify Home Button Functionality
        assert expected_header_home in actual_header_home

        # ====================My Work=Fulfillment=View Jobs=Complete===============
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'My Work')))
        driver.find_element_by_link_text("My Work").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Fulfillment')))
        driver.find_element_by_link_text("Fulfillment").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'View Jobs')))
        driver.find_element_by_link_text("View Jobs").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Complete')))
        driver.find_element_by_link_text("Complete").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Complete = "View Complete Jobs"
        actual_header_Complete = driver.find_element_by_id("content-header").text
        # Verify View Complete Jobs Header
        assert expected_header_Complete in actual_header_Complete
        driver.find_element_by_link_text("Home").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_home = driver.find_element_by_id("content-header").text
        # Verify Home Button Functionality
        assert expected_header_home in actual_header_home

        # ====================My Work=Fulfillment=View Jobs=Other===============
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'My Work')))
        driver.find_element_by_link_text("My Work").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Fulfillment')))
        driver.find_element_by_link_text("Fulfillment").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'View Jobs')))
        driver.find_element_by_link_text("View Jobs").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Other')))
        driver.find_element_by_link_text("Other").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Other = "View Other Jobs"
        actual_header_Other = driver.find_element_by_id("content-header").text
        # Verify View Other Jobs Header
        assert expected_header_Other in actual_header_Other
        driver.find_element_by_link_text("Home").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_home = driver.find_element_by_id("content-header").text
        # Verify Home Button Functionality
        assert expected_header_home in actual_header_home

        # ====================Orders=Order Search================
        driver.find_element_by_link_text("Orders").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Order Search')))
        driver.find_element_by_link_text("Order Search").click()
        expected_header_order_search = "Order Search"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_order_search = driver.find_element_by_id("content-header").text
        # Verify Order Search Header
        assert expected_header_order_search in actual_header_order_search
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Home')))
        driver.find_element_by_link_text("Home").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_home = driver.find_element_by_id("content-header").text
        # Verify Home Button Functionality
        assert expected_header_home in actual_header_home

        # ====================Orders=Bookmarks================
        driver.find_element_by_link_text("Orders").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'fa-bookmark-o')))
        driver.find_element_by_class_name("fa-bookmark-o").click()
        expected_header_Bookmarks = "Bookmarks"
        actual_header_Bookmarks = driver.find_element_by_id("content-header").text
        # Verify Bookmarks Header
        assert expected_header_Bookmarks in actual_header_Bookmarks
        driver.find_element_by_link_text("Home").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_home = driver.find_element_by_id("content-header").text
        # Verify Home Button Functionality
        assert expected_header_home in actual_header_home

        # ====================Orders=SKU Validation================
        driver.find_element_by_link_text("Orders").click()
        driver.find_element_by_link_text("SKU Validation").click()
        expected_header_SKU_Validation = "SKU Validation"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_SKU_Validation = driver.find_element_by_id("content-header").text
        # Verify SKU Validation Header
        assert expected_header_SKU_Validation in actual_header_SKU_Validation
        driver.find_element_by_link_text("Home").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_home = driver.find_element_by_id("content-header").text
        # Verify Home Button Functionality
        assert expected_header_home in actual_header_home

        # ================Spreadsheet Upload===============================================
        driver.find_element_by_link_text("Spreadsheet Upload").click()
        expected_header_spreadsheet_upload = "SS Upload"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_order_search = driver.find_element_by_id("content-header").text
        # Verify Spreadsheet Upload
        assert expected_header_spreadsheet_upload in actual_header_order_search
        driver.find_element_by_link_text("Home").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_home = driver.find_element_by_id("content-header").text
        # Verify Home Button Functionality
        assert expected_header_home in actual_header_home

        # ====================Reports=Operations=Inventory=Out of Stock=====================

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
        # Click on Out of Stock.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Out of Stock')))
        driver.find_element_by_link_text("Out of Stock").click()
        expected_header_Out_of_Stock = "Out of Stock Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Out_of_Stock = driver.find_element_by_id("content-header").text
        # Verify Out of Stock Header
        assert expected_header_Out_of_Stock in actual_header_Out_of_Stock
        driver.find_element_by_link_text("Home").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_home = driver.find_element_by_id("content-header").text
        # Verify Home Button Functionality
        assert expected_header_home in actual_header_home

        # ====================Reports=Operations=Inventory=Open Purchase Orders==============
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
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Open Purchase Orders')))
        driver.find_element_by_link_text("Open Purchase Orders").click()
        time.sleep(1)
        expected_header_Open_Purchase_Orders_Report = "Open Purchase Orders Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Open_Purchase_Orders_Report = driver.find_element_by_id("content-header").text
        # Verify Open Purchase Orders Header
        assert expected_header_Open_Purchase_Orders_Report in actual_header_Open_Purchase_Orders_Report
        driver.find_element_by_link_text("Home").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_home = driver.find_element_by_id("content-header").text
        # Verify Home Button Functionality
        assert expected_header_home in actual_header_home

        # ====================Reports=Operations=Inventory=Inventory Receipts==============
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
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory Receipts')))
        time.sleep(1)
        driver.find_element_by_link_text("Inventory Receipts").click()
        expected_header_Inventory_Receipts = "Inventory Receipts Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Inventory_Receipts = driver.find_element_by_id("content-header").text
        # Verify Inventory Receipts Header
        assert expected_header_Inventory_Receipts in actual_header_Inventory_Receipts
        driver.find_element_by_link_text("Home").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_home = driver.find_element_by_id("content-header").text
        # Verify Home Button Functionality
        assert expected_header_home in actual_header_home

        # ====================Reports=Operations=Inventory=Inventory by Business Unit==============
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
        driver.find_element_by_link_text("Operations").click()
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        time.sleep(1)
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory by Business Unit')))
        driver.find_element_by_link_text("Inventory by Business Unit").click()
        expected_header_Inventory_by_Business_Unit = "Inventory by Business Unit Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Inventory_by_Business_Unit = driver.find_element_by_id("content-header").text

        # Verify Inventory by Business Unit Header
        assert expected_header_Inventory_by_Business_Unit in actual_header_Inventory_by_Business_Unit
        driver.find_element_by_link_text("Home").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_home = driver.find_element_by_id("content-header").text
        # Verify Home Button Functionality
        assert expected_header_home in actual_header_home

        # ====================Reports=Operations=Inventory=Product Usage==============
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        time.sleep(1)
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
        driver.find_element_by_link_text("Operations").click()
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        time.sleep(1)
        driver.find_element_by_link_text("Inventory").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Product Usage')))
        time.sleep(1)
        driver.find_element_by_link_text("Product Usage").click()
        time.sleep(1)
        expected_header_Product_Usage_Report = "Product Usage Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Product_Usage_Report = driver.find_element_by_id("content-header").text
        # Verify Product Usage Header
        assert expected_header_Product_Usage_Report in actual_header_Product_Usage_Report
        driver.find_element_by_link_text("Home").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_home = driver.find_element_by_id("content-header").text
        # Verify Home Button Functionality
        assert expected_header_home in actual_header_home

        # ====================Reports=Orders=Open Orders by Business Unit==============
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        time.sleep(1)
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        time.sleep(1)
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Orders tab. fa-folder-open-o
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'fa-folder-open-o')))
        orders = driver.find_elements_by_link_text("Orders")
        orders[1].click()
        time.sleep(1)
        # Click on Open Orders by Business Unit
        #wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Open Orders by Business Unit')))
        driver.find_element_by_link_text("Open Orders by Business Unit").click()

        expected_header_Open_Orders_by_Business_Unit_Report = "Open Orders by Business Unit Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Open_Orders_by_Business_Unit_Report = driver.find_element_by_id("content-header").text
        # Verify Open Orders by Business Unit Header
        assert expected_header_Open_Orders_by_Business_Unit_Report in actual_header_Open_Orders_by_Business_Unit_Report
        # Verify Home Button Functionality
        driver.find_element_by_link_text("Home").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_home = driver.find_element_by_id("content-header").text


        # ====================Reports=Orders= Order Processing by Keycode==============
        driver.refresh()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        orders = driver.find_elements_by_link_text("Orders")
        orders[1].click()
        time.sleep(1)
        driver.find_element_by_link_text("Order Processing by Keycode").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        time.sleep(1)
        expected_header_Order_Processing_by_Keycode = "Order Processing by Keycode Report"
        actual_header_Order_Processing_by_Keycode = driver.find_element_by_id("content-header").text
        # Verify  Header
        assert expected_header_Order_Processing_by_Keycode in actual_header_Order_Processing_by_Keycode
        driver.find_element_by_link_text("Home").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_home = driver.find_element_by_id("content-header").text
        # Verify Home Button Functionality
        assert expected_header_home in actual_header_home

        # ====================Reports=Orders= Order History Summary==============
        driver.refresh()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        orders = driver.find_elements_by_link_text("Orders")
        orders[1].click()
        time.sleep(1)
        driver.find_element_by_link_text("Order History Summary").click()
        expected_header_Order_History_Summary_Report = "Order History Summary Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Order_History_Summary_Report = driver.find_element_by_id("content-header").text
        # Verify  Header
        assert expected_header_Order_History_Summary_Report in actual_header_Order_History_Summary_Report
        driver.find_element_by_link_text("Home").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_home = driver.find_element_by_id("content-header").text
        # Verify Home Button Functionality
        assert expected_header_home in actual_header_home

        # ====================Reports=Ad-hoc= Shipping=============
        driver.refresh()
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
        driver.find_element_by_link_text("Home").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        time.sleep(1)
        actual_header_home = driver.find_element_by_id("content-header").text
        # Verify Home Button Functionality
        assert expected_header_home in actual_header_home

        # ====================Reports=Ad-hoc=Kitting=============
        driver.refresh()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        time.sleep(1)
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Kitting')))
        time.sleep(1)
        driver.find_element_by_link_text("Kitting").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Kitting_Report = "Kitting Report"
        time.sleep(1)
        actual_header_Kitting_Report = driver.find_element_by_id("content-header").text
        # Verify  Header
        assert expected_header_Kitting_Report in actual_header_Kitting_Report
        driver.find_element_by_link_text("Home").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_home = driver.find_element_by_id("content-header").text
        # Verify Home Button Functionality
        assert expected_header_home in actual_header_home

        # ====================Reports=Ad-hoc=Settlement=============
        driver.refresh()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        time.sleep(1)
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Settlement')))
        time.sleep(1)
        driver.find_element_by_link_text("Settlement").click()
        time.sleep(1)
        expected_header_Settlement_Report = "Settlement Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Settlement_Report = driver.find_element_by_id("content-header").text
        time.sleep(1)
        # Verify  Header
        assert expected_header_Settlement_Report in actual_header_Settlement_Report
        driver.find_element_by_link_text("Home").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_home = driver.find_element_by_id("content-header").text
        time.sleep(1)
        # Verify Home Button Functionality
        assert expected_header_home in actual_header_home

        # ====================Reports=Ad-hoc=Satori Bulk Mailing=============
        driver.refresh()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        time.sleep(1)
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        time.sleep(1)
        driver.find_element_by_link_text("Ad-hoc").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Satori Bulk Mailing')))
        time.sleep(1)
        driver.find_element_by_link_text("Satori Bulk Mailing").click()
        time.sleep(1)
        expected_header_Satori_Bulk_Mailing = "Satori Bulk Mailing Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Satori_Bulk_Mailing = driver.find_element_by_id("content-header").text
        time.sleep(1)
        # Verify  Header
        assert expected_header_Satori_Bulk_Mailing in actual_header_Satori_Bulk_Mailing
        driver.find_element_by_link_text("Home").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_home = driver.find_element_by_id("content-header").text
        time.sleep(1)
        # Verify Home Button Functionality
        assert expected_header_home in actual_header_home

        # ====================Reports= Subscriptions=============
        driver.refresh()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        time.sleep(1)
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Subscriptions')))
        time.sleep(1)
        driver.find_element_by_link_text("Subscriptions").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        time.sleep(1)
        expected_header_Subscriptions = "Subscriptions"
        actual_header_Subscriptions = driver.find_element_by_id("content-header").text
        time.sleep(1)
        # Verify  Header
        assert expected_header_Subscriptions in actual_header_Subscriptions
        driver.find_element_by_link_text("Home").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_home = driver.find_element_by_id("content-header").text
        time.sleep(1)
        # Verify Home Button Functionality
        assert expected_header_home in actual_header_home

        # ====================Tools=Warehouse=Pack Slip============
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Tools')))
        time.sleep(1)
        driver.find_element_by_link_text("Tools").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Warehouse')))
        time.sleep(1)
        driver.find_element_by_link_text("Warehouse").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Pack Slip')))
        time.sleep(1)
        driver.find_element_by_link_text("Pack Slip").click()
        time.sleep(1)
        expected_header_Pack_Slip = "Pack Slip"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Pack_Slip = driver.find_element_by_id("content-header").text
        time.sleep(1)
        # Verify  Header
        assert expected_header_Pack_Slip in actual_header_Pack_Slip
        driver.find_element_by_link_text("Home").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_home = driver.find_element_by_id("content-header").text
        time.sleep(1)
        # Verify Home Button Functionality
        assert expected_header_home in actual_header_home

        # ====================Tools=Warehouse=Delete Bins============
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Tools')))
        time.sleep(1)
        driver.find_element_by_link_text("Tools").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Warehouse')))
        time.sleep(1)
        driver.find_element_by_link_text("Warehouse").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Delete Bins')))
        time.sleep(1)
        driver.find_element_by_link_text("Delete Bins").click()
        time.sleep(1)
        expected_header_Delete_Bins = "Delete Bins"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Delete_Bins = driver.find_element_by_id("content-header").text
        time.sleep(1)
        # Verify  Header
        assert expected_header_Delete_Bins in actual_header_Delete_Bins
        driver.find_element_by_link_text("Home").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_home = driver.find_element_by_id("content-header").text
        time.sleep(1)
        # Verify Home Button Functionality
        assert expected_header_home in actual_header_home

        # ====================Tools=Warehouse=AARP Bundle============
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Tools')))
        time.sleep(1)
        driver.find_element_by_link_text("Tools").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Warehouse')))
        time.sleep(1)
        driver.find_element_by_link_text("Warehouse").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'AARP Bundle')))
        time.sleep(1)
        driver.find_element_by_link_text("AARP Bundle").click()
        time.sleep(1)
        expected_header_AARP_Bundle = "AARP Bundle"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_AARP_Bundle = driver.find_element_by_id("content-header").text
        time.sleep(1)
        # Verify Header
        assert expected_header_AARP_Bundle in actual_header_AARP_Bundle
        driver.find_element_by_link_text("Home").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_home = driver.find_element_by_id("content-header").text
        time.sleep(1)
        # Verify Home Button Functionality
        assert expected_header_home in actual_header_home

        # ====================Tools=Warehouse=CASS Reports====================================

        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Tools')))
        time.sleep(1)
        driver.find_element_by_link_text("Tools").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Warehouse')))
        time.sleep(1)
        driver.find_element_by_link_text("Warehouse").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'CASS Reports')))
        time.sleep(1)
        driver.find_element_by_link_text("CASS Reports").click()
        time.sleep(1)
        expected_header_CASS_Reports = "CASS Reports"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_CASS_Reports = driver.find_element_by_id("content-header").text
        time.sleep(1)
        # Verify  Header
        assert expected_header_CASS_Reports in actual_header_CASS_Reports
        driver.find_element_by_link_text("Home").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_home = driver.find_element_by_id("content-header").text
        time.sleep(1)
        # Verify Home Button Functionality
        assert expected_header_home in actual_header_home


    # ==================================C690==============================================

    def test_FulfilmentVerifyLogoutFunctionality_C690(self, impersonate_fullfilment):
        # Verify the logout functionality
        driver = impersonate_fullfilment['webdriver']
        logout_title = "Numen - Login"
        driver.find_element_by_class_name("dropdown-toggle").click()
        driver.find_element_by_link_text("Logout").click()
        time.sleep(1)
        assert logout_title == driver.title
        time.sleep(5)
        driver.find_element_by_name('user').send_keys('testuser')
        driver.find_element_by_name('password').send_keys('X91VW9u^B6kEBWIw')
        driver.find_element_by_name('user').submit()
        time.sleep(5)

    # ==================================C697===========21 Dec===================================

    def test_FulfilmentVerifyContentOfInventoryOnHand_C697(self, impersonate_fullfilment):
        # Verify the content of Inventory on Hand
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        time.sleep(1)
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
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
        expected_header = "Inventory on Hand Report"
        actual_header = driver.find_element_by_id("content-header").text
        assert expected_header in actual_header
        # Drop down with multiple clients.
        expected_clients = "select"
        actual_clients = driver.find_element_by_id("cClientName").tag_name
        assert expected_clients in actual_clients
        # Generate Report button.
        assert driver.find_element_by_id("sub_btn").is_displayed()
        # Make a Subscription button.
        assert driver.find_element_by_class_name("btn-primary").is_displayed()

    # ==================================C698==========21 Dec====================================
    def test_FulfilmentVerifyContentOfSubscription_C698(self, impersonate_fullfilment):
        # Verify the content of Subscription
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        time.sleep(1)
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        time.sleep(1)
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory on Hand tab.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'fa-folder-open-o')))
        ioh = driver.find_elements_by_class_name('fa-folder-open-o')
        ioh[1].click()
        time.sleep(1)
        # Report: Inventory on Hand (Title) top left side of the page.
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
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

    # ==================================C700============21 Dec==================================
    def test_FulfilmentVerifyUserEmailIdInSubscription_C700(self, impersonate_fullfilment):
        # Verify user email Id display by default in Subscription
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        time.sleep(1)
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
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
        # Click on Make a subscription button right side of the page.
        driver.find_element_by_class_name("btn-primary").click()
        # Verify the Email To text box.
        expected_email = "vlucero@ggoutfitters.com"
        actual_email = driver.find_element_by_id("email").get_attribute("value")
        assert expected_email in actual_email

    # ==================================C701=========21 Dec=====================================
    def test_FulfilmentVerifyBackButtonFunctionalityOnSubscription_C701(self, impersonate_fullfilment):
        # Verify Back button functionality on the Subscription
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
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
        # Click on Make a subscription button right side of the page.
        driver.find_element_by_class_name("btn-primary").click()
        random_number = str(randint(10, 999))
        name = "TestGSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        # Click on Back button at the bottom of the page.
        driver.find_element_by_class_name("btn-default").click()
        time.sleep(1)
        # User should redirect to the Inventory on Hand Report page.
        expected_header = "Inventory on Hand Report"
        actual_header = driver.find_element_by_id("content-header").text
        assert expected_header in actual_header
        assert driver.find_element_by_id("sub_name").is_displayed() == 0

    # ==================================22 Dec=================================================
    # ==================================C728===========22 Dec===================================
    def test_FulfilmentVerifyFunctionalityOfGeneratedReport_C728(self, impersonate_fullfilment):
        # Verify the functionality of Generate Report
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        time.sleep(1)
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
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
        wait.until(EC.visibility_of_element_located((By.ID,'cClientName')))
        select = Select(driver.find_element_by_id("cClientName"))
        select.select_by_visible_text("ARPM")
        # Generate Report
        driver.find_element_by_id("sub_btn").click()
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(10)
        assert driver.find_element_by_id("ReportViewerForm").is_displayed()

    # ==================================C729===========22 Dec===================================
    def test_FulfilmentVerifyShowingFunctionality_C729(self, impersonate_fullfilment):
        # Verify Showing 1 of xx entries functionality
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
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
        # Select the client from the drop down.
        wait.until(EC.visibility_of_element_located((By.ID,'cClientName')))
        select = Select(driver.find_element_by_id("cClientName"))
        select.select_by_visible_text("ARPM")
        # Click on Generate report button.
        driver.find_element_by_id("sub_btn").click()
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(10)
        # In report, Verify show 1 of x page by default
        expected_value = "1"
        actual_value = driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").get_attribute("value")
        assert expected_value in actual_value
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()
        expected_of = "of"
        actual_of = driver.find_element_by_class_name("ToolBarButtonsCell").text
        time.sleep(1)
        assert expected_of in actual_of

    # ==================================C733===========22 Dec===================================
    def test_FulfilmentVerifyDateTimeGeneratedReport_C733(self, impersonate_fullfilment):
        # Verify Date and Time of generated Report
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        time.sleep(1)
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
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
        # Select the client from the drop down.
        wait.until(EC.visibility_of_element_located((By.ID,'cClientName')))
        # Select the client from the drop down
        clients = driver.find_element_by_id("cClientName")
        client_option = "ARPM"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Click on Generate report button.
        driver.find_element_by_id("sub_btn").click()
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(10)
        # Verify the Date and Time of the generated report
        actual_dateTime = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        time.sleep(1)
        exp_dateTime = "Report Created On:"
        exp_dateTime1 = "AM"
        exp_dateTime2 = "PM"
        exp_dateTime3 = ":"
        assert exp_dateTime in actual_dateTime
        assert ((exp_dateTime1 in actual_dateTime) | (exp_dateTime2 in actual_dateTime)) & (exp_dateTime3 in actual_dateTime)

    # ==================================23 Dec=================================================
    # ==================================C736==========23 Dec===================================
    def test_FulfilmentVerifyRefreshButtonFunctionality_C736(self, impersonate_fullfilment):
        # Verify refresh button functionality
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        time.sleep(1)
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
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
        # Select the client from the drop down.
        wait.until(EC.visibility_of_element_located((By.ID,'cClientName')))
        # Select the client from the drop down
        clients = driver.find_element_by_id("cClientName")
        client_option = "ARPM"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Click on Generate report button.
        driver.find_element_by_id("sub_btn").click()
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(10)
        original_text = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        # Click on Refresh icon.
        driver.find_element_by_name("ReportViewerControl$ctl05$ctl05$ctl00$ctl00$ctl00").click()
        wait.until(EC.visibility_of_element_located((By.ID,'VisibleReportContentReportViewerControl_ctl09')))
        latest_text = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        time.sleep(1)
        assert (original_text is not latest_text)

    # ==================================C737==========23 Dec===================================
    def test_FulfilmentVerifySubmittedSubscription_C737(self, impersonate_fullfilment):
        # Verify submitted subscription
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        time.sleep(1)
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
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
        # Select the client from the drop down.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'btn-primary')))
        # Click on Make a Subscription button.
        driver.find_element_by_class_name("btn-primary").click()
        random_number = str(randint(10, 999))
        name = "TestBSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        driver.find_element_by_id("next_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'noty_text')))
        time.sleep(1)
        driver.find_element_by_link_text("Subscriptions").click()
        time.sleep(1)
        # Subscription for: Executive Accounts Receivable pop up is displayed.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Modify')))
        driver.find_element_by_link_text("Modify").click()
        # Data in Subscription for: Executive Accounts should be edited successfully.
        sName_value = driver.find_element_by_id("job_name").get_attribute("value")
        driver.find_element_by_id("sub_name").send_keys("newabc123")
        # .Subscription for: Executive Accounts pop up should be closed successfully.
        driver.find_element_by_class_name("btn-default").click()
        time.sleep(1)
        driver.find_element_by_link_text("Modify").click()
        # Subscription should not be updated successfully.
        sNameNew_value = driver.find_element_by_id("job_name").get_attribute("value")
        time.sleep(1)
        assert sName_value in sNameNew_value

    # ==================================C745==========23 Dec===================================
    def test_FulfilmentVerifyContentOfOutOfStock_C745(self, impersonate_fullfilment):
        # Verify the content of Out of Stock Report page
        driver = impersonate_fullfilment['webdriver']
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
        # Click on Out of Stock.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Out of Stock')))
        driver.find_element_by_link_text("Out of Stock").click()
        time.sleep(1)
        # Select the client from the drop down
        wait.until(EC.visibility_of_element_located((By.ID, 'CustomerNumber')))
        # Verify the contents on Out of Stock Report page.
        # Report: Out of Stock (Title) top left side of the page
        expected_header = "Report: Out of Stock"
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

    # ==================================C746==========28 Dec===================================
    def test_FullfilmentVerifyGenerateReportButtonFunctionality_C746(self, impersonate_fullfilment):
        # Verify the functionality of Generate Report button
        driver = impersonate_fullfilment['webdriver']
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
        # Click on Out of Stock.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Out of Stock')))
        driver.find_element_by_link_text("Out of Stock").click()
        time.sleep(1)
        # Select the client from the drop down
        wait.until(EC.visibility_of_element_located((By.ID, 'CustomerNumber')))
        clients = driver.find_element_by_id("CustomerNumber")
        client_option = "AFNAVY"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Click on Generate report button
        driver.find_element_by_id("sub_btn").click()
        # Report should be generated according to the selected client
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(10)
        expected_report_header = "Out Of Stock Report"
        actual_report_header = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        time.sleep(1)
        assert expected_report_header in actual_report_header

    # ==================================C747==========28 Dec===================================
    def test_FullfilmentVerifyShowingEntriesFunctionality_C747(self, impersonate_fullfilment):
        # Verify Showing 1 of xx entries functionality
        driver = impersonate_fullfilment['webdriver']
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
        # Click on Out of Stock.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Out of Stock')))
        driver.find_element_by_link_text("Out of Stock").click()
        time.sleep(1)
        # Select the client from the drop down
        wait.until(EC.visibility_of_element_located((By.ID, 'CustomerNumber')))
        clients = driver.find_element_by_id("CustomerNumber")
        client_option = "AFNAVY"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Click on Generate report button.
        driver.find_element_by_id("sub_btn").click()
        driver.switch_to_frame("report_src")
        # In report, Verify show 1 of x page by default
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(10)
        expected_value = "1"
        actual_value = driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").get_attribute("value")
        assert expected_value in actual_value
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()
        expected_of = "of"
        actual_of = driver.find_element_by_class_name("ToolBarButtonsCell").text
        time.sleep(1)
        assert expected_of in actual_of

    # ==================================C753==========28 Dec===================================
    def test_FullfilmentVerifyRefreshButtonFunctionality_C753(self, impersonate_fullfilment):
        # Verify refresh button functionality
        driver = impersonate_fullfilment['webdriver']
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
        # Click on Out of Stock.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Out of Stock')))
        driver.find_element_by_link_text("Out of Stock").click()
        time.sleep(1)
        # Select the client from the drop down
        wait.until(EC.visibility_of_element_located((By.ID, 'CustomerNumber')))
        clients = driver.find_element_by_id("CustomerNumber")
        client_option = "AFNAVY"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Click on Generate report button
        driver.find_element_by_id("sub_btn").click()
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(10)
        original_text = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        # Click on Refresh icon.
        driver.find_element_by_name("ReportViewerControl$ctl05$ctl05$ctl00$ctl00$ctl00").click()
        # Generated report should be refreshed.
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        latest_text = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        time.sleep(1)
        assert (original_text is not latest_text)

    # ==================================C754==========28 Dec===================================
    def test_FullfilmentVerifySubmittedSubscriptionFunctionality_C754(self, impersonate_fullfilment):
        # Verify submitted subscription show in the subscription page.
        driver = impersonate_fullfilment['webdriver']
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
        # Click on Out of Stock.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Out of Stock')))
        driver.find_element_by_link_text("Out of Stock").click()
        time.sleep(1)
        # Select the client from the drop down
        wait.until(EC.visibility_of_element_located((By.ID, 'CustomerNumber')))
        clients = driver.find_element_by_id("CustomerNumber")
        client_option = "ARPM"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Click on Make a Subscription button.
        driver.find_element_by_class_name("btn-primary").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        random_number = str(randint(10, 999))
        name = "TestGSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        driver.find_element_by_id("next_btn").click()
        time.sleep(1)
        # Subscription form submitted successfully and display message Subscription Saved.
        expected_message = "Subscription saved."
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'noty_text')))
        actual_message = driver.find_element_by_class_name("noty_text").text
        assert expected_message in actual_message
        # Click on Subscriptions Page
        driver.find_element_by_link_text("Subscriptions").click()
        # On subscriptions page, Subscription name should reflect with Modify and Delete button.
        wait.until(EC.visibility_of_element_located((By.ID, 'jobs_table')))
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


    # ==================================C755==========28 Dec===================================

    def test_FullfilmentVerifyContentOfSubscription_C755(self, impersonate_fullfilment):
        # Verify the content of Subscription for: Out of Stock Report for ARPM form.
        driver = impersonate_fullfilment['webdriver']
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
        # Click on Out of Stock.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Out of Stock')))
        driver.find_element_by_link_text("Out of Stock").click()
        time.sleep(1)
        # Select the client from the drop down
        wait.until(EC.visibility_of_element_located((By.ID, 'CustomerNumber')))

        # Click on Make a subscription button right side of the page.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
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

    # ==================================C757==========28 Dec===============================================

    def test_FullfilmentVerifyEmailIdDisplayByDefault_C757(self, impersonate_fullfilment):
        # Verify user email Id display by default in subscription form.
        driver = impersonate_fullfilment['webdriver']
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
        # Click on Out of Stock.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Out of Stock')))
        driver.find_element_by_link_text("Out of Stock").click()
        time.sleep(1)
        # Select the client from the drop down
        wait.until(EC.visibility_of_element_located((By.ID, 'CustomerNumber')))
        # Click on Make a subscription button right side of the page.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()
        # Verify the Email To text box.
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        expected_email = "vlucero@ggoutfitters.com"
        actual_email = driver.find_element_by_id("email").get_attribute("value")
        assert expected_email in actual_email

    # ==================================04 Jan=================================================
    # ==================================C758==========04 Jan===================================
    def test_FullfilmentVerifyBackButtonFunctionality_C758(self, impersonate_fullfilment):
        # Verify Back button functionality
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
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
        # Select the client from the drop down
        wait.until(EC.visibility_of_element_located((By.ID, 'CustomerNumber')))

        # Click on Make a subscription button right side of the page.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()
        # Verify the Email To text box.
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        random_number = str(randint(10, 999))
        name = "TestGSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        # Click on Back button at the bottom of the page.
        driver.find_element_by_class_name("btn-default").click()

        # User should redirect to the Out of Stock Report page.
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header = "Out of Stock Report"
        actual_header = driver.find_element_by_id("content-header").text
        assert expected_header in actual_header
        assert driver.find_element_by_id("sub_name").is_displayed() == 0

    # ==================================C763==========04 Jan===================================
    def test_FullfilmentVerifyContentOfOpenPurchaseOrdersPage_C763(self, impersonate_fullfilment):
        # Verify the content of Open Purchase Orders page.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        time.sleep(1)
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
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
        # Verify the contents on Open Purchase order Report page.
        # Report: Out of Stock (Title) top left side of the page
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'panel-heading')))
        expected_header = "Report: Open Purchase Orders"
        actual_header = driver.find_element_by_class_name("panel-heading").text
        time.sleep(1)
        assert expected_header in actual_header
        # Drop down with multiple clients
        wait.until(EC.visibility_of_element_located((By.ID, 'CustomerNumber')))
        expected_clients = "select"
        actual_clients = driver.find_element_by_id("CustomerNumber").tag_name
        assert expected_clients in actual_clients
        # Generate Report button verify
        assert driver.find_element_by_id("sub_btn").is_displayed()
        # Make a Subscription button
        assert driver.find_element_by_class_name("btn-primary").is_displayed()

    # ==================================C764==========04 Jan===================================
    def test_FullfilmentVerifyGenerateReportButtonFunctionality_C764(self, impersonate_fullfilment):
        # Verify the functionality of Generate Report button.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
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
        # Report: Out of Stock (Title) top left side of the page
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'panel-heading')))
        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("CustomerNumber"))
        select.select_by_visible_text("ARPM")
        # Click on Generate report button.
        driver.find_element_by_id("sub_btn").click()
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(10)
        assert driver.find_element_by_id("ReportViewerForm").is_displayed()

    # ====================C797======4th Jan============================================
    def test_FulfilmentVerifyContentOnInventoryReceiptsReportPage_C797(self, impersonate_fullfilment):
        # Verify the content on "Inventory Receipts Report" page.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Subscriptions')))
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Inventory tab.
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        # Click on Inventory Receipts.
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Inventory Receipts").click()
        time.sleep(1)
        # Verify Inventory Receipts Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Inventory_Receipts_Report = "Inventory Receipts Report "
        actual_header_Inventory_Receipts_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_Receipts_Report in expected_header_Inventory_Receipts_Report
        # Verify Drop down
        wait.until(EC.visibility_of_element_located((By.ID, 'CustomerNumber')))
        assert driver.find_element_by_id("CustomerNumber").is_displayed()
        # Verify date control
        assert driver.find_element_by_name("daterange").is_displayed()

        # Verify PO number input box
        assert driver.find_element_by_id("RcvSlip").is_displayed()
        # Verify Generate report button
        assert driver.find_element_by_id("sub_btn").is_displayed()
        # Verify make a subscription button
        assert driver.find_element_by_class_name("btn-primary").is_displayed()

    # =============================C798======4th Jan======================================================
    def test_FulfilmentVerifyGenerateReportButtonFunctionality_C798(self, impersonate_fullfilment):
        # Verify Generate Report button functionality.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Subscriptions')))
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Inventory tab.
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        # Click on Inventory Receipts.
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
        # Select Date range
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
        # Click on Generate report button.
        driver.find_element_by_class_name("btn-success").click()
        # Switch to report
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(10)
        # Verify report Generation
        assert driver.find_element_by_id("ReportViewerControl_ctl05").is_displayed()

    # ===================================C799======4th Jan====================================================
    def test_FulfilmentVerifyShowing1OfXXEntriesFunctionalityInReport_C799(self, impersonate_fullfilment):
        # Verify Showing 1 of 'xx' entries functionality in generated report.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
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
        time.sleep(1)
        # Verify Inventory Receipts Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Inventory_Receipts_Report = "Inventory Receipts Report "
        actual_header_Inventory_Receipts_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_Receipts_Report in expected_header_Inventory_Receipts_Report
        # Select the client from the drop down.
        wait.until(EC.visibility_of_element_located((By.ID, 'CustomerNumber')))
        select = Select(driver.find_element_by_id("CustomerNumber"))
        select.select_by_visible_text("ARPM")
        # Select Date range
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
        # Switch to report-items
        driver.switch_to_frame("report_src")
        # In report, Showing 1 of 'xx' entries
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(10)
        expected_value = "1"
        actual_value = driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").get_attribute("value")
        assert expected_value in actual_value
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()
        expected_of = "of"
        actual_of = driver.find_element_by_class_name("ToolBarButtonsCell").text
        time.sleep(1)
        assert expected_of in actual_of

    # ==================================C771==========================6Jan===================================

    def test_FullfilmentVerifyRefreshButtonFunctionality_C771(self, impersonate_fullfilment):
        # Verify refresh button functionality
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
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
        # Report: Out of Stock (Title) top left side of the page
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'panel-heading')))
        # Select the client from the drop down
        clients = driver.find_element_by_id("CustomerNumber")
        client_option = "AFNAVY"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Click on Generate report button
        driver.find_element_by_id("sub_btn").click()
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(3)
        original_text = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        # Click on Refresh icon.
        driver.find_element_by_name("ReportViewerControl$ctl05$ctl05$ctl00$ctl00$ctl00").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        # Generated report should be refreshed.
        latest_text = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        assert (original_text is not latest_text)
        time.sleep(3)

    # ==================================C769==========06 Jan===================================
    def test_FullfilmentVerifyDateTimeOfGeneratedReport_C769(self, impersonate_fullfilment):
        # Verify Date and Time of generated Report
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
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
        # Report: Out of Stock (Title) top left side of the page
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'panel-heading')))
        # Select the client from the drop down
        clients = driver.find_element_by_id("CustomerNumber")
        client_option = "AFNAVY"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Click on Generate report button
        driver.find_element_by_id("sub_btn").click()
        # Verify the Date and Time of the generated report
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(10)
        actual_dateTime = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        exp_dateTime = "Report Created On"
        exp_dateTime1 = "AM"
        exp_dateTime2 = "PM"
        exp_dateTime3 = ":"
        assert exp_dateTime in actual_dateTime
        assert ((exp_dateTime1 in actual_dateTime) | (exp_dateTime2 in actual_dateTime)) & (exp_dateTime3 in actual_dateTime)

    # ==================================C765==========06 Jan====================================================

    def test_FullfilmentVerifyShowingEntries_C765(self, impersonate_fullfilment):
        # Verify Showing 1 of xx entries
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
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
        # Report: Out of Stock (Title) top left side of the page
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'panel-heading')))
        # Select the client from the drop down
        clients = driver.find_element_by_id("CustomerNumber")
        client_option = "ARPM"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Click on Generate report button.
        driver.find_element_by_id("sub_btn").click()
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(10)
        # In report, Verify show 1 of x page by default
        expected_value = "1"
        actual_value = driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").get_attribute("value")
        assert expected_value in actual_value
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()
        expected_of = "of"
        actual_of = driver.find_element_by_class_name("ToolBarButtonsCell").text
        time.sleep(1)
        assert expected_of in actual_of

    # ====================================C801======6th Jan=====================================================

    def test_FullfilmentVerifySearchFunctionalityInReport_C801(self, impersonate_fullfilment):
        # Verify Search functionality in generated report.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
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
        time.sleep(1)
        # Verify Inventory Receipts Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Inventory_Receipts_Report = "Inventory Receipts Report "
        actual_header_Inventory_Receipts_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_Receipts_Report in expected_header_Inventory_Receipts_Report
        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("CustomerNumber"))
        select.select_by_visible_text("ARPM")
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
        # Click on generate report button
        driver.find_element_by_class_name("btn-success").click()
        # Switch to report
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(10)
        # verify valid search
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl00").send_keys("SKU")
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl01").click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
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

    # ================================C807===== 6th Jan=====================================================

    def test_FullfilmentVerifyExportButtonFunctionalityInReport_C807(self, impersonate_fullfilment):
        # Verify Export button functionality in generated report.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
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
        time.sleep(1)
        # Verify Inventory Receipts Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Inventory_Receipts_Report = "Inventory Receipts Report "
        actual_header_Inventory_Receipts_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_Receipts_Report in expected_header_Inventory_Receipts_Report
        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("CustomerNumber"))
        select.select_by_visible_text("ARPM")

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
        driver.find_element_by_class_name("btn-success").click()
        # Report should be generated successfully on the same page.
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(10)
        # Verify Export Link
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_displayed()
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl04_ctl00_ButtonLink").click()
        # Verify report can be exported in following format
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'HoverButton')))
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

    # ==============================C808===========6th Jan==========================================================

    def test_FullfilmentVerifyDateAndTimeInReport_C808(self, impersonate_fullfilment):
        # Verify Date and Time in generated report.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
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
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory Receipts.
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
        # Select Dates
        wait.until(EC.visibility_of_element_located((By.NAME,'daterange')))
        driver.find_element_by_name("daterange").click()
        time.sleep(1)

        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("02/24/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("02/26/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)
        # Verify PO number selection
        driver.find_element_by_id("RcvSlip").send_keys("535271")
        expected_po_number = "535271"
        actual_po_number = driver.find_element_by_id("RcvSlip").get_attribute("value")
        assert actual_po_number in expected_po_number

        # Click on Generate report button.
        driver.find_element_by_class_name("btn-success").click()
        # Report should be generated successfully on the same page.
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(10)
        # Verify the Date and Format of the generated report
        actual_dateTime = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text

        label_dateTime = "Report Created on:"
        exp_dateTime1 = "AM"
        exp_dateTime2 = "PM"
        repdate1 = int(time.strftime("%m"))
        repdate2 = int(time.strftime("%d"))
        repdate3 = int(time.strftime("%Y"))
        todays_date = str(repdate1) + "/" + str(repdate2) + "/" + str(repdate3)
        assert todays_date in actual_dateTime
        assert label_dateTime in actual_dateTime
        assert ((exp_dateTime1 in actual_dateTime) | (exp_dateTime2 in actual_dateTime))

    # ==================================C772===========================07 Jan===================================

    def test_FullfilmentVerifySubmittedSubscriptionFunctionality_C772(self, impersonate_fullfilment):
        # Verify submitted subscription show in the subscription page.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
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
        # Report: Out of Stock (Title) top left side of the page
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'panel-heading')))
        # Select the client from the drop down
        clients = driver.find_element_by_id("CustomerNumber")
        client_option = "ARPM"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Click on Make a Subscription button.
        driver.find_element_by_class_name("btn-primary").click()
        # Submit the subscription form with all the details.
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        random_number = str(randint(10, 999))
        name = "TestGSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        driver.find_element_by_id("next_btn").click()
        # Subscription form submitted successfully and display message Subscription Saved.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'noty_text')))
        expected_message = "Subscription saved."
        actual_message = driver.find_element_by_class_name("noty_text").text
        assert expected_message in actual_message

        # Click on Subscriptions Page
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Subscriptions')))
        time.sleep(1)
        driver.find_element_by_link_text("Subscriptions").click()
        # On subscriptions page, Subscription name should reflect with Modify and Delete button.
        wait.until(EC.visibility_of_element_located((By.ID, 'jobs_table')))
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

    # ==================================C773==========07 Jan===================================

    def test_FullfilmentVerifyContentOfSubscription_C773(self, impersonate_fullfilment):
        # Verify the content of  subscription.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
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
        # Report: Out of Stock (Title) top left side of the page
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'panel-heading')))
        # Click on Make a subscription button right side of the page.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()
        # Verify the content on the subscription form
        wait.until(EC.visibility_of_element_located((By.ID, 'myModalLabel')))
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
        driver.find_element_by_id("next_btn").click()
        time.sleep(1)

    # ==================================C786==========07 Jan===================================
    def test_FullfilmentVerifyDefaultEmailIdDisplay_C786(self, impersonate_fullfilment):
        # Verify user email Id display by default in subscription form.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
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
        # Report: Out of Stock (Title) top left side of the page
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'panel-heading')))
        # Click on Make a subscription button right side of the page.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()
        # Verify the content on the subscription form
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        # Verify the Email To text box.
        expected_email = "vlucero@ggoutfitters.com"
        actual_email = driver.find_element_by_id("email").get_attribute("value")
        assert expected_email in actual_email

    # ====================================C809====07Jan==========================================================

    def test_FullfilmentVerifyContentOfGeneratedReport_C809(self, impersonate_fullfilment):
        # Verify content of generated report.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
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
        time.sleep(1)

        # Verify Inventory Receipts Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Inventory_Receipts_Report = "Inventory Receipts Report "
        actual_header_Inventory_Receipts_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_Receipts_Report in expected_header_Inventory_Receipts_Report
        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("CustomerNumber"))
        select.select_by_visible_text("ARPM")
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
        wait.until(EC.visibility_of_element_located((By.ID, 'RcvSlip')))
        driver.find_element_by_id("RcvSlip").send_keys("PO00012028-1")
        expected_po_number = "PO00012028-1"
        actual_po_number = driver.find_element_by_id("RcvSlip").get_attribute("value")
        assert actual_po_number in expected_po_number
        # Click on Generate report button.
        driver.find_element_by_class_name("btn-success").click()
        # Verify the Date and Time of the generated report.
        driver.switch_to_frame("report_src")
        # Verify the first page - wait until report time is shown
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(10)
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
        exp_content = ['SKU', 'Description', 'PO', 'Issue', 'Date', 'Due Date', 'Date Received', 'Qty on Order',
                       'Qty Received', 'Vendor', 'PO Number', 'Received By']
        for v in exp_content:
            assert v in act

    # ====================================C810====07Jan==========================================================

    def test_FullfilmentVerifyContentOfSubscriptionForm_C810(self, impersonate_fullfilment):
        # Verify content of  Subscription form.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
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
        time.sleep(1)
        # Verify Inventory Receipts Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()
        # Verify Subscription Name
        wait.until(EC.visibility_of_element_located((By.ID, 'sub_name')))
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
        # Collect all checkbox elements
        actual_days = driver.find_elements_by_class_name("checkbox")
        time.sleep(1)
        # Search checkbox elements in expected days
        for day in actual_days:
            name = day.text
            assert name in expected_days
        # Verify back button
        driver.find_element_by_class_name("btn-default").is_displayed()
        # Verify save Subscription button
        driver.find_element_by_id("next_btn").is_displayed()

    # ====================================C812====07Jan==========================================================
    def test_FullfilmentVerifyEmailIdDisplayByDefaultInSubscriptionForm_C812(self, impersonate_fullfilment):
        # Verify user Email Id display by default in subscription form.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
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
        time.sleep(1)
        # Verify Inventory Receipts Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()

        # Verify the "Email To" text box.
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        exp_value = "vlucero@ggoutfitters.com"
        actual_value = driver.find_element_by_id("email").get_attribute("value")
        assert exp_value in actual_value

    # ================================08 Jan================================================================
    # ==================================C787==========08 Jan===================================
    def test_FullfilmentVerifyBackButtonFunctionality_C787(self, impersonate_fullfilment):
        #  Verify Back button functionality
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
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
        # Report: Out of Stock (Title) top left side of the page
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'panel-heading')))
        # Click on Make a subscription button right side of the page.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()
        # Verify the content on the subscription form
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        random_number = str(randint(10, 999))
        name = "TestGSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        # Click on Back button at the bottom of the page.
        driver.find_element_by_class_name("btn-default").click()
        # User should redirect to the Open Purchase Orders Report page.
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header = "Open Purchase Orders Report"
        actual_header = driver.find_element_by_id("content-header").text
        assert expected_header in actual_header
        assert driver.find_element_by_id("sub_name").is_displayed() == 0

    # ==================================C880==========08 Jan===================================
    def test_FullfilmentVerifyContentsOnInventoryByBusinessUnit_C880(self, impersonate_fullfilment):
        #  To verify the contents on Inventory By Business Unit
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory by Business Unit
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory by Business Unit')))
        driver.find_element_by_link_text("Inventory by Business Unit").click()
        time.sleep(1)
        # Verify the contents on Inventory by Business Unit Report page.
        # Report: Inventory by Business Unit (label)
        wait.until(EC.visibility_of_element_located((By.ID, 'criteria')))
        expected_report_label = "Report: Inventory by Business Unit"
        actual_report_label = driver.find_element_by_id("criteria").text
        assert expected_report_label in actual_report_label
        # Business Units(button/dropdown)
        expected_bu_dropdown = "select"
        actual_bu_dropdown = driver.find_element_by_id("BU").tag_name
        assert expected_bu_dropdown in actual_bu_dropdown
        # Product Class: (label)
        time.sleep(1)
        expected_product_label = "Product Class:"
        actual_product_label = driver.find_element_by_class_name("radio").text
        assert expected_product_label in actual_product_label
        # Generate report(button)
        assert driver.find_element_by_id("sub_btn").is_displayed()
        # Make a subscription(button)
        assert driver.find_element_by_class_name("btn-primary").is_displayed()

    # ==================================C881==========08 Jan===================================
    def test_FullfilmentVerifyGenerateButtonFunctionality_C881(self, impersonate_fullfilment):
        #  To verify the generate button Functionality
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory by Business Unit
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory by Business Unit')))
        driver.find_element_by_link_text("Inventory by Business Unit").click()
        time.sleep(1)
        # Report: Inventory by Business Unit (label)
        wait.until(EC.visibility_of_element_located((By.ID, 'criteria')))
        # Verify the contents on Inventory by Business Unit Report page.
        expected_report_label = "Report: Inventory by Business Unit"
        actual_report_label = driver.find_element_by_id("criteria").text
        assert expected_report_label in actual_report_label
        # Business Units(button/dropdown)
        expected_bu_dropdown = "select"
        actual_bu_dropdown = driver.find_element_by_id("BU").tag_name
        assert expected_bu_dropdown in actual_bu_dropdown
        # Product Class: (label)
        expected_product_label = "Product Class:"
        actual_product_label = driver.find_element_by_class_name("radio").text
        assert expected_product_label in actual_product_label
        # Generate report(button)
        assert driver.find_element_by_id("sub_btn").is_displayed()
        # Make a subscription(button)
        assert driver.find_element_by_class_name("btn-primary").is_displayed()
        driver.find_element_by_id("sub_btn").click()
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(10)
        assert driver.find_element_by_id("ReportViewerForm").is_displayed()

    # ==================================C813==========08 Jan===================================
    def test_FullfilmentVerifyBackButtonFunctionalityOnSubscriptionForm_C813(self, impersonate_fullfilment):
        # Verify the Back button functionality on Subscription form
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
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
        time.sleep(1)
        # Verify Inventory Receipts Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()

        # Verify the "Email To" text box.
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        exp_value = "vlucero@ggoutfitters.com"
        actual_value = driver.find_element_by_id("email").get_attribute("value")
        assert exp_value in actual_value
        random_number = str(randint(10, 999))
        name = "TestBSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        # Click on Back button at the bottom of the page.
        driver.find_element_by_class_name("btn-default").click()

        # User should redirect to Inventory Receipts Report  page.
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header = "Inventory Receipts Report"
        actual_header = driver.find_element_by_id("content-header").text
        assert expected_header in actual_header
        assert driver.find_element_by_id("sub_name").is_displayed() == False

    # ================================C814==========08 Jan=============================================
    def test_FullfilmentVerifyInSubscriptionNameOnlyLettersAndNumbersAllowed_C814(self, impersonate_fullfilment):
        #  Verify in "Subscription Name" text box only letters and numbers are allowed
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
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
        time.sleep(1)
        # Verify Inventory Receipts Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))

        # Click on Make a subscription button right side of the page.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()

        # Submit the subscription form with all the details.
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        random_number = str(randint(10, 999))
        name = "TestBSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("next_btn").click()

        # Subscription form submitted successfully and display message Subscription Saved.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'noty_text')))
        expected_message = "Subscription saved."
        actual_message = driver.find_element_by_class_name("noty_text").text
        assert expected_message in actual_message
        time.sleep(1)
        # Verify wrong entry
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        driver.find_element_by_id("sub_name").send_keys("*%&")
        driver.find_element_by_id("next_btn").click()
        time.sleep(1)
        # Verify expected message after wrong entry "Only use letters and numbers.".
        expected_message = "Only use letters and numbers."
        actual_message = driver.find_element_by_id("sub_name").get_attribute("title")
        assert expected_message in actual_message
        driver.find_element_by_class_name("btn-default").click()
        time.sleep(1)

    # ================================C815==========08 Jan=============================================================
    def test_FullfilmentVerifyRefreshButtonFunctionalityInReport_C815(self, impersonate_fullfilment):
        #  Verify refresh button functionality in the report
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
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
        time.sleep(1)
        # Verify Inventory Receipts Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Inventory_Receipts_Report = "Inventory Receipts Report "
        actual_header_Inventory_Receipts_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_Receipts_Report in expected_header_Inventory_Receipts_Report
        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("CustomerNumber"))
        select.select_by_visible_text("ARPM")
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
        wait.until(EC.visibility_of_element_located((By.ID, 'RcvSlip')))
        driver.find_element_by_id("RcvSlip").send_keys("PO00012028-1")
        expected_po_number = "PO00012028-1"
        actual_po_number = driver.find_element_by_id("RcvSlip").get_attribute("value")
        assert actual_po_number in expected_po_number
        # Click on Generate report button.
        driver.find_element_by_class_name("btn-success").click()
        # Verify the Date and Time of the generated report.
        driver.switch_to_frame("report_src")
        # Get content before refresh - wait for report time to show
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(10)
        original_text = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        # Click on Refresh icon.
        driver.find_element_by_name("ReportViewerControl$ctl05$ctl05$ctl00$ctl00$ctl00").click()
        time.sleep(5)
        # Generated report should be refreshed.
        latest_text = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        assert (original_text is not latest_text)

    # ==================================C882==========11 Jan====================================================

    def test_FullfilmentVerifyMakeSubscriptionButtonFunctionality_C882(self, impersonate_fullfilment):
        # To verify the  Make a subscription button functionality in  Inventory by Business Unit Report page.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory by Business Unit
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory by Business Unit')))
        driver.find_element_by_link_text("Inventory by Business Unit").click()
        time.sleep(1)
        # Click on "Make a subscription"button right side of the page.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()
        # Subscription for: Inventory by Business Unit Report for ARPM pop up should be displayed.
        wait.until(EC.visibility_of_element_located((By.ID, 'myModalLabel')))
        expected_subscription_label = "Subscription for: Inventory by Business Unit Report for ARPM"
        actual_subscription_label = driver.find_element_by_class_name("modal-content").text
        assert expected_subscription_label in actual_subscription_label

    # ==================================C883==========11 Jan====================================================
    def test_FullfilmentVerifyShowingFunctionality_C883(self, impersonate_fullfilment):
        # Verify Showing 1 of xx entries functionality in generated report.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory by Business Unit
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory by Business Unit')))
        driver.find_element_by_link_text("Inventory by Business Unit").click()
        time.sleep(1)
        # Click on Generate report button.
        wait.until(EC.visibility_of_element_located((By.ID, 'sub_btn')))
        driver.find_element_by_id("sub_btn").click()
        driver.switch_to_frame("report_src")
        # In report, Verify show 1 of x page by default
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(10)
        expected_value = "1"
        actual_value = driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").get_attribute("value")
        assert expected_value in actual_value
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()
        expected_of = "of"
        actual_of = driver.find_element_by_class_name("ToolBarButtonsCell").text
        time.sleep(1)
        assert expected_of in actual_of

    # ==================================C885==========================11 Jan===================================
    def test_FullfilmentVerifySearchFunctionality_C885(self, impersonate_fullfilment):
        # Verify Search functionality in generated report.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory by Business Unit
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory by Business Unit')))
        driver.find_element_by_link_text("Inventory by Business Unit").click()
        time.sleep(1)
        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("BU"))
        select.select_by_visible_text("All")
        # Click on generate report button
        driver.find_element_by_class_name("btn-success").click()
        # Switch to report
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(10)
        # verify valid search
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl00").send_keys("AARP04059")
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

    # =====================================C816==========11 Jan==============================================

    def test_FullfilmentVerifySubmittedSubscriptionInSubscriptionPage_C816(self, impersonate_fullfilment):
        #   Verify submitted subscription show in the "subscription"page.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
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
        time.sleep(1)
        # Verify Inventory Receipts Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        # Click on Make a subscription button right side of the page.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()
        # Submit the subscription form with all the details.
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        random_number = str(randint(10, 999))
        name = "TestBSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("next_btn").click()
        # Subscription form submitted successfully and display message Subscription Saved.
        expected_message = "Subscription saved."
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'noty_text')))
        actual_message = driver.find_element_by_class_name("noty_text").text
        assert expected_message in actual_message

    # ====================================C831=========11 Jan==========================================
    def test_FullfilmentVerifyProductUsageReportPageContent_C831(self, impersonate_fullfilment):
        # Verify the content on "Product Usage Report" page.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
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
        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("customerNumber"))
        select.select_by_visible_text("ARPM")
        # Verify Selection of the client from the drop down.
        actual_selected_option = select.first_selected_option.text
        expected_selection_option = "ARPM"
        assert expected_selection_option in actual_selected_option
        # Verify Selection of no of days.
        select = Select(driver.find_element_by_id("iDays"))
        actual_selected_option = select.first_selected_option.text
        expected_selection_option = "7 Days"
        assert expected_selection_option in actual_selected_option
        # Verify Make a subscription button right side of the page.
        driver.find_element_by_class_name("btn-primary").is_displayed()
        # Verify generate report button.
        driver.find_element_by_id("sub_btn").is_displayed()

    # ========================================C832==========11 Jan================================================
    def test_FullfilmentVerifyGenerateReportButtonFunctionality_C832(self, impersonate_fullfilment):
        # Verify Generate Report button functionality.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
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
        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("customerNumber"))
        select.select_by_visible_text("ARPM")
        actual_selected_option = select.first_selected_option.text
        expected_selection_option = "ARPM"
        assert expected_selection_option in actual_selected_option
        # Verify Selection of no of days.
        select = Select(driver.find_element_by_id("iDays"))
        actual_selected_option = select.first_selected_option.text
        expected_selection_option = "7 Days"
        assert expected_selection_option in actual_selected_option
        # Click on generate report button
        driver.find_element_by_id("sub_btn").click()
        # Switch to report content.
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerControl_ctl05_ctl00_First_ctl01_ctl00')))
        time.sleep(15)
        # Verify content of generated report
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_First_ctl01_ctl00").is_displayed()
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Previous_ctl01_ctl00").is_displayed()
        time.sleep(1)

    # ==================================C887==========12 Jan===================================

    def test_FullfilmentVerifyDateTimeOfGeneratedReport_C887(self, impersonate_fullfilment):
        # Verify Date and Time of generated Report.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)

        # Click on Inventory by Business Unit
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory by Business Unit')))
        driver.find_element_by_link_text("Inventory by Business Unit").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        # Select the client from the drop down
        clients = driver.find_element_by_id("BU")
        client_option = "All"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Click on Generate report button
        driver.find_element_by_id("sub_btn").click()
        # Verify the Date and Time of the generated report
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(5)
        actual_dateTime = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        time.sleep(1)
        exp_dateTime = "Report Created On"
        exp_dateTime1 = "AM"
        exp_dateTime2 = "PM"
        exp_dateTime3 = ":"
        assert exp_dateTime in actual_dateTime
        assert ((exp_dateTime1 in actual_dateTime) | (exp_dateTime2 in actual_dateTime)) & (exp_dateTime3 in actual_dateTime)

    # ==================================C888==========12 Jan===================================
    def test_FullfilmentVerifyContentOfGeneratedReport_C888(self, impersonate_fullfilment):
        # Verify the content of generated Report.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)

        # Click on Inventory by Business Unit
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory by Business Unit')))
        driver.find_element_by_link_text("Inventory by Business Unit").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        # Select the client from the drop down
        clients = driver.find_element_by_id("BU")
        client_option = "All"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Click on Generate report button.
        driver.find_element_by_class_name("btn-success").click()
        # Verify the Date and Time of the generated report.
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(5)
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
        exp_content = ['Premium', 'Business Unit', 'Premium Description', 'Total', 'Total All Business Units']
        for content in exp_content:
            assert content in act

    # ==================================C890==========12 Jan===================================

    def test_FullfilmentVerifyEmailIdDisplayByDefault_C890(self, impersonate_fullfilment):
        # Verify user Email Id display by default in subscription form.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory by Business Unit
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory by Business Unit')))
        driver.find_element_by_link_text("Inventory by Business Unit").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        # Click on Make a subscription button right side of the page.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()
        # Verify the Email To text box.
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        expected_email = "vlucero@ggoutfitters.com"
        actual_email = driver.find_element_by_id("email").get_attribute("value")
        assert expected_email in actual_email

    # ========================================C833==========12 Jan==========================================
    def test_FullfilmentVerifyShowing1OfXXEntriesFunctionality_C833(self, impersonate_fullfilment):
        # Verify Showing 1 of 'xx' entries functionality in generated report.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
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
        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("customerNumber"))
        select.select_by_visible_text("ARPM")
        # Click on Generate report button.
        driver.find_element_by_id("sub_btn").click()
        # Switch to report content
        driver.switch_to_frame("report_src")
        # In report, Verify show 1 of xx page by default
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerForm')))
        # Verify current page and total pages are displayed
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl00_CurrentPage')))
        time.sleep(1)
        expected_value = "1"
        actual_value = driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").get_attribute("value")
        assert expected_value in actual_value
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()
        expected_of = "of"
        actual_of = driver.find_element_by_class_name("ToolBarButtonsCell").text
        assert expected_of in actual_of
        time.sleep(1)

    # ========================================C835==========12 Jan===================================
    def test_FullfilmentVerifySearchFunctionality_C835(self, impersonate_fullfilment):
        # Verify Search functionality in generated report.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
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
        expected_header_Inventory_Receipts_Report = "Product Usage Report"
        actual_header_Inventory_Receipts_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_Receipts_Report in expected_header_Inventory_Receipts_Report

        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("customerNumber"))
        select.select_by_visible_text("ARPM")

        # Click on Generate report button.
        driver.find_element_by_id("sub_btn").click()
        # Switch to report content
        driver.switch_to_frame("report_src")
        # Verify the ReportViewerForm displayed for report
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerForm')))
        # Verify search text input is displayed
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(1)

        # Send and Verify valid entry that can be searched
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl00").send_keys("AARP00933")
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl01").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerForm')))
        time.sleep(7)

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

    # ===================================C836==========12 Jan======================================
    def test_FullfilmentVerifyExportButtonFunctionality_C836(self, impersonate_fullfilment):
        #  Verify Export button functionality in generated report
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
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
        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("customerNumber"))
        select.select_by_visible_text("ARPM")
        # Click on Generate report button.
        driver.find_element_by_id("sub_btn").click()
        # Switch to report content
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(1)
        # Verify report content
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_displayed()
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl04_ctl00_ButtonLink").click()
        # Verify report can be exported in following format
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'HoverButton')))
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
            time.sleep(1)

    # ==================================C904==========13 Jan===================================

    def test_FullfilmentVerifyBackButtonFunctionality_C904(self, impersonate_fullfilment):
        # Verify the Back button Functionality.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory by Business Unit
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory by Business Unit')))
        driver.find_element_by_link_text("Inventory by Business Unit").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        # Click on Make a subscription button right side of the page.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        random_number = str(randint(10, 999))
        name = "TestGSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        # Click on Back button at the bottom of the page.
        driver.find_element_by_class_name("btn-default").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        # User should redirect to the Open Purchase Orders Report page.
        expected_header = "Inventory by Business Unit Report"
        actual_header = driver.find_element_by_id("content-header").text
        assert expected_header in actual_header
        assert driver.find_element_by_id("sub_name").is_displayed() == 0

    # ==================================C906==========13 Jan================================================

    def test_FullfilmentVerifyRefreshButtonFunctionality_C906(self, impersonate_fullfilment):
        # Verify refresh button Functionality.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory by Business Unit
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory by Business Unit')))
        driver.find_element_by_link_text("Inventory by Business Unit").click()
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        # Click on Generate report button
        driver.find_element_by_id("sub_btn").click()
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(5)
        original_text = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        # Click on Refresh icon.
        driver.find_element_by_name("ReportViewerControl$ctl05$ctl05$ctl00$ctl00$ctl00").click()
        wait.until(EC.element_to_be_clickable((By.NAME, 'ReportViewerControl$ctl05$ctl05$ctl00$ctl00$ctl00')))
        time.sleep(1)
        # Generated report should be refreshed.
        latest_text = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        assert (original_text is not latest_text)

    # ==================================C907==========13 Jan===================================
    def test_FullfilmentVerifySubmittedSubscription_C907(self, impersonate_fullfilment):
        # Verify submitted subscription show in the subscription page.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Inventory by Business Unit
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory by Business Unit')))
        driver.find_element_by_link_text("Inventory by Business Unit").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        # Click on Make a subscription button right side of the page.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        # Submit the subscription form with all the details.
        random_number = str(randint(10, 999))
        name = "TestGSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        driver.find_element_by_id("next_btn").click()
        # Subscription form submitted successfully and display message Subscription Saved.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'noty_text')))
        expected_message = "Subscription saved."
        actual_message = driver.find_element_by_class_name("noty_text").text
        assert expected_message in actual_message

        # Click on Subscriptions Page
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Subscriptions')))
        driver.find_element_by_link_text("Subscriptions").click()

        # On subscriptions page, Subscription name should reflect with Modify and Delete button.
        wait.until(EC.visibility_of_element_located((By.ID, 'jobs_table')))
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


    # ===================================C837==========13 Jan======================================

    def test_FullfilmentVerifyDateAndTimeInReport_C837(self, impersonate_fullfilment):
        #  Verify Date and Time of generated report.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
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
        # Verify Product Usage Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Inventory_Receipts_Report = "Product Usage Report"
        actual_header_Inventory_Receipts_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_Receipts_Report in expected_header_Inventory_Receipts_Report
        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("customerNumber"))
        select.select_by_visible_text("ARPM")
        # Click on Generate report button.
        driver.find_element_by_id("sub_btn").click()
        # Switch to report
        driver.switch_to_frame("report_src")
        # Verify the ReportViewerForm displayed for report
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerForm')))
        # Verify search text input is displayed
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(1)
        actual_date_Time = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        exp_date_Time = "Report Created On:"
        exp_date_Time1 = "AM"
        exp_date_Time2 = "PM"
        assert exp_date_Time in actual_date_Time
        assert ((exp_date_Time1 in actual_date_Time) | (exp_date_Time2 in actual_date_Time))

    # ===================================C838==========13 Jan======================================
    def test_FullfilmentVerifyContentOfGeneratedReport_C838(self, impersonate_fullfilment):
        # Verify the content of generated report.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
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
        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("customerNumber"))
        select.select_by_visible_text("ARPM")
        # Click on Generate report button.
        driver.find_element_by_id("sub_btn").click()
        # Switch to report content
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(5)
        # Verify the first page
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_First_ctl01_ctl00").is_displayed()
        # Verify the Previous page
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Previous_ctl01_ctl00").is_displayed()
        # Verify the current page text box
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_displayed()
        # Verify the  Total Pages
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()

        # Verify the Next Page link
        if driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Next_ctl01_ctl00").is_displayed():
            assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Next_ctl01_ctl00").is_displayed()
        else:
            assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Next_ctl00_ctl00").is_displayed()

        # Verify the Last Page link
        if driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Last_ctl01_ctl00").is_displayed():
            assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Last_ctl01_ctl00").is_displayed()
        else:
            assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Last_ctl00_ctl00").is_displayed()

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
        exp_content = ['SKU', 'Description', 'Quantity Fulfilled', 'Average Usage per Day', 'Quantity on Hand',
                       'Days of Inventory']
        for v in exp_content:
            assert v in act

    # ===================================C839==========13 Jan======================================

    def test_FullfilmentVerifyContentOfSubscriptionForm_C839(self, impersonate_fullfilment):
        # Verify the content of Subscription form.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
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
        # Verify Product Usage Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        # Click on make a Subscription button
        driver.find_element_by_class_name("btn-primary").click()
        # Verify Subscription Name
        wait.until(EC.visibility_of_element_located((By.ID, 'sub_name')))
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
        for day in actual_days:
            name = day.text
        assert name in expected_days
        # Verify back button
        assert driver.find_element_by_class_name("btn-default").is_displayed()
        # Verify save Subscription button
        assert driver.find_element_by_id("next_btn").is_displayed()

    # ==================================C872==========14 Jan===================================

    def test_FullfilmentVerifyContentInOpenOrders_C872(self, impersonate_fullfilment):
        # Verify content in Open Orders by Business Unit report page.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Orders tab. fa-folder-open-o
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'fa-folder-open-o')))
        orders = driver.find_elements_by_link_text("Orders")
        orders[1].click()
        time.sleep(1)
        # Click on Open Orders by Business Unit
        #wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Open Orders by Business Unit')))
        driver.find_element_by_link_text("Open Orders by Business Unit").click()
        time.sleep(1)
        # Verify content in Open Orders by Business Unit page.
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_report_heading = "Open Orders by Business Unit Report"
        actual_report_heading = driver.find_element_by_id("content-header").text
        assert expected_report_heading in actual_report_heading
        # Report: Open Orders by Business Unit(label)
        wait.until(EC.visibility_of_element_located((By.ID, 'criteria')))
        expected_report_label = "Report: Open Orders by Business Unit"
        actual_report_label = driver.find_element_by_id("criteria").text
        assert expected_report_label in actual_report_label
        # Business Units(button/drop down)
        expected_bu_dropdown = "select"
        actual_bu_dropdown = driver.find_element_by_id("BU").tag_name
        time.sleep(1)
        assert expected_bu_dropdown in actual_bu_dropdown
        # Generate report(button)
        assert driver.find_element_by_id("sub_btn").is_displayed()
        # Make a subscription(button)
        assert driver.find_element_by_class_name("btn-primary").is_displayed()

    # ==================================C873==============================14 Jan===================================

    def test_FullfilmentVerifyCancelButtonFunctionality_C873(self, impersonate_fullfilment):
        # Verify cancel button functionality in loading bar in  Open Orders by Business Unit page.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Orders tab. fa-folder-open-o
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'fa-folder-open-o')))
        orders = driver.find_elements_by_link_text("Orders")
        orders[1].click()
        time.sleep(1)
        # Click on Open Orders by Business Unit
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Open Orders by Business Unit')))
        driver.find_element_by_link_text("Open Orders by Business Unit").click()
        time.sleep(1)
        # Verify content in Open Orders by Business Unit page.
        # Open Orders by Business Unit Report(heading)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        # Select any drop down value for Business Unit
        entry_sel = Select(driver.find_element_by_name("BU"))
        entry_sel.select_by_index(1)
        # Click on generate report button.
        driver.find_element_by_id("sub_btn").click()
        driver.switch_to_frame("report_src")
        # Check visibility of Cancel report link in popup.
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Cancel')))
        driver.find_element_by_link_text("Cancel").click()
        # Check report does not load by checking total pages
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerControl_ctl05_ctl00_TotalPages')))
        time.sleep(1)
        tp = driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").text
        time.sleep(1)
        assert int(tp) == 0
        time.sleep(1)

    # ==================================C874==========14 Jan===================================
    def test_FullfilmentVerifyContentInSubscription_C874(self, impersonate_fullfilment):
        # Verify content in Subscription for: Open Orders by Business Report for ARPM pop up.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Orders tab.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'fa-folder-open-o')))
        orders = driver.find_elements_by_link_text("Orders")
        orders[1].click()
        time.sleep(1)
        # Click on Open Orders by Business Unit
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Open Orders by Business Unit')))
        driver.find_element_by_link_text("Open Orders by Business Unit").click()
        time.sleep(1)
        # Verify content in Open Orders by Business Unit page.
        # Open Orders by Business Unit Report(heading)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        # Click on Make a subscription button right side of the page.
        driver.find_element_by_class_name("btn-primary").click()
        # Verify the content on the subscription form
        # Verify Subscription Name
        wait.until(EC.visibility_of_element_located((By.ID, 'sub_name')))
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

    # ==================================C841==========14 Jan=====================================================

    def test_FullfilmentVerifyEmailIdDisplayByDefaultInSubscription_C841(self, impersonate_fullfilment):
        # Verify user Email Id display by default in subscription form.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
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

        # Click on "Make a subscription" button right side of the page.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()
        # Verify the "Email To" text box.
        exp_value = "vlucero@ggoutfitters.com"
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        actual_value = driver.find_element_by_id("email").get_attribute("value")
        assert exp_value in actual_value

    # ==================================C842==========14 Jan===================================
    def test_FullfilmentVerifyBackButtonFunctionalityInSubscription_C842(self, impersonate_fullfilment):
        # Verify the Back button functionality on Subscription fom
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
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

        # Click on "Make a subscription" button right side of the page.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        random_number = str(randint(10, 999))
        name = "TestSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        # Click on Back button at the bottom of the page.
        driver.find_element_by_class_name("btn-default").click()
        time.sleep(1)
        # User should redirect to Inventory Receipts Report  page.
        expected_header = "Product Usage Report"
        actual_header = driver.find_element_by_id("content-header").text
        time.sleep(1)
        assert expected_header in actual_header

    # ==================================C856==========14 Jan===================================================

    def test_FullfilmentVerifyInSubscriptionNameOnlyLettersAndNumbersAllowed_C856(self, impersonate_fullfilment):
        # Verify in "Subscription Name" text box only letters and numbers are allowed.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
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
        time.sleep(1)
        assert actual_header in expected_header

        # Click on "Make a subscription" button right side of the page.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        time.sleep(1)
        driver.find_element_by_class_name("btn-primary").click()
        # Verify the "Email To" text box.
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        # Submit the subscription form with all the details.
        random_number = str(randint(10, 999))
        name = "TestBSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("next_btn").click()
        # Subscription form submitted successfully and display message Subscription Saved.
        expected_message = "Subscription saved."
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'noty_text')))
        actual_message = driver.find_element_by_class_name("noty_text").text
        assert expected_message in actual_message

        # Click on Make a subscription button
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        time.sleep(1)
        driver.find_element_by_class_name("btn-primary").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        # Send the text like "*%&" in name box
        driver.find_element_by_id("sub_name").send_keys("*%&")
        driver.find_element_by_id("next_btn").click()
        # Verify expected message
        expected_message = "Only use letters and numbers."
        actual_message = driver.find_element_by_id("sub_name").get_attribute("title")
        assert expected_message in actual_message
        driver.find_element_by_class_name("btn-default").click()

    # ==================================C898==========15 Jan=======================================================

    def test_FullfilmentVerifyContentInOrderProcessingbyKeycode_C898(self, impersonate_fullfilment):
        # Verify content in Order Processing by Keycode
        driver = impersonate_fullfilment['webdriver']
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
        kc = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Order Processing by Keycode')))
        kc.click()
        time.sleep(1)
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
        # Business Units(button/dropdown)
        expected_bu_dropdown = "select"
        actual_bu_dropdown = driver.find_element_by_id("BU").tag_name
        time.sleep(1)
        assert expected_bu_dropdown in actual_bu_dropdown
        # Date range
        assert driver.find_element_by_name("daterange").is_displayed()
        # Generate report(button)
        assert driver.find_element_by_id("sub_btn").is_displayed()
        # Make a subscription(button)
        assert driver.find_element_by_class_name("btn-primary").is_displayed()

    # ==================================C899==========15 Jan=============================================
    def test_FullfilmentVerifyMakeSubscriptionButtonFunctionality_C899(self, impersonate_fullfilment):
        # Verify the make a subscription button functionality
        driver = impersonate_fullfilment['webdriver']
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
        order_linktext = driver.find_elements_by_link_text("Orders")
        order_linktext[1].click()
        time.sleep(1)
        # Click on Open Orders by Business Unit
        kc = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Order Processing by Keycode')))
        kc.click()
        time.sleep(1)
        # Cli k on Make a subscription(button)
        Make_subscription = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        Make_subscription.click()
        # Subscription for: Order Processing by Keycode Report for ARPM pop up should be displayed.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal-content')))
        expected_subscription_label = "Subscription for: Order Processing by Keycode Report for ARPM"
        actual_subscription_label = driver.find_element_by_class_name("modal-content").text
        assert expected_subscription_label in actual_subscription_label
        driver.find_element_by_class_name("btn-default").click()

    # ==================================C902==========15 Jan===============================================
    def test_FullfilmentVerifyMakeSubscriptionButtonFunctionality_C902(self, impersonate_fullfilment):
        # Verify the back button functionality in Subscription
        driver = impersonate_fullfilment['webdriver']
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
        order_linktext = driver.find_elements_by_link_text("Orders")
        order_linktext[1].click()
        time.sleep(1)
        # Click on Open Orders by Business Unit
        kc = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Order Processing by Keycode')))
        kc.click()
        time.sleep(1)

        # Click on Make a subscription(button)
        ms = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        ms.click()
        time.sleep(1)
        # Subscription for: Order Processing by Keycode Report for ARPM pop up should be displayed.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal-content')))
        expected_subscription_label = "Subscription for: Order Processing by Keycode Report for ARPM"
        actual_subscription_label = driver.find_element_by_class_name("modal-content").text
        time.sleep(1)
        assert expected_subscription_label in actual_subscription_label

        # Enter data in all mandatory fields
        wait.until(EC.visibility_of_element_located((By.ID, 'sub_name')))
        random_number = str(randint(10, 999))
        name = "TestSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        # Subscription for: Order Processing by Keycode Report for ARPM pop up should be closed.
        driver.find_element_by_class_name("btn-default").click()
        time.sleep(1)
        # Order Processing by Keycode Report page should be displayed.--Report: Order Processing by Keycode(Label)
        expected_report_label = "Report: Order Processing by Keycode"
        wait.until(EC.visibility_of_element_located((By.ID, 'criteria')))
        actual_report_label = driver.find_element_by_id("criteria").text
        assert expected_report_label in actual_report_label
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Subscriptions')))
        driver.find_element_by_link_text("Subscriptions").click()
        # Subscription should not be display in subscriptions page with correct data
        wait.until(EC.visibility_of_element_located((By.ID, 'jobs_table')))
        sNameNew_value = driver.find_element_by_id("jobs_table").text
        assert name not in sNameNew_value
    # ==================================C857==========15 Jan==================================================
    def test_FullfilmentVerifyRefreshButtonFunctionality_C857(self, impersonate_fullfilment):
        # Verify refresh button functionality in the report.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
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
        time.sleep(1)
        assert actual_header in expected_header

        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("customerNumber"))
        select.select_by_visible_text("ARPM")
        # Click on Generate report button.
        driver.find_element_by_id("sub_btn").click()
        # Switch to  report content.
        wait.until(EC.visibility_of_element_located((By.ID, 'report_src')))
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(5)
        original_text = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        # Click on Refresh icon.
        driver.find_element_by_name("ReportViewerControl$ctl05$ctl05$ctl00$ctl00$ctl00").click()
        # Generated report should be refreshed.
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(1)
        latest_text = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        assert (original_text is not latest_text)

    # ==================================C858==========15 Jan===================================================

    def test_FullfilmentVerifySubmittedSubscriptionShowInSubscription_C858(self, impersonate_fullfilment):
        # Verify submitted subscription show in the "subscription"page.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        time.sleep(1)
        # Click on Operations tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Product Usage.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Product Usage')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Product Usage").click()
        time.sleep(1)
        # Click on Make a subscription button right side of the page.
        subscription_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        subscription_button.click()
        time.sleep(1)
        # Submit the subscription form with all the details.
        random_number = str(randint(10, 999))
        name = "TTSubscription" + random_number
        username = wait.until(EC.visibility_of_element_located((By.ID, 'sub_name')))
        username.send_keys(name)
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("next_btn").click()
        # Subscription form submitted successfully and display message Subscription Saved.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'noty_text')))
        expected_message = "Subscription saved."
        actual_message = driver.find_element_by_class_name("noty_text").text
        assert expected_message in actual_message

    # ==================================C860==========15 Jan===================================
    def test_FullfilmentVerifyDaysDropDownFunctionality_C860(self, impersonate_fullfilment):
        # Verify the "Days" drop down functionality.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        # Click on Operations tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)
        # Click on Product Usage.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Product Usage')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Product Usage").click()
        time.sleep(1)
        # Verify Inventory Receipts Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Inventory_Receipts_Report = "Product Usage Report"
        actual_header_Inventory_Receipts_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_Receipts_Report in expected_header_Inventory_Receipts_Report
        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("customerNumber"))
        select.select_by_visible_text("ARPM")
        # Verify default selection of "7 Days"
        select = Select(driver.find_element_by_id("iDays"))
        actual_selected_option = select.first_selected_option.text
        expected_selection_option = "7 Days"
        assert expected_selection_option in actual_selected_option
        # Verify "Days" drop down available options for selection
        exp_export_option = ['7 Days',
                             '30 Days',
                             '90 Days']
        el = driver.find_element_by_id("iDays")
        options = [x for x in el.find_elements_by_tag_name("option")]
        time.sleep(1)
        for element in options:
            act = element.text
            assert act in exp_export_option

    # ==================================C900==========18 Jan=============================================

    def test_FullfilmentVerifyContentInSubscription_C900(self, impersonate_fullfilment):
        # Verify the content in Subscription for: Order Processing by Keycode
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        # Click on Operations tab.
        Operations = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        Operations.click()
        # Click on Orders tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Orders')))
        time.sleep(1)
        order_linktext = driver.find_elements_by_link_text("Orders")
        order_linktext[1].click()
        time.sleep(1)
        # Click on Open Orders by Business Unit
        kc = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Order Processing by Keycode')))
        kc.click()
        # Click on Make a subscription(button)
        Make_subscription = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        Make_subscription.click()
        time.sleep(1)
        # Verify the content on the subscription form
        # Verify Subscription Name
        wait.until(EC.visibility_of_element_located((By.ID, 'sub_name')))
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

    # ==================================C901==========18 Jan=============================================

    def test_FullfilmentSaveSubscriptionFunctionality_C901(self, impersonate_fullfilment):
        # Verify the save Subscription functionality in Subscription  for: Order Processing by Keycode Report
        # for ARPM pop up  in Reports/Orders/Order Processing by Keycode page.
        driver = impersonate_fullfilment['webdriver']
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
        time.sleep(1)
        # Click Keycode
        onj = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Order Processing by Keycode')))
        onj.click()
        # Click on Make a subscription(button)
        Make_subscription = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        Make_subscription.click()
        # Enter data in all mandatory fields
        wait.until(EC.visibility_of_element_located((By.ID, 'sub_name')))
        random_number = str(randint(10, 999))
        name = "TestGSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        driver.find_element_by_id("next_btn").click()
        # "Subscription saved" message should be displayed.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'noty_text')))
        assert driver.find_element_by_class_name("noty_text").is_displayed()
        # Subscription for: Order Processing by Keycode Report for ARPM pop up should be closed.
        assert driver.find_element_by_name("daterange").is_displayed()
        # Order Processing by Keycode Report page should be displayed.
        assert driver.find_element_by_id("sub_btn").is_displayed()
        # Subscription should be display in subscriptions page with correct data.
        driver.find_element_by_link_text("Subscriptions").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'jobs_table')))
        NameNew_value = driver.find_element_by_id("jobs_table").text
        assert name in NameNew_value

    # ==================================C903==========18 Jan=============================================
    def test_FullfilmentSaveSubscriptionFunctionality_C903(self, impersonate_fullfilment):
        # Verify the save Subscription functionality in Subscription  for: Order Processing by Keycode Report
        # for ARPM pop up  in Reports/Orders/Order Processing by Keycode page.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
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
        time.sleep(1)
        # Verify Inventory Receipts Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Inventory_Receipts_Report = "Inventory Receipts Report "
        actual_header_Inventory_Receipts_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_Receipts_Report in expected_header_Inventory_Receipts_Report
        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("CustomerNumber"))
        select.select_by_visible_text("ARPM")
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
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)
        # Verify PO number selection
        driver.find_element_by_id("RcvSlip").send_keys("PO00012028-1")
        time.sleep(1)
        expected_po_number = "PO00012028-1"
        actual_po_number = driver.find_element_by_id("RcvSlip").get_attribute("value")
        assert actual_po_number in expected_po_number
        # Click on Generate report button.
        driver.find_element_by_class_name("btn-success").click()
        # Verify the Date and Time of the generated report.
        driver.switch_to_frame("report_src")
        # Get content before refresh - wait for report time to show
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(5)
        original_text = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        # Click on Refresh icon.
        driver.find_element_by_name("ReportViewerControl$ctl05$ctl05$ctl00$ctl00$ctl00").click()
        wait.until(EC.visibility_of_element_located((By.NAME, 'ReportViewerControl$ctl05$ctl05$ctl00$ctl00$ctl00')))
        time.sleep(5)
        # Generated report should be refreshed.
        latest_text = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        assert (original_text is not latest_text)

    # ==================================C944==========18 Jan=============================================
    def test_FullfilmentVerifyContentShipmentHistorySummaryReport_C944(self, impersonate_fullfilment):
        # Verify content in Shipment History Summary  Report page
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        # Click on Operations tab
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()

        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Orders.
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Orders").click()
        time.sleep(1)
        # Click Shipment History Summary.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Shipment History Summary')))
        driver.find_element_by_id("operations-orders-report-items").find_element_by_link_text("Shipment History Summary").click()
        time.sleep(1)
        # Verify Shipment History Summary Report  page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Inventory_Receipts_Report = "Shipment History Summary Report"
        actual_header_Inventory_Receipts_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_Receipts_Report in expected_header_Inventory_Receipts_Report
        # Verify client name drop down
        assert driver.find_element_by_id("CustomerNumber").is_displayed()
        # Verify start ship date range displayed
        assert driver.find_element_by_name("daterange").is_displayed()

        # Verify generate report button visible
        assert driver.find_element_by_id("sub_btn").is_displayed()
        # Verify make a subscription button
        assert driver.find_element_by_class_name("btn-primary").is_displayed()

    # ==================================C945==========18 Jan=============================================
    def test_FullfilmentVerifyMakeASubscriptionButton_C945(self, impersonate_fullfilment):
        # Verify the make a subscription button functionality in  Reports/Orders/Shipment History Summary
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        # Click on Operations tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Orders.
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Orders").click()
        time.sleep(1)
        # Click Shipment History Summary.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Shipment History Summary')))
        driver.find_element_by_id("operations-orders-report-items").find_element_by_link_text("Shipment History Summary").click()
        time.sleep(1)
        # Verify Shipment History Summary Report  page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header = "Shipment History Summary Report"
        actual_header = driver.find_element_by_id("content-header").text
        assert expected_header in actual_header

        driver.find_element_by_class_name("btn-primary").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'myModalLabel')))
        expected_Pop_Up = "Subscription for: Shipment History Summary Report for null"
        actual_Pop_Up = driver.find_element_by_id("myModalLabel").text
        assert actual_Pop_Up in expected_Pop_Up

    # ==================================C946==========18 Jan=============================================

    def test_FullfilmentVerifyContentInSubscription_Form_C946(self, impersonate_fullfilment):
        # Verify the content in Subscription for: Shipment History Summary Report for null pop up in
        # Reports/Orders/Shipment History Summary Report page.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Orders.
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Orders").click()
        time.sleep(1)
        # Click Shipment History Summary.
        driver.find_element_by_id("operations-orders-report-items").find_element_by_link_text("Shipment History Summary").click()
        time.sleep(1)
        # Subscription
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        driver.find_element_by_class_name("btn-primary").click()
        # Verify Subscription Name
        wait.until(EC.element_to_be_clickable((By.ID, 'email')))
        assert driver.find_element_by_id("sub_name").is_displayed()
        # Verify Email to field
        assert driver.find_element_by_id("email").is_displayed()
        # Verify Delivery format in excel
        assert driver.find_element_by_class_name("radio").is_displayed()
        # Verify time
        assert driver.find_element_by_id("time").is_displayed()
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
        assert driver.find_element_by_class_name("btn-default").is_displayed()
        # Verify save Subscription button
        assert driver.find_element_by_id("next_btn").is_displayed()
        time.sleep(1)

    # ==================================C935==========19 Jan=============================================


    def test_FullfilmentVerifyContentInOrderHistorySummaryReport_C935(self, impersonate_fullfilment):
        # Verify content in Order History Summary Report page
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        # Click on Operations tab.
        Operations = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        Operations.click()
        time.sleep(1)
        # Click on Orders tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Orders')))
        time.sleep(1)
        order_linktext = driver.find_elements_by_link_text("Orders")
        order_linktext[1].click()
        time.sleep(1)
        # Click
        Order_History_Summary = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Order History Summary')))
        Order_History_Summary.click()
        time.sleep(1)
        # Verify Report(heading)
        expected_report_heading = "Order History Summary"
        Order_Processing_by_Keycode = wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_report_heading = Order_Processing_by_Keycode.text
        assert expected_report_heading in actual_report_heading
        # Report: Order History Summary(Label)
        expected_report_label = "Report: Order History Summary"
        actual_report_label = driver.find_element_by_id("criteria").text
        assert expected_report_label in actual_report_label
        # Select Client (button/dropdown)
        expected_bu_dropdown = "select"
        actual_bu_dropdown = driver.find_element_by_id("CustomerNumber").tag_name
        assert expected_bu_dropdown in actual_bu_dropdown
        # Verify start ship date range displayed
        assert driver.find_element_by_name("daterange").is_displayed()
        # Generate report(button)
        assert driver.find_element_by_id("sub_btn").is_displayed()
        # Make a subscription(button)
        assert driver.find_element_by_class_name("btn-primary").is_displayed()

        # Unshipped(button/dropdown) all by default
        assert driver.find_element_by_id("Unshipped").is_displayed()
        # Client Order #: (textfield)
        assert driver.find_element_by_id("OrderNumber").is_displayed()
        # Ship Service: (textfield)
        assert driver.find_element_by_id("shipvia").is_displayed()
        # Customer Name: (textfield)
        assert driver.find_element_by_id("customername").is_displayed()

    # ==================================C936==========19 Jan=============================================

    def test_FullfilmentVerifyMakeSubscriptionButtonFunctionality_C936(self, impersonate_fullfilment):
        # Verify the make a subscription button functionality
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        # Click on Operations tab.
        Operations = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        Operations.click()
        time.sleep(1)
        # Click on Orders tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Orders')))
        time.sleep(1)
        order_linktext = driver.find_elements_by_link_text("Orders")
        order_linktext[1].click()
        time.sleep(1)
        # Click on order history
        Order_History_Summary = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Order History Summary')))
        Order_History_Summary.click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        # Click on make a subscription button.
        driver.find_element_by_class_name("btn-primary").click()
        Order_History_Summary = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal-title')))
        expected_title = "Order History Summary Report for null"
        actual_title = driver.find_element_by_class_name("modal-title").text
        assert expected_title in actual_title

    # ==================================C937==========19 Jan=============================================

    def test_FullfilmentVerifyContentInSubscription_C937(self, impersonate_fullfilment):
        # Verify the content in Subscription for: Order History Summary Report
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        # Click on Operations tab.
        Operations = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        Operations.click()
        time.sleep(1)
        # Click on Orders tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Orders')))
        time.sleep(1)
        order_linktext = driver.find_elements_by_link_text("Orders")
        order_linktext[1].click()
        # Click on Order History
        Order_History_Summary = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Order History Summary')))
        Order_History_Summary.click()
        time.sleep(1)
        # Click on make a subscription button.
        driver.find_element_by_class_name("btn-primary").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal-title')))
        # Verify the content on the subscription form
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
        actual_days = driver.find_elements_by_class_name("checkbox")
        for day in actual_days:
            name = day.text
            assert name in expected_days
            # Verify back button
        assert driver.find_element_by_class_name("btn-default").is_displayed()
        # Verify save Subscription button
        assert driver.find_element_by_id("next_btn").is_displayed()

    # =================================C947==========19 Jan=============================================

    def test_FullfilmentVerifySaveSubscriptionFunctionality_C947(self, impersonate_fullfilment):
        # Verify the save Subscription functionality in Subscription for: Shipment History Summary Report
        # for null pop up  in Reports/Orders/Shipment History Summary Report page.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        # Click on Operations tab
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Orders.
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Orders").click()
        time.sleep(1)
        # Click Shipment History Summary.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Shipment History Summary')))
        driver.find_element_by_id("operations-orders-report-items").find_element_by_link_text("Shipment History Summary").click()
        time.sleep(1)
        # Click on Make a subscription button right side of the page.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        # Submit the subscription form with all the details.
        random_number = str(randint(10, 999))
        name = "TTSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("next_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'noty_text')))
        # Subscription form submitted successfully and display message Subscription Saved.
        expected_message = "Subscription saved."
        actual_message = driver.find_element_by_class_name("noty_text").text
        assert expected_message in actual_message
        # User should redirect to Shipment History Summary Report  page.
        expected_header = "Shipment History Summary Report"
        actual_header = driver.find_element_by_id("content-header").text
        assert expected_header in actual_header

    # =================================C948==========19 Jan=============================================

    def test_FullfilmentVerifyBackButtonFunctionalityInSubscription_C948(self, impersonate_fullfilment):
        # Verify the back button functionality in Subscription for: Shipment History Summary Report
        # for null pop up in Reports/Orders/Shipment History Summary Report page.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        # Click on Operations tab
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Orders.
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Orders").click()
        time.sleep(1)
        # Click Shipment History Summary.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Shipment History Summary')))
        driver.find_element_by_id("operations-orders-report-items").find_element_by_link_text("Shipment History Summary").click()
        time.sleep(1)
        # Subscription
        driver.find_element_by_class_name("btn-primary").click()
        random_number = str(randint(10, 999))
        name = "TestBSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        # Click on Back button at the bottom of the page.
        driver.find_element_by_class_name("btn-default").click()
        time.sleep(1)
        # User should redirect to Shipment History Summary Report  page.
        expected_header = "Shipment History Summary Report"
        actual_header = driver.find_element_by_id("content-header").text
        assert expected_header in actual_header
        assert driver.find_element_by_id("sub_name").is_displayed() == 0

    # =================================C949==========19 Jan=============================================

    def test_FullfilmentVerifyGenerateReportButtonFunctionality_C949(self, impersonate_fullfilment):
        # Verify the generate report button functionality in Reports/Orders/Shipment History Summary Report.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 300)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        # Click on Operations tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Orders.
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Orders").click()
        time.sleep(1)
        # Click Shipment History Summary.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Shipment History Summary')))
        driver.find_element_by_id("operations-orders-report-items").find_element_by_link_text("Shipment History Summary").click()
        time.sleep(1)
        # Verify Shipment History Summary Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Shipment_History_Report = "Shipment History Summary Report"
        actual_header_Shipment_History_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Shipment_History_Report in expected_header_Shipment_History_Report

        # Select the client from the drop down
        clients = driver.find_element_by_id("CustomerNumber")
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
        # Switch to the generated report.
        driver.switch_to_frame("report_src")
        time.sleep(5)
        wait.until(EC.presence_of_element_located((By.ID, 'ReportViewerControl_ctl05_ctl00_First_ctl01_ctl00')))
        time.sleep(5)
        # Verify report content for the first page
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_First_ctl01_ctl00").is_displayed()
        # Verify report content for the Previous page
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Previous_ctl01_ctl00").is_displayed()


    # ==================================C938==========19 Jan=============================================

    def test_FullfilmentVerifySaveSubscriptionFunctionality_C938(self, impersonate_fullfilment):
        # Verify the save Subscription functionality in Subscription
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        # Click on Operations tab.
        Operations = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        Operations.click()
        time.sleep(1)
        # Click on Orders tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Orders')))
        time.sleep(1)
        order_linktext = driver.find_elements_by_link_text("Orders")
        order_linktext[1].click()
        time.sleep(1)
        # Click on Order History
        Order_History_Summary = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Order History Summary')))
        Order_History_Summary.click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        # Click on make a subscription button.
        driver.find_element_by_class_name("btn-primary").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal-title')))
        # Submit the subscription form with all the details.
        wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        random_number = str(randint(10, 999))
        name = "TestGSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        driver.find_element_by_id("next_btn").click()
        # Subscription form submitted successfully and display message Subscription Saved.
        time.sleep(1)
        expected_message = "Subscription saved."
        actual_message = driver.find_element_by_class_name("noty_text").text
        assert expected_message in actual_message
        # Click on Subscriptions Page
        driver.find_element_by_link_text("Subscriptions").click()
        # On subscriptions page, Subscription name should reflect with Modify and Delete button.
        wait.until(EC.visibility_of_element_located((By.ID, 'jobs_table')))
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

    # =================================C1151==========19 Jan=============================================

    def test_FullfilmentVerifyShowing1OfXXFunctionality_C1151(self, impersonate_fullfilment):
        # Verify Showing 1 of 'xx' entries functionality in generated report.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 100)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        time.sleep(1)
        # Click on Operations tab
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Orders.
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Orders").click()
        time.sleep(1)
        # Click Shipment History Summary.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Shipment History Summary')))
        driver.find_element_by_id("operations-orders-report-items").find_element_by_link_text("Shipment History Summary").click()
        time.sleep(1)
        # Verify Shipment History Summary Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Shipment_History_Report = "Shipment History Summary Report"
        actual_header_Shipment_History_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Shipment_History_Report in expected_header_Shipment_History_Report
        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("CustomerNumber"))
        select.select_by_visible_text("AFNAVY")

        # Select the Ship Start  and ship end date
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
        # Switch to the generated report.
        driver.switch_to_frame("report_src")
        # Verify the ReportViewerForm displayed for report
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerForm')))
        # Verify search text input is displayed
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(1)

        # In report, Verify show 1 of x page by default
        expected_value = "1"
        actual_value = driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").get_attribute("value")
        assert expected_value in actual_value

    # ==================================C939==========21 Jan=============================================

    def test_FullfilmentVerifyBackButtonFunctionality_C939(self, impersonate_fullfilment):
        # Verify the back button functionality in Subscription
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        # Click on Operations tab.
        Operations = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        Operations.click()
        time.sleep(1)
        # Click on Orders tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Orders')))
        time.sleep(1)
        order_linktext = driver.find_elements_by_link_text("Orders")
        order_linktext[1].click()
        time.sleep(1)
        # Click on Order History
        Order_History_Summary = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Order History Summary')))
        Order_History_Summary.click()
        time.sleep(1)
        # Click on make a subscription button.
        driver.find_element_by_class_name("btn-primary").click()
        time.sleep(1)
        random_number = str(randint(10, 999))
        name = "TestGSubscription" + random_number
        driver.find_element_by_id("sub_name").send_keys(name)
        driver.find_element_by_name("days_of_week").click()
        driver.find_element_by_id("email").clear()
        email = "apriest@ggoutfitters.com"
        driver.find_element_by_id("email").send_keys(email)
        # Click on Back button at the bottom of the page.
        driver.find_element_by_class_name("btn-default").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        # User should redirect Report page.
        expected_header = "Order History Summary Report"
        actual_header = driver.find_element_by_id("content-header").text
        assert expected_header in actual_header
        assert driver.find_element_by_id("sub_name").is_displayed() == 0

    # ==================================C943==========21 Jan=============================================

    def test_FullfilmentVerifyGenerateReportButtonFunctionality_C943(self, impersonate_fullfilment):
        # Verify the generate report button functionality
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        # Click on Operations tab.
        Operations = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        Operations.click()
        time.sleep(1)
        # Click on Orders tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Orders')))
        order_linktext = driver.find_elements_by_link_text("Orders")
        order_linktext[1].click()
        time.sleep(1)
        # Click on Order History
        Order_History_Summary = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Order History Summary')))
        Order_History_Summary.click()
        time.sleep(1)
        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("CustomerNumber"))
        select.select_by_visible_text("AFNAVY")
        # Select Dates
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
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-success')))
        driver.find_element_by_class_name("btn-success").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'report_src')))
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(5)
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerForm')))
        assert driver.find_element_by_id("ReportViewerForm").is_displayed()

    # ==================================C1122==========21 Jan=============================================

    def test_FullfilmentVerifyExportButtonFunctionality_C1122(self, impersonate_fullfilment):
        # Verify the export functionality in generated report
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        # Click on Operations tab.
        Operations = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        Operations.click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Orders')))
        # Click on Orders tab.
        order_linktext = driver.find_elements_by_link_text("Orders")
        order_linktext[1].click()
        time.sleep(1)
        Order_History_Summary = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Order History Summary')))
        # Click on Open Order History Summary
        Order_History_Summary.click()
        time.sleep(3)
        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("CustomerNumber"))
        select.select_by_visible_text("AFNAVY")
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
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-success')))
        driver.find_element_by_class_name("btn-success").click()

        wait.until(EC.visibility_of_element_located((By.ID, 'report_src')))
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerForm')))
        time.sleep(5)
        assert driver.find_element_by_id("ReportViewerForm").is_displayed()
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl04_ctl00_ButtonLink").click()
        # Verify report can be exported in following format
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'HoverButton')))
        assert driver.find_element_by_class_name("HoverButton").is_displayed()
        act = driver.find_elements_by_class_name("ActiveLink")
        exp_report_type = ['XML file with report data', 'CSV (comma delimited)', 'PDF', 'MHTML (web archive)', 'Excel',
                           'TIFF file', 'Word']
        for v in act:
            name = v.text
            assert name in exp_report_type

    # ==================================C1123==========21 Jan=============================================

    def test_FullfilmentVerifyRefreshButtonFunctionality_C1123(self, impersonate_fullfilment):
        # Verify the refresh functionality in report generated
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 100)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        # Click on Operations tab.
        Operations = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        Operations.click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Orders')))
        time.sleep(1)
        # Click on Orders tab.
        order_linktext = driver.find_elements_by_link_text("Orders")
        order_linktext[1].click()
        Order_History_Summary = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Order History Summary')))
        # Click on Open Order History Summary
        Order_History_Summary.click()
        time.sleep(1)
        # Click on Generate Report button.
        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("CustomerNumber"))
        select.select_by_visible_text("AFNAVY")
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
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-success')))
        driver.find_element_by_class_name("btn-success").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'report_src')))
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(5)
        # Get content before refresh
        original_text = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        # Click on Refresh icon.
        driver.find_element_by_name("ReportViewerControl$ctl05$ctl05$ctl00$ctl00$ctl00").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        # Generated report should be refreshed.
        latest_text = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        time.sleep(1)
        assert (original_text is not latest_text)

    # ==================================C1155==========21 Jan=============================================

    def test_FullfilmentVerifyRefreshButtonFunctionality_C1155(self, impersonate_fullfilment):
        # Verify the refresh functionality in report generated
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 200)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        # Click on Operations tab.
        Operations = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        Operations.click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Orders')))
        order_linktext = driver.find_elements_by_link_text("Orders")
        order_linktext[1].click()
        time.sleep(1)
        Order_History_Summary = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Order History Summary')))
        # Click on Open Order History Summary
        Order_History_Summary.click()
        time.sleep(4)
        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("CustomerNumber"))
        select.select_by_visible_text("AFNAVY")
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
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-success')))
        driver.find_element_by_class_name("btn-success").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'report_src')))
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(3)
        actual_dateTime = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        exp_dateTime = "Report Created On"
        exp_dateTime1 = "AM"
        exp_dateTime2 = "PM"
        exp_dateTime3 = ":"
        assert exp_dateTime in actual_dateTime
        assert ((exp_dateTime1 in actual_dateTime) | (exp_dateTime2 in actual_dateTime)) & (exp_dateTime3 in actual_dateTime)

    # ==================================C1153==========21 Jan======================================================

    def test_FullfilmentVerifySearchFunctionality_C1153(self, impersonate_fullfilment):
        # Verify Search functionality in generated report.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 300)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        # Click on Operations tab
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Orders.
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Orders").click()
        time.sleep(1)
        # Click Shipment History Summary.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Shipment History Summary')))
        driver.find_element_by_id("operations-orders-report-items").find_element_by_link_text("Shipment History Summary").click()
        time.sleep(1)
        # Verify Shipment History Summary Report page
        expected_header_Shipment_History_Report = "Shipment History Summary Report"
        actual_header_Shipment_History_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Shipment_History_Report in expected_header_Shipment_History_Report
        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("CustomerNumber"))
        select.select_by_visible_text("AFNAVY")
        # Select the Ship Start  and ship end date
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
        # Switch to the generated report.
        driver.switch_to_frame("report_src")
        time.sleep(5)

        # Send and Verify valid entry that can be searched
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(1)
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl00").send_keys("X003964248ARPM")
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl01").click()
        time.sleep(10)

        try:
            WebDriverWait(driver, 60).until(EC.alert_is_present(), 'The search text was not found.')
            alert = driver.switch_to_alert()
            alert.accept()
            found = True
        except NoAlertPresentException as e:
            found = False

        # If no Alert i.e. Search Successful
        if found == False:
            driver.find_element_by_css_selector("span[style='COLOR:highlighttext;BACKGROUND-COLOR:highlight;']").is_displayed()
            # Click on next button to search next if text is found in first search
            wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl03')))
            driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl03").click()
            time.sleep(3)
            try:
                WebDriverWait(driver, 20).until(EC.alert_is_present(), 'The entire report has been searched.')
                alert = driver.switch_to_alert()
                assert alert.text == "The entire report has been searched."
                alert.accept()
                found2 = True
            except NoAlertPresentException as e:
                found2 = False

        # Verify wrong entry could not be searched
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl00").send_keys("test123")
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl01").click()
        try:
            WebDriverWait(driver, 60).until(EC.alert_is_present(), 'The search text was not found.')
            alert = driver.switch_to_alert()
            assert alert.text == "The search text was not found."
            alert.accept()
            found3 = True
        except NoAlertPresentException as e:
            found3 = False


    # ==================================C1154==========21 Jan=============================================

    def test_FullfilmentVerifySearchFunctionality_C1154(self, impersonate_fullfilment):
        # Verify Export button functionality in generated report.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 300)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        # Click on Operations tab
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Orders.
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Orders").click()
        time.sleep(1)
        # Click Shipment History Summary.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Shipment History Summary')))
        driver.find_element_by_id("operations-orders-report-items").find_element_by_link_text("Shipment History Summary").click()
        time.sleep(1)
        # Verify Shipment History Summary Report page
        expected_header_Shipment_History_Report = "Shipment History Summary Report"
        actual_header_Shipment_History_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Shipment_History_Report in expected_header_Shipment_History_Report
        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("CustomerNumber"))
        select.select_by_visible_text("AFNAVY")
        # Select the Ship Start  and ship end date
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
        # Switch to the generated report.
        driver.switch_to_frame("report_src")
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(5)
        assert driver.find_element_by_id("ReportViewerForm").is_displayed()
        # Report Export button
        wait.until(EC.element_to_be_clickable((By.ID, "ReportViewerControl_ctl05_ctl04_ctl00_ButtonLink")))
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl04_ctl00_ButtonLink").click()
        # Verify report can be exported in following format
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

    # ==================================C1156=========22 Jan=============================================

    def test_FullfilmentVerifyContentOfGeneratedReport_C1156(self, impersonate_fullfilment):
        # Verify the content of generated report.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 100)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        # Click on Operations tab
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Orders.
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Orders").click()
        time.sleep(1)
        # Click Shipment History Summary.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Shipment History Summary')))
        driver.find_element_by_id("operations-orders-report-items").find_element_by_link_text("Shipment History Summary").click()
        time.sleep(1)
        # Verify Shipment History Summary Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Shipment_History_Report = "Shipment History Summary Report"
        actual_header_Shipment_History_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Shipment_History_Report in expected_header_Shipment_History_Report

        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("CustomerNumber"))
        select.select_by_visible_text("AFNAVY")

        # Select the Ship Start  and ship end date
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
        # Switch to the generated report.
        driver.switch_to_frame("report_src")
        time.sleep(3)
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(5)
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerForm')))
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
        # Verify refresh button ReportViewerControl$ctl05$ctl05$ctl00$ctl00$ctl00
        assert driver.find_element_by_name("ReportViewerControl$ctl05$ctl05$ctl00$ctl00$ctl00").is_displayed()
        # Verify export to data feed button
        assert driver.find_element_by_name("ReportViewerControl$ctl05$ctl07$ctl00$ctl00$ctl00").is_displayed()
        # Verify expected report content
        act = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        time.sleep(1)
        exp_content = ['Date Ship', 'Customer', 'Order', 'Client Order', 'Customer Name', 'Company', 'E Mail',
                       'Tracking', 'Number of Units', 'Number of Line Items', 'List Freight', 'SHIP VIA']
        for v in exp_content:
            assert v in act

    # ========================================759===========================15 feb===================================
    def test_FulfilmentInventoryOutOfStock_VerifySubscriptionAcceptOnlyNumberAndLetter_C759(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)

        # Open the 'Inventory by Business Unit' page and verify the page opened properly.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Operations')))

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()

        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()

        #Click on 'Out of Stock' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Out of Stock')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Out of Stock").click()

        # Verify 'Out of Stock' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Out of Stock Report"
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

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

    # ========================================756=============================15 feb=================================
    def test_FulfilmentInventoryOutOfStock_VerifyBlankFieldSubscriptionFieldNotSubmitted_C756(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']

        wait = WebDriverWait(driver, 90)

        # Open the 'Inventory by Business Unit' page and verify the page opened properly.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Operations')))

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()

        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()

        #Click on 'Out of Stock' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Out of Stock')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Out of Stock").click()

        # Verify 'Out of Stock' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Out of Stock Report"
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        #Click on make a subscription button.
        wait.until(EC.visibility_of_element_located((By.ID,'subscription_btn')))
        driver.find_element_by_id("subscription_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'modal-title')))

        # Click on submit button and Verify Subscription form remain displaying.
        wait.until(EC.visibility_of_element_located((By.ID,'next_btn')))
        driver.find_element_by_id("next_btn").click()
        assert driver.find_element_by_id("myModalLabel").is_displayed()
        # Note : Error message 'error message " Please fill out this field".' is not verified because id is not found.

    # ========================================752==============================15 feb================================
    def test_FulfilmentInventoryOutOfStock_VerifyContentInGeneratedReport_C752(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']

        wait = WebDriverWait(driver, 90)

        # Open the 'Inventory by Business Unit' page and verify the page opened properly.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Operations')))

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()

        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()

        #Click on 'Out of Stock' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Out of Stock')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Out of Stock").click()

        # Verify 'Out of Stock' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Out of Stock Report"
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        # Select the client from the drop down
        wait.until(EC.visibility_of_element_located((By.ID, 'CustomerNumber')))
        clients = driver.find_element_by_id("CustomerNumber")
        client_option = "AFNAVY"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Click on Generate Report button.
        driver.find_element_by_class_name("btn-success").click()
        # Switch to report-items
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(5)
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
        exp_content = ['Customer Number','SKU','Description','Held Short','Qty. on Order','Next Delivery Date']
        for v in exp_content:
            assert v in act

    # ========================================748==================================15 feb============================
    def test_FulfilmentInventoryOutOfStock_VerifyPagination_C748(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)

        # Open the 'Inventory by Business Unit' page and verify the page opened properly.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Operations')))

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()

        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()

        #Click on 'Out of Stock' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Out of Stock')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Out of Stock").click()

        # Verify 'Out of Stock' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Out of Stock Report"
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        # Select the client from the drop down
        wait.until(EC.visibility_of_element_located((By.ID, 'CustomerNumber')))
        clients = driver.find_element_by_id("CustomerNumber")
        client_option = "AFNAVY"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Click on Generate Report button.
        driver.find_element_by_class_name("btn-success").click()
        # Switch to report-items
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        wait.until(EC.visibility_of_element_located((By.ID,'ReportViewerControl_ctl05_ctl00_First_ctl01_ctl00')))
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


    # ========================================735===================================15 feb===========================
    def test_FulfilmentInventoryInventoryOnHand_VerifySubscriptionAcceptOnlyNumberAndLetter_C735(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)

        # Open the 'Inventory by Business Unit' page and verify the page opened properly.
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

        #Click on 'Out of Stock' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory on Hand')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Inventory on Hand").click()

        # Verify 'Out of Stock' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Inventory on Hand Report"
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        wait.until(EC.visibility_of_element_located((By.ID,'cClientName')))
        select = Select(driver.find_element_by_id("cClientName"))
        select.select_by_visible_text("ARPM")

        # Click on make a subscription button.
        wait.until(EC.visibility_of_element_located((By.ID,'subscription_btn')))
        time.sleep(1)
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

        # Verify the warning message.
        wait.until(EC.visibility_of_element_located((By.ID,'sub_name')))
        expected_message="Only use letters and numbers."
        actual_message=driver.find_element_by_id("sub_name").get_attribute("title")
        assert expected_message in actual_message
        # Close popup
        driver.find_element_by_class_name("btn-default").click()
        time.sleep(1)

    # ========================================767========================16 feb======================================

    def test_FulfilmentInventoryOpenPurchaseOrder_VerifyPagination_C767(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Open the 'Inventory by Business Unit' page and verify the page opened properly.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Operations')))

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()

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
        client_option = "AFNAVY"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Click on Generate Report button.
        driver.find_element_by_class_name("btn-success").click()
        # Switch to report-items
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID,'ReportViewerControl_ctl05_ctl00_First_ctl01_ctl00')))
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

    # ========================================785==============================16 feb================================
    def test_FulfilmentInventoryOpenPurchaseOrder_VerifySubscriptionAccepOnlyLetterAndNumber_C785(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Open the 'Inventory by Business Unit' page and verify the page opened properly.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Operations')))

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()

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
        client_option = "AFNAVY"
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
        expected_message="Only use letters and numbers."
        actual_message=driver.find_element_by_id("sub_name").get_attribute("title")
        assert expected_message in actual_message

    # ========================================770============================16 feb==================================

    def test_FulfilmentInventoryOpenPurchaseOrder_VerifyContentInGeneratedReport_C770(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Open the 'Inventory by Business Unit' page and verify the page opened properly.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Operations')))

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()

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
        client_option = "AFNAVY"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
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
        exp_content = ['PO Issue Date','SKU','Description','Due Date','Qty on Order','Vendor', 'PO Number']
        for v in exp_content:
            assert v in act

    # ========================================811========================17feb======================================

    def test_FulfilmentInventoryInventoryReceipt_VerifySubscriptionNotSubmittedWithBlankField_C811(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)

        # Open the 'Inventory by Business Unit' page and verify the page opened properly.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Operations')))

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()

        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()

        #Click on 'Inventory Receipts' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory Receipts')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Inventory Receipts").click()

        # Verify 'Inventory Receipts' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Inventory Receipts Report"
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
        # Click on make a subscription button.
        wait.until(EC.visibility_of_element_located((By.ID,'subscription_btn')))
        driver.find_element_by_id("subscription_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'modal-title')))

        # Click on submit button and Verify Subscription form remain displaying.
        wait.until(EC.visibility_of_element_located((By.ID,'next_btn')))
        driver.find_element_by_id("next_btn").click()
        time.sleep(1)
        assert driver.find_element_by_id("myModalLabel").is_displayed()
        # Note : Error message 'error message " Please fill out this field".' is not verified because id is not found.

    # ========================================889==========================17feb====================================

    def test_FulfilmentInventoryInventoryBuBusinessUnit_VerifySubscriptionNotSubmittedWithBlankField_C889(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)

        # Open the 'Inventory by Business Unit' page and verify the page opened properly.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT , 'Reports')))
        report.click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Operations')))

        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()

        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()

        # Click on 'Inventory by Business Unit' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory by Business Unit')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Inventory by Business Unit").click()

        # Verify 'Inventory by Business Unit' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Inventory by Business Unit Report"
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        # Verify business report drop down selection
        select = Select(driver.find_element_by_id("BU"))
        select.select_by_visible_text("Alt Media")
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

    # ========================================905================================17feb==============================

    def test_Fulfillment_InventorybyBusinessUnit_SubscriptionNameAcceptOnlyNumberAndLetter_C905(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)

        # Open the 'Inventory by Business Unit' page and verify the page opened properly.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Operations')))
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
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory by Business Unit')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Inventory by Business Unit").click()

        # Verify 'Inventory by Business Unit' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Inventory by Business Unit Report"
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        # Verify business report drop down selection
        select = Select(driver.find_element_by_id("BU"))
        select.select_by_visible_text("Alt Media")

        # Click on make a subscription button.
        wait.until(EC.visibility_of_element_located((By.ID,'subscription_btn')))
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

    # ========================================800===================================17feb===========================

    def test_FulfilmentInventoryInventoryReceipt_VerifyPagination_C800(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Open the 'Inventory by Business Unit' page and verify the page opened properly.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Operations')))
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()

        # Click on 'Inventory Receipts' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory Receipts')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Inventory Receipts").click()

        # Verify 'Inventory Receipts' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Inventory Receipts Report"
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

        po_number = "123"
        # driver.find_element_by_id("RcvSlip").send_keys(po_number)
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
        driver.find_element_by_class_name("btn-success").click()
        # Switch to report-items
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
    # ========================================734====================================17 feb==========================

    def test_FulfilmentInventoryInventoryOnHand_VerifyContentInGeneratedReport_C734(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)

        # Open the 'Inventory by Business Unit' page and verify the page opened properly.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Operations')))

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()

        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()

        #Click on 'Inventory on Hand' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory on Hand')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Inventory on Hand").click()

        # Verify 'Inventory on Hand' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header = "Inventory on Hand Report"
        actual_header = driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        wait.until(EC.visibility_of_element_located((By.ID,'cClientName')))
        select = Select(driver.find_element_by_id("cClientName"))
        select.select_by_visible_text("ARPM")

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
        # Verify the Total Pages
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
        exp_content = ['On Hand','SKU','Description','On Sales','Net Qty','On Order', 'Future Net Stock', 'Next Delivery Date']
        for v in exp_content:
            assert v in act

    # ========================================696================================18feb==============================
    def test_Fulfilment_VerifyOtherUserCantAccessFullFillmentDashboardExceptFullFillmentUser_C696(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
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

    # ========================================774==============================18feb================================
    def test_FulfilmentInventoryOpenPurchaseOrder_VerifySubscriptionNotSubmittedWithBlankField_C774(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)

        # Open the 'Inventory by Business Unit' page and verify the page opened properly.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Operations')))

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()

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
        client_option = "AFNAVY"
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

    # ========================================699===========================18feb===================================
    def test_FulfilmentInventoryInventoryOnHand_VerifySubscriptionNotSubmittedWithBlankField_C699(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)

        # Open the 'Inventory by Business Unit' page and verify the page opened properly.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Operations')))

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()

        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()

        #Click on 'Inventory on Hand' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory on Hand')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Inventory on Hand").click()

        # Verify 'Inventory on Hand' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Inventory on Hand Report"
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        wait.until(EC.visibility_of_element_located((By.ID,'cClientName')))
        select = Select(driver.find_element_by_id("cClientName"))
        select.select_by_visible_text("ARPM")

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

    # ========================================882=========================18feb=====================================
    def test_FulfilmentInventoryInventoryByBusinessUnit_VerifySubscriptionSubmitted_C882(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Open the 'Inventory by Business Unit' page and verify the page opened properly.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Operations')))

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()

        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()

        #Click on 'Inventory Receipts' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory Receipts')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Inventory Receipts").click()

        # Verify 'Inventory Receipts' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Inventory Receipts Report"
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

        # Click on subscription link and verify newly created subscription displayed on subscription page.
        driver.find_element_by_class_name("fa-rss-square").click()
        wait.until(EC.visibility_of_element_located((By.ID,'jobs_table')))
        assert driver.find_element_by_partial_link_text("Modify").is_displayed()
        assert driver.find_element_by_partial_link_text("Delete").is_displayed()
        tableContent = driver.find_element_by_id("jobs_table").text
        assert name in tableContent

    # ========================================897================feb19==============================================

    def test_FulfilmentOrderOpenOrderByBusinessUnit_VerifybackButtonSubscription_C897(self, impersonate_fullfilment):
        # Orders/Open Orders by Business Unit - Verify back button functionality in Subscription for:
        # Open Orders by Business Report .
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)

        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Operations')))

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Orders").click()
        time.sleep(1)
        #Click on 'Inventory by Business Unit' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-orders-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Open Orders by Business Unit')))
        driver.find_element_by_id("operations-orders-report-items").find_element_by_link_text("Open Orders by Business Unit").click()
        time.sleep(1)
        # Verify 'Inventory by Business Unit' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Open Orders by Business Unit Report"
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        # Verify business report drop down selection
        wait.until(EC.visibility_of_element_located((By.ID,'BU')))
        select = Select(driver.find_element_by_id("BU"))
        select.select_by_visible_text("Alt Media")

        #Click on make a subscription button.
        wait.until(EC.visibility_of_element_located((By.ID,'subscription_btn')))
        driver.find_element_by_id("subscription_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'modal-title')))

        expected_header ="Subscription for: Open Orders by Business Report for ARPM"
        actual_header=driver.find_element_by_class_name("modal-title").text
        assert actual_header in expected_header


        driver.find_element_by_class_name("btn-default").click()
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        # User should be redirected to "Open Orders by Business Unit" page successfully.
        assert driver.find_element_by_id("content-header").is_displayed()

    # ========================================840=================feb19=========================================

    def test_Fulfillment_InventoryProductUsage_VerifyBlankFieldOnSuscription_C840(self, impersonate_fullfilment):
        # Reports/operations/Inventory/Product Usage] - Verify with blank fields subscription form not submitted.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Verify Report link
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
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Product Usage')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Product Usage").click()
        time.sleep(1)
        # Verify 'Inventory by Business Unit' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Product Usage Report"
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        # Select the client from the drop down
        wait.until(EC.visibility_of_element_located((By.ID, 'customerNumber')))
        clients = driver.find_element_by_id("customerNumber")
        client_option = "AFNAVY"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break

        #Click on make a subscription button.
        wait.until(EC.visibility_of_element_located((By.ID,'subscription_btn')))
        driver.find_element_by_id("subscription_btn").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'modal-title')))

        expected_header ="Subscription for: Product Usage Report for AFNAVY"
        actual_header=driver.find_element_by_class_name("modal-title").text
        assert actual_header in expected_header

        # Click on submit button and Verify Subscription form remain displaying.
        wait.until(EC.visibility_of_element_located((By.ID,'next_btn')))
        driver.find_element_by_id("next_btn").click()
        time.sleep(1)
        assert driver.find_element_by_id("myModalLabel").is_displayed()
        # Note : Error message 'error message " Please fill out this field".' is not verified because id is not found.

    # ========================================1121==============================================================
    def test_FulfilmentOrderHistorySummaryreport_VerifyContentInGeneratedReport_C1121(self, impersonate_fullfilment):
        #Orders/Order History Summary Report - Verify the content on generated report in Order History Summary Report page.
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Operations')))

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Orders").click()
        time.sleep(1)
        #Click on 'Inventory by Business Unit' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-orders-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Order History Summary')))
        driver.find_element_by_id("operations-orders-report-items").find_element_by_link_text("Order History Summary").click()
        time.sleep(1)
        # Verify 'Inventory by Business Unit' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Order History Summary Report"
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        # Select the client from the drop down
        wait.until(EC.visibility_of_element_located((By.ID, 'CustomerNumber')))
        clients = driver.find_element_by_id("CustomerNumber")
        client_option = "AFNAVY"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
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
        time.sleep(1)
        act = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        exp_content = ['Order Date','SS Order #','Client PO #','Status','Company','Customer Name', 'E Mail', 'Tracking','Shipped Date','Item Sub -Total','Tax','Freight','Order Total']
        for v in exp_content:
            assert v in act

    # ========================================894==============================================================
    def test_FulfilmentOrderOrderByBusinessUnit_VerifyPagination_C894(self, impersonate_fullfilment):
        #Orders/Open Orders by Business Unit - Verify the pagination functionality in report generated in
        # Business unit report tool in Business unit report tool
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)

        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Operations')))

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Orders").click()
        time.sleep(1)
        #Click on 'Inventory by Business Unit' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-orders-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Open Orders by Business Unit')))
        driver.find_element_by_id("operations-orders-report-items").find_element_by_link_text("Open Orders by Business Unit").click()
        time.sleep(1)
        # Verify 'Inventory by Business Unit' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Open Orders by Business Unit Report"
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

    # ========================================882==============================================================
    def test_FulfilmentInventoryInventoryByBusinessUnit_VerifySubscriptionSubmitted_C882(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Open the 'Inventory by Business Unit' page and verify the page opened properly.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Operations')))

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Orders").click()
        time.sleep(1)
        #Click on 'Inventory by Business Unit' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-orders-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Order History Summary')))
        driver.find_element_by_id("operations-orders-report-items").find_element_by_link_text("Order History Summary").click()
        time.sleep(1)
        # Verify 'Inventory by Business Unit' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Order History Summary Report"
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        # Select the client from the drop down
        time.sleep(5)
        wait.until(EC.visibility_of_element_located((By.ID, 'CustomerNumber')))
        clients = driver.find_element_by_id("CustomerNumber")
        client_option = "AFNAVY"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
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

        # Click on Generate Report button.
        driver.find_element_by_class_name("btn-success").click()
        # Switch to report-items
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

    # ======================================1125=======================22 feb====================================
    def test_FulfilmentReportOrderHistorySummaryReport_VerifyPagination_C1125(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        # Click on Operations tab.
        Operations = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        Operations.click()
        time.sleep(1)
        # Click on Orders tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Orders')))
        order_linktext = driver.find_elements_by_link_text("Orders")
        order_linktext[1].click()
        time.sleep(1)
        # Click on Order History
        Order_History_Summary = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Order History Summary')))
        Order_History_Summary.click()
        time.sleep(1)
        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("CustomerNumber"))
        select.select_by_visible_text("ARPM")
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

    # ======================================1152=======================22 feb===========================================

    def test_FulfilmentReportShipmentHistorySummary_VerifyPagination_C1152(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 300)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        # Click on Operations tab
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Orders.
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Orders").click()
        time.sleep(1)
        # Click Shipment History Summary.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Shipment History Summary')))
        driver.find_element_by_id("operations-orders-report-items").find_element_by_link_text("Shipment History Summary").click()
        time.sleep(1)
        # Verify Shipment History Summary Report page
        expected_header_Shipment_History_Report = "Shipment History Summary Report"
        actual_header_Shipment_History_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Shipment_History_Report in expected_header_Shipment_History_Report
        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("CustomerNumber"))
        select.select_by_visible_text("AFNAVY")
        # Select the Ship Start  and ship end date
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
        # Switch to the generated report.
        driver.switch_to_frame("report_src")
        time.sleep(1)
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

    # ======================================834=======================22 feb======================================

    def test_FulfilmentOperationInventoryProductUsage_VerifyPagination_C834(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']

        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
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
        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("customerNumber"))
        select.select_by_visible_text("ARPM")
        # Verify Selection of the client from the drop down.
        actual_selected_option = select.first_selected_option.text
        expected_selection_option = "ARPM"
        assert expected_selection_option in actual_selected_option
        # Verify Selection of no of days.
        select = Select(driver.find_element_by_id("iDays"))
        actual_selected_option = select.first_selected_option.text
        expected_selection_option = "7 Days"
        assert expected_selection_option in actual_selected_option

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

    # ======================================884=======================22 feb=======================================

    def test_FulfilmentOperationInventoryByBusinessUnit_VerifyPagination_C884(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)

        # Click on Inventory by Business Unit
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory by Business Unit')))
        driver.find_element_by_link_text("Inventory by Business Unit").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        # Select the client from the drop down
        clients = driver.find_element_by_id("BU")
        client_option = "All"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break

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

    # ======================================730=======================22 feb================================

    def test_FulfilmentOperationInventoryOnHand_VerifyPagination_C730(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Open the 'Inventory on Hand' page and verify the page opened properly.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Operations')))

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()

        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()

        #Click on 'Inventory on Hand' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory on Hand')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Inventory on Hand").click()

        # Verify 'Inventory on Hand' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Inventory on Hand Report"
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        wait.until(EC.visibility_of_element_located((By.ID,'cClientName')))
        select = Select(driver.find_element_by_id("cClientName"))
        select.select_by_visible_text("ARPM")

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

    # ========================================1157============================24 feb==================================

    def test_Fulfillment_ShipmentHistorySummary_VerifyBlankSubscriptionNotSubmitted_C1157(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # verify Subscription form is not accepted with blank fields on 'Shipment History Summary' page.
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        # Click on Operations tab
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Orders.
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Orders").click()
        time.sleep(1)
        # Click Shipment History Summary.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Shipment History Summary')))
        driver.find_element_by_id("operations-orders-report-items").find_element_by_link_text("Shipment History Summary").click()
        time.sleep(1)
        # Verify Shipment History Summary Report  page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Inventory_Receipts_Report = "Shipment History Summary Report"
        actual_header_Inventory_Receipts_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_Receipts_Report in expected_header_Inventory_Receipts_Report

        driver.find_element_by_class_name("btn-primary").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'myModalLabel')))
        expected_Pop_Up = "Subscription for: Shipment History Summary Report for null"
        actual_Pop_Up = driver.find_element_by_id("myModalLabel").text
        assert actual_Pop_Up in expected_Pop_Up

        # Click on submit button and Verify Subscription form remain displaying.
        wait.until(EC.visibility_of_element_located((By.ID,'next_btn')))
        driver.find_element_by_id("next_btn").click()
        time.sleep(1)
        assert driver.find_element_by_id("myModalLabel").is_displayed()
        # Note : Error message 'error message " Please fill out this field".' is not verified because id is not found.

    # ========================================1504============================24 feb==================================

    def test_Fulfillment_InventoryOutOfStock_VerifySubscriptionAcceptOnlyNumberAndLetter_C759(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # verify Subscription form accept only letter and number on 'Out Of Stock' page.
        wait = WebDriverWait(driver, 90)
        # Open the 'Inventory by Business Unit' page and verify the page opened properly.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Operations')))

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()

        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()

        #Click on 'Out of Stock' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Out of Stock')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Out of Stock").click()

        # Verify 'Out of Stock' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Out of Stock Report"
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        #Click on make a subscription button.
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

    # ============================808============================24 feb============================================

    def test_Fulfillment_InventoryReceipt_VerifyDateAndTimeInGeneratedReport_C808(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # verify  date and time in generated report 'Inventory Receipt' page.
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Subscriptions')))
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Inventory tab.
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        # Click on Inventory Receipts.
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Inventory Receipts").click()
        time.sleep(1)
        # Verify Inventory Receipts Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Inventory_Receipts_Report = "Inventory Receipts Report "
        actual_header_Inventory_Receipts_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_Receipts_Report in expected_header_Inventory_Receipts_Report
        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("CustomerNumber"))
        select.select_by_visible_text("AFNAVY")
        # Select Dates
        wait.until(EC.visibility_of_element_located((By.NAME,'daterange')))
        driver.find_element_by_name("daterange").click()
        time.sleep(1)

        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("02/24/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("02/26/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)
        # Verify PO number selection
        driver.find_element_by_id("RcvSlip").send_keys("535271")
        expected_po_number = "535271"
        actual_po_number = driver.find_element_by_id("RcvSlip").get_attribute("value")
        assert actual_po_number in expected_po_number

        # Click on Generate report button.
        driver.find_element_by_class_name("btn-success").click()
        # Report should be generated successfully on the same page.
        driver.switch_to_frame("report_src")
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        # Verify the Date and Format of the generated report
        actual_dateTime = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text

        label_dateTime = "Report Created on:"
        exp_dateTime1 = "AM"
        exp_dateTime2 = "PM"
        repdate1 = int(time.strftime("%m"))
        repdate2 = int(time.strftime("%d"))
        repdate3 = int(time.strftime("%Y"))
        todays_date = str(repdate1) + "/" + str(repdate2) + "/" + str(repdate3)

        assert todays_date in actual_dateTime
        assert label_dateTime in actual_dateTime
        assert ((exp_dateTime1 in actual_dateTime) | (exp_dateTime2 in actual_dateTime))

    # ========================================1159============================24 feb==================================

    def test_Fulfillment_ShipmentHistorySummary_VerifySubscriptionAcceptOnlyNumberAndLetter_C1159(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # verify Subscription form accept only letter and number on ''Shipment History Summary' page.
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        # Click on Operations tab
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Orders.
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Orders").click()
        time.sleep(1)
        # Click Shipment History Summary.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Shipment History Summary')))
        driver.find_element_by_id("operations-orders-report-items").find_element_by_link_text("Shipment History Summary").click()
        time.sleep(1)
        # Verify Shipment History Summary Report  page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Inventory_Receipts_Report = "Shipment History Summary Report"
        actual_header_Inventory_Receipts_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Inventory_Receipts_Report in expected_header_Inventory_Receipts_Report
        # Subscription
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'myModalLabel')))
        expected_Pop_Up = "Subscription for: Shipment History Summary Report for null"
        actual_Pop_Up = driver.find_element_by_id("myModalLabel").text
        assert actual_Pop_Up in expected_Pop_Up

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
        time.sleep(1)
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

    # ==============================940===============================26 feb=====================
    def test_FulfillmentReport_VerifyContentOnModifySubscriptionForm_C940(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify Content on 'Modify' subscription page.
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        driver.find_element_by_link_text("Subscriptions").click()
        time.sleep(1)
        # Subscription for: Executive Accounts Receivable pop up is displayed.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Modify')))
        driver.find_element_by_link_text("Modify").click()
        time.sleep(1)
        expected_subscription_label = "Subscription for: "
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'modal-content')))
        actual_subscription_label = driver.find_element_by_class_name("modal-content").text
        #print(actual_subscription_label)
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

    # ==============================951===============================26 feb==================================

    def test_FulfillmentReport_VerifyBackButtonFunctionalityInModifySubscription_C951(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify back button functionality on 'Modify' subscription page.
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        driver.find_element_by_link_text("Subscriptions").click()
        time.sleep(1)
        # Subscription for: Executive Accounts Receivable pop up is displayed.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Modify')))
        driver.find_element_by_link_text("Modify").click()
        time.sleep(1)
        expected_subscription_label = "Subscription for: "
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'modal-content')))
        actual_subscription_label = driver.find_element_by_class_name("modal-content").text
        assert expected_subscription_label in actual_subscription_label

        driver.find_element_by_class_name("btn-default").click()
        time.sleep(1)
        assert driver.find_element_by_class_name("modal-content").is_displayed() == False

    # ==============================941===============================26 feb=====================
    def test_FulfillmentReport_VerifySaveButtonFunctionalityInModifySubscription_C941(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify Save button functionality on 'Modify' subscription page.
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        driver.find_element_by_link_text("Subscriptions").click()
        time.sleep(1)

        # Check Records exist i.e. Modify link exists
        if driver.find_element_by_link_text('Modify').is_displayed():
            driver.find_element_by_link_text('Modify').click()
            # Proceed with modification and save
            wait.until(EC.visibility_of_element_located((By.ID, 'myModalLabel')))
            time.sleep(1)
            # Modify Name
            random_number=str(randint(10,999))
            name="TestSubscription"+random_number
            wait.until(EC.visibility_of_element_located((By.ID, 'sub_name')))
            driver.find_element_by_id('sub_name').clear()
            driver.find_element_by_id('sub_name').send_keys(name)
            # Save Subscription
            driver.find_element_by_id('next_btn').click()
            time.sleep(4)
            driver.find_element_by_link_text("Subscriptions").click()
            time.sleep(1)
            # Verify saved Name content-container
            cnt = driver.find_element_by_id('content-container').text
            time.sleep(1)
            # check new subscription name is displayed in table
            assert name in cnt
            time.sleep(1)

    # ==============================1521===============================26 feb==============================

    def test_FulfillmentReport_VerifyGeneratedReportFunctionality_C1521(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify generated report functionality on 'Order History Summary' page.
        wait = WebDriverWait(driver, 90)
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Operations')))

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Orders").click()
        time.sleep(1)
        #Click on 'Order History Summary' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-orders-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Order History Summary')))
        driver.find_element_by_id("operations-orders-report-items").find_element_by_link_text("Order History Summary").click()
        time.sleep(1)
        # Verify 'Order History Summary' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Order History Summary Report"
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        # Select the client from the drop down
        wait.until(EC.visibility_of_element_located((By.ID, 'CustomerNumber')))
        clients = driver.find_element_by_id("CustomerNumber")
        client_option = "AFNAVY"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
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

        # Click on Generate Report button.
        driver.find_element_by_class_name("btn-success").click()
        # Switch to report-items
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_displayed()
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()


    # ==============================843===============================26 feb=====================
    def test_FulfilmentReport_VerifyContentOnSKUValidationPage_C843(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify Content on 'SKU' validation page.
        wait = WebDriverWait(driver, 90)
        driver.find_element_by_link_text("Orders").click()
        driver.find_element_by_link_text("SKU Validation").click()
        expected_header_SKU_Validation = "SKU Validation"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_SKU_Validation = driver.find_element_by_id("content-header").text
        # Verify SKU Validation Header
        assert expected_header_SKU_Validation in actual_header_SKU_Validation
        # Verify Submit button
        assert driver.find_element_by_class_name("btn-success").is_displayed()
        # Verify N Selected Option.
        assert driver.find_element_by_id("amt-selected").is_displayed()
        # Verify Entries picklist
        assert driver.find_element_by_class_name("input-sm").is_displayed()
        # Verify validation table.
        assert driver.find_element_by_id("validation-table").is_displayed()

    # ====================================731==================29 feb============================================

    def test_FulfilmentInventoryOnHand_VerifySearchFunctionality_C731(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify Search functionality in generated report.
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
        # Drop down with pre filled client name like AFNAVY.
        wait.until(EC.visibility_of_element_located((By.ID, 'cClientName')))
        clients = driver.find_element_by_id("cClientName")
        client_option = "AFNAVY"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Click on Generate Report button.
        driver.find_element_by_id("sub_btn").click()
        # Switch to report content
        driver.switch_to_frame("report_src")
        time.sleep(3)
        # Send and Verify valid entry that can be searched AARP04112
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl00").send_keys("AARP04112")
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl01").click()
        time.sleep(5)
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

    # ====================================732==================29 feb============================================
    def test_FulfilmentInventoryOnHand_VerifyExportFunctionality_C732(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify Export functionality in generated report.
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
        clients = driver.find_element_by_id("cClientName")
        client_option = "AFNAVY"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Click on Generate Report button.
        driver.find_element_by_id("sub_btn").click()
        # Switch to report content
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(1)
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_displayed()
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl04_ctl00_ButtonLink").click()
        # Verify report can be exported in following format
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'HoverButton')))
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
        # Note : Due to automation limit we can't verify the exported file.

    # ====================================749==================29 feb============================================

    def test_FulfilmentOutOfStock_VerifySearchFunctionalityInGeneratedReport_C749(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify Search functionality in generated report.
        wait = WebDriverWait(driver, 300)
        # click reports
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Operations')))

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()

        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()

        #Click on 'Out of Stock' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Out of Stock')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Out of Stock").click()

        # Verify 'Out of Stock' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Out of Stock Report"
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        # Select the client from the drop down
        wait.until(EC.visibility_of_element_located((By.ID, 'CustomerNumber')))
        clients = driver.find_element_by_id("CustomerNumber")
        client_option = "AFNAVY"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Click on Generate Report button.
        driver.find_element_by_class_name("btn-success").click()
        # Switch to report content
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        # Send and Verify valid entry that can be searched AARP04112
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl00").send_keys("AARP04112")
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl01").click()
        time.sleep(5)
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

    # ====================================750==================29 feb============================================
    def test_FulfilmentOutOfStock_VerifyExportFunctionality_C750(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify Export functionality in generated report of 'Out OF Stock' page.
        wait = WebDriverWait(driver, 90)

        # Open Report link
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Operations')))

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()

        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()

        #Click on 'Out of Stock' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-inventory-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Out of Stock')))
        driver.find_element_by_id("operations-inventory-report-items").find_element_by_link_text("Out of Stock").click()

        # Verify 'Out of Stock' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Out of Stock Report"
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        # Select the client from the drop down
        wait.until(EC.visibility_of_element_located((By.ID, 'CustomerNumber')))
        clients = driver.find_element_by_id("CustomerNumber")
        client_option = "AFNAVY"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Click on Generate Report button.
        driver.find_element_by_class_name("btn-success").click()
        # Switch to report content
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(1)
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_displayed()
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl04_ctl00_ButtonLink").click()
        # Verify report can be exported in following format
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'HoverButton')))
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
        # Note : Due to automation limit we can't verify the exported file.

    # ====================================778==================29 feb============================================

    def test_FulfilmentInventoryOpenPurchaseOrder_VerifyPagination_C778(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify the contents on View Other Jobs.
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'My Work')))
        driver.find_element_by_link_text("My Work").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Fulfillment')))
        driver.find_element_by_link_text("Fulfillment").click()
        time.sleep(1)
        driver.find_element_by_id("fulfillment-items").find_element_by_link_text("View Jobs").click()
        time.sleep(1)
        driver.find_element_by_id("view-jobs").find_element_by_link_text("Other").click()
        time.sleep(1)

        # Verify Header  page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="View Other Jobs"
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        col = driver.find_element_by_class_name("col-md-3").text
        assert "Available Jobs:" in col
        assert driver.find_element_by_id("job-select").is_displayed()


    # ====================================847==================29 feb============================================

    def test_FulfilmentSKUValidation_VerifyPagination_C847(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify Pagination functionality on 'SKU Validation' page.
        wait = WebDriverWait(driver, 90)
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        driver.find_element_by_link_text("SKU Validation").click()
        time.sleep(1)
        expected_header_SKU_Validation = "SKU Validation"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_SKU_Validation = driver.find_element_by_id("content-header").text
        # Verify SKU Validation Header
        assert expected_header_SKU_Validation in actual_header_SKU_Validation

        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID,'validation-table_previous')))
        time.sleep(4)
        # Verify by default previous button is displayed as disabled.
        expected_disable_previous = "disabled"
        actual_disable_previous = driver.find_element_by_id("validation-table_previous").get_attribute("class")
        assert expected_disable_previous in actual_disable_previous
        expected_current_page_color = "rgba(229, 65, 45, 1)"

        # Ensure page records exist
        cnt = driver.find_element_by_id('validation-table_info').text

        if cnt != 'Showing 0 to 0 of 0 entries':
                # Click on '1' link and verify the pagination functionality.
                actual_current_page_color = driver.find_element_by_link_text("1").value_of_css_property("background-color")
                assert expected_current_page_color in actual_current_page_color
                next_Button = driver.find_element_by_id("validation-table_next").get_attribute("class")

                # Verify link '2' is displayed, if displayed then click and verify pagination functionality. orders_table_next
                if expected_disable_previous not in next_Button:
                    driver.find_element_by_link_text("2").click()
                    time.sleep(5)
                    actual_disable_previous = driver.find_element_by_id("validation-table_previous").get_attribute("class")
                    assert expected_disable_previous not in actual_disable_previous
                    actual_current_page_color = driver.find_element_by_link_text("2").value_of_css_property("background-color")
                    assert expected_current_page_color in actual_current_page_color

                    # Click on '1' link and verify the pagination functionality.
                    driver.find_element_by_link_text("1").click()
                    time.sleep(5)
                    actual_current_page_color = driver.find_element_by_link_text("1").value_of_css_property("background-color")
                    assert expected_current_page_color in actual_current_page_color

                else:
                    actual_disable_previous = driver.find_element_by_id("validation-table_next").get_attribute("class")
                    assert expected_disable_previous in actual_disable_previous


    # ====================================776==================02 march============================================

    def test_FulfilmentMyWorkViewJob_VerifyContentOnActiveJobPage_C776(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify the contents on View Active Jobs page.
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'My Work')))
        driver.find_element_by_link_text("My Work").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Fulfillment')))
        driver.find_element_by_link_text("Fulfillment").click()
        time.sleep(1)
        driver.find_element_by_id("fulfillment-items").find_element_by_link_text("View Jobs").click()
        time.sleep(1)
        driver.find_element_by_id("view-jobs").find_element_by_link_text("Active").click()
        time.sleep(1)

        # Verify 'View Active Jobs' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="View Active Jobs"
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        col = driver.find_element_by_class_name("col-md-3").text
        assert "Available Jobs:" in col
        assert driver.find_element_by_id("job-select").is_displayed()

    # ====================================849==================02 march============================================

    def test_FulfillmentSKUValidation_VerifyPermissionAccessMessage_C849(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify the order id page of any order in Orders/SKU Validation Page.
        wait = WebDriverWait(driver, 90)
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Orders')))
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        driver.find_element_by_link_text("SKU Validation").click()
        time.sleep(1)
        expected_header_SKU_Validation = "SKU Validation"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_SKU_Validation = driver.find_element_by_id("content-header").text
        # Verify SKU Validation Header
        assert expected_header_SKU_Validation in actual_header_SKU_Validation
        time.sleep(1)
        # Check if no data in SKU table
        actual_content = driver.find_element_by_id("content-container").text
        if "No data available in table" in actual_content:
            flag = 2
        else:
            flag = 1

        # Check if result is displayed in table or not.
        if int(flag) == 1:
            skuValidationCount = len(driver.find_element_by_id('validation-table').find_elements_by_tag_name("tr"))
            v_orderid = driver.find_element_by_id('validation-table').find_element_by_class_name('odd').find_element_by_class_name('checkbox').get_attribute('value')
            driver.find_element_by_link_text(v_orderid).click()
            # Verify order details page opens
            wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
            wait.until(EC.visibility_of_element_located((By.ID, 'bookmark')))
            time.sleep(1)
            # verify details show SKU error
            ord_details = driver.find_element_by_id('details').text
            assert "SKU_VALIDATION_FAILURE" in ord_details
            #actualpermissionErrMsg = driver.find_element_by_class_name("jumbotron").text
            #expectedpermissionErrMsg = "You don't have the permission to access this page."
            #assert expectedpermissionErrMsg in actualpermissionErrMsg

            #helpBtn = driver.find_element_by_class_name("btn-warning")
            #assert helpBtn.is_displayed()
            #assert "Need Help?" in helpBtn.text

    # ====================================848==================02 march============================================

    def test_FulfilmentSKUValidation_VerifySearchFunctionality_C848(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify the search functionality in Orders/SKU Validation Page.
        wait = WebDriverWait(driver, 90)
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        driver.find_element_by_link_text("SKU Validation").click()
        time.sleep(1)
        expected_header_SKU_Validation = "SKU Validation"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_SKU_Validation = driver.find_element_by_id("content-header").text
        # Verify SKU Validation Header
        assert expected_header_SKU_Validation in actual_header_SKU_Validation
        time.sleep(1)
        # Check if no data in SKU table
        actual_content = driver.find_element_by_id("content-container").text
        if "No data available in table" in actual_content:
            flag = 2
        else:
            flag = 1

        # Check if result is displayed in table or not.
        if int(flag) == 1:
            skuValidationCount = len(driver.find_element_by_id('validation-table').find_elements_by_tag_name("tr"))
            v_orderid = driver.find_element_by_id('validation-table').find_element_by_class_name('odd').find_element_by_class_name('checkbox').get_attribute('value')
            driver.find_element_by_class_name("dataTables_filter").find_element_by_class_name("input-sm").click()
            driver.find_element_by_class_name("dataTables_filter").find_element_by_class_name("input-sm").send_keys(v_orderid)
            time.sleep(1)
            firstRowText = driver.find_element_by_class_name("odd").text
            assert v_orderid in firstRowText
            driver.find_element_by_class_name("dataTables_filter").find_element_by_class_name("input-sm").clear()
            driver.find_element_by_class_name("dataTables_filter").find_element_by_class_name("input-sm").send_keys("test3456")
            time.sleep(1)
            assert driver.find_element_by_class_name("dataTables_empty").is_displayed()

    # ====================================821==================02 march============================================

    def test_FulfilmentOrderSearch_VerifySortingFunctionality_C821(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify the sorting functionality on order search page.
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Orders')))
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Order Search')))
        driver.find_element_by_link_text("Order Search").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID,'gen_search')))
        actualtitle=driver.find_element_by_id("content-header").text
        expectedtitle= "Order Search"
        assert expectedtitle in actualtitle
        # Generate search
        driver.find_element_by_id("gen_search").click()
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

    # ====================================775==================02 march============================================

    def test_FulfilmentMyWorkPersortJob_VerifyContent_C775(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify the contents on Create a Presort Job page.
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'My Work')))
        driver.find_element_by_link_text("My Work").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Fulfillment')))
        driver.find_element_by_link_text("Fulfillment").click()
        time.sleep(1)
        driver.find_element_by_id("fulfillment-items").find_element_by_link_text("Presort Jobs").click()
        time.sleep(1)

        # Verify 'Create a Presort Job' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Create a Presort Job"
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        col = driver.find_element_by_id("classification-div").text
        assert "Select a Job Type:" in col

        assert driver.find_element_by_id("classification").is_displayed()

        assert driver.find_element_by_id("client").is_displayed()

        assert driver.find_element_by_id("sku").is_displayed()

        assert driver.find_element_by_id("quantity").is_displayed()

        assert driver.find_element_by_id("add").is_displayed()

        assert driver.find_element_by_id("jobname").is_displayed()

        assert driver.find_element_by_id("save").is_displayed()

        assert driver.find_element_by_id("clear").is_displayed()

    # ====================================777==================02 march============================================

    def test_FulfilmentMyWorkViewJob_VerifyContent_C777(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify the contents on View Complete Jobs.
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'My Work')))
        driver.find_element_by_link_text("My Work").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Fulfillment')))
        driver.find_element_by_link_text("Fulfillment").click()
        time.sleep(1)
        driver.find_element_by_id("fulfillment-items").find_element_by_link_text("View Jobs").click()
        time.sleep(1)
        driver.find_element_by_id("view-jobs").find_element_by_link_text("Complete").click()
        time.sleep(1)

        # Verify 'View Complete Jobs' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="View Complete Jobs"
        actual_header=driver.find_element_by_id("content-header").text
        assert actual_header in expected_header

        col = driver.find_element_by_class_name("col-md-3").text
        assert "Available Jobs:" in col
        assert driver.find_element_by_id("job-select").is_displayed()


    # ===========================================692=============3march=============================================

    def test_fulfillment_verify_pagescroll_C692(self, impersonate_fullfilment):
        # Verify Top button scroll functionality in all the pages in Fulfillment user.
        driver = impersonate_fullfilment['webdriver']
        # Verify page load
        wait = WebDriverWait(driver, 90)
        # Verify Dashboard tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Dashboard')))
        driver.find_element_by_link_text("Dashboard").click()  # click on Dashboard tab
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        time.sleep(1)
        actualTitle = driver.find_element_by_id("content-header").text
        expectedTitle = "Fulfillment Dashboard"
        assert expectedTitle in actualTitle
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 580)")
        time.sleep(4)
        # Verify back to top button
        backtotop = driver.find_element_by_id("back-to-top").is_displayed()
        assert backtotop
        driver.find_element_by_id("back-to-top").click()

    # ===========================766======================3March===================================================

    def test_Fullfilment_openPurchaseOrders_search_C766(self, impersonate_fullfilment):
        # Reports/operations/Inventory/Open Purchase Orders-Verify Search functionality in generated report.
        driver = impersonate_fullfilment['webdriver']
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
        # Report: Out of Stock (Title) top left side of the page
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'panel-heading')))
        # Select the client from the drop down
        clients = driver.find_element_by_id("CustomerNumber")
        client_option = "ARPM"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Click on Generate report button.
        driver.find_element_by_id("sub_btn").click()
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(3)

        # Verify valid search
        rc1 = len(driver.find_element_by_id('ReportViewerControl_fixedTable').find_elements_by_tag_name('tr'))
        if int(rc1) > 1:
            # Search - click on Find
            driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl00").send_keys("SKU")
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
                    # Element found again
                    assert int(found2) == 2
            time.sleep(1)
        # Verify wrong entry should not be searched
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl00").send_keys("test12345")
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl01").click()
        try:
            WebDriverWait(driver, 20).until(EC.alert_is_present(), 'The search text was not found.')
            alert = driver.switch_to_alert()
            assert alert.text == "The search text was not found."
            alert.accept()
            alert_found3 = True
        except NoAlertPresentException as e:
            alert_found3 = False

    # ===========================768======================3March===================================================

    def test_Fullfilment_openPurchaseOrders_verifyExportOptions_C768(self, impersonate_fullfilment):
        # Reports/operations/Inventory/Open Purchase Orders-Verify Export button options in generated report.
        driver = impersonate_fullfilment['webdriver']
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
        # Report: Out of Stock (Title) top left side of the page
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'panel-heading')))
        # Select the client from the drop down
        clients = driver.find_element_by_id("CustomerNumber")
        client_option = "ARPM"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break

        # Click on Generate report button.
        driver.find_element_by_id("sub_btn").click()
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(3)
        # Verify report row count
        rc1 = len(driver.find_element_by_id('ReportViewerControl_fixedTable').find_elements_by_tag_name('tr'))
        if int(rc1) > 1:
            # Verify Export Link
            assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_displayed()
            assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()
            driver.find_element_by_id("ReportViewerControl_ctl05_ctl04_ctl00_ButtonLink").click()

            # Verify report can be exported in following format
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'HoverButton')))
            assert driver.find_element_by_class_name("HoverButton").is_displayed()
            act = driver.find_elements_by_class_name("ActiveLink")
            exp_report_type = ['CSV (comma delimited)','Excel']

            for v in act:
                exp_type = v.text
                assert exp_type in exp_report_type
        # Step 8 - .axd file extension when exporting to excel format is a manual step

    # ====================================1124==================03 march============================================

    def test_FulfilmentOrderHistorySummary_VerifyFindNextBtnFunctionality_C1124(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify the find and next functionality in report generated in Order History Summary Report page.
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        # Click on Operations tab.
        Operations = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        Operations.click()
        time.sleep(1)
        # Click on Orders tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Orders')))
        order_linktext = driver.find_elements_by_link_text("Orders")
        order_linktext[1].click()
        time.sleep(1)
        # Click on Order History
        Order_History_Summary = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Order History Summary')))
        Order_History_Summary.click()
        time.sleep(1)
        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("CustomerNumber"))
        select.select_by_visible_text("AFNAVY")
        # Select Dates
        wait.until(EC.visibility_of_element_located((By.NAME,'daterange')))
        driver.find_element_by_name("daterange").click()
        time.sleep(1)

        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("02/28/2015")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("03/29/2015")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)

        # Click on Generate report button.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-success')))
        driver.find_element_by_class_name("btn-success").click()
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        rc1 = len(driver.find_element_by_id('ReportViewerControl_fixedTable').find_elements_by_tag_name('tr'))
        if int(rc1) > 1:
            # Search  X000062919AFNAVY
            driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl00").send_keys("X000062919AFNAVY")
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

    # ====================================779==================03 march============================================

    def test_FulfilmentOrderSearch_VerifyContent_C779(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Verify the contents on Order Search page.
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Orders')))
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Order Search')))
        driver.find_element_by_link_text("Order Search").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID,'gen_search')))
        actualtitle=driver.find_element_by_id("content-header").text
        expectedtitle= "Order Search"
        assert expectedtitle in actualtitle

        # Check input boxes for Order Search Advanced filters
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

    # ====================================780==================03 march============================================

    def test_FulfilmentOrderSearch_VerifyContent_C780(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify the contents on search results page.
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Orders')))
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Order Search')))
        driver.find_element_by_link_text("Order Search").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID,'gen_search')))
        actualtitle=driver.find_element_by_id("content-header").text
        expectedtitle= "Order Search"
        assert expectedtitle in actualtitle

        driver.find_element_by_id("gen_search").click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'col-id')))
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'orders_table')))
        time.sleep(1)

        # Verify error message from orders table if empty
        ord_tab_content = driver.find_element_by_id("orders_table").text
        no_data_message = "No results found for your search."
        if no_data_message in ord_tab_content:
            flag = 2
            assert no_data_message in ord_tab_content
        else:
            # data exists
            flag = 1
        if flag == 1:
            # Verify visible columns in report are available in expected columns list
            actual = driver.find_element_by_id('orders_table').find_elements_by_tag_name('th')
            expected_OrdTable = ['ID','Client Name','Status','Sales Rep','Client PO','Date Submitted','Production Date','Ship-by Date','Paid Date','Invoice Create Date','Type','In Hands Date'
            'PO #','Tracking #'	,'Invoice #','Art Title','Ship-to Name','Order Origin']

            size = len(actual)
            if int(size) > 0:
                for i in range(size):
                    assert actual[i].text in expected_OrdTable
            time.sleep(1)
            # Verify Order table length control orders_table_length
            assert driver.find_element_by_name('orders_table_length').is_displayed()
            # Verify Filter control displayed form-control input-sm
            assert driver.find_element_by_class_name('input-sm').is_displayed()
            # Verify change column button displayed
            assert driver.find_element_by_class_name('ColVis_MasterButton').is_displayed()

    # ====================================823==================03 march============================================

    def test_FulfilmentBookMark_VerifyContent_C823(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify the content on Bookmarks page.
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Orders')))
        # click on Orders tab
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        # Click on Bookmark
        driver.find_element_by_css_selector(".fa.fa-bookmark-o.fa-fw").click()
        time.sleep(1)
        # Verify Bookmarks page is displayed
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_title = driver.find_element_by_id("content-header").text
        expected_title = "Bookmarks"
        assert expected_title in actual_title

        # Verify error message from orders table if empty
        wait.until(EC.visibility_of_element_located((By.ID,'panel_body')))
        ord_tab_content = driver.find_element_by_id("panel_body").text

        no_data_message = "No Orders Bookmarked"
        if no_data_message in ord_tab_content:
            flag = 2
            assert no_data_message in ord_tab_content
        else:
            # data exists
            flag = 1
        if flag == 1:
            # Verify visible columns in report are available in expected columns list
            actual = driver.find_element_by_id('orders_table').find_elements_by_tag_name('th')
            expected_OrdTable = ['ID','Client Name','Status','Sales Rep','Client PO','Date Submitted','Production Date','Ship-by Date','Paid Date','Invoice Create Date','Type','In Hands Date'
                'PO #','Tracking #'	,'Invoice #','Art Title','Ship-to Name','Order Origin']
            size = len(actual)
            if int(size) > 0:
                for i in range(size):
                    assert actual[i].text in expected_OrdTable
            time.sleep(1)

            # Verify Order table length control orders_table_length
            assert driver.find_element_by_name('orders_table_length').is_displayed()
            # Verify Filter control displayed form-control input-sm
            assert driver.find_element_by_class_name('input-sm').is_displayed()
            # Verify change column button displayed
            assert driver.find_element_by_class_name('ColVis_MasterButton').is_displayed()


    # ====================================950==================03 march============================================

    def test_FulfilmentSubscription_VerifyContent_C950(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify content in Subscriptions page.
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()  # click on Reports tab
        time.sleep(1)
        driver.find_element_by_link_text("Subscriptions").click()  # click on Subscriptions block
        time.sleep(1)
        # Verify Subscriptions page is displayed.
        actualtitle = driver.find_element_by_id("content-header").text
        expectedtitle = "Subscriptions"
        assert expectedtitle in actualtitle

        containerText = driver.find_element_by_id("content-container").text
        noSubscriptionMsg = "You have no subscriptions.";
        if noSubscriptionMsg not in containerText:
            # Verify content
            subscription = driver.find_element_by_id("criteria").is_displayed()
            tablecol1 = driver.find_element_by_css_selector(".table.table-striped.table-bordered thead tr th:nth-of-type(1)").text
            tablecol2 = driver.find_element_by_css_selector(".table.table-striped.table-bordered thead tr th:nth-of-type(2)").text
            tablecol3 = driver.find_element_by_css_selector(".table.table-striped.table-bordered thead tr th:nth-of-type(3)").text
            # verify columns
            td1 = "Subscription Name"
            td2 = "Report Name"
            td3 = "Modify/Delete"
            assert subscription == 1
            assert td1 in tablecol1
            assert td2 in tablecol2
            assert td3 in tablecol3

    # ====================================932==================03 march============================================

    def test_FulfilmentSubscription_VerifyModifySubscriptionForm_C932(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify modify functionality in subscription page.
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        driver.find_element_by_link_text("Subscriptions").click()
        time.sleep(1)
        containerText = driver.find_element_by_id("content-container").text
        noSubscriptionMsg = "You have no subscriptions.";
        if noSubscriptionMsg not in containerText:
            # Subscription for: Executive Accounts Receivable pop up is displayed.
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Modify')))
            driver.find_element_by_link_text("Modify").click()
            time.sleep(1)
            expected_subscription_label = "Subscription for: "
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'modal-content')))
            actual_subscription_label = driver.find_element_by_class_name("modal-content").text
            # print(actual_subscription_label)
            assert expected_subscription_label in actual_subscription_label

    # ===========================875======================4March===================================================

    def test_fullfilment_Verify_generateReport_searchBusinessUnit_C875(self, impersonate_fullfilment):
        # Reports/Orders/Open Orders by Business Unit - Verify functionality of Generate Report
        driver = impersonate_fullfilment['webdriver']
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
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Open Orders by Business Unit')))
        driver.find_element_by_link_text("Open Orders by Business Unit").click()
        time.sleep(1)
        # Verify content in Open Orders by Business Unit page.
        # Open Orders by Business Unit Report(heading)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))

        # Select business unit report drop down selection -Membership Services
        select = Select(driver.find_element_by_id("BU"))
        select.select_by_visible_text("Membership Services")
        time.sleep(1)
        # Click on generate report button.
        driver.find_element_by_id("sub_btn").click()
        driver.switch_to_frame("report_src")
        time.sleep(1)
        # Check report load - wait for search control to be editable
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(3)

        # Verify report row count
        rc1 = len(driver.find_element_by_id('ReportViewerControl_fixedTable').find_elements_by_tag_name('tr'))
        if int(rc1) > 1:
            # Search for Business unit - "Membership Services" in the report
            driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl00").send_keys("Membership Services")
            driver.find_element_by_id("ReportViewerControl_ctl05_ctl03_ctl01").click()
            time.sleep(10)
            try:
                alert = driver.switch_to_alert()
                assert alert.text == "The search text was not found."
                alert.accept()
                alert_found = True
            except NoAlertPresentException as e:
                alert_found = False
            # Verify the searched text is highlighted
            if alert_found == False:
                driver.find_element_by_css_selector("span[style='COLOR:highlighttext;BACKGROUND-COLOR:highlight;']").is_displayed()


    # ===========================878======================4March===================================================

    def test_fulfillment_verify_Reportcontent_BusinessUnit_C878(self, impersonate_fullfilment):
        # Reports/Orders/Open Orders by Business Unit- Verify the content in report generated
        driver = impersonate_fullfilment['webdriver']
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
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Open Orders by Business Unit')))
        driver.find_element_by_link_text("Open Orders by Business Unit").click()
        time.sleep(1)
        # Verify content in Open Orders by Business Unit page.
        # Open Orders by Business Unit Report(heading)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))

        # Select business unit report drop down selection -Membership Services
        select = Select(driver.find_element_by_id("BU"))
        select.select_by_visible_text("Membership Services")
        time.sleep(1)
        # Click on generate report button.
        driver.find_element_by_id("sub_btn").click()
        driver.switch_to_frame("report_src")
        time.sleep(1)
        # Check report load - wait for search control to be editable
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(3)

        # Verify Report Elements
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(10)
        wait.until(EC.visibility_of_element_located((By.ID, 'ReportViewerForm')))
        # Verify the first page
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_First_ctl01_ctl00").is_displayed()
        # Verify the Previous page
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Previous_ctl01_ctl00").is_displayed()
        # Verify the current page text box
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_CurrentPage").is_displayed()
        # Verify the  Total Pages
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()
        # Verify the next Page
        if driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Next_ctl00').is_displayed():
            assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Next_ctl00").is_displayed()
        else:
            assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_Next_ctl01").is_displayed()
        # Verify the last Pages
        if driver.find_element_by_id('ReportViewerControl_ctl05_ctl00_Last_ctl00').is_displayed():
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
        # Verify refresh button ReportViewerControl$ctl05$ctl05$ctl00$ctl00$ctl00
        assert driver.find_element_by_name("ReportViewerControl$ctl05$ctl05$ctl00$ctl00$ctl00").is_displayed()
        # Verify export to data feed button
        assert driver.find_element_by_name("ReportViewerControl$ctl05$ctl07$ctl00$ctl00$ctl00").is_displayed()
        # Verify expected report content
        act = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        time.sleep(1)
        # Verify Report Header Content
        exp_content = ['Premium', 'Business Unit', 'Open Orders', 'Description']
        for v in exp_content:
            assert v in act

    # ====================================826==================04 march============================================

    def test_FulfillmentBookMarks_VerifyEntriesFunctionality_C826(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
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
        # Check bookmarks badges count
        if driver.find_element_by_class_name('badge').is_displayed():
            badge_pages = driver.find_element_by_class_name('badge').text
        else:
            badge_pages = 0
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

    # ====================================828==================04 march============================================

    def test_FulfillmentBookMark_VerifyPagination_C828(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify pagination functionality on Bookmarks page.
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

        if int(flag) == 1:
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
        else:
            # print("Insufficient bookmarks count to validate pagination functionality.")
            time.sleep(1)

    # ====================================829==================04 march============================================

    def test_FulfillmentBookMarks_VerifyCountOfBookMark_C829(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
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
        # Check bookmarks badges count
        if driver.find_element_by_class_name('badge').is_displayed():
            badge_pages_prev = driver.find_element_by_class_name('badge').text
        else:
            badge_pages_prev = 0
        # Check if Page 1 is visible to see bookmarks exist
        if int(badge_pages_prev) > 0:
            # Fetch Order Id dynamically for Valid search criteria
            v_orderidfull = driver.find_element_by_class_name('glyphicon-bookmark').get_attribute('data-order-id')

            # Split order id based on '-' to get orderid
            if '-' in v_orderidfull:
                v_orderidsp = v_orderidfull.split('-')
                v_orderid = v_orderidsp[1]
            else:
                v_orderid = v_orderidfull

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

    # ====================================892==================04 march============================================

    def test_FulfillmentOpenOrderByBusinessUnit_VerifyRefreshFunctionality_C892(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify the refresh functionality in report generated  in Business unit report tool
        # in Business unit report tool in Open Orders by Business Unit page.
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Operations')))

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Orders").click()
        time.sleep(1)
        #Click on 'Inventory by Business Unit' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-orders-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Open Orders by Business Unit')))
        driver.find_element_by_id("operations-orders-report-items").find_element_by_link_text("Open Orders by Business Unit").click()
        time.sleep(1)
        # Verify 'Inventory by Business Unit' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Open Orders by Business Unit Report"
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
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(1)
        original_text = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        # Click on Refresh icon. Generated report should be refreshed.
        driver.find_element_by_name("ReportViewerControl$ctl05$ctl05$ctl00$ctl00$ctl00").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(1)
        latest_text = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        assert (original_text is not latest_text)

    # ================================850=========7mar==================================================

    def test_Fulfillment_verifySpreadsheetUpoadpage_C850(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Spreadsheet Upload - Verify the content on Spreadsheet Upload Page.
        wait = WebDriverWait(driver, 90)
        # Click on Dashboard tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Dashboard')))
        driver.find_element_by_link_text("Dashboard").click()
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        time.sleep(1)
        actualTitle = driver.find_element_by_id("content-header").text
        expectedTitle = "Fulfillment Dashboard"
        assert expectedTitle in actualTitle
        time.sleep(1)
        # Click on Spreadsheet Upload tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Spreadsheet Upload')))
        driver.find_element_by_link_text("Spreadsheet Upload").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        time.sleep(1)
        sstitle = driver.find_element_by_id("content-header").text
        expectedTitle = "SS Upload"
        assert expectedTitle in sstitle
        time.sleep(1)

        # Verify page content
        wait.until(EC.visibility_of_element_located((By.ID,'content-container')))
        page_content = driver.find_element_by_id("content-container").text

        # Verify  Content on Spreadsheet Upload Page should be as follows
        assert "Spreadsheet Upload" in page_content
        # upload type
        assert driver.find_element_by_id('ss_type').is_displayed()
        # Client
        assert driver.find_element_by_id('client_select').is_displayed()
        # Browse button
        assert driver.find_element_by_class_name('btn-file').is_displayed()
        # Upload button
        assert driver.find_element_by_class_name('btn-success').is_displayed()
        # Verify box name
        assert "Spreadsheet Upload Templates" in page_content
        # Check download buttons
        dn = len(driver.find_elements_by_link_text('Download'))
        assert dn == 4
        # Verify Heading My Spreadsheet Uploads
        assert "My Spreadsheet Uploads" in page_content
        # Spread_table_length
        assert driver.find_element_by_name('spread_table_length').is_displayed()
        # Search text box
        assert driver.find_element_by_class_name('input-sm').is_displayed()
        # col-md-12
        cls = driver.find_element_by_class_name('col-md-12').text
        # Check table content
        assert "Upload Date" in page_content
        assert "Type" in page_content
        assert "Client" in page_content
        assert "Status" in page_content
        assert "File Name" in page_content
        assert "Actions" in page_content

    # ================================851===================7mar==================================================

    def test_Fulfillment_verifySearchSpreadsheetUpoadpage_C851(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Spreadsheet Upload- Verify Search functionality in Orders/SKU Validation Page/My Spreadsheet Upload section.
        wait = WebDriverWait(driver, 90)
        # Click on Dashboard tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Dashboard')))
        driver.find_element_by_link_text("Dashboard").click()  # click on Dashboard tab
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        time.sleep(1)
        actualTitle = driver.find_element_by_id("content-header").text
        expectedTitle = "Fulfillment Dashboard"
        assert expectedTitle in actualTitle
        time.sleep(1)

        # Click on Spreadsheet Upload tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Spreadsheet Upload')))
        driver.find_element_by_link_text("Spreadsheet Upload").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        time.sleep(1)
        sstitle = driver.find_element_by_id("content-header").text
        expectedTitle = "SS Upload"
        assert expectedTitle in sstitle
        time.sleep(1)

        # Get Spreadsheet table info spread_table_info  Showing 0 to 0 of 0 entries
        tbinfo = driver.find_element_by_id('spread_table_info').text
        if "Showing 0 to 0 of 0 entries" in tbinfo:
            flag = 0
        else:
            # Entries exist
            flag = 1
        # Validate Search
        if flag == 1:
            # Search in valid text for rows Showing 0 to 0 of 0 entries
            driver.find_element_by_id('spread_table_filter').find_element_by_class_name('input-sm').send_keys('abcde12345')
            time.sleep(1)
            # Validate no records displayed
            tb_srch = driver.find_element_by_id('spread_table_info').text
            assert "Showing 0 to 0 of 0 entries" in tb_srch
            # Search valid text
            driver.find_element_by_id('spread_table_filter').find_element_by_class_name('input-sm').clear()
            driver.find_element_by_id('spread_table_filter').find_element_by_class_name('input-sm').send_keys('Complete')
            time.sleep(1)
            # Validate Page 1 link displayed
            assert driver.find_element_by_link_text('1').is_displayed()

    # ===========================879======================7March===================================================

    def test_fullfilment_verify_ReportExportType_BusinessUnit_C879(self, impersonate_fullfilment):
        # Reports -Orders -Open Orders by Business Unit - Verify the export options in report generated
        driver = impersonate_fullfilment['webdriver']
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
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Open Orders by Business Unit')))
        driver.find_element_by_link_text("Open Orders by Business Unit").click()
        time.sleep(1)
        # Verify content in Open Orders by Business Unit page.
        # Open Orders by Business Unit Report(heading)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))

        # Select business unit report drop down selection -Membership Services
        select = Select(driver.find_element_by_id("BU"))
        select.select_by_visible_text("Membership Services")
        time.sleep(1)
        # Click on generate report button.
        driver.find_element_by_id("sub_btn").click()
        driver.switch_to_frame("report_src")
        time.sleep(1)
        # Check report load - wait for search control to be editable
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(4)
        # Verify Export links
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl04_ctl00_ButtonLink").click()
        # Verify report can be exported in following format
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'HoverButton')))
        assert driver.find_element_by_class_name("HoverButton").is_displayed()
        act = driver.find_elements_by_class_name("ActiveLink")
        exp_report_type = ['CSV (comma delimited)','Excel']
        for v in act:
            name = v.text
            assert name in exp_report_type

    # ==================================C886==========7March================================================

    def test_Fullfilment_GeneratedReport_exporttype_C886(self, impersonate_fullfilment):
        # Reports/operations/Inventory/Inventory By Business Unit - Verify Export options in generated report
        driver = impersonate_fullfilment['webdriver']
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        # Click on Operations tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Operations')))
        time.sleep(1)
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Inventory").click()
        time.sleep(1)

        # Click on Inventory by Business Unit
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Inventory by Business Unit')))
        driver.find_element_by_link_text("Inventory by Business Unit").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        # Select the client from the drop down
        clients = driver.find_element_by_id("BU")
        client_option = "All"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break
        # Click on Generate report button
        driver.find_element_by_id("sub_btn").click()
        # Verify the Date and Time of the generated report
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(4)
        actual_dateTime = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        time.sleep(1)
        exp_dateTime = "Report Created On"
        assert exp_dateTime in actual_dateTime
        # Verify Export links
        assert driver.find_element_by_id("ReportViewerControl_ctl05_ctl00_TotalPages").is_displayed()
        driver.find_element_by_id("ReportViewerControl_ctl05_ctl04_ctl00_ButtonLink").click()
        # Verify report can be exported in following format
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'HoverButton')))
        assert driver.find_element_by_class_name("HoverButton").is_displayed()
        act = driver.find_elements_by_class_name("ActiveLink")
        exp_report_type = ['CSV (comma delimited)','Excel']
        for v in act:
            name = v.text
            assert name in exp_report_type


    # ================================852===================7mar==================================================

    def test_Fulfillment_verifyPaginationSpreadsheetUpoadpage_C852(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Spreadsheet Upload - Verify the pagination functionality in Spreadsheet UploadPage.
        wait = WebDriverWait(driver, 90)
        # Click on Dashboard tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Dashboard')))
        driver.find_element_by_link_text("Dashboard").click()  # click on Dashboard tab
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        time.sleep(1)
        actualTitle = driver.find_element_by_id("content-header").text
        expectedTitle = "Fulfillment Dashboard"
        assert expectedTitle in actualTitle
        time.sleep(1)

        # Click on Spreadsheet Upload tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Spreadsheet Upload')))
        driver.find_element_by_link_text("Spreadsheet Upload").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        time.sleep(1)
        sstitle = driver.find_element_by_id("content-header").text
        expectedTitle = "SS Upload"
        assert expectedTitle in sstitle
        time.sleep(1)

        # Validate Upload Type and Client
        assert driver.find_element_by_id('ss_type').is_displayed()
        assert driver.find_element_by_id('client_select').is_displayed()

        # Get Spreadsheet upload table info
        tbinfo = driver.find_element_by_id('spread_table_info').text
        # Verify Pagination buttons Prev Next
        assert driver.find_element_by_link_text('Previous').is_displayed()
        assert driver.find_element_by_link_text('Next').is_displayed()

        if "Showing 0 to 0 of 0 entries" in tbinfo:
            flag = 0
        else:
            # Entries exist
            flag = 1
            # Validate pagination entries shown
            assert "Showing 0 to 0 of 0 entries" not in tbinfo
        # Get table row count
        rc = len(driver.find_element_by_id('spread_table').find_elements_by_tag_name("tr"))

        # Validate Pagination controls
        if int(rc) > 11:
            # Validate Page 1 is displayed
            assert driver.find_element_by_link_text('1').is_displayed()
            assert driver.find_element_by_link_text('Previous').is_enabled() == False
            # Validate Next is enabled
            assert driver.find_element_by_link_text('Next').is_enabled()
            time.sleep(1)
            driver.find_element_by_link_text('Next').click()
            time.sleep(1)
            assert driver.find_element_by_link_text('2').is_displayed()
            # Validate Previous is enabled
            assert driver.find_element_by_link_text('Previous').is_enabled()

    # ================================853===================7mar==================================================

    def test_Fulfillment_verifyPaginationFiltersSpreadsheetUpoadpage_C853(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify the 'Showing 1 to 'xx'of 'xxx' entries functionality in Spreadsheet Upload/My Spreadsheet Upload Page.
        wait = WebDriverWait(driver, 90)
        # Click on Dashboard tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Dashboard')))
        driver.find_element_by_link_text("Dashboard").click()  # click on Dashboard tab
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        time.sleep(1)
        actualTitle = driver.find_element_by_id("content-header").text
        expectedTitle = "Fulfillment Dashboard"
        assert expectedTitle in actualTitle
        time.sleep(1)

        # Click on Spreadsheet Upload tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Spreadsheet Upload')))
        driver.find_element_by_link_text("Spreadsheet Upload").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        time.sleep(1)
        sstitle = driver.find_element_by_id("content-header").text
        expectedTitle = "SS Upload"
        assert expectedTitle in sstitle
        time.sleep(1)

        # Validate Upload Type and Client
        assert driver.find_element_by_id('ss_type').is_displayed()
        assert driver.find_element_by_id('client_select').is_displayed()

        # Get Spreadsheet upload table info
        tbinfo = driver.find_element_by_id('spread_table_info').text
        # Verify Pagination buttons Prev Next
        assert driver.find_element_by_link_text('Previous').is_displayed()
        assert driver.find_element_by_link_text('Next').is_displayed()

        if "Showing 0 to 0 of 0 entries" in tbinfo:
            flag = 0
        else:
            # Entries exist
            flag = 1
            # Validate pagination entries shown
            assert "Showing 0 to 0 of 0 entries" not in tbinfo
            # Get table row count
            rc = len(driver.find_element_by_id('spread_table').find_elements_by_tag_name("tr"))

        if flag == 1:
            # Select All and count rows
            entry_sel = driver.find_element_by_id("spread_table_length")
            v_optsel = "All"
            for opt in entry_sel.find_elements_by_tag_name("option"):
                if opt.text == v_optsel:
                    opt.click()
                    break
            # Get table row count
            time.sleep(1)
            rc = len(driver.find_element_by_id('spread_table').find_elements_by_tag_name("tr"))
            #print ("Rows = " + str(rc))
            # Validate pages
            if int(rc) > 25:
            # Validate Pagination controls
            # Select 25 entries
                entry_sel = driver.find_element_by_id("spread_table_length")
                v_optsel = "25"
                for opt in entry_sel.find_elements_by_tag_name("option"):
                    if opt.text == v_optsel:
                        opt.click()
                        break
                # Check row count displayed spread_table_info Showing 1 to xx of yy entries spread_table_info
                time.sleep(3)
                srch_text = driver.find_element_by_id('spread_table_info').text
                time.sleep(3)
                assert 'Showing 1 to 25' in srch_text
            if int(rc) > 10:
            # Validate Pagination controls
            # Select 10 entries
                entry_sel = driver.find_element_by_id("spread_table_length")
                v_optsel = "10"
                for opt in entry_sel.find_elements_by_tag_name("option"):
                    if opt.text == v_optsel:
                        opt.click()
                        break
                # Check row count displayed spread_table_info Showing 1 to xx of yy entries spread_table_info
                time.sleep(5)
                srch_text = driver.find_element_by_id('spread_table_info').text
                time.sleep(1)
                assert 'Showing 1 to 10' in srch_text

            if int(rc) > 50:
            # Validate Pagination controls
            # Select 50 entries
                entry_sel = driver.find_element_by_id("spread_table_length")
                v_optsel = "50"
                for opt in entry_sel.find_elements_by_tag_name("option"):
                    if opt.text == v_optsel:
                        opt.click()
                        break
                # Check row count displayed spread_table_info Showing 1 to xx of yy entries spread_table_info
                time.sleep(5)
                srch_text = driver.find_element_by_id('spread_table_info').text
                time.sleep(1)
                assert 'Showing 1 to 50' in srch_text

            if int(rc) > 100:
            # Validate Pagination controls
            # Select 100 entries
                entry_sel = driver.find_element_by_id("spread_table_length")
                v_optsel = "100"
                for opt in entry_sel.find_elements_by_tag_name("option"):
                    if opt.text == v_optsel:
                        opt.click()
                        break
                # Check row count displayed spread_table_info Showing 1 to xx of yy entries spread_table_info
                time.sleep(10)
                srch_text = driver.find_element_by_id('spread_table_info').text
                time.sleep(1)
                assert 'Showing 1 to 100' in srch_text

    # ================================933===================8mar==================================================

    def test_Fulfillment_verifyCancelDeletepopupSubscriptionpage_C933(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Fulfillment user - To verify the cancel button in Delete button functionality on Subscriptions page.
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()  # click on Reports tab
        time.sleep(1)
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
            sub_count = len(driver.find_element_by_id('jobs_table').find_elements_by_tag_name('tr'))
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
            # Verify Delete Modify links
            assert driver.find_element_by_link_text('Delete').is_displayed()
            assert driver.find_element_by_link_text('Modify').is_displayed()
            # Click on Delete
            driver.find_element_by_link_text('Delete').click()
            time.sleep(1)
            # popover-content
            pop = driver.find_element_by_class_name('popover').text
            assert "Are you sure?" in pop
            # Click Cancel btn-default
            driver.find_element_by_class_name('btn-default').click()
            time.sleep(1)
            # Verify that Subscription exists
            sub_count2 = len(driver.find_element_by_id('jobs_table').find_elements_by_tag_name('tr'))
            # Verify subscription count is Same after cancel
            assert int(sub_count) == int(sub_count2)


    # ================================934===================8mar==================================================

    def test_Fulfillment_verifySubscriptionDelete_C934(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Fulfillment user - To verify the cancel button in Delete button functionality on Subscriptions page.
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()  # click on Reports tab
        time.sleep(1)
        driver.find_element_by_link_text("Subscriptions").click()  # click on Subscriptions
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
            sub_count = len(driver.find_element_by_id('jobs_table').find_elements_by_tag_name('tr'))
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
            # Verify Delete Modify links
            assert driver.find_element_by_link_text('Delete').is_displayed()
            assert driver.find_element_by_link_text('Modify').is_displayed()
            # Click on Delete
            driver.find_element_by_link_text('Delete').click()
            time.sleep(1)
            # popover-content
            pop = driver.find_element_by_class_name('popover').text
            assert "Are you sure?" in pop
            # Click Delete
            driver.find_element_by_class_name('btn-danger').click()
            time.sleep(4)
            # Verify that Subscription is deleted
            ord_tab_content = driver.find_element_by_id("content-container").text
            if "You have no subscriptions" in ord_tab_content:
                flag = 1
            else:
                sub_count2 = len(driver.find_element_by_id('jobs_table').find_elements_by_tag_name('tr'))
                # Verify subscription count is changed after Delete
                assert int(sub_count) != int(sub_count2)

    # ================================869===================8mar==================================================

    def test_Fulfillment_verifyContentsSpreadsheetDetailpage_C869(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Spreadsheet Upload - Verify the content in Spreadsheet Details page via My Spreadsheet Upload section.
        wait = WebDriverWait(driver, 90)
        # Click on Dashboard tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Dashboard')))
        driver.find_element_by_link_text("Dashboard").click()  # click on Dashboard tab
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        time.sleep(1)
        actualTitle = driver.find_element_by_id("content-header").text
        expectedTitle = "Fulfillment Dashboard"
        assert expectedTitle in actualTitle
        time.sleep(1)

        # Click on Spreadsheet Upload tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Spreadsheet Upload')))
        driver.find_element_by_link_text("Spreadsheet Upload").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        time.sleep(1)
        sstitle = driver.find_element_by_id("content-header").text
        expectedTitle = "SS Upload"
        assert expectedTitle in sstitle
        time.sleep(1)

        # Validate Upload Type and Client
        assert driver.find_element_by_id('ss_type').is_displayed()
        assert driver.find_element_by_id('client_select').is_displayed()

        # Get Spreadsheet upload table info
        tbinfo = driver.find_element_by_id('spread_table_info').text
        # Verify Pagination buttons Prev Next
        assert driver.find_element_by_link_text('Previous').is_displayed()
        assert driver.find_element_by_link_text('Next').is_displayed()

        if "Showing 0 to 0 of 0 entries" in tbinfo:
            flag = 0
        else:
            # Entries exist
            flag = 1
            # Validate pagination entries shown
            assert "Showing 0 to 0 of 0 entries" not in tbinfo
        # Get table row count
        rc = len(driver.find_element_by_id('spread_table').find_elements_by_tag_name("tr"))

        if int(rc) > 1:
            # Click on View Details Link of the first record
            driver.find_element_by_link_text('View Details').click()
            # Wait for criteria Spreadsheet Details
            wait.until(EC.visibility_of_element_located((By.ID, 'content-container')))
            crt = driver.find_element_by_id('content-container').text
            time.sleep(1)
            assert "Spreadsheet Details" in crt
            # Check  Back to Uploads button
            assert driver.find_element_by_link_text('Back to Uploads').is_displayed()
            # Verify Spreadsheet Detail Page Headers
            assert "Customer Order ID" in crt
            assert "Status" in crt
            assert "Message" in crt
            assert "G&G Order ID" in crt

    # ================================870===================8mar==================================================

    def test_Fulfillment_verifyBackbuttonSpreadsheetDetailpage_C870(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify the back button functionality in Spreadsheet Details page via My Spreadsheet Upload section..
        wait = WebDriverWait(driver, 90)
        # Click on Dashboard tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Dashboard')))
        driver.find_element_by_link_text("Dashboard").click()  # click on Dashboard tab
        time.sleep(1)

        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        time.sleep(1)
        actualTitle = driver.find_element_by_id("content-header").text
        expectedTitle = "Fulfillment Dashboard"
        assert expectedTitle in actualTitle
        time.sleep(1)

        # Click on Spreadsheet Upload tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Spreadsheet Upload')))
        driver.find_element_by_link_text("Spreadsheet Upload").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        time.sleep(1)
        sstitle = driver.find_element_by_id("content-header").text
        expectedTitle = "SS Upload"
        assert expectedTitle in sstitle
        time.sleep(1)

        # Validate Upload Type and Client
        assert driver.find_element_by_id('ss_type').is_displayed()
        assert driver.find_element_by_id('client_select').is_displayed()

        # Get Spreadsheet upload table info
        tbinfo = driver.find_element_by_id('spread_table_info').text
        # Verify Pagination buttons Prev Next
        assert driver.find_element_by_link_text('Previous').is_displayed()
        assert driver.find_element_by_link_text('Next').is_displayed()

        if "Showing 0 to 0 of 0 entries" in tbinfo:
            flag = 0
        else:
            # Entries exist
            flag = 1
            # Validate pagination entries shown
            assert "Showing 0 to 0 of 0 entries" not in tbinfo
        # Get table row count
        rc = len(driver.find_element_by_id('spread_table').find_elements_by_tag_name("tr"))

        if int(rc) > 1:
            # Click on View Details Link of the first record
            driver.find_element_by_link_text('View Details').click()
            # Wait for criteria Spreadsheet Details
            wait.until(EC.visibility_of_element_located((By.ID, 'content-container')))
            crt = driver.find_element_by_id('content-container').text
            time.sleep(1)
            assert "Spreadsheet Details" in crt
            # Click Back to Uploads button
            driver.find_element_by_link_text('Back to Uploads').click()
            time.sleep(1)
            # Verify SS Upload page
            wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
            time.sleep(1)
            sstitle = driver.find_element_by_id("content-header").text
            expectedTitle = "SS Upload"
            assert expectedTitle in sstitle
            time.sleep(1)


    # ================================702===================8mar==================================================

    def test_Fulfillment_verifyUserProfileDashboardpage_C702(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Fulfilment Dashboard - Verify the contents on User profile Dashboard page.
        wait = WebDriverWait(driver, 90)
        # Verify Dashboard tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Dashboard')))
        driver.find_element_by_link_text('Dashboard').click()
        time.sleep(5)
        # These are the 5 widgets that are expected on page
        expected_widgets = [
            'New Orders',
            'Orders Shipped',
            'Items on Backorder',
            "Highest Performing SKU's"]

        # First, collect all the widgets on the page
        widgets = driver.find_elements_by_class_name('widget')
        # Verify actual vs. expected widget count
        assert len(expected_widgets) == len(widgets)
        # Verify Widgets Display
        src = driver.page_source
        text_found1 = re.search(r'New Orders', src)
        text_found2 = re.search(r'Orders Shipped', src)
        text_found3 = re.search(r'Items on Backorder', src)
        text_found4 = re.search(r"Highest Performing SKU's", src)

        # Verify Dashboard content
        # Clients 2 All Available Clients - Validate heading and drop down client value
        cl = len(driver.find_elements_by_class_name('btn-default'))
        clt = driver.find_elements_by_class_name('btn-default')
        cltext1 = clt[0].text
        assert "All Available Clients" in cltext1
        clval = clt[0].get_attribute('title')
        assert "AFNAVY" in clval
        cltext2 = clt[1].text
        assert "All Available Clients" in cltext2
        clval2 = clt[1].get_attribute('title')
        assert "AFNAVY" in clval2

        # timeframe-select 3 items - Validate Values
        tm = len(driver.find_elements_by_class_name('timeframe-select'))
        tms = driver.find_elements_by_class_name('timeframe-select')
        for i in range(0,tm):
            tmtext1 = tms[i].text
            assert "Last 7 Days" in tmtext1
            assert "Last 30 Days" in tmtext1
            assert "Last 90 Days" in tmtext1
            assert "Last 12 Months" in tmtext1

        # client-select 4
        cs = len(driver.find_elements_by_class_name('client-select'))
        clt = driver.find_elements_by_class_name('client-select')
        cltext3 = clt[2].text
        assert "AFNAVY" in cltext3
        cltext4 = clt[3].text
        assert "AFNAVY" in cltext4
        time.sleep(1)

        # Verify the table headers DataTables_Table_0 Items on Backorder
        cnt_tab1 = driver.find_element_by_id('DataTables_Table_0').text
        assert "SKU" in cnt_tab1
        assert "Description" in cnt_tab1
        assert "Qty on Backorder" in cnt_tab1
        assert "Days Out of Stock" in cnt_tab1

        # Verify the table headers DataTables_Table_1 Highest Performing SKU's
        cnt_tab1 = driver.find_element_by_id('DataTables_Table_1').text
        assert "SKU" in cnt_tab1
        assert "Description" in cnt_tab1
        assert "Qty in Stock" in cnt_tab1
        assert "Qty Shipped" in cnt_tab1

    # ====================================824==================08 march============================================

    def test_FulfilmentBookMarks_VerifyFilterFunctionality_C824(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify the filter functionality on Bookmarks page.
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Verify Change column functionality in Orders/BookMarks page.
        # Click on order tab
        # Click on order tab
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        driver.find_element_by_css_selector(".fa.fa-bookmark-o.fa-fw").click()      #Click on Bookmark
        #Verify Bookmarks page is displayed.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        actualtitle=driver.find_element_by_id("content-header").text
        expectedtitle= "Bookmarks"
        assert expectedtitle in actualtitle

        # Check if No Bookmarks exist
        actualcontent = driver.find_element_by_id("panel_body").text
        if "No Orders Bookmarked" in actualcontent:
            flag = 2
        else:
            flag = 1
            wait.until(EC.visibility_of_element_located((By.ID,'orders_table_previous')))
            # Ensure page records exist
            cnt = driver.find_element_by_id('orders_table_wrapper').text
            if cnt != 'Showing 0 to 0 of 0 entries':
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



    # ====================================825==================08 march============================================

    def test_FulfilmentBookMarks_VerifyBookMarkFunctionality_C825(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify the bookmark functionality on Bookmarks page.
        wait = WebDriverWait(driver, 90)
        # Verify Orders tab visibility
        # Click on Orders tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Orders')))
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        # Click on Bookmark
        driver.find_element_by_css_selector(".fa.fa-bookmark-o.fa-fw").click()
        # Verify Bookmarks page is displayed.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        actualtitle=driver.find_element_by_id("content-header").text
        expectedtitle= "Bookmarks"
        assert expectedtitle in actualtitle
        time.sleep(1)

        # Verify error message from orders table if no Bookmark
        wait.until(EC.visibility_of_element_located((By.ID,'content-container')))
        ord_tab_content = driver.find_element_by_id("content-container").text
        no_data_message = "No Orders Bookmarked"

        if no_data_message in ord_tab_content:
            flag = 2
        else:
            # data exists
            flag = 1

        # Go to Page 1 if bookmarks exist
        if int(flag) == 1:
            # Count Bookmark
            time.sleep(1)
            bc = len(driver.find_element_by_id('orders_table').find_elements_by_tag_name("tr"))
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
            time.sleep(4)
            # Check bookmarks badges count
            driver.find_element_by_css_selector(".fa.fa-bookmark-o.fa-fw").click()
            time.sleep(1)

            # Verify error message from orders table if no Bookmark
            wait.until(EC.visibility_of_element_located((By.ID,'content-container')))
            ord_tab_content = driver.find_element_by_id("content-container").text
            no_data_message = "No Orders Bookmarked"

            if no_data_message in ord_tab_content:
                flag = 2
                bk_count=0
            else:
                # data row exists
                flag = 1

            # Go to Page 1 if bookmarks exist
            if int(flag) == 1:
                driver.find_element_by_id("orders_table_filter").find_element_by_class_name("input-sm").send_keys(v_orderid)
                time.sleep(4)
                # Check row count displayed orders_table_info  Showing 0 to 0 of 0 entries
                rc_text = driver.find_element_by_id('orders_table_info').text
                time.sleep(1)
                assert 'Showing 0 to 0 of 0 entries' in rc_text
                time.sleep(1)

            # Click on Order Search link to view all orders
            driver.find_element_by_link_text("Order Search").click()
            time.sleep(1)
            # Click on Generate Search button
            driver.find_element_by_id("gen_search").click()
            time.sleep(5)
            # Wait orders_table_info
            wait.until(EC.visibility_of_element_located((By.ID,'orders_table_info')))
            time.sleep(1)

            if int(len(driver.find_element_by_id("orders_table").find_elements_by_tag_name('tr'))) > 1:
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


    # ====================================827==================08 march============================================

    def test_FulfilmentBookMarks_VerifySortingFunctionality_C827(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify sorting functionality on Bookmarks page.
        wait = WebDriverWait(driver, 90)
        # Click on Orders tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        # Click on Bookmark
        driver.find_element_by_css_selector(".fa.fa-bookmark-o.fa-fw").click()
        #Verify Bookmarks page is displayed.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        actualtitle=driver.find_element_by_id("content-header").text
        expectedtitle= "Bookmarks"
        assert expectedtitle in actualtitle

        # Verify error message from orders table if no Bookmark
        wait.until(EC.visibility_of_element_located((By.ID,'content-container')))
        ord_tab_content = driver.find_element_by_id("content-container").text
        no_data_message = "No Orders Bookmarked"

        # Exit if no Bookmarks Exist
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
                # Skip first col click as it is in ascending order
                if int(i) != 0:
                    actualhdrs[i].click()
                    time.sleep(3)
                asc_order = driver.find_element_by_id("orders_table").find_elements_by_tag_name('th')[i].get_attribute("aria-sort")
                assert asc_order in expected_Ascending_order
                # Click column for Descending Order
                actualhdrs[i].click()
                time.sleep(3)
                desc_order = driver.find_element_by_id("orders_table").find_elements_by_tag_name('th')[i].get_attribute("aria-sort")
                assert desc_order in expected_Descending_order

    # ====================================830==================08March============================================

    def test_FulfilmentBookMarks_VerifyChangeColumnFunctionality_C830(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify the change column functionality in Orders/Bookmarks Page.
        wait = WebDriverWait(driver, 90)
        # Verify Orders tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Orders')))
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        #Click on Bookmark
        driver.find_element_by_css_selector(".fa.fa-bookmark-o.fa-fw").click()

        #Verify Bookmarks page is displayed.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        actualtitle=driver.find_element_by_id("content-header").text
        expectedtitle= "Bookmarks"
        assert expectedtitle in actualtitle

        # Verify error message from orders table if no Bookmark
        wait.until(EC.visibility_of_element_located((By.ID,'content-container')))
        ord_tab_content = driver.find_element_by_id("content-container").text
        no_data_message = "No Orders Bookmarked"

        # Exit if no Bookmarks Exist
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


    # ====================================845==================08 march============================================

    def test_FulfilmentSKUValidation_VerifySelectedFunctionality_C845(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify the selected functionality in Orders/SKU Validation Page.
        wait = WebDriverWait(driver, 90)
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        driver.find_element_by_link_text("SKU Validation").click()
        time.sleep(1)
        expected_header_SKU_Validation = "SKU Validation"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_SKU_Validation = driver.find_element_by_id("content-header").text
        # Verify SKU Validation Header
        assert expected_header_SKU_Validation in actual_header_SKU_Validation
        time.sleep(1)
        # Check if no data in SKU table
        actual_content = driver.find_element_by_id("content-container").text
        if "No data available in table" in actual_content:
            flag = 2
        else:
            flag = 1

        # Check if result is displayed in table or not.
        if int(flag) == 1:
            selectedCount = driver.find_element_by_id("amt-selected").text
            assert "0 selected" in selectedCount

            driver.find_element_by_class_name("odd").find_element_by_class_name("checkbox").click()
            time.sleep(1)

            selectedCount = driver.find_element_by_id("amt-selected").text
            assert "1 selected" in selectedCount
            # Remove selection
            driver.find_element_by_class_name("odd").find_element_by_class_name("checkbox").click()
            time.sleep(1)

            selectedCount = driver.find_element_by_id("amt-selected").text
            assert "0 selected" in selectedCount

    # ================================1158===================9mar==================================================

    def test_Fulfillment_verifyShipmentSubscriptionDefaultEmailid_C1158(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Reports/Operations/Orders/Shipment History Summary-Verify user Email Id display by default in subscription form.
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        # Click on Operations tab
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Orders.
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Orders").click()
        time.sleep(1)
        # Click Shipment History Summary.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Shipment History Summary')))
        driver.find_element_by_id("operations-orders-report-items").find_element_by_link_text("Shipment History Summary").click()
        time.sleep(1)
        # Verify Shipment History Summary Report page
        expected_header_Shipment_History_Report = "Shipment History Summary Report"
        actual_header_Shipment_History_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Shipment_History_Report in expected_header_Shipment_History_Report
        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("CustomerNumber"))
        select.select_by_visible_text("AFNAVY")
        # Select the Ship Start  and ship end date
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

        # Click on Make a Subscription button.
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'btn-primary')))
        driver.find_element_by_class_name("btn-primary").click()
        # Check default email
        wait.until(EC.visibility_of_element_located((By.ID,'email')))
        time.sleep(1)
        em = driver.find_element_by_id("email").get_attribute("value")
        assert em == "vlucero@ggoutfitters.com"
        driver.find_element_by_class_name("btn-default").click()
        time.sleep(1)

    # ================================1164===================9mar==================================================

    def test_Fulfillment_verifyShipmentHistroryStartDateEndDate_C1164(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Reports/Operations/Orders/Shipment History Summary- Verify Start date is not greater than End date in date picker.
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        # Click on Operations tab
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Orders.
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Orders").click()
        time.sleep(1)
        # Click Shipment History Summary.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Shipment History Summary')))
        driver.find_element_by_id("operations-orders-report-items").find_element_by_link_text("Shipment History Summary").click()
        time.sleep(1)
        # Verify Shipment History Summary Report page
        expected_header_Shipment_History_Report = "Shipment History Summary Report"
        actual_header_Shipment_History_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Shipment_History_Report in expected_header_Shipment_History_Report
        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("CustomerNumber"))
        select.select_by_visible_text("AFNAVY")
        # Select the Ship Start  and ship end date
        driver.find_element_by_name("daterange").click()
        time.sleep(1)

        driver.find_element_by_name("daterangepicker_start").clear()
        driver.find_element_by_name("daterangepicker_start").send_keys("02/24/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        driver.find_element_by_name("daterangepicker_end").clear()
        driver.find_element_by_name("daterangepicker_end").send_keys("02/22/2016")
        driver.find_element_by_name("daterangepicker_start").send_keys(Keys.ENTER)
        time.sleep(1)
        dt1 = driver.find_element_by_name("daterangepicker_start").text
        dt2 = driver.find_element_by_name("daterangepicker_end").text
        time.sleep(1)
        assert dt1 == dt2
        driver.find_element_by_class_name('range_inputs').find_element_by_class_name('btn-success').click()
        time.sleep(1)

    # ================================1160===================9mar==================================================

    def test_Fulfillment_verifyShipmentHistroryreportRefresh_C1160(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Reports/Operations/Orders/Shipment History Summary - Verify refresh button functionality in the report.
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        report.click()
        # Click on Operations tab
        assert driver.find_element_by_link_text("Operations").is_displayed()
        assert driver.find_element_by_link_text("Subscriptions").is_displayed()
        # Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        # Click on Orders.
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Orders").click()
        time.sleep(1)
        # Click Shipment History Summary.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Shipment History Summary')))
        driver.find_element_by_id("operations-orders-report-items").find_element_by_link_text("Shipment History Summary").click()
        time.sleep(1)
        # Verify Shipment History Summary Report page
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        expected_header_Shipment_History_Report = "Shipment History Summary Report"
        actual_header_Shipment_History_Report = driver.find_element_by_id("content-header").text
        assert actual_header_Shipment_History_Report in expected_header_Shipment_History_Report

        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("CustomerNumber"))
        select.select_by_visible_text("AFNAVY")

        # Select the Ship Start  and ship end date
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
        # Switch to the generated report.
        driver.switch_to_frame("report_src")
        wait.until(EC.element_to_be_clickable((By.ID, 'ReportViewerControl_ctl05_ctl03_ctl00')))
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, 'VisibleReportContentReportViewerControl_ctl09')))
        time.sleep(3)
        # Verify Refresh
        original_text = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        # Click on Refresh icon.
        driver.find_element_by_name("ReportViewerControl$ctl05$ctl05$ctl00$ctl00$ctl00").click()
        wait.until(EC.element_to_be_clickable((By.NAME, 'ReportViewerControl$ctl05$ctl05$ctl00$ctl00$ctl00')))
        time.sleep(1)
        # Generated report should be refreshed.
        latest_text = driver.find_element_by_id("VisibleReportContentReportViewerControl_ctl09").text
        assert (original_text is not latest_text)


    # ================================925===================9mar==================================================

    def test_Fulfillment_verifySettlementPageReportname_C925(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Reports/Ad-hoc/Settlement- Verify the report name for the generated report on Settlement page.
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Settlement')))
        driver.find_element_by_link_text("Settlement").click()
        time.sleep(1)
        expected_header_Settlement_Report = "Settlement Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Settlement_Report = driver.find_element_by_id("content-header").text
        time.sleep(1)
        # Verify  Header
        assert expected_header_Settlement_Report in actual_header_Settlement_Report

        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("client_id"))
        select.select_by_visible_text("AFNAVY")

        # Select the Ship Start  and ship end date
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
        # Verify generated report.
        wait.until(EC.visibility_of_element_located((By.ID, 'dataTable_info')))
        time.sleep(3)
        # Get report header text
        rh = driver.find_element_by_id('table_report').text
        # Verify Header displayed with dates
        assert "Settlement Summary Report: AFNAVY Report for: 2016-02-22 to 2016-02-24" in rh

    # ================================926===================9mar==================================================

    def test_Fulfillment_verifySettlementPageReportXlsSubscriptionbutton_C926(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Reports/Ad-hoc/Settlement- Verify presence of Excel and Make a Subscription buttons on the report generated.
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Ad-hoc')))
        driver.find_element_by_link_text("Ad-hoc").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Settlement')))
        driver.find_element_by_link_text("Settlement").click()
        time.sleep(1)
        expected_header_Settlement_Report = "Settlement Report"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_Settlement_Report = driver.find_element_by_id("content-header").text
        time.sleep(1)
        # Verify  Header
        assert expected_header_Settlement_Report in actual_header_Settlement_Report

        # Select the client from the drop down.
        select = Select(driver.find_element_by_id("client_id"))
        select.select_by_visible_text("AFNAVY")

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
        # Verify generated report.
        wait.until(EC.visibility_of_element_located((By.ID, 'dataTable_info')))
        time.sleep(3)
        # Get report header text
        rh = driver.find_element_by_id('table_report').text
        # Verify Excel button and Make a Subscription button on report
        assert driver.find_element_by_id('xls_btn').is_displayed()
        assert driver.find_element_by_class_name('btn-primary').is_displayed()

    # ================================695===================9mar==================================================

    def test_Fulfillment_verifyUserProfileSharingPagecontents_C695(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Dashboard/sharing - Verify the contents in sharing page in User profile Dashboard page.
        wait = WebDriverWait(driver, 90)
        # Verify Reports tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        # Click on Sharing link
        driver.find_element_by_id("nav_dropdown").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Sharing')))
        driver.find_element_by_link_text("Sharing").click()
        # Wait for Delegation select drop down
        wait.until(EC.visibility_of_element_located((By.NAME,'new_delegation')))
        time.sleep(1)
        # Verify Share Orders Heading on panel
        pd = driver.find_element_by_id('content-container').text
        assert "Share Orders" in pd
        # Check if not shared
        sh = driver.find_element_by_class_name('panel-body').text
        tx = "You have not shared your orders"
        time.sleep(1)
        if tx in sh:
            # Select any drop down value
            entry_sel = Select(driver.find_element_by_name("new_delegation"))
            entry_sel.select_by_index(2)
            # Verify Submit
            assert driver.find_element_by_class_name('btn-default').is_displayed()


    # ====================================781==================09 march========================================

    def test_FulfillmentOrderSearch_VerifySearchFunctionality_C781(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify the search functionality on order search page.
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

        # select filter dates
        driver.find_element_by_name("submitted_end_date").send_keys("02/24/2016")
        driver.find_element_by_name("submitted_end_date").send_keys(Keys.TAB)
        time.sleep(1)
        driver.find_element_by_name("submitted_start_date").send_keys("01/24/2016")
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

    # ====================================782==================09 march============================================

    def test_FulfillmentOrderSearch_VerifyResetFunctionality_C782(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify the reset functionality on order search page.
        wait = WebDriverWait(driver, 90)
        # Click on Orders tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        time.sleep(1)
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        # Click on Order Search
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Order Search')))
        driver.find_element_by_link_text("Order Search").click()
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

    # ====================================804==================09 march============================================

    def test_FulfillmentOrderSearch_VerifyChangeColumnFunctionality_C804(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify the change column button functionality on order search.
        wait = WebDriverWait(driver, 90)
        # Click on order tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        # Click on Order Search
        driver.find_element_by_link_text("Order Search").click()
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

    # ====================================721==================09 march============================================

    def test_FulfilllmentReportKitting_VerifyContent_C721(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify the content in Kitting report page.
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

    # ====================================722==================09 march============================================

    def test_FulfillmentReportSettlement_VerifyContent_C722(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify the content in Settlement report page.
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


    # ========================================722=========================10Mar=====================================

    def test_FulfillmentReportsSettlement_VerifyContent_C722(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify the content in Settlement report page.
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

        assert driver.find_element_by_id("client_id").is_displayed()
        assert driver.find_element_by_name("daterange").is_displayed()
        assert driver.find_element_by_class_name("btn-success").is_displayed()

    # ========================================723========================10Mar======================================

    def test_FulfillmentReportsSatoriBulkMailing_VerifyContent_C723(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
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


    # ========================================742==========================10Mar====================================

    def test_FulfillmentReportsKitting_VerifyGeneratedReport_C742(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
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

    # ========================================743=====================10Mar=========================================

    def test_FulfillmentReportsSettlement_VerifyGeneratedReport_C743(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
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

    # ========================================744==================================10Mar============================

    def test_FulfillmentReportsSatoriBulkMailing_VerifyGeneratedReport_C744(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify that report is generated for Reports/Ad-hoc/Satori Bulk Mailing page.
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

        # Select the client from the drop down
        clients = driver.find_element_by_id("client_id")
        client_option = "ARA"
        for option in clients.find_elements_by_tag_name("option"):
            if option.text == client_option:
                option.click()
                break

        # Click on Generate report button.
        driver.find_element_by_class_name("btn-success").click()

        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
        time.sleep(5)

        assert driver.find_element_by_id("table_report").is_displayed()

    # ========================================921==============================10Mar================================

    def test_FulfillmentReportShipping_VerifyReportName_C921(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify the report name for the generated report on Shipping page.
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

        reportname = "Shipping Report: ARA Report for: 2016-02-22 to 2016-02-23"
        reportHeaderText = driver.find_element_by_id("table_report").find_element_by_class_name("panel-heading").text
        assert reportname in reportHeaderText

    # ========================================922============================10Mar==================================

    def test_FulfillmentReportsShipping_VerifyExcelAndSubscriptionPresenceInReport_C922(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify the presence of Excel and Make a Subscription buttons on the report generated for Shipping page.
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

        assert driver.find_element_by_id("table_report").find_element_by_class_name("btn-primary").is_displayed()
        assert driver.find_element_by_id("table_report").find_element_by_id("xls_btn").is_displayed()

    # ========================================923==========================10Mar====================================

    def test_FulfillmentReportKitting_VerifyReportName_C923(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify the report name for the generated report on Kitting page.
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

        reportname = "Kitting Report: ARA Report for: 2016-02-22 to 2016-02-23"
        reportHeaderText = driver.find_element_by_id("table_report").find_element_by_class_name("panel-heading").text
        print(reportHeaderText)
        assert reportname in reportHeaderText


    # ========================================924===========10Mar===================================================

    def test_FulfillmentReportsKitting_VerifyExcelAndSubscriptionPresenceInReport_C924(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify the presence of Excel and Make a Subscription buttons on the report generated for Kitting page.
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

        assert driver.find_element_by_id("table_report").find_element_by_class_name("btn-primary").is_displayed()
        assert driver.find_element_by_id("table_report").find_element_by_id("xls_btn").is_displayed()

    # ========================================893===========10Mar===================================================

    def test_FulfillmentOpenOrdersBusinessUnit_VerifyFindAndNextFunctionality_C893(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify the find and next functionality in report generated  in Business unit report tool in
        # Business unit report tool in Open Orders by Business Unit page.
        wait = WebDriverWait(driver, 90)
        # Click on Reports tab.
        report=wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Reports')))
        report.click()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Operations')))

        #Click on Operations tab.
        driver.find_element_by_link_text("Operations").click()
        time.sleep(1)
        #Click on Inventory tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        driver.find_element_by_id("operations-report-items").find_element_by_link_text("Orders").click()
        time.sleep(1)
        #Click on 'Inventory by Business Unit' tab.
        wait.until(EC.visibility_of_element_located((By.ID,'operations-orders-report-items')))
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Open Orders by Business Unit')))
        driver.find_element_by_id("operations-orders-report-items").find_element_by_link_text("Open Orders by Business Unit").click()
        time.sleep(1)
        # Verify 'Inventory by Business Unit' page.
        wait.until(EC.visibility_of_element_located((By.ID,'content-header')))
        expected_header ="Open Orders by Business Unit Report"
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

    # ==============================================================================================================


    # ====================================942==================11 march============================================
    def test_FulfilmentSubscription_VerifyEmailSavedInModifySubscription_C942(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # To verify more than one email can be saved in modify Subscription for: Executive Accounts Receivable pop up
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Click on Reports tab.
        driver.find_element_by_link_text("Reports").click()
        time.sleep(1)
        driver.find_element_by_link_text("Subscriptions").click()
        time.sleep(1)

        # Check Records exist i.e. Modify link exists
        if driver.find_element_by_link_text('Modify').is_displayed():
            driver.find_element_by_link_text('Modify').click()
            # Proceed with modification and save
            wait.until(EC.visibility_of_element_located((By.ID, 'myModalLabel')))
            time.sleep(1)
            # Clear email text box
            driver.find_element_by_id("email").clear()
            # Send two email ids in Email field
            email = "apriest@ggoutfitters.com,apriest@ggoutfitters.com"
            driver.find_element_by_id("email").send_keys(email)
            # Select save button
            driver.find_element_by_id("next_btn").click()
            time.sleep(4)

            assert driver.find_element_by_class_name("modal-dialog").is_displayed()==False

    # ====================================720==================11 march============================================
    def test_FulfillmentReportShipping_VerifyContent_C720(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
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


    # ====================================805==================11 march============================================
    def test_FulfillmentOrderSearch_VerifyFilterFunctionality_C805(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify the filter functionality on order search page.
        wait = WebDriverWait(driver, 90)
        # Click on order tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        driver.find_element_by_link_text("Orders").click()
        # Click on Order Search
        driver.find_element_by_link_text("Order Search").click()
        time.sleep(1)
        # Click on generate report button
        driver.find_element_by_id("gen_search").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'input-sm')))
        assert driver.find_element_by_class_name("input-sm").is_displayed()

        # Verify error message from orders table if empty
        wait.until(EC.visibility_of_element_located((By.ID,'orders_table')))
        ord_tab_content = driver.find_element_by_id("orders_table").text
        no_data_message = "No results found for your search."

        if no_data_message not in ord_tab_content:
            # Verify valid entry and search for same
            driver.find_element_by_id("orders_table_filter").find_element_by_class_name("input-sm").send_keys("TARGV")
            time.sleep(5)
            actual = driver.find_element_by_id("orders_table").find_element_by_class_name("odd").text
            exp_content = ['TARGV']
            for b in exp_content:
                assert b in actual
            driver.find_element_by_id("orders_table_filter").find_element_by_class_name("input-sm").clear()
            time.sleep(3)
            # Send wrong entry in search
            driver.find_element_by_id("orders_table_filter").find_element_by_class_name("input-sm").send_keys("xyz123")
            time.sleep(3)
            # CHECK DATA TABLE EMPTY TEXT
            dt_text = driver.find_element_by_class_name('dataTables_empty').text
            expected_message = "No results found for your search."
            assert dt_text in expected_message

    # ====================================806==================11 march============================================

    def test_FulfillmentOrderSearch_VerifyBookMarkFunctionality_C806(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify the bookmark functionality on order search page.
        wait = WebDriverWait(driver, 90)
        # Click on Orders tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        # Click on Order Search
        driver.find_element_by_link_text("Order Search").click()
        time.sleep(1)
        # Click on generate report button
        driver.find_element_by_id("gen_search").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'input-sm')))
        assert driver.find_element_by_class_name("input-sm").is_displayed()

        # Verify error message from orders table if empty
        wait.until(EC.visibility_of_element_located((By.ID,'orders_table')))
        ord_tab_content = driver.find_element_by_id("orders_table").text
        no_data_message = "No results found for your search."

        if no_data_message not in ord_tab_content:
            v_orderidfull = driver.find_element_by_class_name('glyphicon-bookmark').get_attribute('data-order-id')
            driver.find_element_by_id("orders_table_filter").find_element_by_class_name("input-sm").send_keys(v_orderidfull)
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
            driver.find_element_by_id("orders_table_filter").find_element_by_class_name("input-sm").send_keys(v_orderidfull)
            time.sleep(4)
            # Check row count displayed orders_table_info  Showing 1 to 1 of 1 entries
            rc_text = driver.find_element_by_id('orders_table_info').text
            assert rc_text == 'Showing 1 to 1 of 1 entries'
            time.sleep(1)
            # Return back to Order Search page, Click on Order Search
            driver.find_element_by_link_text("Order Search").click()
            time.sleep(1)
            # Click on Search button
            wait.until(EC.visibility_of_element_located((By.ID,'gen_search')))
            driver.find_element_by_id("gen_search").click()
            # Filter same Order id
            driver.find_element_by_id("orders_table_filter").find_element_by_class_name("input-sm").send_keys(v_orderidfull)
            time.sleep(4)
            # Click on bookmark icon to remove bookmark
            driver.find_element_by_class_name('glyphicon-bookmark').click()
            time.sleep(4)
            # Open Bookmarks page and Search for order-id that no longer has bookmark
            driver.find_element_by_css_selector(".fa.fa-bookmark-o.fa-fw").click()
            time.sleep(1)

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


    # ====================================820==================11 march============================================

    def test_FulfillmentOrderSearch_VerifyEntriesFunctionality_C820(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify the  'Showing 1 to 'xx'of 'xxx' entries functionality on order search page.
        wait = WebDriverWait(driver, 90)
        # Click on order tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        # Click on Order Search
        driver.find_element_by_link_text("Order Search").click()
        time.sleep(1)
        # Click on generate report button
        driver.find_element_by_id("gen_search").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'input-sm')))

        displayedOrderText = driver.find_element_by_class_name('dataTables_info').text
        str = displayedOrderText.split(" ");
        orderCount = str[len(str)-2].replace(",", "", 5)

        # Check if Page 1 is visible to see bookmarks exist
        if int(orderCount) >= 10:
            # Verify  Bookmarks dropdowns 10,25,50,100
            if int(orderCount) >= 100:
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
            if int(orderCount) >= 50:
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
            if int(orderCount) >= 25:
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
            if int(orderCount) >= 10:
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

    # ====================================822==================11 march===========================================

    def test_FulfilmentOrderSearch_VerifyPaginationFunctionality_C822(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify the pagination functionality on order search page.
        wait = WebDriverWait(driver, 90)
        # Click on order tab
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        # Click on Order Search
        driver.find_element_by_link_text("Order Search").click()
        time.sleep(1)
        # Click on generate report button
        driver.find_element_by_id("gen_search").click()
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'input-sm')))
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID,'orders_table_previous')))
        time.sleep(4)
        # Verify by default previous button is displayed as disabled.
        expected_disable_previous = "disabled"
        actual_disable_previous = driver.find_element_by_id("orders_table_previous").get_attribute("class")
        assert expected_disable_previous in actual_disable_previous
        expected_current_page_color = "rgba(229, 65, 45, 1)"

        # Ensure page records exist
        cnt = driver.find_element_by_id('orders_table_info').text

        if cnt != 'Showing 0 to 0 of 0 entries':
                # Click on '1' link and verify the pagination functionality.
                actual_current_page_color = driver.find_element_by_link_text("1").value_of_css_property("background-color")
                assert expected_current_page_color in actual_current_page_color
                next_Button = driver.find_element_by_id("orders_table_next").get_attribute("class")

                # Verify link '2' is displayed, if displayed then click and verify pagination functionality. orders_table_next
                if expected_disable_previous not in next_Button:
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
                else:
                    actual_disable_previous = driver.find_element_by_id("orders_table_next").get_attribute("class")
                    assert expected_disable_previous in actual_disable_previous

    # =================================844==================11 march============================================

    def test_FulfilmentOrderSKUValidation_VerifySubmitButtonFunctionality_C844(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify the submit button functionality in Orders/SKU Validation Page.
        wait = WebDriverWait(driver, 90)
        # Verify Orders tab visibility
        # Verify Orders tab visibility
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Orders')))
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        driver.find_element_by_link_text("SKU Validation").click()
        time.sleep(1)
        expected_header_SKU_Validation = "SKU Validation"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_SKU_Validation = driver.find_element_by_id("content-header").text
        # Verify SKU Validation Header
        assert expected_header_SKU_Validation in actual_header_SKU_Validation
        time.sleep(1)
        selectedCount = driver.find_element_by_id("amt-selected").text
        assert "0 selected" in selectedCount
        # Check SKU Records exist
        tx = driver.find_element_by_id('validation-table').text
        if "No data available in table" in tx:
            flag = 2
        else:
            flag = 1
        skuValidationCount = len(driver.find_element_by_id('validation-table').find_elements_by_tag_name("tr"))
        #print(skuValidationCount)
        # Check if result is displayed in table or not.
        if int(flag) == 1:
            driver.find_element_by_class_name("odd").find_element_by_class_name("checkbox").click()
            time.sleep(1)
            selectedCount = driver.find_element_by_id("amt-selected").text
            assert "1 selected" in selectedCount
            driver.find_element_by_class_name("btn-success").click()
            time.sleep(1)
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'noty_text')))
            expected_message="Flagged 1 orders for reprocessing"
            actual_message=driver.find_element_by_class_name("noty_text").text
            assert expected_message in actual_message

    # ========================================741=====================11 march===================================

    def test_FulfillmentReportShipping_VerifyGeneratedReport_C741(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
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

    # ====================================846==================14 march=======================================

    def test_FulfillmentSKUValidation_VerifyEntriesFunctionality_C846(self, impersonate_fullfilment):
        driver = impersonate_fullfilment['webdriver']
        # Verify the 'Showing 1 to 'xx'of 'xxx' entries  functionality in Orders/SKU Validation Page.
        wait = WebDriverWait(driver, 90)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Reports')))
        # Verify Pagination functionality on 'SKU Validation' page.
        driver.find_element_by_link_text("Orders").click()
        time.sleep(1)
        driver.find_element_by_link_text("SKU Validation").click()
        time.sleep(1)
        expected_header_SKU_Validation = "SKU Validation"
        wait.until(EC.visibility_of_element_located((By.ID, 'content-header')))
        actual_header_SKU_Validation = driver.find_element_by_id("content-header").text
        # Verify SKU Validation Header
        assert expected_header_SKU_Validation in actual_header_SKU_Validation
        time.sleep(1)

        displayedOrderText = driver.find_element_by_id('validation-table_info').text
        str = displayedOrderText.split(" ");
        orderCount = str[len(str)-2].replace(",", "", 5)
        print(orderCount)

        # Check if Page 1 is visible to see bookmarks exist
        if int(orderCount) >= 10:
            # Verify  Bookmarks dropdowns 10,25,50,100
            if int(orderCount) >= 100:
                # Select 100 entries orders_table_length
                entry_sel = driver.find_element_by_name("validation-table_length")
                v_optsel = "100"
                for opt in entry_sel.find_elements_by_tag_name("option"):
                    if opt.text == v_optsel:
                        opt.click()
                        break
                time.sleep(3)
                srch_text = driver.find_element_by_id('validation-table_info').text
                time.sleep(3)
                assert 'Showing 1 to 100' in srch_text
            if int(orderCount) >= 50:
                # Select 50 entries orders_table_length
                entry_sel = driver.find_element_by_name("validation-table_length")
                v_optsel = "50"
                for opt in entry_sel.find_elements_by_tag_name("option"):
                    if opt.text == v_optsel:
                        opt.click()
                        break
                time.sleep(3)
                srch_text = driver.find_element_by_id('validation-table_info').text
                time.sleep(3)
                assert 'Showing 1 to 50' in srch_text
            if int(orderCount) >= 25:
                # Select 25 entries orders_table_length
                entry_sel = driver.find_element_by_name("validation-table_length")
                v_optsel = "25"
                for opt in entry_sel.find_elements_by_tag_name("option"):
                    if opt.text == v_optsel:
                        opt.click()
                        break
                time.sleep(3)
                srch_text = driver.find_element_by_id('validation-table_info').text
                time.sleep(3)
                assert 'Showing 1 to 25' in srch_text
        else:
                print("Insufficient SKU Validation count to validate filters")
        time.sleep(1)

