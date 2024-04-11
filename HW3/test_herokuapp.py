# Так же важно помнить что мы должны получать информацию об вебэлементах и сравнивать ее с ожидаемым результатом.
#
# Например: текст, цвет, расположение, отображение, выбор чекбокса и так далее.
# Ссылка на страницу с документацией: <https://www.selenium.dev/documentation/webdriver/elements/information/>

import pytest
from selenium import webdriver

ADD_BUTTON = ('xpath', '//button[@onclick="addElement()"]')
DELETE_BUTTON = ('xpath', '//button[@onclick="deleteElement()"]')


@pytest.fixture(scope="function", autouse=True)
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    yield driver
    driver.quit()


# 1. <https://the-internet.herokuapp.com/add_remove_elements/> (Необходимо создать и удалить элемент)
def test_create_and_delete_buttons(driver):
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    add_button = driver.find_element(*ADD_BUTTON)

    assert add_button.value_of_css_property('background-color') == "rgba(43, 166, 203, 1)" and \
           add_button.value_of_css_property('color') == 'rgba(255, 255, 255, 1)' and \
           add_button.value_of_css_property("font-size") == '16px' and \
           add_button.text == 'Add Element', "The Element 'Add Element' doesn't look as it should"

    add_button.click()

    delete_button = driver.find_element(*DELETE_BUTTON)

    assert delete_button.value_of_css_property('background-color') == 'rgba(43, 166, 203, 1)' and \
           delete_button.value_of_css_property('color') == 'rgba(255, 255, 255, 1)' and \
           delete_button.value_of_css_property("font-size") == '16px' and \
           delete_button.text == 'Delete', "The Element 'Delete' doesn't look as it should"

    delete_button.click()


# 2. <https://the-internet.herokuapp.com/basic_auth> (Необходимо пройти базовую авторизацию)
def test_base_auth(driver):
    user = 'admin'
    password = 'admin'
    driver.get(f"https://{user}:{password}@the-internet.herokuapp.com/basic_auth")
    confirm_element = driver.find_element('xpath', '//p')

    assert confirm_element.text == 'Congratulations! You must have the proper credentials.', \
        "You don't login to the system"
    assert confirm_element.value_of_css_property('background-color') == 'rgba(0, 0, 0, 0)' and \
           confirm_element.value_of_css_property("color") == 'rgba(34, 34, 34, 1)' and \
           confirm_element.value_of_css_property("font-size") == '16px' and \
           confirm_element.value_of_css_property("margin-top") == '0px', \
           "Message Congratulations doesn't look as it should"
    assert driver.find_element('xpath', '//h3').text == 'Basic Auth'


# 3. <https://the-internet.herokuapp.com/broken_images> (Необходимо найти сломанные изображения)
def test_find_broken_img(driver):
    driver.get('https://the-internet.herokuapp.com/broken_images')
    images = ('xpath', '//img')
    images_on_page = driver.find_elements(*images)
    img_links = [i.get_attribute("src") for i in images_on_page]

    for link in img_links:
        driver.get(link)
        try:
            driver.find_element('xpath', '//h1')
            print(f"\nImage with link {link} is broken")
        except:
            pass


# 4. <https://the-internet.herokuapp.com/checkboxes> (Практика с чек боксами)
def test_checkboxes(driver):
    driver.get('https://the-internet.herokuapp.com/checkboxes')
    checkbox_1 = ('xpath', '(//input)[1]')
    checkbox_2 = ('xpath', '(//input)[2]')

    check_1 = driver.find_element(*checkbox_1)
    check_2 = driver.find_element(*checkbox_2)

    assert check_1.value_of_css_property('background-color') == 'rgba(0, 0, 0, 0)', \
        "Checkbox One doesn't look as it should"

    assert check_2.value_of_css_property('background-color') == 'rgba(0, 0, 0, 0)', \
        "Checkbox Two doesn't look as it should"

    assert check_2.is_selected(), "Checkbox 2 must be selected"

    check_1.click()

    assert check_1.is_selected(), "Checkbox 1 must be selected"

    check_2.click()

    assert not check_2.is_selected(), "Checkbox 2 must be unselected"

    check_1.click()

    assert not check_1.is_selected(), "Checkbox 1 must be unselected"
