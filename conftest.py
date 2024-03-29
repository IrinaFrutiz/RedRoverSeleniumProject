import pytest
from selenium import webdriver


@pytest.fixture(scope="function", autouse=True)
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(5)
    yield browser
    browser.quit()
