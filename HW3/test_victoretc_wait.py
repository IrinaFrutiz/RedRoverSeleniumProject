import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


TEXT_H1 = ("xpath", '//h1')
START_TIME = ('id', 'startTest')
LOGIN = ('id', 'login')
PASSWORD = ('id', 'password')
AGREE = ('id', 'agree')
REGISTER = ('id', 'register')
LOADER = ('id', 'loader')
MESSAGE = ('id', 'successMessage')


@pytest.fixture(scope="function", autouse=True)
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    browser = webdriver.Chrome(options=chrome_options)

    yield browser
    browser.quit()


def test_site_registration_explicitly(browser):
    # Открыть в браузере указанный URL сайта
    browser.get("https://victoretc.github.io/selenium_waits/")
    # Проверить заголовок: Убедиться, что текст в теге <h1> на странице соответствует "Практика с ожиданиями в Selenium"
    assert browser.find_element(*TEXT_H1).text == 'Практика с ожиданиями в Selenium', "Wrong text in H1 tag"
    #  Дождаться появления кнопки "Начать тестирование"
    # * Найти кнопку: Найти на странице кнопку с текстом "Начать тестирование".
    # * Начать тестирование: Кликнуть по кнопке "Начать тестирование".
    start_testing = WebDriverWait(browser, timeout=10).until(EC.element_to_be_clickable(START_TIME))
    assert start_testing.text == 'Начать тестирование', 'Wrong text Начать тестирование'
    start_testing.click()
    #     Ввод логина: Ввести "login" в поле для логина.
    browser.find_element(*LOGIN).send_keys('login_text')
    # * Ввод пароля: Ввести "password" в поле для пароля.
    browser.find_element(*PASSWORD).send_keys('password_text')
    # * Согласие с правилами: Установить флажок в чекбокс "Согласен со всеми правилами".
    browser.find_element(*AGREE).click()
    # * Подтвердить регистрацию: Нажать кнопку "Зарегистрироваться".
    browser.find_element(*REGISTER).click()
    # * Проверка загрузки: Удостовериться, что появился индикатор загрузки.
    assert browser.find_element(*LOADER).is_displayed(), "loader do not displayed"
    # * Проверка сообщения: Убедиться, что после завершения загрузки появилось сообщение "Вы успешно зарегистрированы".
    success_message = WebDriverWait(browser, timeout=10).until(EC.visibility_of_element_located(MESSAGE))
    assert success_message.text == "Вы успешно зарегистрированы!", 'wrong successMessage'


def test_site_registration_implicitly(browser):
    def wait_until_the_element_appears(element):
        while not element.is_displayed():
            pass
    # Открыть в браузере указанный URL сайта
    browser.implicitly_wait(10)
    browser.get("https://victoretc.github.io/selenium_waits/")
    # Проверить заголовок: Убедиться, что текст в теге <h1> на странице соответствует "Практика с ожиданиями в Selenium"
    assert browser.find_element(*TEXT_H1).text == 'Практика с ожиданиями в Selenium', "Wrong text in H1 tag"
    #  Дождаться появления кнопки "Начать тестирование"
    # * Найти кнопку: Найти на странице кнопку с текстом "Начать тестирование".
    # * Начать тестирование: Кликнуть по кнопке "Начать тестирование".
    start_time = browser.find_element(*START_TIME)
    wait_until_the_element_appears(start_time)
    assert start_time.text == 'Начать тестирование', 'Wrong text Начать тестирование'
    start_time.click()
    #     Ввод логина: Ввести "login" в поле для логина.
    browser.find_element(*LOGIN).send_keys('login_text')
    # * Ввод пароля: Ввести "password" в поле для пароля.
    browser.find_element(*PASSWORD).send_keys('password_text')
    # * Согласие с правилами: Установить флажок в чекбокс "Согласен со всеми правилами".
    browser.find_element(*AGREE).click()
    # * Подтвердить регистрацию: Нажать кнопку "Зарегистрироваться".
    browser.find_element(*REGISTER).click()
    # * Проверка загрузки: Удостовериться, что появился индикатор загрузки.
    assert browser.find_element(*LOADER).is_displayed(), "loader do not displayed"
    # * Проверка сообщения: Убедиться, что после завершения загрузки появилось сообщение "Вы успешно зарегистрированы".
    success_message = browser.find_element(*MESSAGE)
    wait_until_the_element_appears(success_message)
    assert success_message.text == "Вы успешно зарегистрированы!", 'wrong successMessage'


def test_site_registration_time(browser):
    # Открыть в браузере указанный URL сайта
    browser.get("https://victoretc.github.io/selenium_waits/")
    # Проверить заголовок: Убедиться, что текст в теге <h1> на странице соответствует "Практика с ожиданиями в Selenium"
    assert browser.find_element(*TEXT_H1).text == 'Практика с ожиданиями в Selenium', "Wrong text in H1 tag"
    #  Дождаться появления кнопки "Начать тестирование"
    # * Найти кнопку: Найти на странице кнопку с текстом "Начать тестирование".
    # * Начать тестирование: Кликнуть по кнопке "Начать тестирование".
    start_time = browser.find_element(*START_TIME)
    time.sleep(5)
    assert start_time.text == 'Начать тестирование', 'Wrong text Начать тестирование'
    start_time.click()
    #     Ввод логина: Ввести "login" в поле для логина.
    browser.find_element(*LOGIN).send_keys('login_text')
    # * Ввод пароля: Ввести "password" в поле для пароля.
    browser.find_element(*PASSWORD).send_keys('password_text')
    # * Согласие с правилами: Установить флажок в чекбокс "Согласен со всеми правилами".
    browser.find_element(*AGREE).click()
    # * Подтвердить регистрацию: Нажать кнопку "Зарегистрироваться".
    browser.find_element(*REGISTER).click()
    # * Проверка загрузки: Удостовериться, что появился индикатор загрузки.
    assert browser.find_element(*LOADER).is_displayed(), "loader do not displayed"
    # * Проверка сообщения: Убедиться, что после завершения загрузки появилось сообщение "Вы успешно зарегистрированы".
    success_message = browser.find_element(*MESSAGE)
    time.sleep(5)
    assert success_message.text == "Вы успешно зарегистрированы!", 'wrong successMessage'
