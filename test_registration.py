def test_registration_with_agree_button(browser):
    browser.get("https://victoretc.github.io/webelements_information/")
    browser.find_element("id", "username").send_keys("a")
    browser.find_element("id", "password").send_keys("b")
    browser.find_element("id", "agreement").click()
    register_button = browser.find_element("id", "registerButton")

    assert register_button.get_attribute("disabled") is None, "Registration button is disabled"
    register_button.click()

    assert browser.find_element("id", "username").text == "", "The form don't refresh"


def test_registration_without_agreement(browser):
    browser.get("https://victoretc.github.io/webelements_information/")
    browser.find_element("id", "username").send_keys("a")
    browser.find_element("id", "password").send_keys("a")
    register_button = browser.find_element("id", "registerButton")
    register_button.click()

    assert register_button.get_attribute("disabled") == "true", "The register button is able to click"


def test_registration_without_pass(browser):
    browser.get("https://victoretc.github.io/webelements_information/")
    browser.find_element("id", "username").send_keys("a")
    browser.find_element("id", "agreement").click()
    register_button = browser.find_element("id", "registerButton")
    register_button.click()

    assert register_button.get_attribute("disabled") == "true", "The register button is able to click"


def test_registration_without_username(browser):
    browser.get("https://victoretc.github.io/webelements_information/")
    browser.find_element("id", "password").send_keys("a")
    browser.find_element("id", "agreement").click()
    register_button = browser.find_element("id", "registerButton")
    register_button.click()

    assert register_button.get_attribute("disabled") == "true", "The register button is able to click"
