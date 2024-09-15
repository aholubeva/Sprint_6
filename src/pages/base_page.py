from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def navigate(self, url):
        self.driver.get(url)

    def current_url(self):
        return self.driver.current_url

    def find_element(self, locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))


    def click_element(self, locator, timeout=10):
        self.find_element(locator, timeout).click()

    def enter_text(self, locator, text, timeout=10):
        self.find_element(locator, timeout).send_keys(text)

    def wait_for_element_visible(self, locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))

    def scroll_page(self):
        return self.driver.execute_script("window.scrollTo(0, 2400)")

    def open_new_window_and_wait(self, url):
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(EC.url_to_be(url))

    def click_return(self, locator, timeout=10):
        self.find_element(locator, timeout).send_keys(Keys.RETURN)

    def element_is_present(self, locator, timeout=10):
        return self.find_element(locator, timeout).is_displayed()


