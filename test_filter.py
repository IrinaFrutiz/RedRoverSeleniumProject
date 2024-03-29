from test_auth import user_auth

ALL_ITEMS_NAMES = ('xpath', '//div[@class="inventory_item_name"]')
ALL_ITEMS_PRICE = ('xpath', '//div[@class="inventory_item_price"]')
DROPDOWN = ('xpath', '//*[@id="inventory_filter_container"]/select')
Z_A = ('xpath', '//option[2]')
LOW_HIGH = ('xpath', '//option[3]')
HIGH_LOW = ('xpath', '//option[4]')


# Проверка работоспособности фильтра (A to Z)
def test_filter_a_to_z(browser, user_auth):
    items = browser.find_elements(*ALL_ITEMS_NAMES)
    items_name_list = []
    for item_id in range(len(items)):
        items_name_list.append(browser.find_element('xpath',
                                                    f'(//div[@class="inventory_item_name"])[{item_id + 1}]').text)
    sorted_list = sorted(items_name_list)
    for i in range(len(items)):
        assert sorted_list[i] == items_name_list[i], f'{sorted_list[i]} != {items_name_list[i]}'


# Проверка работоспособности фильтра (Z to A)
def test_filter_z_to_a(browser, user_auth):
    browser.find_element(*DROPDOWN).click()
    browser.find_element(*Z_A).click()
    items = browser.find_elements(*ALL_ITEMS_NAMES)
    items_name_list = []
    for item_id in range(len(items)):
        items_name_list.append(browser.find_element('xpath',
                                                    f'(//div[@class="inventory_item_name"])[{item_id + 1}]').text)
    sorted_list = sorted(items_name_list, reverse=True)
    for i in range(len(items)):
        assert sorted_list[i] == items_name_list[i], f'{sorted_list[i]} != {items_name_list[i]}'


# Проверка работоспособности фильтра (low to high)
def test_filter_low_to_high(browser, user_auth):
    browser.find_element(*DROPDOWN).click()
    browser.find_element(*LOW_HIGH).click()
    items = browser.find_elements(*ALL_ITEMS_PRICE)
    items_price_list = []
    for item_id in range(len(items)):
        items_price_list.append(float(browser.find_element('xpath',
                                                           f'(//div[@class="inventory_item_price"])[{item_id + 1}]').text[
                                      1:]))
    sorted_list = sorted(items_price_list)
    for i in range(len(items)):
        assert sorted_list[i] == items_price_list[i], f'{sorted_list[i]} != {items_price_list[i]}'


# Проверка работоспособности фильтра (high to low)
def test_filter_high_to_low(browser, user_auth):
    browser.find_element(*DROPDOWN).click()
    browser.find_element(*HIGH_LOW).click()
    items = browser.find_elements(*ALL_ITEMS_PRICE)
    items_price_list = []
    for item_id in range(len(items)):
        items_price_list.append(float(browser.find_element('xpath',
                                            f'(//div[@class="inventory_item_price"])[{item_id + 1}]').text[1:]))
    sorted_list = sorted(items_price_list, reverse=True)
    for i in range(len(items)):
        assert sorted_list[i] == items_price_list[i], f'{sorted_list[i]} != {items_price_list[i]}'
