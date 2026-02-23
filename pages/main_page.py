from selenium.common.exceptions import StaleElementReferenceException

from pages.base_page import BasePage
from locators import MainPageLocators, RegistrationFormLocators


class MainPage(BasePage):

    def go_to_sign_in_form(self):
        btn = self.wait_element_located(MainPageLocators.SIGNIN_SIGNUP_BUTTON)
        btn.click()

        return self.driver  
    
    def logout(self):
        btn = self.wait_element_clickable(MainPageLocators.LOGOUT_BUTTON)
        btn.click()

        return self.driver  

    def go_to_sign_up_form(self):
        btn = self.wait_element_clickable(MainPageLocators.SIGNUP_BUTTON)
        btn.click()

        return self.driver
    
    def go_to_announcement(self):
        btn = self.wait_element_clickable(MainPageLocators.ANNOUNCEMENT_BUTTON)
        try:
            btn.click()
        except StaleElementReferenceException:
            btn = self.driver.find_element(*MainPageLocators.ANNOUNCEMENT_BUTTON)
            btn.click()
        return self.driver
    
    def go_to_account_page(self):
        btn = self.wait_element_located(MainPageLocators.ACCOUNT_BUTTON)
        try:
            btn.click()
        except Exception:
            btn = self.wait_element_located(MainPageLocators.ACCOUNT_BUTTON)
            btn.click()

        return self.driver
    
    def scroll_up(self):
        self.wait_element_located(MainPageLocators.ACCOUNT_BUTTON)
        self.scroll_into_element(MainPageLocators.ACCOUNT_BUTTON)
        return self.driver

    def fill_sign_up_form(self, user_data):
        email, password = user_data

        email_field = self.wait_element_located(RegistrationFormLocators.EMAIL)
        email_field.send_keys(email)
        
        self.driver.find_element(
            *RegistrationFormLocators.PASSWORD
        ).send_keys(password)
        self.driver.find_element(
            *RegistrationFormLocators.SUBMIT_PASSWORD
        ).send_keys(password)

        self.driver.find_element(
            *RegistrationFormLocators.CREATE_ACCOUNT_BUTTON
        ).click()
        return self.driver
    
    def fill_sign_in_form(self, user_data):
        email, password = user_data

        email_field = self.wait_element_located(RegistrationFormLocators.EMAIL)
        email_field.send_keys(email)
        
        self.driver.find_element(
            *RegistrationFormLocators.PASSWORD
        ).send_keys(password)
        self.driver.find_element(
            *RegistrationFormLocators.SIGN_IN_BUTTON
        ).click()
        return self.driver

    def get_user_name(self):
        user_name = self.wait_element_located(MainPageLocators.USER_NAME)
        return user_name.text
    
    def get_error_message_email_field(self):
        error_mes = self.wait_element_located(
            RegistrationFormLocators.ERROR_MESSAGE_EMAIL
        )

        return error_mes.text
    
    def has_button_sign_in_and_sign_out(self):
        return self.wait_element_located(
            MainPageLocators.SIGNIN_SIGNUP_BUTTON
        )
    
    def has_title_you_should_sign_in(self):
        return self.wait_element_located(
            RegistrationFormLocators.YOU_SHOULD_SIGN_IN_TITLE
        )
    
    def has_avatar_user_located(self):
        return self.wait_element_located(
            MainPageLocators.AVATAR_SVG
        )
