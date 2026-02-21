from selenium.webdriver.common.by import By


class RegistrationFormLocators:
    EMAIL = (By.XPATH, ".//input[@name='email']")
    PASSWORD = (By.XPATH, ".//input[@name='password']")
    SUBMIT_PASSWORD = (By.XPATH, ".//input[@name='submitPassword']")
    SIGN_IN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Создать аккаунт']")
    ERROR_MESSAGE_EMAIL = (By.XPATH, ".//span[text()='Ошибка']")


class MainPageLocators:
    USER_NAME = (By.XPATH, ".//h3[contains(@class, 'profileText')]")
    SIGNIN_SIGNUP_BUTTON = (By.XPATH, ".//button[text()='Вход и регистрация']")
    SIGNUP_BUTTON = (By.XPATH, ".//button[text()='Нет аккаунта']")
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выйти']")
