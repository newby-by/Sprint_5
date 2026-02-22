import chromedriver_autoinstaller
import pytest
from selenium import webdriver

import data
from pages.main_page import MainPage


@pytest.fixture(scope='function')
def driver():
    chromedriver_autoinstaller.install() 
    driver = webdriver.Chrome()

    yield driver

    # driver is None or 
    driver.quit()


@pytest.fixture(scope='function')
def main_page(driver):
    start_page = MainPage(driver, data.BASE_URL)
    start_page.open()
    yield start_page


@pytest.fixture(scope='function')
def sign_in_page(main_page):
    main_page.go_to_sign_in_form()
    yield main_page


@pytest.fixture(scope='function')
def sign_up_page(sign_in_page):
    sign_in_page.go_to_sign_up_form()
    yield sign_in_page


@pytest.fixture(scope='function')
def registration_user(sign_up_page):
    sign_up_page.fill_sign_up_form(data.user.new)
    yield sign_up_page


@pytest.fixture(scope='function')
def logout(registration_user):
    registration_user.logout()
    yield registration_user

