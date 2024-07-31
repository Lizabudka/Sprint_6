import allure
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from .objects_locators import *
from .variables import *


class MainPageScooterService:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Переход на главную страницу сайта')
    def go_to_main_page(self):
        self.driver.get(MAIN_PAGE_URL)

    @allure.step('Клик на лого "Яндекс"')
    def click_on_logo_yandex(self):
        self.driver.find_element(*CommonLocators.logo_yandex).click()

    @allure.step('Клик по кнопке')
    def check_if_element_is_clickable(self, element, locator_type, locator_path):
        element_is_clickable = False
        while not element_is_clickable:
            try:
                element.click()
                element_is_clickable = True
            except ElementClickInterceptedException:
                WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(
                    (locator_type, locator_path)))

    @allure.step('Переходим к кнопке оформления заказа')
    def click_order_button(self, option):
        element = self.driver.find_element(*MainPageLocators.order_button[option])
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        self.check_if_element_is_clickable(element, MainPageLocators.order_button[option][0],
                                           MainPageLocators.order_button[option][1])

    @allure.step('Ожидание, пока вопросы не будут кликабельны')
    def wait_questions_faq_section_be_clickable(self, question_line):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(
            (MainPageLocators.questions_locators[question_line][0],
             MainPageLocators.questions_locators[question_line][1])))

    @allure.step('Получить текст вопроса')
    def get_question_faq_section(self, question_line):
        question_text = self.driver.find_element(*MainPageLocators.questions_locators[question_line]).text
        return question_text

    @allure.step(f'Клик на вопрос из секции со списком вопросов')
    def click_question_faq_section(self, question_line):
        element = self.driver.find_element(*MainPageLocators.questions_locators[question_line])
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        self.check_if_element_is_clickable(element, MainPageLocators.questions_locators[question_line][0],
                                           MainPageLocators.questions_locators[question_line][1])

    @allure.step('Ожидание отображения ответов на вопросы из раскрывшегося списка')
    def wait_answer_faq_section_be_visible(self, question_line):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(
            (MainPageLocators.answers_locators[question_line][0],
             MainPageLocators.answers_locators[question_line][1])))

    @allure.step('Получить текст ответа на вопрос из раскрывшегося списка')
    def get_answer_faq_section(self, question_line):
        answer_text = self.driver.find_element(*MainPageLocators.answers_locators[question_line]).text
        return answer_text
