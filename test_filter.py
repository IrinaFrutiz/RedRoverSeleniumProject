from locators import Main


# Проверка работоспособности фильтра (A to Z), базового фильтра
def test_filter_a_to_z(browser, user_auth):
    items = browser.find_elements(*Main.ALL_ITEMS_NAMES)
    items_name_list = []
    for item_id in range(len(items)):
        items_name_list.append(browser.find_element('xpath',
                                                    f'(//div[@class="inventory_item_name"])[{item_id + 1}]').text)
    sorted_list = sorted(items_name_list)

    assert sorted_list == items_name_list, 'Base sorting from a to z is not correct'


# Проверка работоспособности фильтра (Z to A)
def test_filter_z_to_a(browser, user_auth):
    browser.find_element(*Main.BUTTON_FILTER).click()
    browser.find_element(*Main.FILTER_Z_A).click()
    items = browser.find_elements(*Main.ALL_ITEMS_NAMES)
    items_name_list = []
    for item_id in range(len(items)):
        items_name_list.append(browser.find_element('xpath',
                                                    f'(//div[@class="inventory_item_name"])[{item_id + 1}]').text)
    sorted_list = sorted(items_name_list, reverse=True)

    assert sorted_list == items_name_list, 'Sorting from z to z is not correct'


# Проверка работоспособности фильтра (low to high)
def test_filter_low_to_high(browser, user_auth):
    browser.find_element(*Main.BUTTON_FILTER).click()
    browser.find_element(*Main.FILTER_LOW_HIGH).click()
    items = browser.find_elements(*Main.ALL_ITEMS_PRICE)
    items_price_list = []
    for item_id in range(len(items)):
        items_price_list.append(float(browser.find_element('xpath', f'(//div[@class="inventory_item_price"])'
                                                                    f'[{item_id + 1}]').text[1:]))
    sorted_list = sorted(items_price_list)

    assert sorted_list == items_price_list, 'Sorting by price from low to high is not correct'


# Проверка работоспособности фильтра (high to low)
def test_filter_high_to_low(browser, user_auth):
    browser.find_element(*Main.BUTTON_FILTER).click()
    browser.find_element(*Main.FILTER_HIGH_LOW).click()
    items = browser.find_elements(*Main.ALL_ITEMS_PRICE)
    items_price_list = []
    for item_id in range(len(items)):
        items_price_list.append(float(browser.find_element('xpath', f'(//div[@class="inventory_item_price"])'
                                                                    f'[{item_id + 1}]').text[1:]))
    sorted_list = sorted(items_price_list, reverse=True)

    assert sorted_list == items_price_list, 'Sorting by price from high to low is not correct'
