import allure
from .variables import *
from .objects_locators import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class OrderFormPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Переход на страницу оформления заказа')
    def go_to_main_page(self):
        self.driver.get(ORDER_PAGE_URL)

    @allure.step('Клик на лого "Самокат"')
    def click_on_logo_samokat(self):
        self.driver.find_element(*CommonLocators.logo_samokat).click()

    @allure.step('Ожидание отображения элемента на странице')
    def wait_element_to_be_visible(self, locator_type, locator_path):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            (locator_type, locator_path)))

    @allure.step('Ожидание пока элемент не станет кликабелен')
    def wait_element_to_be_clickable(self, locator_type, locator_path):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(
            (locator_type, locator_path)))

    @allure.step('Заполнение имени')
    def set_name(self, name):
        self.driver.find_element(*OrderPageLocators.name_field).send_keys(name)

    @allure.step('Заполнение фамилии')
    def set_surname(self, surname):
        self.driver.find_element(*OrderPageLocators.surname_field).send_keys(surname)

    @allure.step('Заролнение адреса')
    def set_address(self, address):
        self.driver.find_element(*OrderPageLocators.address_field).send_keys(address)

    @allure.step('Заполнение станции метро')
    def set_metro(self, option):
        self.driver.find_element(*OrderPageLocators.metro_station_field).click()
        self.wait_element_to_be_visible(OrderPageLocators.metro_example[option][0],
                                        OrderPageLocators.metro_example[option][1])
        self.driver.find_element(*OrderPageLocators.metro_example[option]).click()

    @allure.step('Заполнение телефона')
    def set_phone_number(self, phone_number):
        self.wait_element_to_be_visible(OrderPageLocators.phone_number_field[0],
                                        OrderPageLocators.phone_number_field[1])
        self.driver.find_element(*OrderPageLocators.phone_number_field).send_keys(phone_number)

    @allure.step('Клик по кнопке "Далее"')
    def click_next_button(self):
        element = self.driver.find_element(*OrderPageLocators.next_button)
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        self.wait_element_to_be_clickable(OrderPageLocators.next_button[0], OrderPageLocators.next_button[1])
        element.click()

    @allure.step('Ожидание загрузки следующей формы для заполнения информации о заказе')
    def wait_next_page_form_to_load(self):
        self.wait_element_to_be_visible(OrderPageLocators.order_header[0], OrderPageLocators.order_header[1])
        element_text = self.driver.find_element(*OrderPageLocators.order_header).text
        return element_text

    @allure.step('Нажатие на кнопку с куки, чтобы она не перекрывала другие кнопки')
    def click_cookie_button(self):
        try:
            self.driver.find_element(*CommonLocators.cookie_button).click()
        except Exception:
            pass

    @allure.step('Заполнение первой формы заказа')
    def fill_in_order_form(self, name, surname, address, option, phone_number):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro(option)
        self.set_phone_number(phone_number)

    @allure.step('Заролнение даты аренды')
    def set_order_date_field(self):
        self.driver.find_element(*OrderPageLocators.date_field).click()
        self.wait_element_to_be_clickable(OrderPageLocators.date_next_month_button[0],
                                          OrderPageLocators.date_next_month_button[1])
        self.driver.find_element(*OrderPageLocators.date_next_month_button).click()
        self.wait_element_to_be_clickable(OrderPageLocators.date_day_to_choose[0],
                                          OrderPageLocators.date_day_to_choose[1])
        self.driver.find_element(*OrderPageLocators.date_day_to_choose).click()

    @allure.step('Заполнение срока аренды')
    def set_order_term_field(self):
        self.driver.find_element(*OrderPageLocators.term_field).click()
        self.driver.find_element(*OrderPageLocators.term_example_field).click()

    @allure.step('Выбор цвета')
    def set_colour_field(self, option):
        self.driver.find_element(OrderPageLocators.colour_field[option][0],
                                 OrderPageLocators.colour_field[option][1]).click()

    @allure.step('Заполнение комментария')
    def set_comment_field(self, comment):
        self.driver.find_element(*OrderPageLocators.comment_field).send_keys(comment)

    @allure.step('Клик кнопки оформления заказа')
    def click_form_order_button(self):
        self.driver.find_element(*OrderPageLocators.form_order_button).click()

    @allure.step('Заполнение второй формы заказа')
    def fill_in_second_order_form(self, option, comment):
        self.set_order_date_field()
        self.set_order_term_field()
        self.set_colour_field(option)
        self.set_comment_field(comment)

    @allure.step('Клик на кнопку подтверждения заказа')
    def click_yes_on_order_confirmation_window(self):
        self.driver.find_element(*OrderPageLocators.button_yes).click()

    @allure.step('Ожидание загрузки окна с информацией о заказе')
    def wait_order_complete_window_to_load(self):
        self.wait_element_to_be_visible(OrderPageLocators.order_is_confirmed_window[0],
                                        OrderPageLocators.order_is_confirmed_window[1])
        confirmation_text = self.driver.find_element(*OrderPageLocators.order_is_confirmed_window).text
        return confirmation_text
