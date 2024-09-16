from selenium.webdriver.common.by import By

class MainPageLocators:
    FIRST_QUESTION = (By.ID, 'accordion__heading-0')
    SECOND_QUESTION = (By.ID, 'accordion__heading-1')
    THIRD_QUESTION = (By.ID, 'accordion__heading-2')
    FOURTH_QUESTION = (By.ID, 'accordion__heading-3')
    FIFTH_QUESTION = (By.ID, 'accordion__heading-4')
    SIXTH_QUESTION = (By.ID, 'accordion__heading-5')
    SEVENTH_QUESTION = (By.ID, 'accordion__heading-6')
    EIGHTH_QUESTION = (By.ID, 'accordion__heading-7')
    FIRST_ANSWER = (By.XPATH, '//*[@aria-labelledby="accordion__heading-0"]')
    SECOND_ANSWER = (By.XPATH, '//*[@aria-labelledby="accordion__heading-1"]')
    THIRD_ANSWER = (By.XPATH, '//*[@aria-labelledby="accordion__heading-2"]')
    FOURTH_ANSWER = (By.XPATH, '//*[@aria-labelledby="accordion__heading-3"]')
    FIFTH_ANSWER = (By.XPATH, '//*[@aria-labelledby="accordion__heading-4"]')
    SIXTH_ANSWER = (By.XPATH, '//*[@aria-labelledby="accordion__heading-5"]')
    SEVENTH_ANSWER = (By.XPATH, '//*[@aria-labelledby="accordion__heading-6"]')
    EIGHTH_ANSWER = (By.XPATH, '//*[@aria-labelledby="accordion__heading-7"]')

