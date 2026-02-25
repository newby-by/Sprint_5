from conftest import driver
import data
from pages.account_user_page import AccountUserPage
from pages.create_listing_page import CreateListingPage
from pages.main_page import MainPage


class TestMainPage:
    
    def test_registration_with_correct_credentials(
            self,
            sign_up_page
    ):
        """Registration with correct credentials.
        
        Steps:
            1. Press the button «Вход и регистрация».
            2. Press the button «Нет аккаунта».
            3. Fill all fields up.
            4. Press the button «Создать аккаунт».
        Check:
            1. Redirect to the main page app.
            2. On the right corner near the button «Разместить объявление» 
               display a user avatar and a the name `User`.
        """
        sign_up_page.fill_sign_up_form(
            data.user.user_with_correct_credentials
        )
        main_page = MainPage(
            sign_up_page.driver,
            sign_up_page.driver.current_url
        )
        actual_user_name = main_page.get_user_name()

        assert (
            main_page.has_avatar_user_located() and
            actual_user_name == data.USER_NAME
        )
    
    def test_registration_with_incorrect_email(
            self,
            sign_up_page
    ):
        """Registration with INcorrect email.
        
        Steps:
        1. Press the button «Вход и регистрация».
        2. Press the button «Нет аккаунта».
        3. Fill the email field up with incorrect data.
        4. Press the button «Создать аккаунт».
        Check:
        The fields `Email`, `Пароль`, `Повторите пароль` are marked by 
        red color and under the field `Email` showed up the message `Ошибка`.
        """
        sign_up_page.fill_sign_up_form(data.user.user_with_incorrect_email)
        actual_error_message = sign_up_page.get_error_message_email_field()

        assert (actual_error_message == data.ERROR_MESSAGE_EMAIL_FIELD and
                sign_up_page.has_error_class_in_fields())

    def test_registration_by_existent_user(
            self,
            logout
    ):
        """Registration by existent user.
        
        Steps:
        1. Press the button «Вход и регистрация».
        2. Press the button «Нет аккаунта».
        3. Fill the fields up with existent user data.
        4. Press the button «Создать аккаунт».
        Check:
        The fields `Email`, `Пароль`, `Повторите пароль` are marked by 
        red color and under the field `Email` showed up the message `Ошибка`.
        """
        logout.go_to_sign_in_form()
        logout.go_to_sign_up_form()

        logout.fill_sign_up_form(data.user.existent)
        actual_error_message = logout.get_error_message_email_field()

        assert (actual_error_message == data.ERROR_MESSAGE_EMAIL_FIELD and
                logout.has_error_class_in_fields())
   
    def test_login_by_existent_user(
            self,
            logout
    ):
        """Login by existent user.
        
        Steps:
        1. Press the button «Вход и регистрация».
        2. Fill the fields up with existent user data.
        3. Press the button «Войти».
        Check:
        1. Redirect to the main page app.
        2. On the right corner near the button «Разместить объявление» 
            display a user avatar and a the name `User`.
        """
        logout.go_to_sign_in_form()
        logout.fill_sign_in_form(data.user.existent)
       
        actual_user_name = logout.get_user_name()

        assert (
            logout.has_avatar_user_located() and
            actual_user_name == data.USER_NAME
        )
    
    def test_logout(
            self,
            registration_user
    ):
        """Logout by existent user."""
        registration_user.logout()
               
        
        assert registration_user.has_button_sign_in_and_sign_out()

    def test_announcement_guest_user_login_only(
            self,
            main_page
    ):
        """Login by existent user."""
        main_page.go_to_announcement()

        assert main_page.has_title_you_should_sign_in()

    def test_announcement_auth_user(
                self,
                logout
        ):
            """Login by existent user.
            
            Steps:
            1. Sign in by an existence user.
            2. Fill an announcement up:
                name, description, price, categories, city, choose.
            3. Choose 'new' or 'used'.
            4. Press publish.

            Asserts:
            The name, the city and the price have expected values. 
            """
            logout.go_to_sign_in_form()
            logout.fill_sign_in_form(data.user.existent)
            main_page = MainPage(
                logout.driver,
                logout.driver.current_url
            )
            main_page.go_to_announcement()
            anounce_page: CreateListingPage = CreateListingPage(
                 main_page.driver,
                 main_page.driver.current_url
            )
            expected_announce = data.announcement
            (anounce_page.
             set_name(expected_announce.name).
             set_category(expected_announce.category).
             set_condition_goods(expected_announce.condition).
             set_city(expected_announce.city).
             set_description(expected_announce.description).
             set_price(expected_announce.price))
            anounce_page.publish()

            main_page = MainPage(
                 anounce_page.driver,
                 anounce_page.driver.current_url
                 )
            
            main_page.scroll_up()
            main_page.go_to_account_page()
            account_page: AccountUserPage = AccountUserPage(
                 anounce_page.driver,
                 anounce_page.driver.current_url
            )
            account_page.scroll_to_card()

            assert account_page.has_announcement(
                 expected_announce.name,
                 expected_announce.city,
                 expected_announce.price
            )

