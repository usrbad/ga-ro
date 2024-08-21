import os
from dotenv import load_dotenv
from pages.login_page import LoginPage

class TestLooksPage:

    def test_folder_created(self, driver):
        load_dotenv()
        url = os.getenv('TEST_URL')
        email = os.getenv('TEST_EMAIL')
        password = os.getenv('TEST_PASSWORD')

        login_page = LoginPage(driver, url)
        login_page.open()
        login_page.submit_login(email,password)
        # TODO: create folder


