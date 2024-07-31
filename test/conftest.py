import pytest
from selenium import webdriver
import allure

@allure.step('Открываем\закрываем браузер')
@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
