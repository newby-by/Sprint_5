import chromedriver_autoinstaller
import pytest
from faker import Faker
from selenium import webdriver

import data
from pages.main_page import MainPage


@pytest.fixture(scope='function')
def driver():
    chromedriver_autoinstaller.install() 
    driver = webdriver.Chrome()

    yield driver

    driver.quit()


@pytest.fixture(scope='function')
def sign_in_page(driver):
    main_page = MainPage(driver, data.BASE_URL)
    main_page.open()
    main_page.go_to_sign_in_form()

    yield main_page


@pytest.fixture(scope='function')
def sign_up_page(sign_in_page):
    sign_in_page.go_to_sign_up_form()
    yield sign_in_page


@pytest.fixture(scope='function')
def user_with_correct_credentials():
    faker = Faker()
    yield (faker.unique.email(), faker.password()) 


@pytest.fixture(scope='function')
def fill_sign_up_form_with_correct_data(sign_up_page,
                                        user_with_correct_credentials):
    sign_up_page.fill_sign_up_form(user_with_correct_credentials)
    yield sign_up_page
