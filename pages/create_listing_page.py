import data
from pages.base_page import BasePage
from locators import CreateListingLocators


class CreateListingPage(BasePage):

    def set_name(self, name):
        element = self.wait_element_located(CreateListingLocators.NAME_FIELD)
        element.send_keys(name)

        return self
    
    def set_category(self, category):
        drop_down = self.wait_element_located(CreateListingLocators.CATEGORY_OPEN)
        drop_down.click()

        select = self.wait_element_located(
            CreateListingLocators.CATEGORIES[data.CATEGORIES[category] - 1]
        )
        select.click()
        return self
    
    def set_condition_goods(self, condition):
        radio_button = self.wait_element_located(
            (CreateListingLocators.
             CONDITIONS[data.CONDITION_GOODS[condition] - 1])
        )
        radio_button.click()
        return self
    
    def set_city(self, city):

        radio_button = self.wait_element_located(
            CreateListingLocators.CITY_OPEN
        )
        radio_button.click()

        select = self.wait_element_located(
            CreateListingLocators.CITIES[data.CITIES[city] - 1]
        )
        select.click()
        return self

    def set_description(self, description):
        element = self.wait_element_located(CreateListingLocators.DESCRIPTION)
        element.send_keys(description)

        return self
    
    def set_price(self, price):
        element = self.wait_element_located(CreateListingLocators.PRICE)
        element.send_keys(price)

        return self
    
    
    def publish(self):
        btn = self.wait_element_located(CreateListingLocators.CREATE_BUTTON)
        btn.click()

        return self.driver
    

