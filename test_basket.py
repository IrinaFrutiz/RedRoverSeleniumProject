from selenium.common import NoSuchElementException
from test_auth import user_auth

BUTTON_ADD_TO_CART = ('xpath', '//button[text()="ADD TO CART"]')
BUTTON_REMOVE = ('xpath', '//button[text()="REMOVE"]')
BASKET_ITEMS = ('xpath', '//*[@id="shopping_cart_container"]/a/span')
BASKET = ('xpath', '//*[@id="shopping_cart_container"]')
ITEMS_IN_THE_BASKET = ('xpath', '//div[@class="cart_item"]')


# Добавление товара в корзину через каталог
def test_add_item_from_catalog(browser, user_auth):
    browser.find_element(*BUTTON_ADD_TO_CART).click()
    basket_items = browser.find_element(*BASKET_ITEMS).text
    assert basket_items == '1', f"There is more or less item in the basket. {basket_items} not equal 1"


# Удаление товара из корзины через корзину
def test_delete_item_from_the_basket(browser, user_auth):
    browser.find_element(*BUTTON_ADD_TO_CART).click()
    browser.find_element(*BASKET).click()
    browser.find_element(*BUTTON_REMOVE).click()
    try:
        items_in_the_basket = browser.find_element(*BASKET_ITEMS).text
        assert items_in_the_basket == 0, "Basket is not empty"
    except NoSuchElementException:
        pass
    items_in_the_basket = browser.find_elements(*ITEMS_IN_THE_BASKET)
    assert len(items_in_the_basket) == 0, "Basket is not empty"


# Добавление товара в корзину из карточки товара
def test_add_item_from_product_card(browser, user_auth):
    browser.get('https://www.saucedemo.com/v1/inventory-item.html?id=4')
    browser.find_element(*BUTTON_ADD_TO_CART).click()
    basket_items = browser.find_element(*BASKET_ITEMS).text
    assert basket_items == '1', f"There are more or less items in the basket. {basket_items} not equal 1"


# Удаление товара из корзины через карточку товара
def test_delete_item_from_product_card(browser, user_auth):
    browser.get('https://www.saucedemo.com/v1/inventory-item.html?id=4')
    browser.find_element(*BUTTON_ADD_TO_CART).click()
    browser.find_element(*BUTTON_REMOVE).click()
    try:
        items_in_the_basket = browser.find_element(*BASKET_ITEMS).text
        assert items_in_the_basket == 0, "Basket is not empty"
    except NoSuchElementException:
        pass
