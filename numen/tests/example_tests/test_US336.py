# coding: utf-8
import time

class TestUS336:

    def check_copyright(self, driver, url):
        numen_url = 'https://numen.qa.ggoutfitters.com'
        driver.get(numen_url+url)
        crtext = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div')
        is_copyright_on_page = '2014-'+str(time.localtime().tm_year) in crtext
        print url, is_copyright_on_page 
        assert is_copyright_on_page
        
    def test_copyright_on_numen_dash(self, setup):


	driver = setup['webdriver']
	userfield = driver.find_element_by_name('user')
	userfield.clear()
	userfield.send_keys('bstanley')
	passwdfield = driver.find_element_by_name('password')
	passwdfield.clear()
	passwdfield.send_keys('2By6krdd')
	driver.find_element_by_name('user').submit()

        #Go to My Work Overview
	driver.find_element_by_xpath('//*[@id="main-nav"]/li[2]/a').click()
	driver.find_element_by_xpath('//*[@id="main-nav"]/li[2]/ul/li[1]/a').click()
	driver.implicitly_wait(10)
	numen = driver.find_element_by_xpath('//*[@id="site-logo"]/a/img')
        numen.click()
	driver.implicitly_wait(10)
	

