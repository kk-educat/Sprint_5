from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators


def test_access_to_sauces_section(driver):
    # входим в аккаунт
    driver.get("https://stellarburgers.education-services.ru/login")
    driver.find_element(By.XPATH, locators.SIGN_IN_MAIL_FIELD).send_keys('kostya_kozhanov_49@domen.org')
    driver.find_element(By.XPATH, locators.SIGN_IN_PSWD_FIELD).send_keys('e7Yhgt')
    driver.find_element(By.XPATH, locators.SIGN_IN_BUTTON).click()
    # ПРОВЕРЯЕМ ПЕРЕХОД К РАЗДЕЛУ "СОУСЫ"
    # дожидаемся кликабельности раздела Соусы и кликаем на него
    section = WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, locators.SAUCES_SECTION)))
    section.click()
    # находим активный раздел конструктора на странице (раздел, к которому перешли)
    active_section = driver.find_element(By.XPATH, locators.ACTIVE_SECTION)
    # получаем элемент span, находящийся внутри активного раздела и содержащий его название
    active_section_span = active_section.find_element(By.TAG_NAME, 'span')
    # проверяем название активного раздела
    assert active_section_span.text == 'Соусы'

def test_access_to_fillings_section(driver):
    # входим в аккаунт
    driver.get("https://stellarburgers.education-services.ru/login")
    driver.find_element(By.XPATH, locators.SIGN_IN_MAIL_FIELD).send_keys('kostya_kozhanov_49@domen.org')
    driver.find_element(By.XPATH, locators.SIGN_IN_PSWD_FIELD).send_keys('e7Yhgt')
    driver.find_element(By.XPATH, locators.SIGN_IN_BUTTON).click()
    # проверяем переход к разделу Начинки (аналогично тестовому шагу для раздела Соусы)
    section = WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, locators.FILLINGS_SECTION)))
    section.click()
    active_section = driver.find_element(By.XPATH, locators.ACTIVE_SECTION)
    active_section_span = active_section.find_element(By.TAG_NAME, 'span')
    assert active_section_span.text == 'Начинки'

def test_access_to_buns_section(driver):
    # входим в аккаунт
    driver.get("https://stellarburgers.education-services.ru/login")
    driver.find_element(By.XPATH, locators.SIGN_IN_MAIL_FIELD).send_keys('kostya_kozhanov_49@domen.org')
    driver.find_element(By.XPATH, locators.SIGN_IN_PSWD_FIELD).send_keys('e7Yhgt')
    driver.find_element(By.XPATH, locators.SIGN_IN_BUTTON).click()
    # предварительно переходим к другому разделу конструктора (т.к. раздел Булки выбран по умолчанию)
    section = WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, locators.FILLINGS_SECTION)))
    section.click()
    # переходим обратно к разделу Булки
    driver.find_element(By.XPATH, locators.BUNS_SECTION).click()
    # находим текущий активный раздел конструктора
    active_section = driver.find_element(By.XPATH, locators.ACTIVE_SECTION)
    # получаем элемент span, находящийся внутри активного раздела и содержащий его название
    active_section_span = active_section.find_element(By.TAG_NAME, 'span')
    # проверяем название активного раздела
    assert active_section_span.text == 'Булки'
