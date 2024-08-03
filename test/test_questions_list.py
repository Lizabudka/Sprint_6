from pages.main_page import MainPageScooterService
import pytest
import allure
import pages.variables


class TestQuestionsSection:

    @allure.title('Проверка секции с вопросами')
    @pytest.mark.parametrize('question_line', [0, 1, 2, 3, 4, 5, 6, 7])
    def test_click_on_question_answer_is_opened(self, question_line, driver):
        main_page = MainPageScooterService(driver)

        # Переход на главную страницу
        main_page.go_to_main_page()
        main_page.wait_questions_faq_section_be_clickable(question_line)

        # Клик на вопрос и проверка ответа
        question_text = main_page.get_question_faq_section(question_line)
        main_page.click_question_faq_section(question_line)
        main_page.wait_answer_faq_section_be_visible(question_line)
        answer_text = main_page.get_answer_faq_section(question_line)

        answer_should_be = pages.variables.questions_and_answers[question_text]

        with allure.step(f'Проверяем, что на вопрос "{question_text}" есть ответ "{answer_should_be}"'):
            assert answer_should_be == answer_text
