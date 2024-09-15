from src.pages.base_page import BasePage
from src.locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def cookie_button_click(self):
        self.driver.find_element(*MainPageLocators.COOKIE_BUTTON).click()

    def check_question_and_answer(self, question_number, answer_number):
        self.driver.find_element(*question_number).click()
        return self.driver.find_element(*answer_number).is_displayed()













