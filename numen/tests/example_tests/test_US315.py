def test_graphs_have_money_breakdown_on_hover(setup):
    '''
    Description:  When hovering the mouse over a bar of the graphs on the
    dashboard, a popup with the money breakdown, as well as a total should
    appear.
    Test procedure:  Log in, click on one of the bar graph elements.  Ensure
    ASI, Embroidery, Screen, Mixed, and Total appear.
    Expected result:  All the correct items appear in the hover box.
    '''

    breakdown = ['ASI','Embroidery','Screen','Mixed','Total']
    driver = setup['webdriver']
    userfield = driver.find_element_by_name('user')
    userfield.clear()
    userfield.send_keys('bstanley')
    passwdfield = driver.find_element_by_name('password')
    passwdfield.clear()
    passwdfield.send_keys('2By6krdd')
    driver.implicitly_wait(10)
    driver.find_element_by_name('user').submit()
    driver.implicitly_wait(10)

#   Utility function to extract the titles for the money breakdown of a
#   bargraph element

    def getTitles(circle):
        circle = circle.find_element_by_xpath('../..')
        return circle
    driver.implicitly_wait(10)	
#   Select a random bar from the graphs on the page
    circles = driver.find_elements_by_tag_name('circle')[45:50]
    for circle in circles:
        circle.click()
        print circle.find_element_by_xpath('../..').text
    import random
    acircle = random.choice(circles)
    acircle.click()
    info = acircle.find_element_by_xpath('../..').text
    for title in breakdown:
        assert title in info

