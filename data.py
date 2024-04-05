class URL:
    BASE_URL = 'https://www.saucedemo.com/v1/'
    MAIN_URL = BASE_URL + 'inventory.html'
    BACKPACK_URL = BASE_URL + 'inventory-item.html?id=4'
    PART_OF_PRODUCT_URL = BASE_URL + 'inventory-item.html?id='


class Data:
    USER_CORRECT = 'standard_user'
    user_incorrect = 'a'
    USER_LOCKED = 'locked_out_user'
    USER_PROBLEM = 'problem_user'
    USER_PERFORMANCE = 'performance_glitch_user'
    PASS_CORRECT = 'secret_sauce'
    pass_incorrect = 'bsecret_sauce'


def random_number(num):
    import random
    return random.randint(0, num - 1)


def fake_data():
    from faker import Faker
    fake = Faker()
    return fake.first_name(), fake.last_name(), fake.postcode()
