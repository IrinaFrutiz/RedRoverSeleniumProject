from locators import ProductCard, URL, Main


# Успешный переход к карточке товара после клика на картинку товара
def test_go_to_product_card_img(browser, user_auth):
    browser.find_element(*Main.PRODUCT_IMG).click()

    assert URL.PART_OF_PRODUCT_URL in browser.current_url, "It's not a product page"


# Успешный переход к карточке товара после клика на название товара
def test_go_to_product_card_name(browser, user_auth):
    first_product_name = browser.find_element(*Main.PRODUCT_NAME)
    first_product_name_text = first_product_name.text
    first_product_name.click()

    assert URL.PART_OF_PRODUCT_URL in browser.current_url \
           and first_product_name_text == browser.find_element(*ProductCard.PRODUCT_NAME).text, \
           "It's not a product page"
