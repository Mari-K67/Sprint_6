import pytest
import allure
from pages.base_page import BasePage
from locators.questions_locators import QuestionsLocators
import data
#python -m pytest tests/test_questions.py

class TestQuestions:
    @allure.title('Проверка ответов на вопросы')
    @pytest.mark.parametrize("question_locator, answer_locator, expected_answer", [
       (QuestionsLocators.question_1,  QuestionsLocators.answer_1, data.expected_answer_1),
       (QuestionsLocators.question_2,  QuestionsLocators.answer_2, data.expected_answer_2),
       (QuestionsLocators.question_3,  QuestionsLocators.answer_3, data.expected_answer_3),
       (QuestionsLocators.question_4,  QuestionsLocators.answer_4, data.expected_answer_4),
       (QuestionsLocators.question_5,  QuestionsLocators.answer_5, data.expected_answer_5),
       (QuestionsLocators.question_6,  QuestionsLocators.answer_6, data.expected_answer_6),
       (QuestionsLocators.question_7,  QuestionsLocators.answer_7, data.expected_answer_7),
       (QuestionsLocators.question_8,  QuestionsLocators.answer_8, data.expected_answer_8)
    ])
    def test_answer_for_question(self, driver, question_locator, answer_locator, expected_answer):
        page = BasePage(driver)
        
        with allure.step('1. прокрутка страницы вниз'):
            page.scroll_to_botton(driver)

        with allure.step('2. кликнуть на вопрос'):
            page.click(question_locator)

        with allure.step('3. получить текущий ответ и сравнить с ожидаемым'):
            assert page.get_text(answer_locator) == expected_answer
