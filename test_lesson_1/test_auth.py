import pytest

BASE_URL = 'https://www.saucedemo.com/v1/'

USER_NAME = ('xpath', '//*[@id="user-name"]')
USER_PASSWORD = ('xpath', '//*[@id="password"]')
BUTTON_LOGIN = ('xpath', '//*[@id="login-button"]')
LOGIN_ERROR = ('xpath', '//h3')


@pytest.fixture(scope="function")
def test_auth_positive(browser):
    browser.get(BASE_URL)

    browser.find_element(*USER_NAME).send_keys('standard_user')
    browser.find_element(*USER_PASSWORD).send_keys('secret_sauce')
    browser.find_element(*BUTTON_LOGIN).click()
    assert browser.current_url == f'{BASE_URL}inventory.html', 'url не соответствует ожидаемому'
    assert browser.title == 'Swag Labs', 'Wrong browser title'


def test_auth_negative_wrong_pass(browser):
    browser.get(BASE_URL)

    browser.find_element(*USER_NAME).send_keys('standard_user')
    browser.find_element(*USER_PASSWORD).send_keys('notsecret_sauce')
    browser.find_element(*BUTTON_LOGIN).click()
    error_text = browser.find_element(*LOGIN_ERROR).text
    assert error_text == 'Epic sadface: Username and password do not match any user in this service', \
        'Wrong Error text on the site'
    assert browser.current_url == BASE_URL, 'Browser go to another URL'


def test_auth_negative_wrong_username(browser):
    browser.get(BASE_URL)

    browser.find_element(*USER_NAME).send_keys('standard_userr')
    browser.find_element(*USER_PASSWORD).send_keys('secret_sauce')
    browser.find_element(*BUTTON_LOGIN).click()
    error_text = browser.find_element(*LOGIN_ERROR).text
    assert error_text == 'Epic sadface: Username and password do not match any user in this service', \
        'Wrong Error text on the site'
    assert browser.current_url == BASE_URL, 'Browser go to another URL'
