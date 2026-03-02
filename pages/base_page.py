from selenium.webdriver.support.expected_conditions import (
    element_to_be_clickable,
    presence_of_element_located,
    visibility_of_element_located,
)
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def wait_element_located(self, locator, time=5):
        element = WebDriverWait(self.driver, time).until(
            presence_of_element_located(locator)
        )
        return element

    def wait_element_dislocated(self, locator, time=5):
        element = WebDriverWait(self.driver, time).until_not(
            presence_of_element_located(locator)
        )
        return element

    def wait_element_visibility(self, locator, time=5):
        element = WebDriverWait(self.driver, time).until(
            visibility_of_element_located(locator)
        )
        return element

    def wait_element_clickable(self, locator, time=5):
        element = WebDriverWait(self.driver, time).until(
            element_to_be_clickable(locator)
        )
        return element

    def scroll_into_element(self, locator):
        btn = self.driver.find_element(*locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", btn
        )
