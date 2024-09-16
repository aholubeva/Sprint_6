from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import allure
from src.locators.base_page_locators import BasePageLocators

class BasePage:

    @allure.step('Открываем браузер Firefox')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Переходим на заданную страницу')
    def navigate(self, url):
        self.driver.get(url)

    @allure.step('Проверяем текущую страницу')
    def current_url(self):
        return self.driver.current_url

    @allure.step('Ищем заданный элемент')
    def find_element(self, locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Кликаем на элемент')
    def click_element(self, locator, timeout=10):
        self.find_element(locator, timeout).click()

    @allure.step('Вводим текст')
    def enter_text(self, locator, text, timeout=10):
        self.find_element(locator, timeout).send_keys(text)

    @allure.step('Ждем пока заданный элемент загрузится')
    def wait_for_element_visible(self, locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Скроллим страницу')
    def scroll_page(self):
        return self.driver.execute_script("window.scrollTo(0, 2400)")

    @allure.step('Ждем пока заданный урл откроется в отдельной вкладке')
    def open_new_window_and_wait(self, url):
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(EC.url_to_be(url))

    @allure.step('Кликаем по кнопке Ввод')
    def click_return(self, locator, timeout=10):
        self.find_element(locator, timeout).send_keys(Keys.RETURN)

    @allure.step('Проверяем наличие элемента')
    def element_is_present(self, locator, timeout=10):
        return self.find_element(locator, timeout).is_displayed()

    @allure.step('Принять куки')
    def cookie_button_click(self):
        self.driver.find_element(*BasePageLocators.COOKIE_BUTTON).click()


