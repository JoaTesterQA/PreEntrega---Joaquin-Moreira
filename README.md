# Proyecto de pruebas automatizadas de la web SAUCE DEMO

## herramientas que se utilizo:
- Python 3.13.5
- Pytest 8.4.1
- Selenium 4.34.0
- WebDriver 4.0.2

## Resumen del proyecto:
- Resumen del proyecto.
Este proyecto consiste en la **automatización de pruebas funcionales** sobre la página [Sauce Demo](https://www.saucedemo.com/).  
El objetivo principal es verificar el **flujo completo de usuario**, incluyendo:
- Inicio de sesión exitoso.
- Visualización de productos.
- Aplicación de filtros.
- Adición de productos al carrito.
- Validación de elementos dentro del carrito.


## Estructura del proyecto:
- Carpeta test: En esta carpeta se encuentra todas las pruebas que relizamos.
- conftest.py: Archivo que se encuentra en la rama del proyecto, aca se encuentra la configuracion general de las pruebas.
- utils.py: aca se encuentra la parte logica de la prueba login, un archivo general que se puede reutilizar en otras pruebas.
- run_test.py: Aca es donde se corre todas las pruebas realizadas.
- report.html: este archivo se genera cuando corremos la prueba, nos da un enfoque visual de todas las pruebas hechas.

## Como correr las pruebas:
- Clonar repositorio:
git clone https://github.com/JoaTesterQA/PreEntrega---Joaquin-Moreira.git
- instalar dependencias:
pip install -r requirements.txt
- Nos dirigimos al archivo run_test.py y lo corremos desde el run python.


