import pytest
from pages.base_for_pages import BaseForPages 
from locators.questions_locators import QuestionsLocators as ql
#python -m pytest tests/test_questions.py

class TestQuestions:
    #Проверка вопросов и ответов
    @pytest.mark.parametrize("question_locator, answer_locator, expected_answer", [
       (ql.question_1,  ql.answer_1, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
       (ql.question_2,  ql.answer_2, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
       (ql.question_3,  ql.answer_3, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
       (ql.question_4,  ql.answer_4, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
       (ql.question_5,  ql.answer_5, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
       (ql.question_6,  ql.answer_6, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
       (ql.question_7,  ql.answer_7, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
       (ql.question_8,  ql.answer_8, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
    ])
    def test_answer_for_question(self, driver, question_locator, answer_locator, expected_answer):
        page = BaseForPages(driver)
        
        #прокрутка страницы вниз
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        #кликнуть на вопрос
        page.click(question_locator)

        #получить текущий ответ
        assert page.get_text(answer_locator) == expected_answer
