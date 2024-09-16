from src.pages.base_page import BasePage
from src.locators.order_page_locators import OrderPageLocators
from src.helpers import get_user_data
import allure
from src.config import Config
from src.helpers import generate_date


class OrderPage(BasePage):

    @allure.step('Открыть браузер Firefox')
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открыть страницу оформления заказа')
    def navigate_to_order_page(self):
        self.navigate(Config.URL)

    @allure.step('Кликнуть на верхнюю кнопку Заказать')
    def click_first_order_button(self):
        self.click_element(OrderPageLocators.FIRST_ORDER_BUTTON)

    @allure.step('Кликнуть на кнопку Заказать после заполнения формы')
    def click_order_button(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Кликнуть Да в появившейся форме Подтвердить заказ')
    def click_confirmation_button(self):
        self.click_element(OrderPageLocators.CONFIRMATION_BUTTON)

    @allure.step('Проверить что появилось окно с успешным подверждением заказа')
    def check_confirmation_form(self):
        return self.element_is_present(OrderPageLocators.CONFIRMATION_POPUP)

    @allure.step('Выбрать станцию метро из выпадающего списка')
    def select_metro(self, metro_station):
        self.click_element(OrderPageLocators.METRO_FIELD)
        self.click_element(metro_station)

    @allure.step('Выбрать день доставки из календаря')
    def select_day(self, day):
        self.enter_text(OrderPageLocators.CALENDAR, day)
        self.click_return(OrderPageLocators.CALENDAR)

    @allure.step('Выбрать срок аренды из выпадающего списка')
    def select_rental_period(self, rental_period):
        self.click_element(OrderPageLocators.RENTAL_PERIOD_FIELD)
        self.click_element(rental_period)

    @allure.step('Заполнить форму заказа с двумя наборами данных')
    def fill_in_order_form_with_parametrization(self, metro_station, day, rental_period):
        first_name, last_name, address, phone = get_user_data()
        self.enter_text(OrderPageLocators.FIRST_NAME_FIELD, first_name)
        self.enter_text(OrderPageLocators.LAST_NAME_FIELD, last_name)
        self.enter_text(OrderPageLocators.ADDRESS, address)
        self.select_metro(metro_station)
        self.enter_text(OrderPageLocators.PHONE, phone)
        self.click_element(OrderPageLocators.NEXT_BUTTON)
        self.select_day(day)
        self.select_rental_period(rental_period)
        self.click_element(OrderPageLocators.COLOR_LABEL)

    @allure.step('Проскроллить до нижней кнопки Заказать')
    def scroll_to_order_button(self):
        return self.driver.execute_script("window.scrollTo(0, 1900)")

    @allure.step('Кликнуть на нижнюю кнопку Заказать')
    def click_second_order_button(self):
        self.click_element(OrderPageLocators.SECOND_ORDER_BUTTON)

    @allure.step('Заполнить форму заказа с одним заданным набором данных')
    def fill_in_order_form(self):
        day_1, day_2 = generate_date()
        first_name, last_name, address, phone = get_user_data()
        self.enter_text(OrderPageLocators.FIRST_NAME_FIELD, first_name)
        self.enter_text(OrderPageLocators.LAST_NAME_FIELD, last_name)
        self.enter_text(OrderPageLocators.ADDRESS, address)
        self.select_metro(OrderPageLocators.METRO_STATION_1)
        self.enter_text(OrderPageLocators.PHONE, phone)
        self.click_element(OrderPageLocators.NEXT_BUTTON)
        self.select_day(day_1)
        self.select_rental_period(OrderPageLocators.RENTAL_PERIOD_DAY)
        self.click_element(OrderPageLocators.COLOR_LABEL)

    @allure.step('Кликнуть на кнопку Посмотреть статус заказа')
    def click_order_status_button(self):
        self.click_element(OrderPageLocators.ORDER_STATUS_BUTTON)

    @allure.step('Кликнуть на лого Самоката')
    def click_on_scooter_logo(self):
        self.click_element(OrderPageLocators.SCOOTER_LOGO)

    @allure.step('Проверить что текущая страница - это главная страница Самоката')
    def check_scooter_main_page(self):
        if self.current_url() == Config.URL:
            return True

    @allure.step('Кликнуть на лого Yandex')
    def click_on_yandex_logo(self):
        self.click_element(OrderPageLocators.YANDEX_LOGO)

    @allure.step('Ждем пока главная страница Дзена откроется в отдельной вкладке и переходим туда')
    def open_dzen_window_and_wait(self):
        self.open_new_window_and_wait(Config.DZEN_URL)

    @allure.step('Проверить что текущая страница - это главная страница Дзена')
    def check_dzen_main_page(self):
        if self.current_url() == Config.DZEN_URL:
            return True

