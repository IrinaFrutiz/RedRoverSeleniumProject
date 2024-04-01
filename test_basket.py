from selenium.common import NoSuchElementException
from locators import Basket, URL, Main


# Добавление товара в корзину через каталог
def test_add_item_from_catalog(browser, user_auth):
    browser.find_element(*Main.BUTTON_ADD_TO_CART).click()
    basket_items = browser.find_element(*Main.BASKET_ITEMS).text

    assert basket_items == '1', f"There is more or less item in the basket. {basket_items} not equal 1"


# Удаление товара из корзины через корзину
def test_delete_item_from_the_basket(browser, user_auth):
    browser.find_element(*Main.BUTTON_ADD_TO_CART).click()
    browser.find_element(*Main.BUTTON_BASKET).click()
    browser.find_element(*Basket.BUTTON_REMOVE).click()

    try:
        items_in_the_basket = browser.find_element(*Main.BASKET_ITEMS).text
        assert items_in_the_basket == 0, "Basket is not empty"
    except NoSuchElementException:
        pass
    items_in_the_basket = browser.find_elements(*Basket.ITEMS_IN_THE_BASKET)

    assert len(items_in_the_basket) == 0, "Basket is not empty"


# Добавление товара в корзину из карточки товара
def test_add_item_from_product_card(browser, user_auth):
    browser.get(URL.BACKPACK_URL)
    browser.find_element(*Main.BUTTON_ADD_TO_CART).click()
    basket_items = browser.find_element(*Main.BASKET_ITEMS).text

    assert basket_items == '1', f"There are more or less items in the basket. {basket_items} not equal 1"


# Удаление товара из корзины через карточку товара
def test_delete_item_from_product_card(browser, user_auth):
    browser.get(URL.BACKPACK_URL)
    browser.find_element(*Main.BUTTON_ADD_TO_CART).click()
    browser.find_element(*Basket.BUTTON_REMOVE).click()

    try:
        items_in_the_basket = browser.find_element(*Main.BASKET_ITEMS).text
        assert items_in_the_basket == 0, "Basket is not empty"
    except NoSuchElementException:
        pass
