import os
from selenium import webdriver

def test_login_firefox_valid_credentials_logout():

	driver = webdriver.Firefox()
	driver.get("https://numen.qa.ggoutfitters.com/dashboard")
	"Numen" in driver.title
	userlogin = {'user':'bstanley', 'password':'2By6krdd'}
	for cred in userlogin: driver.find_element_by_name(cred).send_keys(userlogin[cred])
	driver.find_element_by_name('user').submit()
	logoutbutton = driver.find_element_by_xpath('//ul[2]/li/a')
	if logoutbutton.is_displayed():
		logoutbutton.click()
		print 'Login Successful:FireFox'
		driver.find_element_by_xpath('//*[@id="top-bar"]/ul[2]/li/ul/li[3]/a').click()
		driver.find_element_by_xpath('//html/body/div[1]/div/div[2]/div/div')
		print 'Logout Succesful:FireFox'
	else:
		print 'Test Failed Logout Unsuccessful:FireFox'
	driver.close()
	driver.quit()

def test_login_firefox_invalid_credentials_logout():

	driver = webdriver.Firefox()
	driver.get("https://numen.qa.ggoutfitters.com/dashboard")
	"Numen" in driver.title
	userlogin = {'user':'invalid', 'password':'2By6krdd1234'}
	for cred in userlogin: driver.find_element_by_name(cred).send_keys(userlogin[cred])
	driver.find_element_by_name('user').submit()
	#Login should fail due to Invalid Password
	logincopyright = driver.find_element_by_xpath("//html/body/div[1]/div/div[2]/div/div")
	if logincopyright.is_displayed():
		print 'Invalid Credentials Test Passed:FireFox'
	else:
		print 'Invalid Credentials Test Failed:FireFox'
	driver.close()
	driver.quit()
def test_login_chrome_valid_credentials_logout():


	driver = webdriver.Chrome('/usr/bin/chromedriver')
	driver.get("https://numen.qa.ggoutfitters.com/dashboard")
	"Numen" in driver.title
	userlogin = {'user':'bstanley', 'password':'2By6krdd'}
	for cred in userlogin: driver.find_element_by_name(cred).send_keys(userlogin[cred])
	driver.find_element_by_name('user').submit()
	logoutbutton = driver.find_element_by_xpath('//ul[2]/li/a')
	if logoutbutton.is_displayed():
		logoutbutton.click()
		print 'Login Successful:Chrome'
		driver.find_element_by_xpath('//*[@id="top-bar"]/ul[2]/li/ul/li[3]/a')
		print 'Logout Successful:Chrome'
	else:
		print 'Test Failed Logout Unsuccessful:Chrome'
	driver.close()
	driver.quit()

def test_login_chrome_invalid_credentials_logout():
	driver = webdriver.Chrome('/usr/bin/chromedriver')
	driver.get("https://numen.qa.ggoutfitters.com/dashboard")
	"Numen" in driver.title
	userlogin = {'user':'invalid1234', 'password':'joe02123'}
	for cred in userlogin: driver.find_element_by_name(cred).send_keys(userlogin[cred])
	driver.find_element_by_name('user').submit()
	logincopyright= driver.find_element_by_xpath('//html/body/div[1]/div/div[2]/div/div')
	if logincopyright.is_displayed():
		print 'Invalid Credentials Test Passed:Chrome'
	else:
		print 'Invalid Credentials Test Failed:Chrome'
	driver.close()
	driver.quit()

