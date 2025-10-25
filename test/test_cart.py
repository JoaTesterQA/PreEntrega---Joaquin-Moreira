from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_cart(login_in_driver):
    driver = login_in_driver
    
    producto = driver.find_element(By.XPATH, '//button[@name="add-to-cart-sauce-labs-backpack"]')
    producto.click()
    carrito = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping_cart_badge")) # espera explicita una vez ingresado a la pagina para que carge todos sus elementos
    )
    assert carrito.text == "1"
    carrito_producto = driver.find_element(By.ID, "shopping_cart_container")
    carrito_producto.click()
    validar_producto = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert validar_producto == "Sauce Labs Backpack"
    print("- producto añadido con exito")