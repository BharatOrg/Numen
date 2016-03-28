import pytest
import time
import re
from selenium import webdriver
from random import randint
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class TestSalesUsers_better:

    #==============================================81===========================5 mar================

    def test_SalesProfileVerifyRemoveUserFunctionality_C81(self, impersonate_sales):
        # Verify sales impersonation
        driver = impersonate_sales['webdriver']

