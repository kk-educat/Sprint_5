from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from generator import generate_login
import locators


class TestSignUp:
    def test_registration_success(self, driver):
        test_pswd = 'e7Yhgt'
        test_user_name = 'Konstantin'
        test_email = generate_login()
        driver.get("https://stellarburgers.education-services.ru/register")
        driver.find_element(By.XPATH, locators.REGISTRATION_NAME_FIELD).send_keys(test_user_name)
        driver.find_element(By.XPATH, locators.REGISTRATION_MAIL_FIELD).send_keys(test_email)
        driver.find_element(By.XPATH, locators.REGISTRATION_PSWD_FIELD).send_keys(test_pswd)
        driver.find_element(By.XPATH, locators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be('https://stellarburgers.education-services.ru/login'))
        assert driver.current_url == 'https://stellarburgers.education-services.ru/login'

    def test_registration_error(self, driver):
        test_pswd = 'e7Yhg' # некорректный пароль длиной меньше 6 символов
        test_user_name = 'Konstantin'
        test_email = generate_login()
        driver.get("https://stellarburgers.education-services.ru/register")
        driver.find_element(By.XPATH, locators.REGISTRATION_NAME_FIELD).send_keys(test_user_name)
        driver.find_element(By.XPATH, locators.REGISTRATION_MAIL_FIELD).send_keys(test_email)
        driver.find_element(By.XPATH, locators.REGISTRATION_PSWD_FIELD).send_keys(test_pswd)
        driver.find_element(By.XPATH, locators.REGISTRATION_BUTTON).click()
        error = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.REGISTRATION_WRONG_PSWD_MSG)))
        assert error.text == "Некорректный пароль"
