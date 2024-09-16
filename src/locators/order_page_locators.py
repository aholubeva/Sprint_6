from selenium.webdriver.common.by import By

class OrderPageLocators:
    FIRST_ORDER_BUTTON = (By.CLASS_NAME, 'Button_Button__ra12g')
    SECOND_ORDER_BUTTON = (By.XPATH, '//button[contains(@class,"Button_Middle")]')
    FIRST_NAME_FIELD = (By.XPATH, "//input[contains(@placeholder, 'Имя')]")
    LAST_NAME_FIELD = (By.XPATH, "//input[contains(@placeholder, 'Фамилия')]")
    ADDRESS = (By.XPATH, "//input[contains(@placeholder, 'Адрес')]")
    METRO_FIELD = (By.CLASS_NAME, 'select-search__input')
    METRO_STATION_1 = (By.XPATH, '//*[@class="Order_Text__2broi" and (text()="Комсомольская")]')
    METRO_STATION_2 = (By.XPATH, '//*[@class="Order_Text__2broi" and (text()="Лубянка")]')
    PHONE = (By.XPATH, "//input[contains(@placeholder, 'Телефон')]")
    NEXT_BUTTON = SUBMIT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    CALENDAR = (By.XPATH, "//input[contains(@placeholder, 'Когда привезти самокат')]")
    RENTAL_PERIOD_FIELD = (By.XPATH, '//*[@class="Dropdown-arrow"]')
    RENTAL_PERIOD_DAY = (By.XPATH, '//*[@class="Dropdown-option" and (text()="сутки")]')
    RENTAL_PERIOD_TWO_DAYS = (By.XPATH, '//*[@class="Dropdown-option" and (text()="двое суток")]')
    COLOR_LABEL = (By.ID, 'black')
    ORDER_BUTTON = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and (text()="Заказать")]')
    CONFIRMATION_BUTTON = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and (text()="Да")]')
    CONFIRMATION_POPUP = (By.XPATH, '//*[@class="Order_ModalHeader__3FDaJ"]')
    ORDER_STATUS_BUTTON = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and (text()="Посмотреть статус")]')
    SCOOTER_LOGO = (By.XPATH, '//*[@src = "/assets/scooter.svg"]')
    YANDEX_LOGO = (By.XPATH, '//*[@src = "/assets/ya.svg"]')








