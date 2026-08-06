from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators


class TestAccessToConstructor:
    def test_access_to_constructor_through_link(self, driver):
        # входим в аккаунт
        driver.get("https://stellarburgers.education-services.ru/login")
        driver.find_element(By.XPATH, locators.SIGN_IN_MAIL_FIELD).send_keys('kostya_kozhanov_49@domen.org')
        driver.find_element(By.XPATH, locators.SIGN_IN_PSWD_FIELD).send_keys('e7Yhgt')
        driver.find_element(By.XPATH, locators.SIGN_IN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.CREATE_ORDER_BUTTON)))
        # переходим в личный кабинет
        driver.find_element(By.XPATH, locators.PERSONAL_CABINET_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be('https://stellarburgers.education-services.ru/account/profile'))
        # проверяем переход в конструктор
        driver.find_element(By.XPATH, locators.CONSTRUCTOR_LINK).click()
        header = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.CONSTRUCTOR_HEADER)))
        assert header.text == 'Соберите бургер'
        
    def test_access_to_constructor_through_logo(self, driver):
        # входим в аккаунт
        driver.get("https://stellarburgers.education-services.ru/login")
        driver.find_element(By.XPATH, locators.SIGN_IN_MAIL_FIELD).send_keys('kostya_kozhanov_49@domen.org')
        driver.find_element(By.XPATH, locators.SIGN_IN_PSWD_FIELD).send_keys('e7Yhgt')
        driver.find_element(By.XPATH, locators.SIGN_IN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.CREATE_ORDER_BUTTON)))
        # переходим в личный кабинет
        driver.find_element(By.XPATH, locators.PERSONAL_CABINET_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be('https://stellarburgers.education-services.ru/account/profile'))
        # проверяем переход в конструктор
        driver.find_element(By.XPATH, locators.LOGO_LINK).click()
        header = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.CONSTRUCTOR_HEADER)))
        assert header.text == 'Соберите бургер'
