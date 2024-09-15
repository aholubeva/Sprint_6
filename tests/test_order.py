from src.pages.order_page import OrderPage
from src.locators.order_page_locators import OrderPageLocators
from src.config import Config
import pytest
from src.helpers import generate_date


class TestOrder:

    day_1, day_2 = generate_date()
    @pytest.mark.parametrize(
        "metro_station, day, rental_period",
        [
            (OrderPageLocators.METRO_STATION_1, day_1, OrderPageLocators.RENTAL_PERIOD_DAY),
            (OrderPageLocators.METRO_STATION_2, day_2, OrderPageLocators.RENTAL_PERIOD_TWO_DAYS)
        ]
    )

    def test_create_order_first_entry_point(self, driver, metro_station, day, rental_period):

        order_page = OrderPage(driver)
        order_page.navigate(Config.URL)
        order_page.click_element(OrderPageLocators.COOKIE_BUTTON)
        order_page.click_element(OrderPageLocators.FIRST_ORDER_BUTTON)
        order_page.fill_in_order_form(metro_station, day, rental_period)
        order_page.click_element(OrderPageLocators.FIRST_ORDER_BUTTON)
        order_page.click_element(OrderPageLocators.ORDER_BUTTON)
        order_page.click_element(OrderPageLocators.CONFIRMATION_BUTTON)
        assert order_page.element_is_present(OrderPageLocators.CONFIRMATION_POPUP)

    def test_create_order_second_entry_point(self, driver):

        order_page = OrderPage(driver)
        order_page.navigate(Config.URL)
        order_page.click_element(OrderPageLocators.COOKIE_BUTTON)
        order_page.scroll_to_order_button()
        order_page.click_element(OrderPageLocators.SECOND_ORDER_BUTTON)
        order_page.fill_in_order_form(OrderPageLocators.METRO_STATION_1, self.day_1, OrderPageLocators.RENTAL_PERIOD_DAY)
        order_page.click_element(OrderPageLocators.ORDER_BUTTON)
        order_page.click_element(OrderPageLocators.CONFIRMATION_BUTTON)
        assert order_page.element_is_present(OrderPageLocators.CONFIRMATION_POPUP)

    def test_click_scooter_logo(self, driver):

        order_page = OrderPage(driver)
        order_page.navigate(Config.URL)
        order_page.click_element(OrderPageLocators.COOKIE_BUTTON)
        order_page.click_element(OrderPageLocators.FIRST_ORDER_BUTTON)
        order_page.fill_in_order_form(OrderPageLocators.METRO_STATION_1, self.day_1, OrderPageLocators.RENTAL_PERIOD_DAY)
        order_page.click_element(OrderPageLocators.ORDER_BUTTON)
        order_page.click_element(OrderPageLocators.CONFIRMATION_BUTTON)
        order_page.click_element(OrderPageLocators.CHECK_STATUS_BUTTON)
        order_page.click_element(OrderPageLocators.SCOOTER_LOGO)
        assert order_page.current_url() == f'{Config.URL}', "Login Url is wrong"

    def test_click_yandex_logo(self, driver):

        order_page = OrderPage(driver)
        order_page.navigate(Config.URL)
        order_page.click_element(OrderPageLocators.COOKIE_BUTTON)
        order_page.click_element(OrderPageLocators.FIRST_ORDER_BUTTON)
        order_page.fill_in_order_form(OrderPageLocators.METRO_STATION_1, self.day_1, OrderPageLocators.RENTAL_PERIOD_DAY)
        order_page.click_element(OrderPageLocators.ORDER_BUTTON)
        order_page.click_element(OrderPageLocators.CONFIRMATION_BUTTON)
        order_page.click_element(OrderPageLocators.CHECK_STATUS_BUTTON)
        order_page.click_element(OrderPageLocators.YANDEX_LOGO)
        order_page.open_new_window_and_wait(Config.DZEN_URL)
        assert order_page.current_url() == f'{Config.DZEN_URL}', "Login Url is wrong"





