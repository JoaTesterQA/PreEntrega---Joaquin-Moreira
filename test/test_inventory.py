from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select

def test_inventory(login_in_driver):
    driver = login_in_driver
    
    title = driver.find_element(By.CSS_SELECTOR, ".app_logo").text
    assert title == "Swag Labs"
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")[0]
    nombre = products.find_element(By.CLASS_NAME, "inventory_item_name ").text
    print(f"- producto {nombre}")
    filtro = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    filtro.select_by_index(2) #seleccionamos la tercera opcion del filtro
    print("- test exitoso")