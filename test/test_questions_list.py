from selenium import webdriver
from pages.main_page import MainPageScooterService
import pytest
import allure


class TestQuestionsSection:
    driver = None
    questions_and_answers = {
        "Сколько это стоит? И как оплатить?": 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
        "Хочу сразу несколько самокатов! Так можно?": 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.',
        "Как рассчитывается время аренды?": 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
        "Можно ли заказать самокат прямо на сегодня?": 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
        "Можно ли продлить заказ или вернуть самокат раньше?": 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',
        "Вы привозите зарядку вместе с самокатом?": 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.',
        "Можно ли отменить заказ?": 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.',
        "Я живу за МКАДом, привезёте?": 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
        }

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка секции с вопросами')
    @pytest.mark.parametrize('question_line', [0, 1, 2, 3, 4, 5, 6, 7])
    def test_click_on_question_answer_is_opened(self, question_line):
        main_page = MainPageScooterService(self.driver)

        # Переход на главную страницу
        main_page.go_to_main_page()
        main_page.wait_questions_faq_section_be_clickable(question_line)

        # Клик на вопрос и проверка ответа
        question_text = main_page.get_question_faq_section(question_line)
        main_page.click_question_faq_section(question_line)
        main_page.wait_answer_faq_section_be_visible(question_line)
        answer_text = main_page.get_answer_faq_section(question_line)

        answer_should_be = self.questions_and_answers[question_text]
        assert answer_should_be == answer_text

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
