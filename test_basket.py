import time

from selenium.common import NoSuchElementException
from locators import Basket, Main, ProductCard
from data import URL
import random


# Добавление товара в корзину через каталог
def test_add_item_from_catalog(browser, user_auth):
    product_add = browser.find_elements(*Main.BUTTON_ADD_TO_CART)
    product_add[random.randint(0, len(product_add) - 1)].click()
    basket_items = browser.find_element(*Main.BASKET_ITEMS).text

    assert basket_items == '1', f"There is more or less item in the basket. {basket_items} not equal 1"


# Удаление товара из корзины через корзину
def test_delete_item_from_the_basket(browser, user_auth):
    product_add = browser.find_elements(*Main.BUTTON_ADD_TO_CART)
    product_add[random.randint(0, len(product_add) - 1)].click()
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
    product_names = browser.find_elements(*Main.ALL_ITEMS_NAMES)
    product_number = random.randint(0, len(product_names) - 1)
    product_name = product_names[product_number].text
    product_names[product_number].click()
    browser.find_element(*Main.BUTTON_ADD_TO_CART).click()
    basket_items = browser.find_element(*Main.BASKET_ITEMS).text
    product_name_basket = browser.find_element(*ProductCard.PRODUCT_NAME).text

    assert product_name == product_name_basket, \
        f"Wrong product's name on basket. {product_names} != {product_name_basket}"
    assert basket_items == '1', f"There are more or less items in the basket. {basket_items} not equal 1"


# Удаление товара из корзины через карточку товара
def test_delete_item_from_product_card(browser, user_auth):
    product_names = browser.find_elements(*Main.ALL_ITEMS_NAMES)
    product_number = random.randint(0, len(product_names) - 1)
    product_names[product_number].click()
    browser.find_element(*Main.BUTTON_ADD_TO_CART).click()
    browser.find_element(*Basket.BUTTON_REMOVE).click()

    try:
        items_in_the_basket = browser.find_element(*Main.BASKET_ITEMS).text
        assert items_in_the_basket == 0, "Basket is not empty"
    except NoSuchElementException:
        pass
