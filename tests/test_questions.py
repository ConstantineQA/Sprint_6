import allure
import pytest
from pages.main_page import MainPage
import data

class TestQuestions:

    @allure.title('Соответствие текста ответа вопросу FAQ')
    @allure.description('Проверка, что текст раскрывшегося элемента аккордеона соответствует своему вопросу')
    @pytest.mark.parametrize("question_locator, answer_locator, expected_text", [
        (MainPage.ACCORDION_ITEM_ONE, MainPage.ANSWER_FAQ_ONE, data.FAQ_ANSWER_1),
        (MainPage.ACCORDION_ITEM_TWO, MainPage.ANSWER_FAQ_TWO, data.FAQ_ANSWER_2),
        (MainPage.ACCORDION_ITEM_THREE, MainPage.ANSWER_FAQ_THREE, data.FAQ_ANSWER_3),
        (MainPage.ACCORDION_ITEM_FOUR, MainPage.ANSWER_FAQ_FOUR, data.FAQ_ANSWER_4),
        (MainPage.ACCORDION_ITEM_FIVE, MainPage.ANSWER_FAQ_FIVE, data.FAQ_ANSWER_5),
        (MainPage.ACCORDION_ITEM_SIX, MainPage.ANSWER_FAQ_SIX, data.FAQ_ANSWER_6),
        (MainPage.ACCORDION_ITEM_SEVEN, MainPage.ANSWER_FAQ_SEVEN, data.FAQ_ANSWER_7),
        (MainPage.ACCORDION_ITEM_EIGHT, MainPage.ANSWER_FAQ_EIGHT, data.FAQ_ANSWER_8),
    ])
    def test_question(self, driver, question_locator, answer_locator, expected_text):
        page = MainPage(driver) 
        page.open_main_page()
        page.load_main_page()
        page.scroll_in_accordion()
        page.click_element(question_locator)
        text = page.get_text(answer_locator)
        assert text == expected_text
