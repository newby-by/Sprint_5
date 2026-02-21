import data


class TestRegistrationPage:
    
    def test_registration_with_correct_credentials(
            self,
            fill_sign_up_form_with_correct_data
    ):
        """Registration with correct credentials."""
        actual_user_name = fill_sign_up_form_with_correct_data.get_user_name()

        assert actual_user_name == data.USER_NAME
    
    def test_registration_with_incorrect_email(
            self,
            fill_sign_up_form_with_incorrect_email
    ):
        """Registration with INcorrect email."""
        actual_error_message = (fill_sign_up_form_with_incorrect_email.
                                get_error_message_email_field())

        assert actual_error_message == data.ERROR_MESSAGE_EMAIL_FIELD
