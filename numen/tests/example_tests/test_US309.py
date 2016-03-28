from random import randint
from random import choice
from time import sleep

searchurl = '''https://numen.qa.ggoutfitters.com/orders/search'''
bookmarkurl = '''https://numen.qa.ggoutfitters.com/orders/bookmarks'''

class TestUS309:

    def test_order_search_change_columns_persists(self, setup):
        '''
        ::Description:  Checks if changes to the 'Change Columns' checkbox filter on
        Numen order searches persists after the page has been reloaded.
        ::Expected Behavior:  Changes to columns on the order seach page should last
        until the 10 minutes it takes for the cookie to expire
        ::Test procedure:  Login to main page, click order search, select a 
        random combination of columns, ensure [reload page, back button, new 
        search] does not change column settings before 10 minute cookie expirey
        for each combination.
        '''
	driver = setup['webdriver']
	userfield = driver.find_element_by_name('user')
	userfield.clear()
	userfield.send_keys('bstanley')
	passwdfield = driver.find_element_by_name('password')
	passwdfield.clear()
	passwdfield.send_keys('2By6krdd')
	driver.find_element_by_name('user').submit()
	driver.implicitly_wait(20)
        driver.get(searchurl)
        driver.find_element_by_id('gen_search').click()
#   Collect the possible column selections
        driver.find_element_by_class_name('ColVis_Button ColVis_MasterButton').click()
        colchecks = driver.find_elements_by_xpath('''//li/label/input''')
#   Check random columns, store the ones we checked
        checked = {}
        for i in range(len(colchecks)):
            if(randint(0,1)):
                print 'selecting '+str(i)+'th '+'checkbox'
                colchecks[i].click()
                checked[i] = False
            else:
                checked[i] = True
#   Refresh page and make sure correct columns are still checked
        driver.refresh()
        driver.get(searchurl)
        driver.find_element_by_id('gen_search').click()
        driver.find_element_by_class_name('ColVis_Button ColVis_MasterButton').click()
        colchecks = [i.is_selected() for i in driver.find_elements_by_xpath('''//li/label/input''')]

        assert colchecks == checked.values()

    def test_bookmark_search_change_columns_persists(self, setup):
#   Perform search and add a few random bookmarks

        driver = setup['webdriver']
        driver.get(searchurl)
        driver.find_element_by_id('gen_search').click()
#   Wait for the search to complete
        while driver.find_element_by_id('loading_btn').is_displayed():
            sleep(4)
        bookmarks = driver.find_elements_by_xpath('''//*[contains(concat('', normalize-space(@class),''),'glyphicon glyphicon-bookmark pull-left')]''')
        print bookmarks
        for i in range(1,len(bookmarks)):
            choice(bookmarks).click()

#   Go to bookmarks and perform a the same checks as for the general searches
        driver.get(bookmarkurl)
        driver.find_element_by_class_name('ColVis_Button ColVis_MasterButton').click()
        colchecks = driver.find_elements_by_xpath('''//li/label/input''')
        checked = {}
        for i in range(len(colchecks)):
            if(randint(0,1)):
                print 'selecting '+str(i)+'th '+'checkbox'
                colchecks[i].click()
                checked[i] = False
            else:
                checked[i] = True
        driver.get(bookmarkurl)
        driver.find_element_by_class_name('ColVis_Button ColVis_Masterbutton').click()
        colchecks = [i.is_selected() for i in driver.find_elements_by_xpath('''//li/label/input''')]

        assert colchecks == checked.values()
