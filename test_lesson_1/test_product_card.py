from test_auth import BASE_URL, test_auth_positive

PRODUCT_IMG = ('xpath', '//*[@id="item_4_img_link"]/img')
PRODUCT_NAME = ('xpath', '//*[@id="item_4_title_link"]')


# Успешный переход к карточке товара после клика на картинку товара
def test_go_to_product_card_img(browser, test_auth_positive):
    browser.find_element(*PRODUCT_IMG).click()
    assert f'{BASE_URL}inventory-item.html?id=' in browser.current_url, \
        "It's not a product page"


# Успешный переход к карточке товара после клика на название товара
def test_go_to_product_card_name(browser, test_auth_positive):
    browser.find_element(*PRODUCT_NAME).click()
    assert f'{BASE_URL}inventory-item.html?id=' in browser.current_url, \
        "It's not a product page"
