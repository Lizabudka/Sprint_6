import time
from selenium import webdriver
from pages.main_page import MainPageScooterService
from pages.order_form_page import OrderFormPage
import allure


class TestLogoClick:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка перехода на главную страницу через клик по лого "Самокат"')
    def test_click_on_samokat_logo_go_to_main_page(self):
        order_page = OrderFormPage(self.driver)

        # Переход на страницу с формой заказа
        order_page.go_to_main_page()
        order_page.wait_form_to_be_loaded()

        # Клик на лого "Самокат"
        order_page.click_on_logo_samokat()
        current_url = self.driver.current_url

        assert current_url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Проверка перехода на сайт Дзен через клик по лого "Яндекс"')
    def test_click_on_yandex_logo_go_to_dzen_page(self):
        main_page = MainPageScooterService(self.driver)

        # Переход на главную страницу сайта
        main_page.go_to_main_page()
        main_page.wait_order_button_be_clickable(1)

        # Клик на лого "Яндекс", проверка url
        main_page.click_on_logo_yandex()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(1)

        current_url = self.driver.current_url

        assert current_url == 'https://dzen.ru/?yredirect=true'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
