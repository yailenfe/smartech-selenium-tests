import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from commons import get_element

url = 'http://designing-solutions-smartech.herokuapp.com/'


class SmartechTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')
        self.driver = webdriver.Chrome(
            executable_path='./chromedriver', options=options)

    def test01_cargo_pagina(self):
        try:
            driver = self.driver
            driver.get(url)
            self.assertIn('SmartTech', driver.title)
        except Exception:
            driver.save_screenshot(
                'screenshots/test02_login_incorrecto_username.png')
            raise

    def test07_login_correcto(self):
        try:
            driver = self.driver
            driver.get(url)
            username = get_element(driver, By.NAME, 'username')
            username.send_keys('admin')
            password = get_element(driver, By.NAME, 'password')
            password.send_keys('admin')

            boton_login = get_element(driver, By.XPATH,
                                           '/html/body/div/div[2]/form/div[3]/div[2]/button')
            boton_login.click()

            user_mensaje = get_element(driver, By.CLASS_NAME, 'user-panel')
            self.assertIsNotNone(user_mensaje)
            

        except Exception:
            driver.save_screenshot(
                'screenshots/test07_login_correcto_username.png')
            raise

    def test02_login_incorrecto_username(self):
        try:
            driver = self.driver
            driver.get(url)
            username = get_element(driver, By.NAME, 'username')
            username.send_keys('algo')
            password = get_element(driver, By.NAME, 'password')
            password.send_keys('admin')

            boton_login = get_element(driver, By.XPATH,
                                           '/html/body/div/div[2]/form/div[3]/div[2]/button')
            boton_login.click()

            user_error_mensaje = get_element(driver, By.CLASS_NAME,
                                                  'control-label')
            self.assertIsNotNone(user_error_mensaje)
            self.assertIn(
                'These credentials do not match our records.', user_error_mensaje.text)
        except Exception:
            driver.save_screenshot(
                'screenshots/test02_login_incorrecto_username.png')
            raise

    def test03_login_Incorrecto_password(self):
        try:

            driver = self.driver
            driver.get(url)
            username = get_element(driver, By.NAME, 'username')
            username.send_keys('admin')
            password = get_element(driver, By.NAME, 'password')
            password.send_keys('algo')

            boton_login = get_element(driver, By.XPATH,
                                           '/html/body/div/div[2]/form/div[3]/div[2]/button')
            boton_login.click()

            user_error_mensaje = get_element(driver, By.CLASS_NAME,
                                                  'control-label')
            self.assertIsNotNone(user_error_mensaje)
        

        except Exception:
            driver.save_screenshot(
                'screenshots/test03_login_incorrecto_password.png')
            raise

    def test04_login_campo_obligatorio(self):
        try:

            driver = self.driver
            driver.get(url)
            username = get_element(driver, By.NAME, 'username')
            username.send_keys('')
            password = get_element(driver, By.NAME, 'password')
            password.send_keys('')

            boton_login = get_element(driver, By.XPATH,
                                           '/html/body/div/div[2]/form/div[3]/div[2]/button')
            boton_login.click()
            user_error_mensaje = get_element(driver, By.CLASS_NAME,
                                                  'control-label')
            self.assertIsNotNone(user_error_mensaje)
            self.assertIn('The field username is required.',
                          user_error_mensaje.text)

        except Exception:
            driver.save_screenshot(
                'screenshots/test04_login_campo_obligatorio.png')
            raise

    def test05_login_campo_username_vacio(self):
        try:

            driver = self.driver
            driver.get(url)
            username = get_element(driver, By.NAME, 'username')
            username.send_keys('')
            password = get_element(driver, By.NAME, 'password')
            password.send_keys('admin')

            boton_login = get_element(driver, By.XPATH,
                                           '/html/body/div/div[2]/form/div[3]/div[2]/button')
            boton_login.click()
            user_error_mensaje = get_element(driver, By.CLASS_NAME,
                                                  'control-label')
            self.assertIsNotNone(user_error_mensaje)
            self.assertIn('The field username is required.',
                          user_error_mensaje.text)

        except Exception:
            driver.save_screenshot('screenshots/test05_login_campo_username_vacio.png')
            raise

    def test06_login_campo_password_vacio(self):
        try:

            driver = self.driver
            driver.get(url)
            username = get_element(driver, By.NAME, 'username')
            username.send_keys('admin')
            password = get_element(driver, By.NAME, 'password')
            password.send_keys('')

            boton_login = get_element(driver, By.XPATH,
                                           '/html/body/div/div[2]/form/div[3]/div[2]/button')
            boton_login.click()
            user_error_mensaje = get_element(driver, By.CLASS_NAME,
                                                  'control-label')
            self.assertIsNotNone(user_error_mensaje)
        

        except Exception:
            driver.save_screenshot(
                'screenshots/test06_login_campo_password_vacio.png')
            raise

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
