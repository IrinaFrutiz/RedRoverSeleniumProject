import pytest


@pytest.fixture(scope="function")
def register_is_disable(browser):
    yield register_is_disable
    assert browser.find_element("id", "registerButton").get_attribute("disabled") == "true", \
        "The register button is able to click"


def test_registration_with_agree_button(browser, register_is_disable):
    browser.get("https://victoretc.github.io/webelements_information/")
    browser.find_element("id", "username").send_keys("a")
    browser.find_element("id", "password").send_keys("b")
    browser.find_element("id", "agreement").click()
    register_button = browser.find_element("id", "registerButton")

    assert register_button.get_attribute("disabled") is None, "Registration button is disabled"
    register_button.click()

    assert browser.find_element("id", "username").text == "", "The form don't refresh"


def test_registration_without_agreement(browser, register_is_disable):
    browser.get("https://victoretc.github.io/webelements_information/")
    browser.find_element("id", "username").send_keys("a")
    browser.find_element("id", "password").send_keys("a")


def test_registration_without_pass(browser, register_is_disable):
    browser.get("https://victoretc.github.io/webelements_information/")
    browser.find_element("id", "username").send_keys("a")
    browser.find_element("id", "agreement").click()


def test_registration_without_username(browser, register_is_disable):
    browser.get("https://victoretc.github.io/webelements_information/")
    browser.find_element("id", "password").send_keys("a")
    browser.find_element("id", "agreement").click()
