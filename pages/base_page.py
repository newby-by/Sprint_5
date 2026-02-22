from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    presence_of_element_located,
    visibility_of_element_located,
    element_to_be_clickable,
)


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)
    
    def wait_element_located(self, locator, time=15):
        element = WebDriverWait(self.driver, time).until(
            presence_of_element_located(locator)
        )
        return element 
    
    def wait_element_visibility(self, locator, time=15):
        element = WebDriverWait(self.driver, time).until(
            visibility_of_element_located(locator)
        )
        return element 

    def wait_element_clickable(self, locator, time=15):
        element = WebDriverWait(self.driver, time).until(
            element_to_be_clickable(locator)
        )
        return element 
    
    def scroll_into_element(self, locator):
        btn = self.driver.find_element(*locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", btn
        )