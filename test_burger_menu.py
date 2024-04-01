from selenium.common import NoSuchElementException
from locators import Main, Basket, Login


# Выход из системы
def test_user_logout(browser, user_auth):
    browser.find_element(*Main.BUTTON_MENU).click()
    browser.find_element(*Main.BUTTON_LOGOUT).click()

    assert browser.find_element(*Login.BUTTON_LOGIN), 'Element Login is not found'


# Проверка работоспособности кнопки "About" в меню
def test_about(browser, user_auth):
    browser.find_element(*Main.BUTTON_MENU).click()
    browser.find_element(*Main.BUTTON_ABOUT).click()

    assert browser.current_url == 'https://saucelabs.com/' and \
           browser.title == 'Sauce Labs: Cross Browser Testing, Selenium Testing & Mobile Testing', \
           "The site where we go after click about is not correct"


# Проверка работоспособности кнопки "Reset App State"
def test_reset_sidebar_link_basket(browser, user_auth):
    browser.find_element(*Main.BUTTON_ADD_TO_CART).click()
    browser.find_element(*Main.BUTTON_BASKET).click()
    browser.find_element(*Main.BUTTON_MENU).click()
    browser.find_element(*Main.BUTTON_RESET).click()
    browser.refresh()
    items_in_the_basket = browser.find_elements(*Basket.ITEMS_IN_THE_BASKET)

    assert len(items_in_the_basket) == 0, "Basket is not empty"


def test_reset_sidebar_link(browser, user_auth):
    browser.find_element(*Main.BUTTON_ADD_TO_CART).click()
    browser.find_element(*Main.BUTTON_MENU).click()
    browser.find_element(*Main.BUTTON_RESET).click()
    browser.find_element(*Main.BUTTON_CLOSE).click()
    try:
        items_in_the_basket = browser.find_element(*Main.BASKET_ITEMS).text
        assert items_in_the_basket == 0, "Basket is not empty"
    except NoSuchElementException:
        pass
