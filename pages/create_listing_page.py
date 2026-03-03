from data import AnnouncementFormData
from locators import CreateListingLocators
from pages.base_page import BasePage


class CreateListingPage(BasePage):

    def set_name(self, name):
        self.fill_field(CreateListingLocators.NAME_FIELD, name)

    def set_category(self, category):
        self.click(CreateListingLocators.CATEGORY_OPEN)
        category = AnnouncementFormData.CATEGORIES[category] - 1
        self.click(CreateListingLocators.CATEGORIES[category])

    def set_condition_goods(self, condition):
        condition = AnnouncementFormData.CONDITION_GOODS[condition] - 1
        self.click(CreateListingLocators.CONDITIONS[condition])

    def set_city(self, city):
        self.click(CreateListingLocators.CITY_OPEN)

        city = AnnouncementFormData.CITIES[city] - 1
        self.click(CreateListingLocators.CITIES[city])

    def set_description(self, description):
        self.fill_field(CreateListingLocators.DESCRIPTION, description)

    def set_price(self, price):
        self.fill_field(CreateListingLocators.PRICE, price)

    def publish(self):
        self.click(CreateListingLocators.CREATE_BUTTON)
