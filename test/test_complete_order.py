import pytest
import allure
from selenium import webdriver
from pages.main_page import MainPageScooterService
from pages.order_form_page import OrderFormPage


class TestOrder:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка оформления заказа')
    @pytest.mark.parametrize('option, name, surname, address, phone_number, comment',
                             [[0, 'Катя', 'Овечкина', 'ул. Пушкина, д. 18', '+79999999999', 'Привезите печеньки'],
                             [1, 'Оля', 'Бойко', 'ул. Петрова, д. 3', '+79908476657', 'Чаевые выдаю фантиками']])
    def test_make_order_with_order_button_order_complited(self, name, surname, address, option, phone_number, comment):
        main_page = MainPageScooterService(self.driver)

        # Переход на главную страницу и клик по кнопке заказа
        main_page.go_to_main_page()
        main_page.wait_order_button_be_clickable(option)
        main_page.click_order_button(option)

        assert 'order' in self.driver.current_url

        # Заполнение первой формы заказа
        order_page = OrderFormPage(self.driver)
        order_page.fill_in_order_form(name, surname, address, option, phone_number)
        order_page.click_next_button()

        # Заполнение второй формы заказа
        order_page.wait_next_page_form_to_load()
        order_page.fill_in_second_order_form(option, comment)
        order_page.click_form_order_button()

        # Подтверждение заказа в сплывающем окне
        order_page.wait_confirm_window_to_be_loaded()
        order_page.click_yes_on_order_confirmation_window()

        confirmation_text = order_page.wait_order_complete_window_to_load()

        assert 'Заказ оформлен' in confirmation_text

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
