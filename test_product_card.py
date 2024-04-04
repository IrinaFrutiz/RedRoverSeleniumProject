from locators import ProductCard, Main
from data import URL, random_number


# Успешный переход к карточке товара после клика на картинку товара + browser back
def test_go_to_product_card_img(browser, user_auth):
    product_images = browser.find_elements(*Main.ALL_ITEMS_IMAGES)
    number_of_product = random_number(len(product_images))
    product_images[number_of_product].click()

    assert URL.PART_OF_PRODUCT_URL in browser.current_url, "It's not a product page"
    browser.back()


# Успешный переход к карточке товара после клика на название товара и использование back на карточке товара
def test_go_to_product_card_name(browser, user_auth):
    product_names = browser.find_elements(*Main.ALL_ITEMS_NAMES)
    number_of_product = random_number(len(product_names))
    product_name = product_names[number_of_product].text
    product_names[number_of_product].click()

    assert URL.PART_OF_PRODUCT_URL in browser.current_url, "Wrong URL"
    assert product_name == browser.find_element(*ProductCard.PRODUCT_NAME).text, \
        "Different product's name on main and product pages"

    browser.find_element(*ProductCard.BACK).click()


# сравнение описания товара на главной странице и в карточке + back
def test_check_product_descriptions(browser, user_auth):
    product_names = browser.find_elements(*Main.ALL_ITEMS_NAMES)
    product_descriptions = browser.find_elements(*Main.ALL_ITEMS_DESCRIPTIONS)
    number_of_product = random_number(len(product_names))
    product_name = product_names[number_of_product].text
    product_desc = product_descriptions[number_of_product].text
    product_names[number_of_product].click()

    assert product_desc == browser.find_element(*ProductCard.DESCRIPTION).text, \
        f"Item with name {product_name} have different description on main and product pages"


# сравнение цены товара на главной странице и в карточке
def test_check_product_prices(browser, user_auth):
    product_names = browser.find_elements(*Main.ALL_ITEMS_NAMES)
    product_prises = browser.find_elements(*Main.ALL_ITEMS_PRICES)
    number_of_product = random_number(len(product_names))
    product_name = product_names[number_of_product].text
    product_price = product_prises[number_of_product].text
    product_names[number_of_product].click()

    assert product_price == browser.find_element(*ProductCard.PRICE).text, \
        f"Item with name {product_name} have different price on main page {product_price} and product"


# проверка перехода на продуктовую страницу из корзины
def test_check_product_page_from_basket(browser, user_auth):
    product_add = browser.find_elements(*Main.BUTTON_ADD_TO_CART)
    number_of_products = random_number(len(product_add))
    product_add[number_of_products].click()
    browser.find_element(*Main.BUTTON_BASKET).click()
    product_name_basket = browser.find_element(*Main.ALL_ITEMS_NAMES)
    name_basket = product_name_basket.text
    product_name_basket.click()

    assert name_basket == browser.find_element(*ProductCard.PRODUCT_NAME).text, \
        "The product name in your cart does not match the product name on the product page."
    assert URL.PART_OF_PRODUCT_URL in browser.current_url, "Wrong URL"
