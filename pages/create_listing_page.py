from data import AnnouncementFormData
from locators import CreateListingLocators
from pages.base_page import BasePage


class CreateListingPage(BasePage):

    def set_name(self, name):
        element = self.wait_element_located(CreateListingLocators.NAME_FIELD)
        element.send_keys(name)

    def set_category(self, category):
        drop_down = self.wait_element_located(
            CreateListingLocators.CATEGORY_OPEN
        )
        drop_down.click()

        category = AnnouncementFormData.CATEGORIES[category] - 1
        select = self.wait_element_located(
            CreateListingLocators.CATEGORIES[category]
        )
        select.click()

    def set_condition_goods(self, condition):
        condition = AnnouncementFormData.CONDITION_GOODS[condition] - 1
        radio_button = self.wait_element_located(
            CreateListingLocators.CONDITIONS[condition]
        )
        radio_button.click()

    def set_city(self, city):

        radio_button = self.wait_element_located(
            CreateListingLocators.CITY_OPEN
        )
        radio_button.click()

        city = AnnouncementFormData.CITIES[city] - 1
        select = self.wait_element_located(
            CreateListingLocators.CITIES[city]
        )
        select.click()

    def set_description(self, description):
        element = self.wait_element_located(CreateListingLocators.DESCRIPTION)
        element.send_keys(description)

    def set_price(self, price):
        element = self.wait_element_located(CreateListingLocators.PRICE)
        element.send_keys(price)

    def publish(self):
        btn = self.wait_element_located(CreateListingLocators.CREATE_BUTTON)
        btn.click()

        return self.driver
