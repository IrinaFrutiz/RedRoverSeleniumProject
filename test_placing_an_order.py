import pytest
from locators import Basket, Main
from data import random_number, fake_data


# Оформление заказа используя корректные данные
def test_placing_an_order_one_product(browser, user_auth):
    product_add = browser.find_elements(*Main.BUTTON_ADD_TO_CART)
    product_add[random_number(len(product_add))].click()
    browser.find_element(*Main.BUTTON_BASKET).click()
    browser.find_element(*Basket.CHECKOUT).click()

    first, last, zip_code = fake_data()
    browser.find_element(*Basket.INPUT_F_NAME).send_keys(first)
    browser.find_element(*Basket.INPUT_L_NAME).send_keys(last)
    browser.find_element(*Basket.INPUT_ZIP).send_keys(zip_code)

    browser.find_element(*Basket.CONTINUE).click()

    browser.find_element(*Basket.FINISH).click()

    assert browser.find_element(*Basket.THANKS_TEXT).text == "THANK YOU FOR YOUR ORDER", \
        "Wrong text on the page"


# Оформление заказа используя корректные данные 2 продукта
def test_placing_an_order_two_products(browser, user_auth):
    product_add = browser.find_elements(*Main.BUTTON_ADD_TO_CART)
    product_add[random_number(len(product_add))].click()
    product_add[random_number(len(product_add))].click()

    browser.find_element(*Main.BUTTON_BASKET).click()
    browser.find_element(*Basket.CHECKOUT).click()

    first, last, zip_code = fake_data()
    browser.find_element(*Basket.INPUT_F_NAME).send_keys(first)
    browser.find_element(*Basket.INPUT_L_NAME).send_keys(last)
    browser.find_element(*Basket.INPUT_ZIP).send_keys(zip_code)

    browser.find_element(*Basket.CONTINUE).click()

    browser.find_element(*Basket.FINISH).click()

    assert browser.find_element(*Basket.THANKS_TEXT).text == "THANK YOU FOR YOUR ORDER", \
        "Wrong text on the page"


# Проверка попытки покупки без данных о пользователе
def test_placing_an_order_without_user_data(browser, user_auth):
    product_add = browser.find_elements(*Main.BUTTON_ADD_TO_CART)
    product_add[random_number(len(product_add))].click()
    browser.find_element(*Main.BUTTON_BASKET).click()
    browser.find_element(*Basket.CHECKOUT).click()

    browser.find_element(*Basket.CONTINUE).click()

    assert browser.find_element(*Main.ERROR).text == 'Error: First Name is required', 'Wrong error message(first name)'


# Проверка попытки покупки без имени
def test_placing_an_order_without_user_first_name(browser, user_auth):
    product_add = browser.find_elements(*Main.BUTTON_ADD_TO_CART)
    product_add[random_number(len(product_add))].click()
    browser.find_element(*Main.BUTTON_BASKET).click()
    browser.find_element(*Basket.CHECKOUT).click()

    first, last, zip_code = fake_data()
    browser.find_element(*Basket.INPUT_F_NAME).send_keys("")
    browser.find_element(*Basket.INPUT_L_NAME).send_keys(last)
    browser.find_element(*Basket.INPUT_ZIP).send_keys(zip_code)
    browser.find_element(*Basket.CONTINUE).click()

    assert browser.find_element(*Main.ERROR).text == 'Error: First Name is required', 'Wrong error message(first name)'


# Проверка попытки покупки без фамилии
def test_placing_an_order_without_user_last_name(browser, user_auth):
    product_add = browser.find_elements(*Main.BUTTON_ADD_TO_CART)
    product_add[random_number(len(product_add))].click()
    browser.find_element(*Main.BUTTON_BASKET).click()
    browser.find_element(*Basket.CHECKOUT).click()

    first, last, zip_code = fake_data()
    browser.find_element(*Basket.INPUT_F_NAME).send_keys(first)
    browser.find_element(*Basket.INPUT_L_NAME).send_keys("")
    browser.find_element(*Basket.INPUT_ZIP).send_keys(zip_code)
    browser.find_element(*Basket.CONTINUE).click()

    assert browser.find_element(*Main.ERROR).text == 'Error: Last Name is required', 'Wrong error message(last name)'


# Проверка попытки покупки без zip code
def test_placing_an_order_without_user_zip_code(browser, user_auth):
    product_add = browser.find_elements(*Main.BUTTON_ADD_TO_CART)
    product_add[random_number(len(product_add))].click()
    browser.find_element(*Main.BUTTON_BASKET).click()
    browser.find_element(*Basket.CHECKOUT).click()

    first, last, zip_code = fake_data()
    browser.find_element(*Basket.INPUT_F_NAME).send_keys(first)
    browser.find_element(*Basket.INPUT_L_NAME).send_keys(last)
    browser.find_element(*Basket.INPUT_ZIP).send_keys("")
    browser.find_element(*Basket.CONTINUE).click()

    assert browser.find_element(*Main.ERROR).text == 'Error: Postal Code is required', \
        'Wrong error message(zip/postal code)'


# Оформление заказа без продуктов
@pytest.mark.xfail
def test_placing_an_order_without_product(browser, user_auth):
    browser.find_element(*Main.BUTTON_BASKET).click()
    browser.find_element(*Basket.CHECKOUT).click()

    assert browser.find_element(*Main.ERROR).text == "You can't checkout without any product", \
        "Wrong text on the page"


# Оформление заказа без продуктов, удалили продукты
@pytest.mark.xfail
def test_placing_an_order_with_removed_product(browser, user_auth):
    product_add = browser.find_elements(*Main.BUTTON_ADD_TO_CART)
    product_add[random_number(len(product_add))].click()
    browser.find_element(*Main.BUTTON_BASKET).click()

    browser.find_element(*Main.BUTTON_REMOVE)
    browser.find_element(*Basket.CHECKOUT).click()

    assert browser.find_element(*Main.ERROR).text == "You can't checkout without any product", \
        "Wrong text on the page"
