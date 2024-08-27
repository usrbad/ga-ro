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

class TestFoldersCreationSmoke:
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
        assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Checking created folder
        assert looks_page.if_folder_exists(data, driver), 'the folder cannot be created'

        # Post-condition: Delete folder
        looks_page.delete_folder(data, driver)

    def test_folder_created_with_only_name(self, driver):
        # Pre-condition: Login
        data = folder_random_data(10, DT.TYPES['cyrillic'] + DT.TYPES['latin'], 15, DT.TYPES['latin'])
        login_page = LoginPage(driver, url)
        login_page.open()
        login_page.submit_login(email, password)

        # Create folder
        looks_page = LooksPage(driver, url)
        assert looks_page.if_folder_exists(data, driver) == False, 'the folder already exists, please delete the folder'
        looks_page.new_folder_button()
        looks_page.fill_only_name(data)
        assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Checking created folder
        assert looks_page.if_folder_exists(data, driver), 'the folder cannot be created'

        # Post-condition: Delete folder
        looks_page.delete_folder(data, driver)

    def test_cant_save_folder_with_empty_fields(self, driver):
        # Pre-condition: Login
        login_page = LoginPage(driver, url)
        login_page.open()
        login_page.submit_login(email, password)

        # Open popup and test
        looks_page = LooksPage(driver, url)
        looks_page.new_folder_button()
        looks_page.save_folder_button()
        assert looks_page.is_popup_new_folder_visible().get_attribute('style') == 'visibility: visible;', 'the popup closed by save button with empty fields'

    def test_cant_create_folder_with_duplicate_name(self, driver):
        # Pre-condition: Login
        data = folder_random_data(10, DT.TYPES['cyrillic'] + DT.TYPES['latin'], 15, DT.TYPES['latin'])
        login_page = LoginPage(driver, url)
        login_page.open()
        login_page.submit_login(email, password)

        # Create folder 1
        looks_page = LooksPage(driver, url)
        looks_page.new_folder_button()
        looks_page.fill_only_name(data)
        assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Create folder 2
        looks_page.new_folder_button()
        looks_page.fill_only_name(data)
        assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
        looks_page.save_folder_button()

        # Checking that popup is still on the screen
        assert looks_page.is_popup_new_folder_visible().get_attribute('style') == 'visibility: visible;', 'the folder created with duplicate name'

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
        assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Delete folder
        looks_page.delete_folder(data, driver)
        assert looks_page.if_folder_exists(data, driver), 'the folder is not deleted'

    def test_cancel_button_folder_creation(self, driver):
        # Precondition: Login
        data = folder_random_data(10, DT.TYPES['cyrillic'] + DT.TYPES['latin'], 15, DT.TYPES['latin'])
        login_page = LoginPage(driver, url)
        login_page.open()
        login_page.submit_login(email, password)
        looks_page = LooksPage(driver, url)
        assert looks_page.if_folder_exists(data, driver) == False, 'the folder already exists, please delete the folder'

        # Open New folder popup and test
        looks_page.new_folder_button()
        looks_page.fill_folder_fields(data)
        looks_page.cancel_folder_creation_button()
        assert looks_page.is_popup_new_folder_visible().get_attribute('style') == 'visibility: hidden;', 'the cancel button is not closing the popup'
        assert not looks_page.if_folder_exists(data, driver), 'the folder is created but should not be'

    def test_can_open_new_folder_popup(self, driver):
        # Precondition: Login
        login_page = LoginPage(driver, url)
        login_page.open()
        login_page.submit_login(email, password)
        looks_page = LooksPage(driver, url)

        # Open New folder popup and test
        looks_page.new_folder_button()
        assert looks_page.is_popup_new_folder_visible().get_attribute('style') == 'visibility: visible;', 'the popup is not shown'

    def test_close_popup_new_folder(self, driver):
        # Precondition: Login
        login_page = LoginPage(driver, url)
        login_page.open()
        login_page.submit_login(email, password)
        looks_page = LooksPage(driver, url)

        # Open New folder popup and test
        looks_page.new_folder_button()
        looks_page.close_button_folder_creation()
        assert looks_page.is_popup_new_folder_visible().get_attribute('style') == 'visibility: hidden;', 'the close button is not closing the popup'

class TestFoldersCreationRegressionNameLength:
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
        assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
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
        assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
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
            assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
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
            assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
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
            assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
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
            assert len(looks_page.get_folder_name_in_form()) == 32, 'name of the folder is more than 32 symbols'

class TestFoldersCreationRegressionUserIDLength:
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
            assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
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
                assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
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
                    assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
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
                    assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
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
                    assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
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
                    assert len(
                        looks_page.get_folder_user_id_in_form()) == 32, 'user_id of the folder is more than 32 symbols'

class TestFoldersCreationRegressionNameUserIDSymbols:
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
                assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
                assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
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
                assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
                assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
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
                assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
                assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
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
                assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
                assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
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
                assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
                assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
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
                assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
                assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
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
                assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
                assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
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
                assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
                assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
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
                assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
                assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
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
                assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
                assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
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
                assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
                assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
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
                assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
                assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
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
                assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
                assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
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
                assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
                assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
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
                assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
                assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
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
                assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
                assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
                looks_page.save_folder_button()

                # Delete cookies and login again for checking
                driver.delete_all_cookies()
                login_page.open()
                login_page.submit_login(email, password)

                # Checking created folder
                assert looks_page.if_folder_exists(data, driver), 'the folder cannot be created'

                # Post-condition: Delete folder
                looks_page.delete_folder(data, driver)

class TestFoldersEditionSmoke:
    # @pytest.mark.parametrize('exec_number', range(5))
    def test_edit_folder_smoke(self, driver):
        # Pre-condition: Login, Create folder
        data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['latin'])
        replace_data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['latin'])
        login_page = LoginPage(driver, url)
        login_page.open()
        login_page.submit_login(email, password)
        looks_page = LooksPage(driver, url)
        assert looks_page.if_folder_exists(data, driver) == False, 'the folder already exists, please delete the folder'
        looks_page.new_folder_button()
        looks_page.fill_folder_fields(data)
        assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
        assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Edit folder
        looks_page.clear_folder_form(data, driver)
        looks_page.fill_folder_fields(replace_data)
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Checking edited folder
        assert looks_page.if_folder_exists(replace_data, driver), 'the folder is not changed!'

        # Post-condition: Delete folder
        looks_page.delete_folder(replace_data, driver)

    def test_can_cancel_folder_edition(self, driver):
        # Pre-condition: Login, Create folder
        data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['latin'])
        replace_data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['latin'])
        login_page = LoginPage(driver, url)
        login_page.open()
        login_page.submit_login(email, password)
        looks_page = LooksPage(driver, url)
        assert looks_page.if_folder_exists(data, driver) == False, 'the folder already exists, please delete the folder'
        looks_page.new_folder_button()
        looks_page.fill_folder_fields(data)
        assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
        assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Edit folder
        looks_page.clear_folder_form(data, driver)
        looks_page.fill_folder_fields(replace_data)
        looks_page.cancel_folder_creation_button()
        assert looks_page.is_popup_new_folder_visible().get_attribute('style') == 'visibility: hidden;', 'the cancel button is not closing the popup'

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Checking edited folder
        assert looks_page.if_folder_exists(data, driver), 'the folder is changed but should not be'

        # Post-condition: Delete folder
        looks_page.delete_folder(data, driver)

    def test_cant_save_folder_with_empty_name(self, driver):
        # Pre-condition: Login, Create folder
        data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['latin'])
        replace_data = folder_random_data(0, DT.TYPES['latin'], 10, DT.TYPES['latin'])
        login_page = LoginPage(driver, url)
        login_page.open()
        login_page.submit_login(email, password)
        looks_page = LooksPage(driver, url)
        assert looks_page.if_folder_exists(data, driver) == False, 'the folder already exists, please delete the folder'
        looks_page.new_folder_button()
        looks_page.fill_folder_fields(data)
        assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
        assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Edit folder
        looks_page.clear_folder_form(data, driver)
        looks_page.fill_folder_fields(replace_data)
        looks_page.save_folder_button()
        assert looks_page.is_popup_new_folder_visible().get_attribute('style') == 'visibility: visible;', 'the cancel button is not closing the popup'

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Checking edited folder
        assert looks_page.if_folder_exists(data, driver), 'the folder is changed but should not be'

        # Post-condition: Delete folder
        looks_page.delete_folder(data, driver)

class TestFoldersEditionRegressionNameLength:
    def test_folder_edition_name_1_symbol(self, driver):
        # Pre-condition: Login, Create folder
        data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['latin'])
        replace_data = folder_random_data(1, DT.TYPES['latin'], 0, DT.TYPES['latin'])
        login_page = LoginPage(driver, url)
        login_page.open()
        login_page.submit_login(email, password)
        looks_page = LooksPage(driver, url)
        assert looks_page.if_folder_exists(data, driver) == False, 'the folder already exists, please delete the folder'
        looks_page.new_folder_button()
        looks_page.fill_folder_fields(data)
        assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
        assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Edit folder
        looks_page.clear_folder_form(data, driver)
        looks_page.fill_folder_fields(replace_data)
        assert looks_page.get_folder_name_in_form() == replace_data['name'], 'name of the folder is different'
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Checking edited folder
        assert looks_page.if_folder_exists(replace_data, driver), 'the folder is not changed!'

        # Post-condition: Delete folder
        looks_page.delete_folder(replace_data, driver)

    def test_folder_edition_name_2_symbols(self, driver):
            # Pre-condition: Login, Create folder
            data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['latin'])
            replace_data = folder_random_data(2, DT.TYPES['latin'], 0, DT.TYPES['latin'])
            login_page = LoginPage(driver, url)
            login_page.open()
            login_page.submit_login(email, password)
            looks_page = LooksPage(driver, url)
            assert looks_page.if_folder_exists(data, driver) == False, 'the folder already exists, please delete the folder'
            looks_page.new_folder_button()
            looks_page.fill_folder_fields(data)
            assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
            assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
            looks_page.save_folder_button()

            # Delete cookies and login again for checking
            driver.delete_all_cookies()
            login_page.open()
            login_page.submit_login(email, password)

            # Edit folder
            looks_page.clear_folder_form(data, driver)
            looks_page.fill_folder_fields(replace_data)
            assert looks_page.get_folder_name_in_form() == replace_data['name'], 'name of the folder is different'
            looks_page.save_folder_button()

            # Delete cookies and login again for checking
            driver.delete_all_cookies()
            login_page.open()
            login_page.submit_login(email, password)

            # Checking edited folder
            assert looks_page.if_folder_exists(replace_data, driver), 'the folder is not changed!'

            # Post-condition: Delete folder
            looks_page.delete_folder(replace_data, driver)

    def test_folder_edition_name_10_symbols(self, driver):
            # Pre-condition: Login, Create folder
            data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['latin'])
            replace_data = folder_random_data(10, DT.TYPES['latin'], 0, DT.TYPES['latin'])
            login_page = LoginPage(driver, url)
            login_page.open()
            login_page.submit_login(email, password)
            looks_page = LooksPage(driver, url)
            assert looks_page.if_folder_exists(data, driver) == False, 'the folder already exists, please delete the folder'
            looks_page.new_folder_button()
            looks_page.fill_folder_fields(data)
            assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
            assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
            looks_page.save_folder_button()

            # Delete cookies and login again for checking
            driver.delete_all_cookies()
            login_page.open()
            login_page.submit_login(email, password)

            # Edit folder
            looks_page.clear_folder_form(data, driver)
            looks_page.fill_folder_fields(replace_data)
            assert looks_page.get_folder_name_in_form() == replace_data['name'], 'name of the folder is different'
            looks_page.save_folder_button()

            # Delete cookies and login again for checking
            driver.delete_all_cookies()
            login_page.open()
            login_page.submit_login(email, password)

            # Checking edited folder
            assert looks_page.if_folder_exists(replace_data, driver), 'the folder is not changed!'

            # Post-condition: Delete folder
            looks_page.delete_folder(replace_data, driver)

    def test_folder_edition_name_31_symbols(self, driver):
            # Pre-condition: Login, Create folder
            data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['latin'])
            replace_data = folder_random_data(31, DT.TYPES['latin'], 0, DT.TYPES['latin'])
            login_page = LoginPage(driver, url)
            login_page.open()
            login_page.submit_login(email, password)
            looks_page = LooksPage(driver, url)
            assert looks_page.if_folder_exists(data, driver) == False, 'the folder already exists, please delete the folder'
            looks_page.new_folder_button()
            looks_page.fill_folder_fields(data)
            assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
            assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
            looks_page.save_folder_button()

            # Delete cookies and login again for checking
            driver.delete_all_cookies()
            login_page.open()
            login_page.submit_login(email, password)

            # Edit folder
            looks_page.clear_folder_form(data, driver)
            looks_page.fill_folder_fields(replace_data)
            assert looks_page.get_folder_name_in_form() == replace_data['name'], 'name of the folder is different'
            looks_page.save_folder_button()

            # Delete cookies and login again for checking
            driver.delete_all_cookies()
            login_page.open()
            login_page.submit_login(email, password)

            # Checking edited folder
            assert looks_page.if_folder_exists(replace_data, driver), 'the folder is not changed!'

            # Post-condition: Delete folder
            looks_page.delete_folder(replace_data, driver)

    def test_folder_edition_name_32_symbols(self, driver):
            # Pre-condition: Login, Create folder
            data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['latin'])
            replace_data = folder_random_data(32, DT.TYPES['latin'], 0, DT.TYPES['latin'])
            login_page = LoginPage(driver, url)
            login_page.open()
            login_page.submit_login(email, password)
            looks_page = LooksPage(driver, url)
            assert looks_page.if_folder_exists(data, driver) == False, 'the folder already exists, please delete the folder'
            looks_page.new_folder_button()
            looks_page.fill_folder_fields(data)
            assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
            assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
            looks_page.save_folder_button()

            # Delete cookies and login again for checking
            driver.delete_all_cookies()
            login_page.open()
            login_page.submit_login(email, password)

            # Edit folder
            looks_page.clear_folder_form(data, driver)
            looks_page.fill_folder_fields(replace_data)
            assert looks_page.get_folder_name_in_form() == replace_data['name'], 'name of the folder is different'
            looks_page.save_folder_button()

            # Delete cookies and login again for checking
            driver.delete_all_cookies()
            login_page.open()
            login_page.submit_login(email, password)

            # Checking edited folder
            assert looks_page.if_folder_exists(replace_data, driver), 'the folder is not changed!'

            # Post-condition: Delete folder
            looks_page.delete_folder(replace_data, driver)

    def test_folder_not_edit_name_33_symbols(self, driver):
            # Pre-condition: Login, Create folder
            data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['latin'])
            replace_data = folder_random_data(33, DT.TYPES['latin'], 0, DT.TYPES['latin'])
            login_page = LoginPage(driver, url)
            login_page.open()
            login_page.submit_login(email, password)
            looks_page = LooksPage(driver, url)
            assert looks_page.if_folder_exists(data, driver) == False, 'the folder already exists, please delete the folder'
            looks_page.new_folder_button()
            looks_page.fill_folder_fields(data)
            assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
            assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
            looks_page.save_folder_button()

            # Delete cookies and login again for checking
            driver.delete_all_cookies()
            login_page.open()
            login_page.submit_login(email, password)

            # Edit folder
            looks_page.clear_folder_form(data, driver)
            looks_page.fill_folder_fields(replace_data)

            # Checking name length
            assert len(looks_page.get_folder_name_in_form()) == 32, 'name of the folder is more than 32 symbols'

            # Delete cookies and login again for checking
            driver.delete_all_cookies()
            login_page.open()
            login_page.submit_login(email, password)

            # Post-condition: Delete folder
            looks_page.delete_folder(data, driver)

class TestFoldersEditionRegressionUserIDLength:
    def test_folder_edition_user_id_1_symbol(self, driver):
            # Pre-condition: Login, Create folder
            data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['latin'])
            replace_data = folder_random_data(10, DT.TYPES['latin'], 1, DT.TYPES['latin'])
            login_page = LoginPage(driver, url)
            login_page.open()
            login_page.submit_login(email, password)
            looks_page = LooksPage(driver, url)
            assert looks_page.if_folder_exists(data, driver) == False, 'the folder already exists, please delete the folder'
            looks_page.new_folder_button()
            looks_page.fill_folder_fields(data)
            assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
            assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
            looks_page.save_folder_button()

            # Delete cookies and login again for checking
            driver.delete_all_cookies()
            login_page.open()
            login_page.submit_login(email, password)

            # Edit folder
            looks_page.clear_folder_form(data, driver)
            looks_page.fill_folder_fields(replace_data)
            assert looks_page.get_folder_user_id_in_form() == replace_data['user_id'], 'user_id of the folder is different'
            looks_page.save_folder_button()

            # Delete cookies and login again for checking
            driver.delete_all_cookies()
            login_page.open()
            login_page.submit_login(email, password)

            # Checking edited folder
            assert looks_page.if_folder_exists(replace_data, driver), 'the folder is not changed!'

            # Post-condition: Delete folder
            looks_page.delete_folder(replace_data, driver)

    def test_folder_edition_user_id_10_symbols(self, driver):
            # Pre-condition: Login, Create folder
            data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['latin'])
            replace_data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['latin'])
            login_page = LoginPage(driver, url)
            login_page.open()
            login_page.submit_login(email, password)
            looks_page = LooksPage(driver, url)
            assert looks_page.if_folder_exists(data, driver) == False, 'the folder already exists, please delete the folder'
            looks_page.new_folder_button()
            looks_page.fill_folder_fields(data)
            assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
            assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
            looks_page.save_folder_button()

            # Delete cookies and login again for checking
            driver.delete_all_cookies()
            login_page.open()
            login_page.submit_login(email, password)

            # Edit folder
            looks_page.clear_folder_form(data, driver)
            looks_page.fill_folder_fields(replace_data)
            assert looks_page.get_folder_user_id_in_form() == replace_data['user_id'], 'user_id of the folder is different'
            looks_page.save_folder_button()

            # Delete cookies and login again for checking
            driver.delete_all_cookies()
            login_page.open()
            login_page.submit_login(email, password)

            # Checking edited folder
            assert looks_page.if_folder_exists(replace_data, driver), 'the folder is not changed!'

            # Post-condition: Delete folder
            looks_page.delete_folder(replace_data, driver)

    def test_folder_edition_user_id_31_symbols(self, driver):
            # Pre-condition: Login, Create folder
            data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['latin'])
            replace_data = folder_random_data(10, DT.TYPES['latin'], 31, DT.TYPES['latin'])
            login_page = LoginPage(driver, url)
            login_page.open()
            login_page.submit_login(email, password)
            looks_page = LooksPage(driver, url)
            assert looks_page.if_folder_exists(data, driver) == False, 'the folder already exists, please delete the folder'
            looks_page.new_folder_button()
            looks_page.fill_folder_fields(data)
            assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
            assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
            looks_page.save_folder_button()

            # Delete cookies and login again for checking
            driver.delete_all_cookies()
            login_page.open()
            login_page.submit_login(email, password)

            # Edit folder
            looks_page.clear_folder_form(data, driver)
            looks_page.fill_folder_fields(replace_data)
            assert looks_page.get_folder_user_id_in_form() == replace_data['user_id'], 'user_id of the folder is different'
            looks_page.save_folder_button()

            # Delete cookies and login again for checking
            driver.delete_all_cookies()
            login_page.open()
            login_page.submit_login(email, password)

            # Checking edited folder
            assert looks_page.if_folder_exists(replace_data, driver), 'the folder is not changed!'

            # Post-condition: Delete folder
            looks_page.delete_folder(replace_data, driver)

    def test_folder_edition_user_id_32_symbols(self, driver):
            # Pre-condition: Login, Create folder
            data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['latin'])
            replace_data = folder_random_data(10, DT.TYPES['latin'], 32, DT.TYPES['latin'])
            login_page = LoginPage(driver, url)
            login_page.open()
            login_page.submit_login(email, password)
            looks_page = LooksPage(driver, url)
            assert looks_page.if_folder_exists(data, driver) == False, 'the folder already exists, please delete the folder'
            looks_page.new_folder_button()
            looks_page.fill_folder_fields(data)
            assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
            assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
            looks_page.save_folder_button()

            # Delete cookies and login again for checking
            driver.delete_all_cookies()
            login_page.open()
            login_page.submit_login(email, password)

            # Edit folder
            looks_page.clear_folder_form(data, driver)
            looks_page.fill_folder_fields(replace_data)
            assert looks_page.get_folder_user_id_in_form() == replace_data['user_id'], 'user_id of the folder is different'
            looks_page.save_folder_button()

            # Delete cookies and login again for checking
            driver.delete_all_cookies()
            login_page.open()
            login_page.submit_login(email, password)

            # Checking edited folder
            assert looks_page.if_folder_exists(replace_data, driver), 'the folder is not changed!'

            # Post-condition: Delete folder
            looks_page.delete_folder(replace_data, driver)

    def test_folder_not_edit_user_id_33_symbols(self, driver):
            # Pre-condition: Login, Create folder
            data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['latin'])
            replace_data = folder_random_data(10, DT.TYPES['latin'], 33, DT.TYPES['latin'])
            login_page = LoginPage(driver, url)
            login_page.open()
            login_page.submit_login(email, password)
            looks_page = LooksPage(driver, url)
            assert looks_page.if_folder_exists(data, driver) == False, 'the folder already exists, please delete the folder'
            looks_page.new_folder_button()
            looks_page.fill_folder_fields(data)
            assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
            assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
            looks_page.save_folder_button()

            # Delete cookies and login again for checking
            driver.delete_all_cookies()
            login_page.open()
            login_page.submit_login(email, password)

            # Edit folder
            looks_page.clear_folder_form(data, driver)
            looks_page.fill_folder_fields(replace_data)

            # Checking name length
            assert len(looks_page.get_folder_user_id_in_form()) == 32, 'user_id of the folder is more than 32 symbols'

            # Delete cookies and login again for checking
            driver.delete_all_cookies()
            login_page.open()
            login_page.submit_login(email, password)

            # Post-condition: Delete folder
            looks_page.delete_folder(data, driver)

class TestFoldersEditionRegressionNameUserIDSymbols:
    def test_edit_folder_name_latin_user_id_latin(self, driver):
        # Pre-condition: Login, Create folder
        data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['latin'])
        replace_data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['latin'])
        login_page = LoginPage(driver, url)
        login_page.open()
        login_page.submit_login(email, password)
        looks_page = LooksPage(driver, url)
        assert looks_page.if_folder_exists(data, driver) == False, 'the folder already exists, please delete the folder'
        looks_page.new_folder_button()
        looks_page.fill_folder_fields(data)
        assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
        assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Edit folder
        looks_page.clear_folder_form(data, driver)
        looks_page.fill_folder_fields(replace_data)
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Post-condition: Delete folder
        looks_page.delete_folder(replace_data, driver)

    def test_edit_folder_name_latin_user_id_cyrillic(self, driver):
        # Pre-condition: Login, Create folder
        data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['latin'])
        replace_data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['cyrillic'])
        login_page = LoginPage(driver, url)
        login_page.open()
        login_page.submit_login(email, password)
        looks_page = LooksPage(driver, url)
        assert looks_page.if_folder_exists(data, driver) == False, 'the folder already exists, please delete the folder'
        looks_page.new_folder_button()
        looks_page.fill_folder_fields(data)
        assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
        assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Edit folder
        looks_page.clear_folder_form(data, driver)
        looks_page.fill_folder_fields(replace_data)
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Post-condition: Delete folder
        looks_page.delete_folder(replace_data, driver)

    def test_edit_folder_name_latin_user_id_digits(self, driver):
        # Pre-condition: Login, Create folder
        data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['latin'])
        replace_data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['digits'])
        login_page = LoginPage(driver, url)
        login_page.open()
        login_page.submit_login(email, password)
        looks_page = LooksPage(driver, url)
        assert looks_page.if_folder_exists(data, driver) == False, 'the folder already exists, please delete the folder'
        looks_page.new_folder_button()
        looks_page.fill_folder_fields(data)
        assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
        assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Edit folder
        looks_page.clear_folder_form(data, driver)
        looks_page.fill_folder_fields(replace_data)
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Post-condition: Delete folder
        looks_page.delete_folder(replace_data, driver)

    def test_edit_folder_name_latin_user_id_spec(self, driver):
        # Pre-condition: Login, Create folder
        data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['latin'])
        replace_data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['spec'])
        login_page = LoginPage(driver, url)
        login_page.open()
        login_page.submit_login(email, password)
        looks_page = LooksPage(driver, url)
        assert looks_page.if_folder_exists(data, driver) == False, 'the folder already exists, please delete the folder'
        looks_page.new_folder_button()
        looks_page.fill_folder_fields(data)
        assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
        assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Edit folder
        looks_page.clear_folder_form(data, driver)
        looks_page.fill_folder_fields(replace_data)
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Post-condition: Delete folder
        looks_page.delete_folder(replace_data, driver)

    def test_edit_folder_name_cyrillic_user_id_cyrillic(self, driver):
        # Pre-condition: Login, Create folder
        data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['latin'])
        replace_data = folder_random_data(10, DT.TYPES['cyrillic'], 10, DT.TYPES['cyrillic'])
        login_page = LoginPage(driver, url)
        login_page.open()
        login_page.submit_login(email, password)
        looks_page = LooksPage(driver, url)
        assert looks_page.if_folder_exists(data, driver) == False, 'the folder already exists, please delete the folder'
        looks_page.new_folder_button()
        looks_page.fill_folder_fields(data)
        assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
        assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Edit folder
        looks_page.clear_folder_form(data, driver)
        looks_page.fill_folder_fields(replace_data)
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Post-condition: Delete folder
        looks_page.delete_folder(replace_data, driver)

    def test_edit_folder_name_cyrillic_user_id_digits(self, driver):
        # Pre-condition: Login, Create folder
        data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['latin'])
        replace_data = folder_random_data(10, DT.TYPES['cyrillic'], 10, DT.TYPES['digits'])
        login_page = LoginPage(driver, url)
        login_page.open()
        login_page.submit_login(email, password)
        looks_page = LooksPage(driver, url)
        assert looks_page.if_folder_exists(data, driver) == False, 'the folder already exists, please delete the folder'
        looks_page.new_folder_button()
        looks_page.fill_folder_fields(data)
        assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
        assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Edit folder
        looks_page.clear_folder_form(data, driver)
        looks_page.fill_folder_fields(replace_data)
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Post-condition: Delete folder
        looks_page.delete_folder(replace_data, driver)

    def test_edit_folder_name_cyrillic_user_id_spec(self, driver):
        # Pre-condition: Login, Create folder
        data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['latin'])
        replace_data = folder_random_data(10, DT.TYPES['cyrillic'], 10, DT.TYPES['spec'])
        login_page = LoginPage(driver, url)
        login_page.open()
        login_page.submit_login(email, password)
        looks_page = LooksPage(driver, url)
        assert looks_page.if_folder_exists(data, driver) == False, 'the folder already exists, please delete the folder'
        looks_page.new_folder_button()
        looks_page.fill_folder_fields(data)
        assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
        assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Edit folder
        looks_page.clear_folder_form(data, driver)
        looks_page.fill_folder_fields(replace_data)
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Post-condition: Delete folder
        looks_page.delete_folder(replace_data, driver)

    def test_edit_folder_name_cyrillic_user_id_latin(self, driver):
        # Pre-condition: Login, Create folder
        data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['latin'])
        replace_data = folder_random_data(10, DT.TYPES['cyrillic'], 10, DT.TYPES['latin'])
        login_page = LoginPage(driver, url)
        login_page.open()
        login_page.submit_login(email, password)
        looks_page = LooksPage(driver, url)
        assert looks_page.if_folder_exists(data, driver) == False, 'the folder already exists, please delete the folder'
        looks_page.new_folder_button()
        looks_page.fill_folder_fields(data)
        assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
        assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Edit folder
        looks_page.clear_folder_form(data, driver)
        looks_page.fill_folder_fields(replace_data)
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Post-condition: Delete folder
        looks_page.delete_folder(replace_data, driver)

    def test_edit_folder_name_digits_user_id_digits(self, driver):
        # Pre-condition: Login, Create folder
        data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['latin'])
        replace_data = folder_random_data(10, DT.TYPES['digits'], 10, DT.TYPES['digits'])
        login_page = LoginPage(driver, url)
        login_page.open()
        login_page.submit_login(email, password)
        looks_page = LooksPage(driver, url)
        assert looks_page.if_folder_exists(data, driver) == False, 'the folder already exists, please delete the folder'
        looks_page.new_folder_button()
        looks_page.fill_folder_fields(data)
        assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
        assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Edit folder
        looks_page.clear_folder_form(data, driver)
        looks_page.fill_folder_fields(replace_data)
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Post-condition: Delete folder
        looks_page.delete_folder(replace_data, driver)

    def test_edit_folder_name_digits_user_id_spec(self, driver):
        # Pre-condition: Login, Create folder
        data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['latin'])
        replace_data = folder_random_data(10, DT.TYPES['digits'], 10, DT.TYPES['spec'])
        login_page = LoginPage(driver, url)
        login_page.open()
        login_page.submit_login(email, password)
        looks_page = LooksPage(driver, url)
        assert looks_page.if_folder_exists(data, driver) == False, 'the folder already exists, please delete the folder'
        looks_page.new_folder_button()
        looks_page.fill_folder_fields(data)
        assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
        assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Edit folder
        looks_page.clear_folder_form(data, driver)
        looks_page.fill_folder_fields(replace_data)
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Post-condition: Delete folder
        looks_page.delete_folder(replace_data, driver)

    def test_edit_folder_name_digits_user_id_latin(self, driver):
        # Pre-condition: Login, Create folder
        data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['latin'])
        replace_data = folder_random_data(10, DT.TYPES['digits'], 10, DT.TYPES['latin'])
        login_page = LoginPage(driver, url)
        login_page.open()
        login_page.submit_login(email, password)
        looks_page = LooksPage(driver, url)
        assert looks_page.if_folder_exists(data, driver) == False, 'the folder already exists, please delete the folder'
        looks_page.new_folder_button()
        looks_page.fill_folder_fields(data)
        assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
        assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Edit folder
        looks_page.clear_folder_form(data, driver)
        looks_page.fill_folder_fields(replace_data)
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Post-condition: Delete folder
        looks_page.delete_folder(replace_data, driver)

    def test_edit_folder_name_digits_user_id_cyrillic(self, driver):
        # Pre-condition: Login, Create folder
        data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['latin'])
        replace_data = folder_random_data(10, DT.TYPES['digits'], 10, DT.TYPES['cyrillic'])
        login_page = LoginPage(driver, url)
        login_page.open()
        login_page.submit_login(email, password)
        looks_page = LooksPage(driver, url)
        assert looks_page.if_folder_exists(data, driver) == False, 'the folder already exists, please delete the folder'
        looks_page.new_folder_button()
        looks_page.fill_folder_fields(data)
        assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
        assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Edit folder
        looks_page.clear_folder_form(data, driver)
        looks_page.fill_folder_fields(replace_data)
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Post-condition: Delete folder
        looks_page.delete_folder(replace_data, driver)

    def test_edit_folder_name_spec_user_id_spec(self, driver):
        # Pre-condition: Login, Create folder
        data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['latin'])
        replace_data = folder_random_data(10, DT.TYPES['spec'], 10, DT.TYPES['spec'])
        login_page = LoginPage(driver, url)
        login_page.open()
        login_page.submit_login(email, password)
        looks_page = LooksPage(driver, url)
        assert looks_page.if_folder_exists(data, driver) == False, 'the folder already exists, please delete the folder'
        looks_page.new_folder_button()
        looks_page.fill_folder_fields(data)
        assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
        assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Edit folder
        looks_page.clear_folder_form(data, driver)
        looks_page.fill_folder_fields(replace_data)
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Post-condition: Delete folder
        looks_page.delete_folder(replace_data, driver)

    def test_edit_folder_name_spec_user_id_latin(self, driver):
        # Pre-condition: Login, Create folder
        data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['latin'])
        replace_data = folder_random_data(10, DT.TYPES['spec'], 10, DT.TYPES['latin'])
        login_page = LoginPage(driver, url)
        login_page.open()
        login_page.submit_login(email, password)
        looks_page = LooksPage(driver, url)
        assert looks_page.if_folder_exists(data, driver) == False, 'the folder already exists, please delete the folder'
        looks_page.new_folder_button()
        looks_page.fill_folder_fields(data)
        assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
        assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Edit folder
        looks_page.clear_folder_form(data, driver)
        looks_page.fill_folder_fields(replace_data)
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Post-condition: Delete folder
        looks_page.delete_folder(replace_data, driver)

    def test_edit_folder_name_spec_user_id_cyrillic(self, driver):
        # Pre-condition: Login, Create folder
        data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['latin'])
        replace_data = folder_random_data(10, DT.TYPES['spec'], 10, DT.TYPES['cyrillic'])
        login_page = LoginPage(driver, url)
        login_page.open()
        login_page.submit_login(email, password)
        looks_page = LooksPage(driver, url)
        assert looks_page.if_folder_exists(data, driver) == False, 'the folder already exists, please delete the folder'
        looks_page.new_folder_button()
        looks_page.fill_folder_fields(data)
        assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
        assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Edit folder
        looks_page.clear_folder_form(data, driver)
        looks_page.fill_folder_fields(replace_data)
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Post-condition: Delete folder
        looks_page.delete_folder(replace_data, driver)

    def test_edit_folder_name_spec_user_id_digits(self, driver):
        # Pre-condition: Login, Create folder
        data = folder_random_data(10, DT.TYPES['latin'], 10, DT.TYPES['latin'])
        replace_data = folder_random_data(10, DT.TYPES['spec'], 10, DT.TYPES['digits'])
        login_page = LoginPage(driver, url)
        login_page.open()
        login_page.submit_login(email, password)
        looks_page = LooksPage(driver, url)
        assert looks_page.if_folder_exists(data, driver) == False, 'the folder already exists, please delete the folder'
        looks_page.new_folder_button()
        looks_page.fill_folder_fields(data)
        assert looks_page.get_folder_name_in_form() == data['name'], 'name of the folder is different'
        assert looks_page.get_folder_user_id_in_form() == data['user_id'], 'user_id of the folder is different'
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Edit folder
        looks_page.clear_folder_form(data, driver)
        looks_page.fill_folder_fields(replace_data)
        looks_page.save_folder_button()

        # Delete cookies and login again for checking
        driver.delete_all_cookies()
        login_page.open()
        login_page.submit_login(email, password)

        # Post-condition: Delete folder
        looks_page.delete_folder(replace_data, driver)