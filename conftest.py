import pytest
from selenium import webdriver
from locators import Login, URL


@pytest.fixture(scope="function", autouse=True)
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(5)

    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def user_auth(browser):
    browser.get(URL.BASE_URL)
    browser.find_element(*Login.USER_NAME).send_keys('standard_user')
    browser.find_element(*Login.USER_PASSWORD).send_keys('secret_sauce')
    browser.find_element(*Login.BUTTON_LOGIN).click()
