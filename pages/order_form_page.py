import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class OrderFormPage:
    order_page_url = 'https://qa-scooter.praktikum-services.ru/order'
    logo_samokat = [By.XPATH, './/*[@alt="Scooter"]']

    name_field = [By.XPATH, './/input[@placeholder="* Имя"]']
    surname_field = [By.XPATH, './/input[@placeholder="* Фамилия"]']
    address_field = [By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]']
    metro_station_field = [By.XPATH, './/input[@placeholder="* Станция метро"]']
    phone_number_field = [By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]']

    metro_example = ['.//*[text()="Черкизовская"]', './/*[text()="Бульвар Рокоссовского"]']
    date_field = [By.XPATH, './/input[@placeholder="* Когда привезти самокат"]']
    date_next_month_button = [By.XPATH, './/button[@aria-label="Next Month"]']
    date_day_to_choose = [By.XPATH, './/div[@class="react-datepicker__week"][1]/div[7]']
    term_field = [By.XPATH, './/*[text()="* Срок аренды"]']
    term_example_field = [By.XPATH, './/div[@class="Dropdown-menu"]/div[1]']
    colour_field = ['.//*[text()="серая безысходность"]', './/*[text()="чёрный жемчуг"]']
    comment_field = [By.XPATH, './/input[@placeholder="Комментарий для курьера"]']

    next_button = [By.XPATH, './/button[text()="Далее"]']
    order_header = [By.XPATH, './/*[text()="Про аренду"]']
    form_order_button = [By.XPATH, './/div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]']
    confirm_window = [By.XPATH, './/*[text()="Хотите оформить заказ?"]']
    button_yes = [By.XPATH, './/button[text()="Да"]']
    order_is_confirmed_window = [By.XPATH, './/div[text()="Заказ оформлен"]']

    cookie_button = [By.XPATH, './/*[text()="да все привыкли"]']

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Переход на страницу оформления заказа')
    def go_to_main_page(self):
        self.driver.get(self.order_page_url)

    @allure.step('Клик на лого "Самокат"')
    def click_on_logo_samokat(self):
        self.driver.find_element(*self.logo_samokat).click()

    @allure.step('Ожидание загрузки формы для заполнения информации о заказе')
    def wait_form_to_be_loaded(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(
            (self.name_field[0], self.name_field[1])))

    @allure.step('Заполнение имени')
    def set_name(self, name):
        self.driver.find_element(*self.name_field).send_keys(name)

    @allure.step('Заполнение фамилии')
    def set_surname(self, surname):
        self.driver.find_element(*self.surname_field).send_keys(surname)

    @allure.step('Заролнение адреса')
    def set_address(self, address):
        self.driver.find_element(*self.address_field).send_keys(address)

    @allure.step('Заполнение станции метро')
    def set_metro(self, option):
        self.driver.find_element(*self.metro_station_field).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, self.metro_example[option])))
        self.driver.find_element(By.XPATH, self.metro_example[option]).click()

    @allure.step('Заполнение телефона')
    def set_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_number_field).send_keys(phone_number)

    @allure.step('Клик по кнопке "Далее"')
    def click_next_button(self):
        element = self.driver.find_element(*self.next_button)
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        time.sleep(1)
        element.click()

    @allure.step('Ожидание загрузки следующей формы для заполнения информации о заказе')
    def wait_next_page_form_to_load(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            (self.order_header[0], self.order_header[1])))
        element_text = self.driver.find_element(*self.order_header).text
        return element_text

    @allure.step('Нажатие на кнопку с куки, чтобы она не перекрывала другие кнопки')
    def click_cookie_button(self):
        try:
            self.driver.find_element(*self.cookie_button).click()
        except Exception:
            pass

    @allure.step('Заполнение первой формы заказа')
    def fill_in_order_form(self, name, surname, address, option, phone_number):
        self.click_cookie_button()
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro(option)
        self.set_phone_number(phone_number)

    @allure.step('Заролнение даты аренды')
    def set_order_date_field(self):
        self.driver.find_element(*self.date_field).click()
        time.sleep(1)
        self.driver.find_element(*self.date_next_month_button).click()
        time.sleep(1)
        self.driver.find_element(*self.date_day_to_choose).click()

    @allure.step('Заполнение срока аренды')
    def set_order_term_field(self):
        self.driver.find_element(*self.term_field).click()
        self.driver.find_element(*self.term_example_field).click()

    @allure.step('Выбор цвета')
    def set_colour_field(self, option):
        self.driver.find_element(By.XPATH, self.colour_field[option]).click()

    @allure.step('Заполнение комментария')
    def set_comment_field(self, comment):
        self.driver.find_element(*self.comment_field).send_keys(comment)

    @allure.step('Клик кнопки оформления заказа')
    def click_form_order_button(self):
        self.driver.find_element(*self.form_order_button).click()

    @allure.step('Заполнение второй формы заказа')
    def fill_in_second_order_form(self, option, comment):
        self.set_order_date_field()
        self.set_order_term_field()
        self.set_colour_field(option)
        self.set_comment_field(comment)

    @allure.step('Ожидание загрузки окна с подтверждением')
    def wait_confirm_window_to_be_loaded(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            (self.confirm_window[0], self.confirm_window[1])))

    @allure.step('Клик на кнопку подтверждения заказа')
    def click_yes_on_order_confirmation_window(self):
        self.driver.find_element(*self.button_yes).click()

    @allure.step('Ожидание загрузки окна с информацией о заказе')
    def wait_order_complete_window_to_load(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(
            (self.order_is_confirmed_window[0], self.order_is_confirmed_window[1])))
        confirmation_text = self.driver.find_element(*self.order_is_confirmed_window).text
        return confirmation_text
