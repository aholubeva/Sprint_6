from src.pages.base_page import BasePage
from src.locators.order_page_locators import OrderPageLocators
from src.helpers import get_user_data


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def select_metro(self, metro_station):
        self.driver.find_element(*OrderPageLocators.METRO_FIELD).click()
        self.driver.find_element(*metro_station).click()

    def select_day(self, day):
        self.driver.find_element(*OrderPageLocators.CALENDAR).send_keys(day)
        self.click_return(OrderPageLocators.CALENDAR)

    def select_rental_period(self, rental_period):
        self.click_element(OrderPageLocators.RENTAL_PERIOD_FIELD)
        self.click_element(rental_period)

    def fill_in_order_form(self, metro_station, day, rental_period):
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

    def scroll_to_order_button(self):
        return self.driver.execute_script("window.scrollTo(0, 1800)")




