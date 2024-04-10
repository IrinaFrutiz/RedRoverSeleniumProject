from locators import Basket, Main, ProductCard
from data import URL, random_number


# Добавление товара в корзину через каталог
def test_add_item_from_catalog(browser, user_auth):
    product_add = browser.find_elements(*Main.BUTTON_ADD_TO_CART)
    product_add[random_number(len(product_add))].click()
    basket_items = browser.find_element(*Main.BASKET_ITEMS).text

    assert basket_items == '1', f"There is more or less item in the basket. {basket_items} not equal 1"


# Удаление товара из корзины через корзину
def test_delete_item_from_the_basket(browser, user_auth):
    product_add = browser.find_elements(*Main.BUTTON_ADD_TO_CART)
    product_add[random_number(len(product_add))].click()
    browser.find_element(*Main.BUTTON_BASKET).click()
    browser.find_element(*Main.BUTTON_REMOVE).click()

    assert len(browser.find_elements(*Basket.ITEMS_IN_THE_BASKET)) == 0, "Basket is not empty"


# Добавление товара в корзину из карточки товара
def test_add_item_from_product_card(browser, user_auth):
    product_names = browser.find_elements(*Main.ALL_ITEMS_NAMES)
    product_number = random_number(len(product_names))
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
    product_number = random_number(len(product_names))
    product_names[product_number].click()
    browser.find_element(*Main.BUTTON_ADD_TO_CART).click()
    browser.find_element(*Main.BUTTON_REMOVE).click()

    assert len(browser.find_elements(*Basket.ITEMS_IN_THE_BASKET)) == 0, "Basket is not empty"


# добавление всех товаров из каталога в корзину
def test_add_all_products_to_the_basket(browser, user_auth):
    product_names = browser.find_elements(*Main.ALL_ITEMS_NAMES)
    lst_product_names = []
    for name in product_names:
        lst_product_names.append(name.text)
    product_add_to_cards = browser.find_elements(*Main.BUTTON_ADD_TO_CART)
    for add_to_card in product_add_to_cards:
        add_to_card.click()
    browser.find_element(*Main.BUTTON_BASKET).click()
    product_names_basket = browser.find_elements(*Main.ALL_ITEMS_NAMES)
    lst_product_names_basket = []
    for name in product_names_basket:
        lst_product_names_basket.append(name.text)

    assert lst_product_names == lst_product_names_basket, "Product's names don't much"


# continue shopping
def test_continue_shopping_button(browser, user_auth):
    product_add = browser.find_elements(*Main.BUTTON_ADD_TO_CART)
    product_add[random_number(len(product_add))].click()
    browser.find_element(*Main.BUTTON_BASKET).click()
    browser.find_element(*Basket.CONTINUE_SHOPPING).click()

    assert browser.current_url == URL.MAIN_URL, 'Wrong URL'
    assert browser.find_elements(*Main.ALL_ITEMS_NAMES), "Can't find product's name on the page"
