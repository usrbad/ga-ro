from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL = (By.XPATH, '//*[@id="id_username"]')
    PASSWORD = (By.XPATH, '//*[@id="id_password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@class="btn btn-primary btn-block"]')