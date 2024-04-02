from selenium.common import NoSuchElementException
from locators import Main, Basket, Login


# Все элементы меню видны
def test_all_menu_elements_are_visible(browser, user_auth):
    browser.find_element(*Main.BUTTON_MENU).click()

    assert browser.find_element(*Main.BUTTON_ALL_ITEMS), "Element All Items in Menu do not present"
    assert browser.find_element(*Main.BUTTON_ABOUT), "Element About in Menu do not present"
    assert browser.find_element(*Main.BUTTON_LOGOUT), "Element Logout in Menu do not present"
    assert browser.find_element(*Main.BUTTON_RESET), "Element Reset App State in Menu do not present"
    assert browser.find_element(*Main.BUTTON_CLOSE), "Element Close Menu in Menu do not present"


# Выход из системы
def test_user_logout(browser, user_auth):
    browser.find_element(*Main.BUTTON_MENU).click()
    browser.find_element(*Main.BUTTON_LOGOUT).click()

    assert browser.find_element(*Login.BUTTON_LOGIN), 'User do not logout'


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
