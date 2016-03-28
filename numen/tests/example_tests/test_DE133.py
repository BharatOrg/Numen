def test_graphs_have_correct_totals_on_money_breakdown_on_hover(setup):
    '''
    Description:  When hovering the mouse over a bar of the graphs on the
    dashboard, a popup with the money breakdown, as well as a total should
    appear.
    Test procedure:  Log in, click on one of the bar graph elements.  Ensure
    ASI, Embroidery, Screen, Mixed, and Total appear.
    Expected result:  All the correct items appear in the hover box.
    '''
    breakdown = ['ASI','Embroidery','Screen','Mixed','Total','Unknown']
    driver = setup['webdriver']
    driver.implicitly_wait(10)
    userfield = driver.find_element_by_name('user')
    userfield.clear()
    userfield.send_keys('bstanley')
    passwdfield = driver.find_element_by_name('password')
    passwdfield.clear()
    passwdfield.send_keys('2By6krdd')
    driver.find_element_by_name('user').submit()

#   Utility function to extract the titles for the money breakdown of a
#   bargraph element
    driver.implicitly_wait(20)
    def getTitles(circle):
        circle = path.find_element_by_xpath('../..')
        return circle

#   Utility function to return an integer version of a unicode string
#   representation of money 

    def launderMoney(money):
        laundered = ''
        for char in money:
            try:
                laundered+=str(int(char))
            except ValueError:
                pass 
        return int(laundered)

#   Select a random bar from the graphs on the page
    circles = driver.find_elements_by_tag_name('circle')
    import random
    acircle = random.choice(circles)
    acircle.click()
    info = acircle.find_element_by_xpath('../..').text.split()

    total = 0
    for title in [title for title in breakdown if title != 'Total']:
        dollars = info[(info.index(title+':')+1)]
        total += launderMoney(dollars)
        print title, (dollars)
    displayed_total = launderMoney(info[(info.index('Total'+':')+1)])
    print total, displayed_total
    assert total == displayed_total

