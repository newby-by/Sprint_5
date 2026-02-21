from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    presence_of_element_located
)


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)
    
    def wait_element_located(self, locator, time=5):
        element = WebDriverWait(self.driver, time).until(
            presence_of_element_located(locator)
        )

        return element 
