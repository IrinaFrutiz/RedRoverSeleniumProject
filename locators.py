class URL:
    BASE_URL = 'https://www.saucedemo.com/v1/'
    BACKPACK_URL = BASE_URL + 'inventory-item.html?id=4'
    PART_OF_PRODUCT_URL = BASE_URL + 'inventory-item.html?id='


class Login:
    USER_NAME = ('xpath', '//*[@id="user-name"]')
    USER_PASSWORD = ('xpath', '//*[@id="password"]')
    BUTTON_LOGIN = ('xpath', '//*[@id="login-button"]')
    LOGIN_ERROR = ('xpath', '//h3')


class Basket:
    BUTTON_REMOVE = ('xpath', '//button[text()="REMOVE"]')
    ITEMS_IN_THE_BASKET = ('xpath', '//div[@class="cart_item"]')
    CHECKOUT = ('xpath', '//a[@class="btn_action checkout_button"]')
    INPUT_F_NAME = ('xpath', '//*[@id="first-name"]')
    INPUT_L_NAME = ('xpath', '//*[@id="last-name"]')
    INPUT_ZIP = ('xpath', '//*[@id="postal-code"]')
    CONTINUE = ('xpath', '//input[@type="submit"]')
    FINISH = ('xpath', '//*[@id="checkout_summary_container"]//a[2]')
    THANKS_TEXT = ('xpath', '//h2')


class Main:
    BUTTON_MENU = ('xpath', '//button[text()="Open Menu"]')
    BUTTON_LOGOUT = ('xpath', '//*[@id="logout_sidebar_link"]')
    BUTTON_ABOUT = ('xpath', '//*[@id="about_sidebar_link"]')
    BUTTON_RESET = ('xpath', '//*[@id="reset_sidebar_link"]')
    BUTTON_CLOSE = ('xpath', '//button[text()="Close Menu"]')
    ALL_ITEMS_NAMES = ('xpath', '//div[@class="inventory_item_name"]')
    ALL_ITEMS_PRICE = ('xpath', '//div[@class="inventory_item_price"]')
    BUTTON_FILTER = ('xpath', '//*[@id="inventory_filter_container"]/select')
    FILTER_Z_A = ('xpath', '//option[2]')
    FILTER_LOW_HIGH = ('xpath', '//option[3]')
    FILTER_HIGH_LOW = ('xpath', '//option[4]')
    PRODUCT_NAME = ('xpath', '//*[@class="inventory_item_name"]')
    PRODUCT_IMG = ('xpath', '//*[@id="item_4_img_link"]/img')
    BUTTON_BASKET = ('xpath', '//*[@id="shopping_cart_container"]')
    BASKET_ITEMS = ('xpath', '//*[@id="shopping_cart_container"]/a/span')
    BUTTON_ADD_TO_CART = ('xpath', '//button[text()="ADD TO CART"]')
    BUTTON_REMOVE = ('xpath', '//button[text()="REMOVE"]')


class ProductCard:
    PRODUCT_NAME = ('xpath', '//div[@class ="inventory_details_name"]')
