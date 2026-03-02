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
    start_page = MainPage(driver)
    start_page.open(data.BASE_URL)
    return start_page


@pytest.fixture(scope='function')
def sign_in_page(main_page):
    main_page.go_to_sign_in_form()
    return main_page


@pytest.fixture(scope='function')
def sign_up_page(sign_in_page):
    sign_in_page.go_to_sign_up_form()
    return sign_in_page


@pytest.fixture(scope='function')
def registration_user(sign_up_page):
    sign_up_page.fill_sign_up_form(data.user.new)
    return sign_up_page


@pytest.fixture(scope='function')
def logout(registration_user):
    registration_user.logout()
    return registration_user
