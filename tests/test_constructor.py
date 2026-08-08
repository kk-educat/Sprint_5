from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators


class TestConstructor:
    def test_access_to_sauces_section(self, driver):
        # входим в аккаунт
        driver.get("https://stellarburgers.education-services.ru/login")
        driver.find_element(By.XPATH, locators.SIGN_IN_MAIL_FIELD).send_keys('kostya_kozhanov_49@domen.org')
        driver.find_element(By.XPATH, locators.SIGN_IN_PSWD_FIELD).send_keys('e7Yhgt')
        driver.find_element(By.XPATH, locators.SIGN_IN_BUTTON).click()
        # ПРОВЕРЯЕМ ПЕРЕХОД К РАЗДЕЛУ "СОУСЫ"
        # дожидаемся кликабельности раздела Соусы и кликаем на него
        section = WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, locators.SAUCES_SECTION)))
        section.click()
        # ожидаем изменения активного раздела конструктора и сохраняем его в переменную
        active_section = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.ACTIVE_SECTION.format(section_name='Соусы'))))
        # проверяем наличие слова Соусы в текстовом содержимом элемента active_section и вложенных в него элементов
        assert 'Соусы' in active_section.text

    def test_access_to_fillings_section(self, driver):
        # входим в аккаунт
        driver.get("https://stellarburgers.education-services.ru/login")
        driver.find_element(By.XPATH, locators.SIGN_IN_MAIL_FIELD).send_keys('kostya_kozhanov_49@domen.org')
        driver.find_element(By.XPATH, locators.SIGN_IN_PSWD_FIELD).send_keys('e7Yhgt')
        driver.find_element(By.XPATH, locators.SIGN_IN_BUTTON).click()
        # проверяем переход к разделу Начинки (аналогично тестовому шагу для раздела Соусы)
        section = WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, locators.FILLINGS_SECTION)))
        section.click()
        active_section = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.ACTIVE_SECTION.format(section_name='Начинки'))))
        assert 'Начинки' in active_section.text

    def test_access_to_buns_section(self, driver):
        # входим в аккаунт
        driver.get("https://stellarburgers.education-services.ru/login")
        driver.find_element(By.XPATH, locators.SIGN_IN_MAIL_FIELD).send_keys('kostya_kozhanov_49@domen.org')
        driver.find_element(By.XPATH, locators.SIGN_IN_PSWD_FIELD).send_keys('e7Yhgt')
        driver.find_element(By.XPATH, locators.SIGN_IN_BUTTON).click()
        # предварительно переходим к другому разделу конструктора (т.к. раздел Булки выбран по умолчанию) и дожидаемся когда он будет активным
        section = WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, locators.FILLINGS_SECTION)))
        section.click()
        active_section = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.ACTIVE_SECTION.format(section_name='Начинки'))))
        # переходим обратно к разделу Булки
        driver.find_element(By.XPATH, locators.BUNS_SECTION).click()
        # ожидаем изменения активного раздела конструктора и сохраняем его в переменную
        active_section = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.ACTIVE_SECTION.format(section_name='Булки'))))
        # проверяем наличие слова Булки в текстовом содержимом элемента active_section и вложенных в него элементов
        assert 'Булки' in active_section.text
