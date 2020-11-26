# Smartech Selenium Tests
Pruebas automatizadas del proyecto Smartech con la herramienta de Selenium

## Cómo ejecutar las pruebas

- El chromedriver es para la versión 85 de linux. En cualquier otro caso se puede descargar de [aquí](https://chromedriver.chromium.org/downloads)
- Es necesario tener instalada la dependencia `selenium`

```shell
python3 test_login.py
python3 test_proyectos.py
python3 test_administracion.py
```


- En caso de que alguna prueba falle se almacenará una imagen en la carpeta `screenshots` con el nombre de la prueba.
