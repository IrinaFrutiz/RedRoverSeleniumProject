class URL:
    BASE_URL = 'https://www.saucedemo.com/v1/'
    BACKPACK_URL = BASE_URL + 'inventory-item.html?id=4'
    PART_OF_PRODUCT_URL = BASE_URL + 'inventory-item.html?id='


class Data:
    user_correct = 'standard_user'
    user_incorrect = 'a'
    user_locked = 'locked_out_user'
    user_problem = 'problem_user'
    user_performance = 'performance_glitch_user'
    pass_correct = 'secret_sauce'
    pass_incorrect = 'bsecret_sauce'
