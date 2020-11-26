import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from commons import login, get_element

url = 'http://designing-solutions-smartech.herokuapp.com/'


class SmartechTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')
        self.driver = webdriver.Chrome(
            executable_path='./chromedriver', options=options)

    def test01_crear_usuario_correcto(self):
        try:
            driver = self.driver
            driver.get(url)
            login(driver)

            boton_adminitracion = get_element(driver, By.XPATH,
                                              '/html/body/div[1]/aside/section/ul/li[3]/a')
            boton_adminitracion.click()

            boton_usuario = get_element(driver, 
                By.XPATH, '/html/body/div[1]/aside/section/ul/li[3]/ul/li[1]')
            boton_usuario.click()

            boton_crear_usuario = get_element(driver, 
                By.XPATH, '//*[@id="app"]/section[2]/div/div/div/div[1]/div[1]/div[3]/a')
            boton_crear_usuario.click()

            Nombre_usuario = get_element(driver, By.ID, 'username')
            Nombre_usuario.send_keys('PedroL')

            Nombre = get_element(driver, By.ID,
                                 'name')
            Nombre.send_keys('Pedro')

            Contrasena = get_element(driver, By.ID, 'password')
            Contrasena.send_keys('1237')

            Contrasena_confirmacion = get_element(driver, 
                By.ID, 'password_confirmation')
            Contrasena_confirmacion.send_keys('1237')

            permiso = get_element(driver, 
                By.XPATH, '//*[@id="app"]/section[2]/div/div/div/form/div[1]/div/div/div[7]/div/span/span[1]/span/ul/li/input')
            permiso.send_keys('1237')

            boton_enviar = get_element(driver, By.XPATH,
                                       '/html/body/div[1]/div/div/section[2]/div/div/div/form/div[2]/div[2]/div[1]/button')
            boton_enviar.click()
        except Exception:
            driver.save_screenshot(
                'screenshots/test01_crear_usuario_correcto.png')
            raise

    def test02_crear_usuario_campo_vacio(self):
        try:
            driver = self.driver
            driver.get(url)
            login(driver)

            boton_adminitracion = get_element(driver, By.XPATH,
                                              '/html/body/div[1]/aside/section/ul/li[3]/a')
            boton_adminitracion.click()

            boton_usuario = get_element(driver, 
                By.XPATH, '/html/body/div[1]/aside/section/ul/li[3]/ul/li[1]')
            boton_usuario.click()

            boton_crear_usuario = get_element(driver, 
                By.XPATH, '//*[@id="app"]/section[2]/div/div/div/div[1]/div[1]/div[3]/a')
            boton_crear_usuario.click()

            Nombre_usuario = get_element(driver, By.ID, 'username')
            Nombre_usuario.send_keys('')

            Nombre = get_element(driver, By.ID,
                                 'name')
            Nombre.send_keys('')

            Contrasena = get_element(driver, By.ID, 'password')
            Contrasena.send_keys('')

            Contrasena_confirmacion = get_element(driver, 
                By.ID, 'password_confirmation')
            Contrasena_confirmacion.send_keys('')


            permiso = get_element(driver, 
                By.XPATH, '//*[@id="app"]/section[2]/div/div/div/form/div[1]/div/div/div[7]/div/span/span[1]/span/ul/li/input')
            permiso.send_keys('')


            boton_enviar = get_element(driver, By.XPATH,
                                       '/html/body/div[1]/div/div/section[2]/div/div/div/form/div[2]/div[2]/div[1]/button')
            boton_enviar.click()
        except Exception:
            driver.save_screenshot(
                'screenshots/test02_crear_usurio_campo_vacio.png')
            raise

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
