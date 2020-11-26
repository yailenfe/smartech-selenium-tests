import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time

from commons import login, get_element

url = 'http://designing-solutions-smartech.herokuapp.com/'

class SmartechTest(unittest.TestCase):

    def _get_nuevo_titulo(self):
        return 'Titlo - ' + str(random.random())

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')
        self.driver = webdriver.Chrome(
            executable_path='./chromedriver', options=options)

    def test01_crear_proyecto_correcto(self):
        try:
            driver = self.driver
            driver.get(url)
            login(driver)

            boton_ListadoProyecto = get_element(driver, By.XPATH,
                                                '//*[@id="app"]/section[2]/div/div[1]/div/div/a')
            boton_ListadoProyecto.click()

            boton_crear_Proyecto = get_element(driver, 
                By.XPATH, '/html/body/div/div/div/section[2]/div/div/div/div[1]/div[1]/div[2]/a')

            boton_crear_Proyecto.click()

            titulo = get_element(driver, By.ID, 'name')
            titulo.send_keys(self._get_nuevo_titulo())

            descripcion = get_element(driver, By.XPATH,
                                      '/html/body/div/div/div/section[2]/div/div/div/form/div[1]/div/div/div[2]/div/textarea')
            descripcion.send_keys('ESte es un nuevo proyecto')

            normas = get_element(driver, By.XPATH,
                                 '//*[@id="app"]/section[2]/div/div/div/form/div[1]/div/div/div[3]/div/span/span[1]/span/ul/li/input')
            normas.send_keys('ESte es un nuevo proyecto')

            user_panel = get_element(driver, By.CLASS_NAME, 'user-panel')
            self.assertIsNotNone(user_panel)

            boton_enviar = get_element(driver, By.XPATH,
                                       '//*[@id="app"]/section[2]/div/div/div/form/div[2]/div[2]/div[1]/button')
            boton_enviar.click()
        except Exception:
            driver.save_screenshot(
                'screenshots/test01_crear_proyecto_correcto.png')
            raise

    def test02_crear_proyecto_campo_vacio(self):
        try:
            driver = self.driver
            driver.get(url)
            login(driver)

            boton_ListadoProyecto = get_element(driver, By.XPATH,
                                                '//*[@id="app"]/section[2]/div/div[1]/div/div/a')
            boton_ListadoProyecto.click()

            boton_crear_Proyecto = get_element(driver, 
                By.XPATH, '/html/body/div/div/div/section[2]/div/div/div/div[1]/div[1]/div[2]/a')

            boton_crear_Proyecto.click()

            titulo = get_element(driver, By.ID, 'name')
            titulo.send_keys('')

            descripcion = get_element(driver, By.XPATH,
                                      '/html/body/div/div/div/section[2]/div/div/div/form/div[1]/div/div/div[2]/div/textarea')
            descripcion.send_keys('')

            normas = get_element(driver, By.XPATH,
                                 '//*[@id="app"]/section[2]/div/div/div/form/div[1]/div/div/div[3]/div/span/span[1]/span/ul/li/input')
            normas.send_keys('')


            boton_enviar = get_element(driver, By.XPATH,
                                       '//*[@id="app"]/section[2]/div/div/div/form/div[2]/div[2]/div[1]/button')
            boton_enviar.click()

            boton_deisboard = get_element(driver, By.XPATH,
                                          '/html/body/div/aside/section/ul/li[4]/a')
            boton_deisboard.click()

        except Exception:
            driver.save_screenshot(
                'screenshots/test02_crear_proyecto_campo_vacio.png')
            raise

    def test03_crear_proyecto_restablecer(self):
        try:
            driver = self.driver
            driver.get(url)
            login(driver)

            boton_ListadoProyecto = get_element(driver, By.XPATH,
                                                '//*[@id="app"]/section[2]/div/div[1]/div/div/a')
            boton_ListadoProyecto.click()

            boton_crear_Proyecto = get_element(driver, 
                By.XPATH, '/html/body/div/div/div/section[2]/div/div/div/div[1]/div[1]/div[2]/a')

            boton_crear_Proyecto.click()

            titulo = get_element(driver, By.ID, 'name')
            titulo.send_keys(self._get_nuevo_titulo())

            descripcion = get_element(driver, By.XPATH,
                                      '/html/body/div/div/div/section[2]/div/div/div/form/div[1]/div/div/div[2]/div/textarea')
            descripcion.send_keys('ESte es un nuevo proyecto')

            normas = get_element(driver, By.XPATH,
                                 '//*[@id="app"]/section[2]/div/div/div/form/div[1]/div/div/div[3]/div/span/span[1]/span/ul/li/input')
            normas.send_keys('ESte es un nuevo proyecto')

            boton_restablecer = get_element(driver, By.XPATH,
                                            '/html/body/div/div/div/section[2]/div/div/div/form/div[2]/div[2]/div[2]')
            boton_restablecer.click()

        except Exception:
            driver.save_screenshot(
                'screenshots/test03_crear_proyecto_restablecer.png')
            raise

    def test04_eliminar_proyecto(self):
        try:
            driver = self.driver
            driver.get(url)
            login(driver)

            boton_ListadoProyecto = get_element(driver, By.XPATH,
                                                '//*[@id="app"]/section[2]/div/div[1]/div/div/a')
            boton_ListadoProyecto.click()

            boton_crear_Proyecto = get_element(driver, 
                By.XPATH, '/html/body/div/div/div/section[2]/div/div/div/div[1]/div[1]/div[2]/a')

            boton_crear_Proyecto.click()

            titulo = get_element(driver, By.ID, 'name')
            titulo.send_keys(self._get_nuevo_titulo())

            descripcion = get_element(driver, By.XPATH,
                                      '/html/body/div/div/div/section[2]/div/div/div/form/div[1]/div/div/div[2]/div/textarea')
            descripcion.send_keys('ESte es un nuevo proyecto')


            boton_ver = get_element(driver, By.XPATH,
                                    '//*[@id="app"]/section[2]/div/div/div/form/div[2]/div[2]/label[3]/div')
            boton_ver.click()

            boton_enviar = get_element(driver, By.XPATH,
                                       '//*[@id="app"]/section[2]/div/div/div/form/div[2]/div[2]/div[1]/button')
            boton_enviar.click()

            boton_eliminar = get_element(driver, By.XPATH,
                                         '/html/body/div/div/div/section[2]/div/div/div/div[1]/div/div[1]/div/div[1]/a')
            boton_eliminar.click()

            time.sleep(2)

            boton_confirmar = get_element(driver, By.XPATH,
                                          '/html/body/div[2]/div/div[3]/button[1]')
            boton_confirmar.click()

            time.sleep(2)

            proyecto_eliminar_satiscactorio = get_element(driver, By.XPATH,
                                                          '//*[@id="swal2-title"]')
            self.assertIsNotNone(proyecto_eliminar_satiscactorio)
            self.assertIn('¡ Eliminación exitosa !',
                          proyecto_eliminar_satiscactorio.text)

            boton_confirmar_ok = get_element(driver, By.XPATH,
                                             '/html/body/div[2]/div/div[3]/button[1]')
            boton_confirmar_ok.click()

        except Exception:
            driver.save_screenshot(
                'screenshots/test04_eliminar_proyecto.png')
            raise

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
