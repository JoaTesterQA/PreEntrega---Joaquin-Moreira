from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_validation(login_in_driver): #creamos una funcion y llamamos al login desde el archivo conftest
    driver = login_in_driver
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item")) # espera explicita una vez ingresado a la pagina para que carge todos sus elementos
    )
    assert "inventory" in driver.current_url #validamos que se ingreso a la pagina con un assert
    print("- login exitoso")