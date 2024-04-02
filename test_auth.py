from locators import Login, URL


def test_auth_positive(browser, user_auth):
    assert browser.current_url == f'{URL.BASE_URL}inventory.html', 'url не соответствует ожидаемому'
    assert browser.title == 'Swag Labs', 'Wrong browser title'


def test_auth_negative_wrong_pass(browser):
    browser.get(URL.BASE_URL)
    browser.find_element(*Login.USER_NAME).send_keys('standard_user')
    browser.find_element(*Login.USER_PASSWORD).send_keys('notsecret_sauce')
    login_button = browser.find_element(*Login.BUTTON_LOGIN)
    login_button.click()

    error_text = browser.find_element(*Login.LOGIN_ERROR).text
    assert error_text == 'Epic sadface: Username and password do not match any user in this service', \
        'Wrong Error text on the site'
    assert login_button.get_attribute("value") == "LOGIN", "There is no LOGIN button"


def test_auth_negative_wrong_username(browser):
    browser.get(URL.BASE_URL)
    browser.find_element(*Login.USER_NAME).send_keys('standard_userr')
    browser.find_element(*Login.USER_PASSWORD).send_keys('secret_sauce')
    login_button = browser.find_element(*Login.BUTTON_LOGIN)
    login_button.click()

    error_text = browser.find_element(*Login.LOGIN_ERROR).text

    assert error_text == 'Epic sadface: Username and password do not match any user in this service', \
        'Wrong Error text on the site'
    assert browser.current_url == URL.BASE_URL, 'Browser go to another URL'
    assert login_button.get_attribute("value") == "LOGIN", "There is no LOGIN button"


def test_auth_negative_wrong_user_data(browser):
    browser.get(URL.BASE_URL)
    browser.find_element(*Login.USER_NAME).send_keys('a')
    browser.find_element(*Login.USER_PASSWORD).send_keys('b')
    login_button = browser.find_element(*Login.BUTTON_LOGIN)
    login_button.click()

    error_text = browser.find_element(*Login.LOGIN_ERROR).text

    assert error_text == 'Epic sadface: Username and password do not match any user in this service', \
        'Wrong Error text on the site'
    assert browser.current_url == URL.BASE_URL, 'Browser go to another URL'
    assert login_button.get_attribute("value") == "LOGIN", "There is no LOGIN button"


def test_auth_negative_without_user_data(browser):
    browser.get(URL.BASE_URL)
    login_button = browser.find_element(*Login.BUTTON_LOGIN)
    login_button.click()

    error_text = browser.find_element(*Login.LOGIN_ERROR).text

    assert error_text == 'Epic sadface: Username is required', \
        'Wrong Error text on the site'
    assert browser.current_url == URL.BASE_URL, 'Browser go to another URL'
    assert login_button.get_attribute("value") == "LOGIN", "There is no LOGIN button"
