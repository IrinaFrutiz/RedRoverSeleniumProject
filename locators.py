class Login:
    USER_NAME = ('id', 'user-name')
    USER_PASSWORD = ('id', 'password')
    BUTTON_LOGIN = ('id', 'login-button')
    LOGIN_ERROR = ('xpath', '//h3')


class Basket:
    BUTTON_REMOVE = ('xpath', '//button[text()="REMOVE"]')
    ITEMS_IN_THE_BASKET = ('xpath', '//div[@class="cart_item"]')
    CHECKOUT = ('xpath', '//a[@class="btn_action checkout_button"]')
    INPUT_F_NAME = ('id', 'first-name')
    INPUT_L_NAME = ('id', 'last-name')
    INPUT_ZIP = ('id', 'postal-code')
    CONTINUE = ('xpath', '//input[@type="submit"]')
    FINISH = ('xpath', '//*[@id="checkout_summary_container"]//a[2]')
    THANKS_TEXT = ('xpath', '//h2')


class Main:
    BUTTON_MENU = ('xpath', '//button[text()="Open Menu"]')
    BUTTON_ALL_ITEMS = ('id', 'inventory_sidebar_link')
    BUTTON_ABOUT = ('id', 'about_sidebar_link')
    BUTTON_LOGOUT = ('id', 'logout_sidebar_link')
    BUTTON_RESET = ('id', 'reset_sidebar_link')
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
    SOCIAL_MEDIA_TWITTER =('class name', 'social_twitter')
    SOCIAL_MEDIA_FACEBOOK =('class name', 'social_facebook')
    SOCIAL_MEDIA_LINKEDIN =('class name', 'social_linkedin')
    FOOTER =('class name', 'footer_copy')


class ProductCard:
    PRODUCT_NAME = ('xpath', '//div[@class ="inventory_details_name"]')
