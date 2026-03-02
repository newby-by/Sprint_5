from pages.base_page import BasePage
from locators import AccountUserLocators


class AccountUserPage(BasePage):

    def scroll_to_card(self):
        self.scroll_into_element(AccountUserLocators.TITLE_CARDS)

    def has_announcement(self, name, city, price):
        self.wait_element_located(AccountUserLocators.CARDS)

        card = self.driver.find_element(*AccountUserLocators.CARDS)

        actual_name = card.find_element(*AccountUserLocators.NAME_GOODS).text
        actual_city = card.find_element(*AccountUserLocators.CITY_GOODS).text
        actual_price = card.find_element(
            *AccountUserLocators.PRICE_GOODS
        ).text.split()[0]

        return (actual_name == name and
                actual_city == city and
                int(actual_price) == price)
