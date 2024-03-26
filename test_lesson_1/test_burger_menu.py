from test_auth import BASE_URL
from test_basket import BUTTON_ADD_TO_CART, ITEMS_IN_THE_BASKET
from test_lesson_1.test_auth import test_auth_positive

BUTTON_MENU = ('xpath', '//button[text()="Open Menu"]')
BUTTON_LOGOUT = ('xpath', '//*[@id="logout_sidebar_link"]')
BUTTON_ABOUT = ('xpath', '//*[@id="about_sidebar_link"]')
BUTTON_RESET = ('xpath', '//*[@id="reset_sidebar_link"]')
BUTTON_CLOSE = ('xpath', '(//button)[1]')


# Выход из системы
def test_user_logout(browser, test_auth_positive):
    browser.find_element(*BUTTON_MENU).click()
    browser.find_element(*BUTTON_LOGOUT).click()
    assert browser.current_url == f'{BASE_URL}index.html', 'Browser go to another URL'
    assert browser.title == 'Swag Labs', 'Wrong browser title'


# Проверка работоспособности кнопки "About" в меню
def test_about(browser, test_auth_positive):
    browser.find_element(*BUTTON_MENU).click()
    browser.find_element(*BUTTON_ABOUT).click()
    assert browser.current_url == 'https://saucelabs.com/', "Wrong browser URL"
    assert browser.title == 'Sauce Labs: Cross Browser Testing, Selenium Testing & Mobile Testing', \
        "Wrong browser title"


# Проверка работоспособности кнопки "Reset App State"
def test_reset_sidebar_link(browser, test_auth_positive):
    browser.find_element(*BUTTON_ADD_TO_CART).click()
    browser.find_element(*BUTTON_MENU).click()
    browser.find_element(*BUTTON_RESET).click()
    browser.find_element(*BUTTON_CLOSE).click()
    items_in_the_basket = browser.find_elements(*ITEMS_IN_THE_BASKET)
    assert len(items_in_the_basket) == 0, "Basket is not empty"
