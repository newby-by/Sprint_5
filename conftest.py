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
