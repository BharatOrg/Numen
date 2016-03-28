url = "https://numen.qa.ggoutfitters.com/"
errormsg_badlogin = 'Please enter a correct username and password. Note that both fields are case-sensitive.'
login_title = 'Numen - Login'
homepage_title = 'Numen'
test_user = 'jdoe'
test_password = 'yupHuke3'
test_firstn = 'John'
test_lastn = 'Doe'

class TestLoginActions:

    def test_no_username_no_pw(self, setup):
        '''
        Description:  Try a login with no password or username.
        Expected Behavior:  Logging in without a username or password produces the
            correct error message.  User should remain on login page.
        Test Procedure:  Attempt login without a username and without a password.
            Verify that user is still on login page after attempt.  Verify that the
            correct error message has appeared.
        '''

        driver = setup['webdriver']
        driver.find_element_by_name('user').submit()
        #  Are we still on the login page?
        assert login_title == driver.title
        #  Did we receive an error?
        error = driver.find_element_by_class_name('noty_message').text
        #  Has the correct error message appeared?
        assert error == errormsg_badlogin

    def test_no_username(self, setup):
        '''
        Description:  Try a login with no username.
        Expected Behavior:  Logging in without a username produces the correct error
            message.  User should remain on login page.
        Test Procedure:  Attempt login without a username.  Verify that user is
            still on the login page after attempt.  Verify that the correct error
            message has appeared.
        
        '''

        driver = setup['webdriver']
        passwdfield = driver.find_element_by_name('password')
        passwdfield.send_keys('thisisapassword')
        passwdfield.submit()
        #  Are we still on the login page?
        assert login_title == driver.title
        #  Did we receive an error?
        error = driver.find_element_by_class_name('noty_message').text
        #  Has the correct error message appeared?
        assert error == errormsg_badlogin

    def test_bad_username(self, setup):
        '''
        Description:  Try a login with some strange usernames.  Ie:  digits, single letters, very large usernames
        Expected Behavior:  Logging in with strange usernames produces the correct
            error message.  User should remain on login page.
        Test Procedure:  Attempt a few logins with single digit/letter usernames,
            a gibberish username, and a very long username with 256 characters.
            Verify that the user is still on the login page after the attempt.  
            Verify that the correct error message has appeared.
        '''

        driver = setup['webdriver']
        #  some likely to fail usernames:
        testnames = ['0','1','a','','ahsdfjhasd3sdafjasf444',
                ('a'*256),
        ]
        for username in testnames:
            userfield = driver.find_element_by_name('user')
            userfield.clear()
            userfield.send_keys(username)
            userfield.submit()
        #  Are we still on the login page?
        assert login_title == driver.title
        #  Did we receive an error?
        error = driver.find_element_by_class_name('noty_message').text
        #  Has the correct error message appeared?
        assert error == errormsg_badlogin

