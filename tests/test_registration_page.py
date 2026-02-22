import data


class TestRegistrationPage:
    
    def test_registration_with_correct_credentials(
            self,
            sign_up_page
    ):
        """Registration with correct credentials."""
        sign_up_page.fill_sign_up_form(data.user.user_with_correct_credentials)
        actual_user_name = sign_up_page.get_user_name()

        assert actual_user_name == data.USER_NAME
    
    def test_registration_with_incorrect_email(
            self,
            sign_up_page
    ):
        """Registration with INcorrect email."""
        sign_up_page.fill_sign_up_form(data.user.user_with_incorrect_email)
        actual_error_message = sign_up_page.get_error_message_email_field()

        assert actual_error_message == data.ERROR_MESSAGE_EMAIL_FIELD

    def test_registration_by_existent_user(
            self,
            logout
    ):
        """Registration by existent user."""
        logout.go_to_sign_in_form()
        logout.go_to_sign_up_form()

        logout.fill_sign_up_form(data.user.existent)
        actual_error_message = logout.get_error_message_email_field()

        assert actual_error_message == data.ERROR_MESSAGE_EMAIL_FIELD
   
    def test_login_by_existent_user(
            self,
            logout
    ):
        """Login by existent user."""
        logout.go_to_sign_in_form()
        logout.fill_sign_in_form(data.user.existent)
       
        actual_user_name = logout.get_user_name()

        assert actual_user_name == data.USER_NAME
    
    def test_logout(
            self,
            registration_user
    ):
        """Logout by existent user."""
        registration_user.logout()
               
        
        assert registration_user.has_button_sign_in_and_sign_out()
