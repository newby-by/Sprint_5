from pages.base_page import BasePage
from locators import AccountUserLocators


class AccountUserPage(BasePage):

    def scroll_to_card(self):
        self.scroll_into_element(AccountUserLocators.TITLE_CARDS)

    def has_announcement(self, name, city, price):
        self.wait_element_located(AccountUserLocators.CARDS)

        actual_name = self.get_text(AccountUserLocators.NAME_GOODS)
        actual_city = self.get_text(AccountUserLocators.CITY_GOODS)
        actual_price = self.get_text(AccountUserLocators.PRICE_GOODS).split()[0]

        return (actual_name == name and
                actual_city == city and
                int(actual_price) == price)
