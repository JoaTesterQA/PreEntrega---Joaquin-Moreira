from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Carrito de compras
def test_cart(login_in_driver):
    driver = login_in_driver
    
    producto = driver.find_element(By.XPATH, '//button[@name="add-to-cart-sauce-labs-backpack"]')
    producto.click() #elegimos el primer producto y hacemos click en ADD TO CART
    carrito = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping_cart_badge")) # espera explicita una vez ingresado a la pagina para que carge todos sus elementos
    )
    assert carrito.text == "1" #validamos que incremento el carrito cuando añadimos el producto
    carrito_producto = driver.find_element(By.ID, "shopping_cart_container")
    carrito_producto.click() #hacemos click en el carrito de compras
    validar_producto = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert validar_producto == "Sauce Labs Backpack" #validamos que el producto se haya añadido correctamente
    time.sleep(5)
    print("- producto añadido con exito")