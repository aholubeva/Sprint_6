from src.pages.base_page import BasePage
from src.locators.main_page_locators import MainPageLocators
import allure
from src.config import Config

class MainPage(BasePage):

    @allure.step('Открываем браузер Firefox')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открыть главную страницу Самоката')
    def navigate_to_main_page(self):
        self.navigate(Config.URL)

    @allure.step('Проскроллить до Важных вопросов')
    def scroll_page_to_questions(self):
        return self.driver.execute_script("window.scrollTo(0, 2400)")

    @allure.step('Принять куки')
    def cookie_button_click_on_main_page(self):
        self.cookie_button_click()

    @allure.step('Раскрыть вопрос и проверить ответ')
    def check_question_and_answer(self, question_number, answer_number):
        self.click_element(question_number)
        return self.element_is_present(answer_number)













