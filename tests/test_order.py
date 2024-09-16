from src.pages.order_page import OrderPage
from src.locators.order_page_locators import OrderPageLocators
import pytest
from src.helpers import generate_date
import allure


class TestOrder:

    day_1, day_2 = generate_date()
    @pytest.mark.parametrize(
        "metro_station, day, rental_period",
        [
            (OrderPageLocators.METRO_STATION_1, day_1, OrderPageLocators.RENTAL_PERIOD_DAY),
            (OrderPageLocators.METRO_STATION_2, day_2, OrderPageLocators.RENTAL_PERIOD_TWO_DAYS)
        ]
    )
    @allure.title('Проверка оформления заказа по клику на верхнюю кнопку Заказать')
    def test_create_order_first_entry_point(self, driver, metro_station, day, rental_period):

        order_page = OrderPage(driver)
        order_page.navigate_to_order_page()
        order_page.cookie_button_click()
        order_page.click_first_order_button()
        order_page.fill_in_order_form_with_parametrization(metro_station, day, rental_period)
        order_page.click_order_button()
        order_page.click_confirmation_button()
        assert order_page.check_confirmation_form()

    @allure.title('Проверка оформления заказа по клику на нижнюю кнопку Заказать')
    def test_create_order_second_entry_point(self, driver):

        order_page = OrderPage(driver)
        order_page.navigate_to_order_page()
        order_page.cookie_button_click()
        order_page.scroll_to_order_button()
        order_page.click_second_order_button()
        order_page.fill_in_order_form()
        order_page.click_order_button()
        order_page.click_confirmation_button()
        assert order_page.check_confirmation_form()

    @allure.title('Проверка открытия главной страницы Самоката по клику на лого Самоката')
    def test_click_scooter_logo(self, driver):

        order_page = OrderPage(driver)
        order_page.navigate_to_order_page()
        order_page.cookie_button_click()
        order_page.click_first_order_button()
        order_page.fill_in_order_form()
        order_page.click_order_button()
        order_page.click_confirmation_button()
        order_page.click_order_status_button()
        order_page.click_on_scooter_logo()
        assert order_page.check_scooter_main_page()

    @allure.title('Проверка открытия главной страницы Дзена на отдельной вкладке по клику на лого Yandex')
    def test_click_yandex_logo(self, driver):
        order_page = OrderPage(driver)
        order_page.navigate_to_order_page()
        order_page.cookie_button_click()
        order_page.click_first_order_button()
        order_page.fill_in_order_form()
        order_page.click_order_button()
        order_page.click_confirmation_button()
        order_page.click_order_status_button()
        order_page.click_on_yandex_logo()
        order_page.open_dzen_window_and_wait()
        assert order_page.check_dzen_main_page()





