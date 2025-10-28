from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

# Inventario
def test_inventory(login_in_driver):
    driver = login_in_driver
    
    title = driver.find_element(By.CSS_SELECTOR, ".app_logo").text #validamos que se encuentre el titulo de la pagina utilizando un assert
    assert title == "Swag Labs"
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")[0]  # creamos una variable y seleccionamos el item 1
    nombre = products.find_element(By.CLASS_NAME, "inventory_item_name ").text #creamos otra variable y llamamos a la que creamos anteriormente
    print(f"- producto {nombre}") #hacemos print para visualizar el nombre del producto seleccioando
    filtro_menu = driver.find_element(By.ID, "react-burger-menu-btn")
    filtro_menu.click()
    filtro = Select(driver.find_element(By.CLASS_NAME, "product_sort_container")) #usamos un select para elegir la tercera opcion del filtro
    filtro.select_by_index(2) #seleccionamos la tercera opcion del filtro
    time.sleep(3)
    print("- test exitoso")