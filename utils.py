from selenium.webdriver.common.by import By
import time

def test_form(driver):
#-----------LOGIN-----------------
    driver.get("https://www.saucedemo.com/") 
    
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    button = driver.find_element(By.ID, "login-button")
    button.click()
    
    time.sleep(5)