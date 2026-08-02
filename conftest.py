import pytest

from selenium import webdriver


# Фикстура, создающая экземпляр driver браузера и закрывающая его в конце каждого теста
@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    yield browser  # передаем браузер в тест
    browser.quit()  # этот код сработает всегда после завершения теста
