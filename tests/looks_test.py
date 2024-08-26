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

class TestFoldersSmoke:
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
        looks_page.fill_folder_fields(data)
        assert looks_page.get_folder_name_in_form(data) == data['name'], 'name of the folder is different'
        looks_page.save_folder_button()

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
        looks_page.fill_folder_fields(data)
        assert looks_page.get_folder_name_in_form(data) == data['name'], 'name of the folder is different'
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Delete folder
        looks_page.delete_folder(data, driver)
        assert looks_page.if_folder_exists(data, driver), 'the folder is not deleted'

class TestFoldersRegressionNameLength:
    def test_folder_created_name_1_symbol(self, driver):
        # Pre-condition: Login
        data = folder_random_data(1, DT.TYPES['cyrillic'] + DT.TYPES['latin'], 0, DT.TYPES['latin'])
        login_page = LoginPage(driver, url)
        login_page.open()
        login_page.submit_login(email, password)

        # Create folder
        looks_page = LooksPage(driver, url)
        assert looks_page.if_folder_exists(data, driver) == False, 'the folder with this name already exists, please delete the folder'
        looks_page.new_folder_button()
        looks_page.fill_folder_fields(data)
        assert looks_page.get_folder_name_in_form(data) == data['name'], 'name of the folder is different'
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Checking created folder
        assert looks_page.if_folder_exists(data, driver), 'the folder cannot be created'

        # Post-condition: Delete folder
        looks_page.delete_folder(data, driver)

    def test_folder_created_name_2_symbols(self, driver):
        # Pre-condition: Login
        data = folder_random_data(2, DT.TYPES['cyrillic'] + DT.TYPES['latin'], 0, DT.TYPES['latin'])
        login_page = LoginPage(driver, url)
        login_page.open()
        login_page.submit_login(email, password)

        # Create folder
        looks_page = LooksPage(driver, url)
        assert looks_page.if_folder_exists(data, driver) == False, 'the folder with this name already exists, please delete the folder'
        looks_page.new_folder_button()
        looks_page.fill_folder_fields(data)
        assert looks_page.get_folder_name_in_form(data) == data['name'], 'name of the folder is different'
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Checking created folder
        assert looks_page.if_folder_exists(data, driver), 'the folder cannot be created'

        # Post-condition: Delete folder
        looks_page.delete_folder(data, driver)

    def test_folder_created_name_10_symbols(self, driver):
            # Pre-condition: Login
            data = folder_random_data(10, DT.TYPES['cyrillic'] + DT.TYPES['latin'], 0, DT.TYPES['latin'])
            login_page = LoginPage(driver, url)
            login_page.open()
            login_page.submit_login(email, password)

            # Create folder
            looks_page = LooksPage(driver, url)
            assert looks_page.if_folder_exists(data, driver) == False, 'the folder with this name already exists, please delete the folder'
            looks_page.new_folder_button()
            looks_page.fill_folder_fields(data)
            assert looks_page.get_folder_name_in_form(data) == data['name'], 'name of the folder is different'
            looks_page.save_folder_button()

            # Delete cookies and login again for checking
            driver.delete_all_cookies()
            login_page.open()
            login_page.submit_login(email, password)

            # Checking created folder
            assert looks_page.if_folder_exists(data, driver), 'the folder cannot be created'

            # Post-condition: Delete folder
            looks_page.delete_folder(data, driver)

    def test_folder_created_name_31_symbols(self, driver):
            # Pre-condition: Login
            data = folder_random_data(31, DT.TYPES['cyrillic'] + DT.TYPES['latin'], 0, DT.TYPES['latin'])
            login_page = LoginPage(driver, url)
            login_page.open()
            login_page.submit_login(email, password)

            # Create folder
            looks_page = LooksPage(driver, url)
            assert looks_page.if_folder_exists(data, driver) == False, 'the folder with this name already exists, please delete the folder'
            looks_page.new_folder_button()
            looks_page.fill_folder_fields(data)
            assert looks_page.get_folder_name_in_form(data) == data['name'], 'name of the folder is different'
            looks_page.save_folder_button()

            # Delete cookies and login again for checking
            driver.delete_all_cookies()
            login_page.open()
            login_page.submit_login(email, password)

            # Checking created folder
            assert looks_page.if_folder_exists(data, driver), 'the folder cannot be created'

            # Post-condition: Delete folder
            looks_page.delete_folder(data, driver)

    def test_folder_created_name_32_symbols(self, driver):
            # Pre-condition: Login
            data = folder_random_data(32, DT.TYPES['cyrillic'] + DT.TYPES['latin'], 0, DT.TYPES['latin'])
            login_page = LoginPage(driver, url)
            login_page.open()
            login_page.submit_login(email, password)

            # Create folder
            looks_page = LooksPage(driver, url)
            assert looks_page.if_folder_exists(data, driver) == False, 'the folder with this name already exists, please delete the folder'
            looks_page.new_folder_button()
            looks_page.fill_folder_fields(data)
            assert looks_page.get_folder_name_in_form(data) == data['name'], 'name of the folder is different'
            looks_page.save_folder_button()

            # Delete cookies and login again for checking
            driver.delete_all_cookies()
            login_page.open()
            login_page.submit_login(email, password)

            # Checking created folder
            assert looks_page.if_folder_exists(data, driver), 'the folder cannot be created'

            # Post-condition: Delete folder
            looks_page.delete_folder(data, driver)

    def test_folder_not_created_name_33_symbols(self, driver):
            # Pre-condition: Login
            data = folder_random_data(33, DT.TYPES['cyrillic'] + DT.TYPES['latin'], 0, DT.TYPES['latin'])
            login_page = LoginPage(driver, url)
            login_page.open()
            login_page.submit_login(email, password)

            # Create folder
            looks_page = LooksPage(driver, url)
            assert looks_page.if_folder_exists(data, driver) == False, 'the folder with this name already exists, please delete the folder'
            looks_page.new_folder_button()
            looks_page.fill_folder_fields(data)
            assert len(looks_page.get_folder_name_in_form(data)) == 32, 'name of the folder is more than 32 symbols'

class TestFoldersRegressionUserIDLength:
    def test_folder_created_user_id_0_symbols(self, driver):
            # Pre-condition: Login
            data = folder_random_data(10, DT.TYPES['cyrillic'] + DT.TYPES['latin'], 0, DT.TYPES['latin'])
            login_page = LoginPage(driver, url)
            login_page.open()
            login_page.submit_login(email, password)

            # Create folder
            looks_page = LooksPage(driver, url)
            assert looks_page.if_folder_exists(data, driver) == False, 'the folder with this name already exists, please delete the folder'
            looks_page.new_folder_button()
            looks_page.fill_folder_fields(data)
            assert looks_page.get_folder_user_id_in_form(data) == data['user_id'], 'user_id of the folder is different'
            looks_page.save_folder_button()

            # Delete cookies and login again for checking
            driver.delete_all_cookies()
            login_page.open()
            login_page.submit_login(email, password)

            # Checking created folder
            assert looks_page.if_folder_exists(data, driver), 'the folder cannot be created'

            # Post-condition: Delete folder
            looks_page.delete_folder(data, driver)

    def test_folder_created_user_id_1_symbol(self, driver):
                # Pre-condition: Login
                data = folder_random_data(10, DT.TYPES['cyrillic'] + DT.TYPES['latin'], 1, DT.TYPES['latin'])
                login_page = LoginPage(driver, url)
                login_page.open()
                login_page.submit_login(email, password)

                # Create folder
                looks_page = LooksPage(driver, url)
                assert looks_page.if_folder_exists(data, driver) == False, 'the folder with this name already exists, please delete the folder'
                looks_page.new_folder_button()
                looks_page.fill_folder_fields(data)
                assert looks_page.get_folder_user_id_in_form(data) == data['user_id'], 'user_id of the folder is different'
                looks_page.save_folder_button()

                # Delete cookies and login again for checking
                driver.delete_all_cookies()
                login_page.open()
                login_page.submit_login(email, password)

                # Checking created folder
                assert looks_page.if_folder_exists(data, driver), 'the folder cannot be created'

                # Post-condition: Delete folder
                looks_page.delete_folder(data, driver)

    def test_folder_created_user_id_10_symbols(self, driver):
                    # Pre-condition: Login
                    data = folder_random_data(10, DT.TYPES['cyrillic'] + DT.TYPES['latin'], 10, DT.TYPES['latin'])
                    login_page = LoginPage(driver, url)
                    login_page.open()
                    login_page.submit_login(email, password)

                    # Create folder
                    looks_page = LooksPage(driver, url)
                    assert looks_page.if_folder_exists(data, driver) == False, 'the folder with this name already exists, please delete the folder'
                    looks_page.new_folder_button()
                    looks_page.fill_folder_fields(data)
                    assert looks_page.get_folder_user_id_in_form(data) == data['user_id'], 'user_id of the folder is different'
                    looks_page.save_folder_button()

                    # Delete cookies and login again for checking
                    driver.delete_all_cookies()
                    login_page.open()
                    login_page.submit_login(email, password)

                    # Checking created folder
                    assert looks_page.if_folder_exists(data, driver), 'the folder cannot be created'

                    # Post-condition: Delete folder
                    looks_page.delete_folder(data, driver)

    def test_folder_created_user_id_31_symbols(self, driver):
                    # Pre-condition: Login
                    data = folder_random_data(10, DT.TYPES['cyrillic'] + DT.TYPES['latin'], 31, DT.TYPES['latin'])
                    login_page = LoginPage(driver, url)
                    login_page.open()
                    login_page.submit_login(email, password)

                    # Create folder
                    looks_page = LooksPage(driver, url)
                    assert looks_page.if_folder_exists(data, driver) == False, 'the folder with this name already exists, please delete the folder'
                    looks_page.new_folder_button()
                    looks_page.fill_folder_fields(data)
                    assert looks_page.get_folder_user_id_in_form(data) == data['user_id'], 'user_id of the folder is different'
                    looks_page.save_folder_button()

                    # Delete cookies and login again for checking
                    driver.delete_all_cookies()
                    login_page.open()
                    login_page.submit_login(email, password)

                    # Checking created folder
                    assert looks_page.if_folder_exists(data, driver), 'the folder cannot be created'

                    # Post-condition: Delete folder
                    looks_page.delete_folder(data, driver)

    def test_folder_created_user_id_32_symbols(self, driver):
                    # Pre-condition: Login
                    data = folder_random_data(10, DT.TYPES['cyrillic'] + DT.TYPES['latin'], 32, DT.TYPES['latin'])
                    login_page = LoginPage(driver, url)
                    login_page.open()
                    login_page.submit_login(email, password)

                    # Create folder
                    looks_page = LooksPage(driver, url)
                    assert looks_page.if_folder_exists(data, driver) == False, 'the folder with this name already exists, please delete the folder'
                    looks_page.new_folder_button()
                    looks_page.fill_folder_fields(data)
                    assert looks_page.get_folder_user_id_in_form(data) == data['user_id'], 'user_id of the folder is different'
                    looks_page.save_folder_button()

                    # Delete cookies and login again for checking
                    driver.delete_all_cookies()
                    login_page.open()
                    login_page.submit_login(email, password)

                    # Checking created folder
                    assert looks_page.if_folder_exists(data, driver), 'the folder cannot be created'

                    # Post-condition: Delete folder
                    looks_page.delete_folder(data, driver)

    def test_folder_not_created_user_id_33_symbols(self, driver):
                    # Pre-condition: Login
                    data = folder_random_data(10, DT.TYPES['cyrillic'] + DT.TYPES['latin'], 33, DT.TYPES['latin'])
                    login_page = LoginPage(driver, url)
                    login_page.open()
                    login_page.submit_login(email, password)

                    # Create folder
                    looks_page = LooksPage(driver, url)
                    assert looks_page.if_folder_exists(data, driver) == False, 'the folder with this name already exists, please delete the folder'
                    looks_page.new_folder_button()
                    looks_page.fill_folder_fields(data)
                    assert len(looks_page.get_folder_user_id_in_form(data)) == 32, 'user_id of the folder is more than 32 symbols'

class TestFoldersRegressionNameUserIDSymbols:
    def test_folder_created_name_latin_user_id_latin(self, driver):
                # Pre-condition: Login
                data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['latin'])
                login_page = LoginPage(driver, url)
                login_page.open()
                login_page.submit_login(email, password)

                # Create folder
                looks_page = LooksPage(driver, url)
                assert looks_page.if_folder_exists(data, driver) == False, 'the folder with this name already exists, please delete the folder'
                looks_page.new_folder_button()
                looks_page.fill_folder_fields(data)
                assert looks_page.get_folder_user_id_in_form(data) == data['user_id'], 'user_id of the folder is different'
                looks_page.save_folder_button()

                # Delete cookies and login again for checking
                driver.delete_all_cookies()
                login_page.open()
                login_page.submit_login(email, password)

                # Checking created folder
                assert looks_page.if_folder_exists(data, driver), 'the folder cannot be created'

                # Post-condition: Delete folder
                looks_page.delete_folder(data, driver)

    def test_folder_created_name_latin_user_id_cyrillic(self, driver):
                # Pre-condition: Login
                data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['cyrillic'])
                login_page = LoginPage(driver, url)
                login_page.open()
                login_page.submit_login(email, password)

                # Create folder
                looks_page = LooksPage(driver, url)
                assert looks_page.if_folder_exists(data, driver) == False, 'the folder with this name already exists, please delete the folder'
                looks_page.new_folder_button()
                looks_page.fill_folder_fields(data)
                assert looks_page.get_folder_user_id_in_form(data) == data['user_id'], 'user_id of the folder is different'
                looks_page.save_folder_button()

                # Delete cookies and login again for checking
                driver.delete_all_cookies()
                login_page.open()
                login_page.submit_login(email, password)

                # Checking created folder
                assert looks_page.if_folder_exists(data, driver), 'the folder cannot be created'

                # Post-condition: Delete folder
                looks_page.delete_folder(data, driver)

    def test_folder_created_name_latin_user_id_digits(self, driver):
                # Pre-condition: Login
                data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['digits'])
                login_page = LoginPage(driver, url)
                login_page.open()
                login_page.submit_login(email, password)

                # Create folder
                looks_page = LooksPage(driver, url)
                assert looks_page.if_folder_exists(data, driver) == False, 'the folder with this name already exists, please delete the folder'
                looks_page.new_folder_button()
                looks_page.fill_folder_fields(data)
                assert looks_page.get_folder_user_id_in_form(data) == data['user_id'], 'user_id of the folder is different'
                looks_page.save_folder_button()

                # Delete cookies and login again for checking
                driver.delete_all_cookies()
                login_page.open()
                login_page.submit_login(email, password)

                # Checking created folder
                assert looks_page.if_folder_exists(data, driver), 'the folder cannot be created'

                # Post-condition: Delete folder
                looks_page.delete_folder(data, driver)

    def test_folder_created_name_latin_user_id_spec(self, driver):
                # Pre-condition: Login
                data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['spec'])
                login_page = LoginPage(driver, url)
                login_page.open()
                login_page.submit_login(email, password)

                # Create folder
                looks_page = LooksPage(driver, url)
                assert looks_page.if_folder_exists(data, driver) == False, 'the folder with this name already exists, please delete the folder'
                looks_page.new_folder_button()
                looks_page.fill_folder_fields(data)
                assert looks_page.get_folder_user_id_in_form(data) == data['user_id'], 'user_id of the folder is different'
                looks_page.save_folder_button()

                # Delete cookies and login again for checking
                driver.delete_all_cookies()
                login_page.open()
                login_page.submit_login(email, password)

                # Checking created folder
                assert looks_page.if_folder_exists(data, driver), 'the folder cannot be created'

                # Post-condition: Delete folder
                looks_page.delete_folder(data, driver)

    def test_folder_created_name_cyrillic_user_id_cyrillic(self, driver):
                # Pre-condition: Login
                data = folder_random_data(10, DT.TYPES['cyrillic'], 10, DT.TYPES['cyrillic'])
                login_page = LoginPage(driver, url)
                login_page.open()
                login_page.submit_login(email, password)

                # Create folder
                looks_page = LooksPage(driver, url)
                assert looks_page.if_folder_exists(data, driver) == False, 'the folder with this name already exists, please delete the folder'
                looks_page.new_folder_button()
                looks_page.fill_folder_fields(data)
                assert looks_page.get_folder_user_id_in_form(data) == data['user_id'], 'user_id of the folder is different'
                looks_page.save_folder_button()

                # Delete cookies and login again for checking
                driver.delete_all_cookies()
                login_page.open()
                login_page.submit_login(email, password)

                # Checking created folder
                assert looks_page.if_folder_exists(data, driver), 'the folder cannot be created'

                # Post-condition: Delete folder
                looks_page.delete_folder(data, driver)

    def test_folder_created_name_cyrillic_user_id_digits(self, driver):
                # Pre-condition: Login
                data = folder_random_data(10, DT.TYPES['cyrillic'], 10, DT.TYPES['digits'])
                login_page = LoginPage(driver, url)
                login_page.open()
                login_page.submit_login(email, password)

                # Create folder
                looks_page = LooksPage(driver, url)
                assert looks_page.if_folder_exists(data, driver) == False, 'the folder with this name already exists, please delete the folder'
                looks_page.new_folder_button()
                looks_page.fill_folder_fields(data)
                assert looks_page.get_folder_user_id_in_form(data) == data['user_id'], 'user_id of the folder is different'
                looks_page.save_folder_button()

                # Delete cookies and login again for checking
                driver.delete_all_cookies()
                login_page.open()
                login_page.submit_login(email, password)

                # Checking created folder
                assert looks_page.if_folder_exists(data, driver), 'the folder cannot be created'

                # Post-condition: Delete folder
                looks_page.delete_folder(data, driver)

    def test_folder_created_name_cyrillic_user_id_spec(self, driver):
                # Pre-condition: Login
                data = folder_random_data(10, DT.TYPES['cyrillic'], 10, DT.TYPES['spec'])
                login_page = LoginPage(driver, url)
                login_page.open()
                login_page.submit_login(email, password)

                # Create folder
                looks_page = LooksPage(driver, url)
                assert looks_page.if_folder_exists(data, driver) == False, 'the folder with this name already exists, please delete the folder'
                looks_page.new_folder_button()
                looks_page.fill_folder_fields(data)
                assert looks_page.get_folder_user_id_in_form(data) == data['user_id'], 'user_id of the folder is different'
                looks_page.save_folder_button()

                # Delete cookies and login again for checking
                driver.delete_all_cookies()
                login_page.open()
                login_page.submit_login(email, password)

                # Checking created folder
                assert looks_page.if_folder_exists(data, driver), 'the folder cannot be created'

                # Post-condition: Delete folder
                looks_page.delete_folder(data, driver)

    def test_folder_created_name_cyrillic_user_id_latin(self, driver):
                # Pre-condition: Login
                data = folder_random_data(10, DT.TYPES['cyrillic'], 10, DT.TYPES['latin'])
                login_page = LoginPage(driver, url)
                login_page.open()
                login_page.submit_login(email, password)

                # Create folder
                looks_page = LooksPage(driver, url)
                assert looks_page.if_folder_exists(data, driver) == False, 'the folder with this name already exists, please delete the folder'
                looks_page.new_folder_button()
                looks_page.fill_folder_fields(data)
                assert looks_page.get_folder_user_id_in_form(data) == data['user_id'], 'user_id of the folder is different'
                looks_page.save_folder_button()

                # Delete cookies and login again for checking
                driver.delete_all_cookies()
                login_page.open()
                login_page.submit_login(email, password)

                # Checking created folder
                assert looks_page.if_folder_exists(data, driver), 'the folder cannot be created'

                # Post-condition: Delete folder
                looks_page.delete_folder(data, driver)

    def test_folder_created_name_digits_user_id_digits(self, driver):
                # Pre-condition: Login
                data = folder_random_data(10, DT.TYPES['digits'], 10, DT.TYPES['digits'])
                login_page = LoginPage(driver, url)
                login_page.open()
                login_page.submit_login(email, password)

                # Create folder
                looks_page = LooksPage(driver, url)
                assert looks_page.if_folder_exists(data, driver) == False, 'the folder with this name already exists, please delete the folder'
                looks_page.new_folder_button()
                looks_page.fill_folder_fields(data)
                assert looks_page.get_folder_user_id_in_form(data) == data['user_id'], 'user_id of the folder is different'
                looks_page.save_folder_button()

                # Delete cookies and login again for checking
                driver.delete_all_cookies()
                login_page.open()
                login_page.submit_login(email, password)

                # Checking created folder
                assert looks_page.if_folder_exists(data, driver), 'the folder cannot be created'

                # Post-condition: Delete folder
                looks_page.delete_folder(data, driver)

    def test_folder_created_name_digits_user_id_spec(self, driver):
                # Pre-condition: Login
                data = folder_random_data(10, DT.TYPES['digits'], 10, DT.TYPES['spec'])
                login_page = LoginPage(driver, url)
                login_page.open()
                login_page.submit_login(email, password)

                # Create folder
                looks_page = LooksPage(driver, url)
                assert looks_page.if_folder_exists(data, driver) == False, 'the folder with this name already exists, please delete the folder'
                looks_page.new_folder_button()
                looks_page.fill_folder_fields(data)
                assert looks_page.get_folder_user_id_in_form(data) == data['user_id'], 'user_id of the folder is different'
                looks_page.save_folder_button()

                # Delete cookies and login again for checking
                driver.delete_all_cookies()
                login_page.open()
                login_page.submit_login(email, password)

                # Checking created folder
                assert looks_page.if_folder_exists(data, driver), 'the folder cannot be created'

                # Post-condition: Delete folder
                looks_page.delete_folder(data, driver)

    def test_folder_created_name_digits_user_id_latin(self, driver):
                # Pre-condition: Login
                data = folder_random_data(10, DT.TYPES['digits'], 10, DT.TYPES['latin'])
                login_page = LoginPage(driver, url)
                login_page.open()
                login_page.submit_login(email, password)

                # Create folder
                looks_page = LooksPage(driver, url)
                assert looks_page.if_folder_exists(data, driver) == False, 'the folder with this name already exists, please delete the folder'
                looks_page.new_folder_button()
                looks_page.fill_folder_fields(data)
                assert looks_page.get_folder_user_id_in_form(data) == data['user_id'], 'user_id of the folder is different'
                looks_page.save_folder_button()

                # Delete cookies and login again for checking
                driver.delete_all_cookies()
                login_page.open()
                login_page.submit_login(email, password)

                # Checking created folder
                assert looks_page.if_folder_exists(data, driver), 'the folder cannot be created'

                # Post-condition: Delete folder
                looks_page.delete_folder(data, driver)

    def test_folder_created_name_digits_user_id_cyrillic(self, driver):
                # Pre-condition: Login
                data = folder_random_data(10, DT.TYPES['digits'], 10, DT.TYPES['cyrillic'])
                login_page = LoginPage(driver, url)
                login_page.open()
                login_page.submit_login(email, password)

                # Create folder
                looks_page = LooksPage(driver, url)
                assert looks_page.if_folder_exists(data, driver) == False, 'the folder with this name already exists, please delete the folder'
                looks_page.new_folder_button()
                looks_page.fill_folder_fields(data)
                assert looks_page.get_folder_user_id_in_form(data) == data['user_id'], 'user_id of the folder is different'
                looks_page.save_folder_button()

                # Delete cookies and login again for checking
                driver.delete_all_cookies()
                login_page.open()
                login_page.submit_login(email, password)

                # Checking created folder
                assert looks_page.if_folder_exists(data, driver), 'the folder cannot be created'

                # Post-condition: Delete folder
                looks_page.delete_folder(data, driver)

    def test_folder_created_name_spec_user_id_spec(self, driver):
                # Pre-condition: Login
                data = folder_random_data(10, DT.TYPES['spec'], 10, DT.TYPES['spec'])
                login_page = LoginPage(driver, url)
                login_page.open()
                login_page.submit_login(email, password)

                # Create folder
                looks_page = LooksPage(driver, url)
                assert looks_page.if_folder_exists(data, driver) == False, 'the folder with this name already exists, please delete the folder'
                looks_page.new_folder_button()
                looks_page.fill_folder_fields(data)
                assert looks_page.get_folder_user_id_in_form(data) == data['user_id'], 'user_id of the folder is different'
                looks_page.save_folder_button()

                # Delete cookies and login again for checking
                driver.delete_all_cookies()
                login_page.open()
                login_page.submit_login(email, password)

                # Checking created folder
                assert looks_page.if_folder_exists(data, driver), 'the folder cannot be created'

                # Post-condition: Delete folder
                looks_page.delete_folder(data, driver)

    def test_folder_created_name_spec_user_id_latin(self, driver):
                # Pre-condition: Login
                data = folder_random_data(10, DT.TYPES['spec'], 10, DT.TYPES['latin'])
                login_page = LoginPage(driver, url)
                login_page.open()
                login_page.submit_login(email, password)

                # Create folder
                looks_page = LooksPage(driver, url)
                assert looks_page.if_folder_exists(data, driver) == False, 'the folder with this name already exists, please delete the folder'
                looks_page.new_folder_button()
                looks_page.fill_folder_fields(data)
                assert looks_page.get_folder_user_id_in_form(data) == data['user_id'], 'user_id of the folder is different'
                looks_page.save_folder_button()

                # Delete cookies and login again for checking
                driver.delete_all_cookies()
                login_page.open()
                login_page.submit_login(email, password)

                # Checking created folder
                assert looks_page.if_folder_exists(data, driver), 'the folder cannot be created'

                # Post-condition: Delete folder
                looks_page.delete_folder(data, driver)

    def test_folder_created_name_spec_user_id_cyrillic(self, driver):
                # Pre-condition: Login
                data = folder_random_data(10, DT.TYPES['spec'], 10, DT.TYPES['cyrillic'])
                login_page = LoginPage(driver, url)
                login_page.open()
                login_page.submit_login(email, password)

                # Create folder
                looks_page = LooksPage(driver, url)
                assert looks_page.if_folder_exists(data, driver) == False, 'the folder with this name already exists, please delete the folder'
                looks_page.new_folder_button()
                looks_page.fill_folder_fields(data)
                assert looks_page.get_folder_user_id_in_form(data) == data['user_id'], 'user_id of the folder is different'
                looks_page.save_folder_button()

                # Delete cookies and login again for checking
                driver.delete_all_cookies()
                login_page.open()
                login_page.submit_login(email, password)

                # Checking created folder
                assert looks_page.if_folder_exists(data, driver), 'the folder cannot be created'

                # Post-condition: Delete folder
                looks_page.delete_folder(data, driver)

    def test_folder_created_name_spec_user_id_digits(self, driver):
                # Pre-condition: Login
                data = folder_random_data(10, DT.TYPES['spec'], 10, DT.TYPES['digits'])
                login_page = LoginPage(driver, url)
                login_page.open()
                login_page.submit_login(email, password)

                # Create folder
                looks_page = LooksPage(driver, url)
                assert looks_page.if_folder_exists(data, driver) == False, 'the folder with this name already exists, please delete the folder'
                looks_page.new_folder_button()
                looks_page.fill_folder_fields(data)
                assert looks_page.get_folder_user_id_in_form(data) == data['user_id'], 'user_id of the folder is different'
                looks_page.save_folder_button()

                # Delete cookies and login again for checking
                driver.delete_all_cookies()
                login_page.open()
                login_page.submit_login(email, password)

                # Checking created folder
                assert looks_page.if_folder_exists(data, driver), 'the folder cannot be created'

                # Post-condition: Delete folder
                looks_page.delete_folder(data, driver)

