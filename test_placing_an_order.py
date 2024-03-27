from test_basket import BUTTON_ADD_TO_CART, BASKET
from faker import Faker
from test_auth import user_auth

fake = Faker()


CHECKOUT = ('xpath', '//a[@class="btn_action checkout_button"]')
INPUT_F_NAME = ('xpath', '//*[@id="first-name"]')
INPUT_L_NAME = ('xpath', '//*[@id="last-name"]')
INPUT_ZIP = ('xpath', '//*[@id="postal-code"]')
CONTINUE = ('xpath', '//input[@type="submit"]')
FINISH = ('xpath', '//*[@id="checkout_summary_container"]//a[2]')
THANKS_TEXT = ('xpath', '//h2')


# Оформление заказа используя корректные данные
def test_placing_an_order_using_correct_data(browser, user_auth):
    browser.find_element(*BUTTON_ADD_TO_CART).click()
    browser.find_element(*BASKET).click()
    browser.find_element(*CHECKOUT).click()
    browser.find_element(*INPUT_F_NAME).send_keys(fake.first_name())
    browser.find_element(*INPUT_L_NAME).send_keys(fake.last_name())
    browser.find_element(*INPUT_ZIP).send_keys(fake.postcode())
    browser.find_element(*CONTINUE).click()
    browser.find_element(*FINISH).click()
    assert browser.find_element(*THANKS_TEXT).text == "THANK YOU FOR YOUR ORDER", \
        "Wrong text on the page"
