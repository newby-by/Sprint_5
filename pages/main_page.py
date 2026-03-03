import data
from locators import MainPageLocators, RegistrationFormLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def go_to_sign_in_form(self):
        self.click(MainPageLocators.SIGNIN_SIGNUP_BUTTON)

    def logout(self):
        self.click(MainPageLocators.LOGOUT_BUTTON)

    def go_to_sign_up_form(self):
        self.click(MainPageLocators.SIGNUP_BUTTON)

    def go_to_announcement(self):
        self.click(MainPageLocators.ANNOUNCEMENT_BUTTON)

    def go_to_account_page(self):
        self.click(MainPageLocators.ACCOUNT_BUTTON)

    def scroll_up(self):
        self.wait_element_located(MainPageLocators.ACCOUNT_BUTTON)
        self.scroll_into_element(MainPageLocators.ACCOUNT_BUTTON)

    def fill_sign_up_form(self, user_data):
        email, password = user_data

        self.fill_field(RegistrationFormLocators.EMAIL, email)
        self.fill_field(RegistrationFormLocators.PASSWORD, password)
        self.fill_field(RegistrationFormLocators.SUBMIT_PASSWORD, password)
        self.click(RegistrationFormLocators.CREATE_ACCOUNT_BUTTON)

    def fill_sign_in_form(self, user_data):
        email, password = user_data

        self.fill_field(RegistrationFormLocators.EMAIL, email)
        self.fill_field(RegistrationFormLocators.PASSWORD, password)
        self.click(RegistrationFormLocators.SIGN_IN_BUTTON)

    def get_user_name(self):
        return self.get_text(MainPageLocators.USER_NAME)

    def get_error_message_email_field(self):
        return self.get_text(RegistrationFormLocators.ERROR_MESSAGE_EMAIL)

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

        return (data.HomePageData.ERROR_CLASS in class_for_email and
                data.HomePageData.ERROR_CLASS in class_for_password and
                data.HomePageData.ERROR_CLASS in class_for_submit_password)

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
