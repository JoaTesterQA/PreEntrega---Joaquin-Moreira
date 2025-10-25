import pytest
from selenium import webdriver
from utils import test_form

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5) #espera implicita en cada script
    yield driver
    driver.quit()

@pytest.fixture    
def login_in_driver(driver):
    test_form(driver)
    return driver
    