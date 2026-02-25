from selenium.common.exceptions import StaleElementReferenceException

import data
from locators import MainPageLocators, RegistrationFormLocators
from pages.base_page import BasePage


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
        user_name = self.wait_element_located(MainPageLocators.USER_NAME).text
        return user_name
    
    def get_error_message_email_field(self):
        error_mes = self.wait_element_located(
            RegistrationFormLocators.ERROR_MESSAGE_EMAIL
        )

        return error_mes.text
    
    def has_error_class_in_fields(self):
        email = self.wait_element_located(
            RegistrationFormLocators.PARENT_EMAIL_NODE
        )
        class_for_email = email.get_attribute('class')
        
        password = self.wait_element_located(
            RegistrationFormLocators.PARENT_PASSWORD_NODE
        )
        class_for_password = password.get_attribute('class')
        
        submit_password = self.wait_element_located(
            RegistrationFormLocators.PARENT_SUBMIT_PASSWORD_NODE
        )
        class_for_submit_password = submit_password.get_attribute('class')

        return (data.ERROR_CLASS in class_for_email and 
                data.ERROR_CLASS in class_for_password and 
                data.ERROR_CLASS in class_for_submit_password)
    
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
    
    def is_avatar_user_dislocated(self):
        return self.wait_element_dislocated(
            MainPageLocators.AVATAR_SVG
        )

    def is_user_name_dislocated(self):
        return self.wait_element_dislocated(MainPageLocators.USER_NAME)
    