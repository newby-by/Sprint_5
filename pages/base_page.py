from selenium.common.exceptions import StaleElementReferenceException
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

    def wait_element_located(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(
            presence_of_element_located(locator)
        )
        return element

    def wait_element_dislocated(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until_not(
            presence_of_element_located(locator)
        )
        return element

    def wait_element_visibility(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(
            visibility_of_element_located(locator)
        )
        return element

    def wait_element_clickable(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(
            element_to_be_clickable(locator)
        )
        return element

    def scroll_into_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", element
        )

    def click(self, locator):
        btn = self.wait_element_clickable(locator)
        try:
            btn.click()
        except StaleElementReferenceException:
            btn = self.driver.find_element(*locator)
            btn.click()

    def fill_field(self, locator, value):
        self.wait_element_located(locator).send_keys(value)

    def get_text(self, locator):
        element = self.wait_element_located(locator)
        return element.text
