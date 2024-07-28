import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class MainPageScooterService:
    main_page_url = 'https://qa-scooter.praktikum-services.ru/'
    logo_yandex = [By.XPATH, './/*[@alt="Yandex"]']
    order_button = [[By.XPATH, './/*[@class="Button_Button__ra12g" and text()="Заказать"]'],
                    [By.XPATH, './/*[@class="Home_FinishButton__1_cWm"]/button[text()="Заказать"]']]
    questions_locators = [[By.ID, 'accordion__heading-0'],
                        [By.ID, 'accordion__heading-1'],
                        [By.ID, 'accordion__heading-2'],
                        [By.ID, 'accordion__heading-3'],
                        [By.ID, 'accordion__heading-4'],
                        [By.ID, 'accordion__heading-5'],
                        [By.ID, 'accordion__heading-6'],
                        [By.ID, 'accordion__heading-7']]
    answers_locators = [[By.ID, 'accordion__panel-0'],
                        [By.ID, 'accordion__panel-1'],
                        [By.ID, 'accordion__panel-2'],
                        [By.ID, 'accordion__panel-3'],
                        [By.ID, 'accordion__panel-4'],
                        [By.ID, 'accordion__panel-5'],
                        [By.ID, 'accordion__panel-6'],
                        [By.ID, 'accordion__panel-7']]

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Переход на главную страницу сайта')
    def go_to_main_page(self):
        self.driver.get(self.main_page_url)

    @allure.step('Клик на лого "Яндекс"')
    def click_on_logo_yandex(self):
        self.driver.find_element(*self.logo_yandex).click()

    @allure.step('Ожидание, пока кнопка заказа не будет кликабельна')
    def wait_order_button_be_clickable(self, option):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(
            (self.order_button[option][0], self.order_button[option][1])))

    @allure.step('Клик по кнопке оформления заказа')
    def click_order_button(self, option):
        element = self.driver.find_element(*self.order_button[option])
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        time.sleep(1)
        element.click()

    @allure.step('Ожидание, пока вопросы не будут кликабельны')
    def wait_questions_faq_section_be_clickable(self, question_line):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(
            (self.questions_locators[question_line][0], self.questions_locators[question_line][1])))

    @allure.step('Получить текст вопроса')
    def get_question_faq_section(self, question_line):
        question_text = self.driver.find_element(*self.questions_locators[question_line]).text
        return question_text

    @allure.step('Клик на вопрос из секция со списком вопросов')
    def click_question_faq_section(self, question_line):
        element = self.driver.find_element(*self.questions_locators[question_line])
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        time.sleep(1)
        element.click()

    @allure.step('Ожидание отображения ответов на вопросы из раскрывшегося списка')
    def wait_answer_faq_section_be_visible(self, question_line):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(
            (self.answers_locators[question_line][0], self.answers_locators[question_line][1])))

    @allure.step('Получить текст ответа на вопрос из раскрывшегося списка')
    def get_answer_faq_section(self, question_line):
        answer_text = self.driver.find_element(*self.answers_locators[question_line]).text
        return answer_text
