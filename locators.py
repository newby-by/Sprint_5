from selenium.webdriver.common.by import By


class RegistrationFormLocators:
    EMAIL = (By.XPATH, ".//input[@name='email']")
    PASSWORD = (By.XPATH, ".//input[@name='password']")
    SUBMIT_PASSWORD = (By.XPATH, ".//input[@name='submitPassword']")
    SIGN_IN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Создать аккаунт']")
    ERROR_MESSAGE_EMAIL = (By.XPATH, ".//span[text()='Ошибка']")
    YOU_SHOULD_SIGN_IN_TITLE = (
        By.XPATH,
        ".//h1[text()='Чтобы разместить объявление, авторизуйтесь']"
    )


class MainPageLocators:
    USER_NAME = (By.XPATH, ".//h3[contains(@class, 'profileText')]")
    AVATAR_SVG = (By.XPATH, ".//*[@class='svgSmall']")
    SIGNIN_SIGNUP_BUTTON = (
        By.XPATH, ".//button[text()='Вход и регистрация']"
    )
    ANNOUNCEMENT_BUTTON = (
        By.XPATH, ".//button[text()='Разместить объявление']"
    )
    SIGNUP_BUTTON = (By.XPATH, ".//button[text()='Нет аккаунта']")
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выйти']")
    ACCOUNT_BUTTON = (By.XPATH, ".//button[@class='circleSmall']")


class CreateListingLocators:
    CREATE_BUTTON = (By.XPATH, ".//button[text()='Опубликовать']")
    NAME_FIELD = (By.XPATH, ".//input[@name='name']")
    CATEGORY_OPEN = (By.XPATH, ".//form/div[2]/div[2]/div[1]//button[1]")
    CATEGORY_AUTO = (By.XPATH, ".//form/div[2]/div[2]/div[2]//button[1]")
    CATEGORY_BOOK = (By.XPATH, ".//form/div[2]/div[2]/div[2]//button[2]")
    CATEGORY_GARDEN = (By.XPATH, ".//form/div[2]/div[2]/div[2]//button[3]")
    CATEGORY_HOBBY = (By.XPATH, ".//form/div[2]/div[2]/div[2]//button[4]")
    CATEGORY_TECH = (By.XPATH, ".//form/div[2]/div[2]/div[2]//button[5]")
    CATEGORIES = (CATEGORY_AUTO, CATEGORY_BOOK, CATEGORY_GARDEN,
                  CATEGORY_HOBBY, CATEGORY_TECH, )
    CONDITION_GOODS_NEW = (By.XPATH, ".//fieldset//label[text()='Новый']")
    CONDITION_GOODS_USED = (By.XPATH, ".//fieldset//label[text()='Б/У']")
    CONDITIONS = (CONDITION_GOODS_NEW, CONDITION_GOODS_USED, )
    CITY_OPEN = (
        By.XPATH,
        ".//form/div[contains(@class,'dropDownMenu')]/div[1]/button"
    )
    CITY_MOSCOW = (
        By.XPATH,
        ".//form/div[contains(@class, 'dropDownMenu')]/div[2]/button[1]"
    )
    CITY_SPB = (
        By.XPATH,
        ".//form/div[contains(@class, 'dropDownMenu')]/div[2]/button[2]"
    )
    CITY_NOVOSIB = (
        By.XPATH,
        ".//form/div[contains(@class, 'dropDownMenu')]/div[2]/button[3]"
    )
    CITY_EBURG = (
        By.XPATH,
        ".//form/div[contains(@class, 'dropDownMenu')]/div[2]/button[4]"
    )
    CITY_BOTTOM_NEW_CITY = (
        By.XPATH,
        ".//form/div[contains(@class, 'dropDownMenu')]/div[2]/button[5]"
    )
    CITY_KAZAN = (
        By.XPATH,
        ".//form/div[contains(@class, 'dropDownMenu')]/div[2]/button[6]"
    )
    CITIES = (CITY_MOSCOW, CITY_SPB, CITY_NOVOSIB, 
              CITY_EBURG, CITY_BOTTOM_NEW_CITY, CITY_KAZAN, )
    DESCRIPTION = (By.XPATH, ".//textarea[@name='description']")
    PRICE = (By.XPATH, ".//input[@name='price']")


class AccountUserLocators:

    CARDS = (By.XPATH, ".//div[@class='card']")
    TITLE_CARDS = (By.XPATH, ".//h1[text()='Мои объявления']")
    TEXT_PAGINATION = (By.XPATH, ".//p")
    NAME_GOODS = (By.XPATH, ".//div[@class='about']/h2")
    CITY_GOODS = (By.XPATH, ".//div[@class='about']/h3")
    PRICE_GOODS = (By.XPATH, ".//div[@class='price']/h2")
    
