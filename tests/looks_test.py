import os
from dotenv import load_dotenv
from data.data_generator import folder_random_data
from pages.login_page import LoginPage
from pages.looks_page import LooksPage
from data.data_types import DataTypes as DT

load_dotenv()
url = os.getenv('TEST_URL')
email = os.getenv('TEST_EMAIL')
password = os.getenv('TEST_PASSWORD')

class TestLooksPage:
    def test_folder_created_smoke(self, driver):
        # Pre-condition: Login
        data = folder_random_data(10, DT.TYPES['cyrillic'] + DT.TYPES['latin'], 15, DT.TYPES['latin'])
        login_page = LoginPage(driver, url)
        login_page.open()
        login_page.submit_login(email,password)

        # Create folder
        looks_page = LooksPage(driver, url)
        assert looks_page.if_folder_exists(data, driver) == False, 'the folder already exists, please delete the folder'
        looks_page.new_folder_button()
        looks_page.create_folder(data)

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Checking created folder
        assert looks_page.if_folder_exists(data, driver), 'the folder cannot be created'

        # Post-condition: Delete folder
        looks_page.delete_folder(data, driver)

    def test_delete_folder_smoke(self, driver):
        # Precondition: Login, Create folder
        data = folder_random_data(10, DT.TYPES['cyrillic'] + DT.TYPES['latin'], 15, DT.TYPES['latin'])
        login_page = LoginPage(driver, url)
        login_page.open()
        login_page.submit_login(email, password)
        looks_page = LooksPage(driver, url)
        assert looks_page.if_folder_exists(data, driver) == False, 'the folder already exists, please delete the folder'
        looks_page.new_folder_button()
        looks_page.create_folder(data)

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Delete folder
        looks_page.delete_folder(data, driver)
        assert looks_page.if_folder_exists(data, driver), 'the folder is not deleted'




