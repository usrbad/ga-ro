import os
from pages.login_page import LoginPage
from dotenv import load_dotenv

class TestLoginPage:

    def test_login_successful(self, driver):
        load_dotenv()
        url = os.getenv('TEST_URL')
        email = os.getenv('TEST_EMAIL')
        password = os.getenv('TEST_PASSWORD')

        login_page = LoginPage(driver, url)
        login_page.open()
        login_page.submit_login(email, password)
        assert driver.current_url == url + 'looks/'

