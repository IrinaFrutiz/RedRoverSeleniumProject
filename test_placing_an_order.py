from locators import Basket, Main
from faker import Faker

fake = Faker()


# Оформление заказа используя корректные данные
def test_placing_an_order_using_correct_data(browser, user_auth):
    browser.find_element(*Main.BUTTON_ADD_TO_CART).click()
    browser.find_element(*Main.BUTTON_BASKET).click()
    browser.find_element(*Basket.CHECKOUT).click()

    browser.find_element(*Basket.INPUT_F_NAME).send_keys(fake.first_name())
    browser.find_element(*Basket.INPUT_L_NAME).send_keys(fake.last_name())
    browser.find_element(*Basket.INPUT_ZIP).send_keys(fake.postcode())

    browser.find_element(*Basket.CONTINUE).click()

    browser.find_element(*Basket.FINISH).click()

    assert browser.find_element(*Basket.THANKS_TEXT).text == "THANK YOU FOR YOUR ORDER", \
        "Wrong text on the page"
