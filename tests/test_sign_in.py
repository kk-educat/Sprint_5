from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators


def test_sign_in(driver):
    """Непосредственная проверка входа с зарегестрированным email и верным паролем"""
    test_email = 'kostya_kozhanov_49@domen.org'
    test_pswd = 'e7Yhgt'
    driver.get("https://stellarburgers.education-services.ru/login")
    driver.find_element(By.XPATH, locators.SIGN_IN_MAIL_FIELD).send_keys(test_email)
    driver.find_element(By.XPATH, locators.SIGN_IN_PSWD_FIELD).send_keys(test_pswd)
    driver.find_element(By.XPATH, locators.SIGN_IN_BUTTON).click()
    element = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.CREATE_ORDER_BUTTON)))
    assert element.text == 'Оформить заказ'

def test_sign_in_through_into_account_button(driver):
    """Проверка попадения на страницу входа при нажатии на кнопку Войти в аккаунт
    
       Проверка возможности входа со страницы входа проверяется в функции test_sign_in и проверка этого тут будет лишней.
    """
    driver.get("https://stellarburgers.education-services.ru")
    driver.find_element(By.XPATH, locators.SIGN_IN_INTO_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be('https://stellarburgers.education-services.ru/login'))
    assert driver.current_url == 'https://stellarburgers.education-services.ru/login'

def test_sign_in_through_personal_cabinet(driver):
    """Проверка попадения на страницу входа при нажатии на кнопку Личный кабинет незарегистрированным пользователем"""
    driver.get("https://stellarburgers.education-services.ru")
    driver.find_element(By.XPATH, locators.PERSONAL_CABINET_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be('https://stellarburgers.education-services.ru/login'))
    assert driver.current_url == 'https://stellarburgers.education-services.ru/login'

def test_sign_in_through_link_in_register_form(driver):
    """Проверка попадения на страницу входа при нажатии на ссылку Войти на странице Регистрации"""
    driver.get("https://stellarburgers.education-services.ru/register")
    driver.find_element(By.LINK_TEXT, 'Войти').click()
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be('https://stellarburgers.education-services.ru/login'))
    assert driver.current_url == 'https://stellarburgers.education-services.ru/login'

def test_sign_in_through_link_in_pswd_recovery(driver):
    """Проверка попадения на страницу входа при нажатии на ссылку Войти на странице Восстановления пароля"""
    driver.get("https://stellarburgers.education-services.ru/forgot-password")
    driver.find_element(By.LINK_TEXT, 'Войти').click()
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be('https://stellarburgers.education-services.ru/login'))
    assert driver.current_url == 'https://stellarburgers.education-services.ru/login'
