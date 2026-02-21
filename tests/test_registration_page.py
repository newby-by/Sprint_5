import data


class TestRegistrationPage:
    
    def test_registration_with_correct_credentials(
            self,
            fill_sign_up_form_with_correct_data
    ):
        """Registration with correct credentials."""
        actual_user_name = fill_sign_up_form_with_correct_data.get_user_name()

        assert actual_user_name == data.USER_NAME
