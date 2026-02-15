import os

import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DRIVER_PATH = os.path.join(BASE_DIR, 'chromedriver.exe')

    driver = webdriver.Chrome(executable_path=DRIVER_PATH)

    yield driver

    driver.quit()
