from src.pages.main_page import MainPage
from src.pages.main_page import MainPageLocators
from src.config import Config
import pytest


class TestImportantQuestions:

    @pytest.mark.parametrize(
        "question_number, answer_number",
        [
            (MainPageLocators.FIRST_QUESTION, MainPageLocators.FIRST_ANSWER),
            (MainPageLocators.SECOND_QUESTION, MainPageLocators.SECOND_ANSWER),
            (MainPageLocators.THIRD_QUESTION, MainPageLocators.THIRD_ANSWER),
            (MainPageLocators.FOURTH_QUESTION, MainPageLocators.FOURTH_ANSWER),
            (MainPageLocators.FIFTH_QUESTION, MainPageLocators.FIFTH_ANSWER),
            (MainPageLocators.SIXTH_QUESTION, MainPageLocators.SIXTH_ANSWER),
            (MainPageLocators.SEVENTH_QUESTION, MainPageLocators.SEVENTH_ANSWER),
            (MainPageLocators.EIGHTH_QUESTION, MainPageLocators.EIGHTH_ANSWER)
        ]
    )

    def test_expand_question(self, driver, question_number, answer_number):
        main_page = MainPage(driver)
        main_page.navigate(Config.URL)
        main_page.scroll_page()
        main_page.cookie_button_click()
        assert main_page.check_question_and_answer(question_number, answer_number)







