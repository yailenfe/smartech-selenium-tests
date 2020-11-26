from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login(driver):
    username = driver.find_element_by_name('username')
    username.send_keys('admin')
    password = driver.find_element_by_name('password')
    password.send_keys('admin')

    boton_login = driver.find_element_by_xpath(
        '/html/body/div/div[2]/form/div[3]/div[2]/button')
    boton_login.click()


def get_element(driver, by, value):
    return WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((by, value)))
