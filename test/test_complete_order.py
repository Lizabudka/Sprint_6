import pytest
import allure
from pages.objects_locators import *
from pages.main_page import MainPageScooterService
from pages.order_form_page import OrderFormPage
import pages.variables


class TestOrder:

    @allure.title('Проверка оформления заказа через две кнопки')
    @pytest.mark.parametrize('option, name, surname, address, phone_number, comment',
                             [[0, 'Катя', 'Овечкина', 'ул. Пушкина, д. 18', '+79999999999', 'Привезите печеньки'],
                              [1, 'Оля', 'Бойко', 'ул. Петрова, д. 3', '+79908476657', 'Чаевые выдаю фантиками']])
    def test_make_order_with_order_button_order_complited(self, driver, name, surname, address,
                                                          option, phone_number, comment):
        main_page = MainPageScooterService(driver)
        order_page = OrderFormPage(driver)

        # Переход на главную страницу и клик по кнопке заказа
        main_page.go_to_main_page()
        order_page.click_cookie_button()
        main_page.click_order_button(option)

        with allure.step(f'Проверяем, что перешли на страницу для заказа'):
            assert pages.variables.order_text in driver.current_url

        # Заполнение первой формы заказа
        order_page.fill_in_order_form(name, surname, address, option, phone_number)
        order_page.click_next_button()

        # Заполнение второй формы заказа
        order_page.wait_next_page_form_to_load()
        order_page.fill_in_second_order_form(option, comment)
        order_page.click_form_order_button()

        # Подтверждение заказа в сплывающем окне
        order_page.wait_element_to_be_visible(OrderPageLocators.confirm_window[0], OrderPageLocators.confirm_window[1])
        order_page.click_yes_on_order_confirmation_window()

        confirmation_text = order_page.wait_order_complete_window_to_load()

        with allure.step(f'Проверяем, что заказ оформлен, появилось окно с текстом: "{confirmation_text}"'):
            assert pages.variables.order_is_complited_text in confirmation_text
