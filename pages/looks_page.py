import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tests.conftest import driver
from pages.base_page import BasePage
from locators.looks_locators import FoldersLocators as Locators

class LooksPage(BasePage):
    def new_folder_button(self):
        self.element_is_visible(Locators.ADD_FOLDER_BUTTON).click()

    def fill_only_name(self, data):
        self.element_is_visible(Locators.FOLDER_NAME_FIELD).send_keys(data['name'])

    def fill_folder_fields(self, data):
        self.element_is_visible(Locators.FOLDER_NAME_FIELD).send_keys(data['name'])
        self.element_is_visible(Locators.USER_ID_FIELD).send_keys(data['user_id'])
        for g in data['gender']:
            self.element_is_visible(Locators.GENDER_FIELD).send_keys(g)
            self.element_is_visible(Locators.GENDER_FIELD).send_keys(Keys.RETURN)
            self.element_is_visible(Locators.GENDER_FIELD).click()
        for t in data['top_size']:
            self.element_is_visible(Locators.TOP_SIZE_FIELD).send_keys(t)
            self.element_is_visible(Locators.TOP_SIZE_FIELD).send_keys(Keys.RETURN)
        for b in data['bottom_size']:
            self.element_is_visible(Locators.BOTTOM_SIZE_FIELD).send_keys(b)
            self.element_is_visible(Locators.BOTTOM_SIZE_FIELD).send_keys(Keys.RETURN)
        for s in data['shoes_size']:
            self.element_is_visible(Locators.SHOES_SIZE_FIELD).send_keys(s)
            self.element_is_visible(Locators.SHOES_SIZE_FIELD).send_keys(Keys.RETURN)
        for b in data['brands']:
            self.element_is_visible(Locators.BRAND_FIELD).send_keys(b)
            self.element_is_visible(Locators.BRAND_FIELD).send_keys(Keys.RETURN)
            self.element_is_visible(Locators.BRAND_CONFIRM).click()

    def save_folder_button(self):
        self.element_is_visible(Locators.SAVE_BUTTON).click()

    def open_folder_for_edit(self, data, driver):
        # Locators
        folder_hover_locator = (By.XPATH, '//span[text()="' + data['name'] + '"]/ancestor::a')
        edit_folder_button = (By.XPATH, '//span[text()="' + data['name'] + '"]/ancestor::a/div/img[2]')

        # Hover to folder item and push Edit
        actions = ActionChains(driver)
        actions.move_to_element(self.element_is_visible(folder_hover_locator))
        actions.click(self.presence_of_element_located(edit_folder_button))
        actions.perform()

    def clear_folder_form(self, data, driver):
        # Open folder for edit
        self.open_folder_for_edit(data,driver)
        # Clear form
        self.element_is_visible(Locators.FOLDER_NAME_FIELD).clear()
        self.element_is_visible(Locators.USER_ID_FIELD).clear()
        # TODO: remove time.sleep, wait until gender field fully loads
        time.sleep(0.5)
        for _ in range(len(data['gender'])):
            self.element_is_visible(Locators.GENDER_FIELD).send_keys(Keys.BACKSPACE)
        for _ in range(len(data['top_size'])):
            self.element_is_visible(Locators.TOP_SIZE_FIELD).send_keys(Keys.BACKSPACE)
        for _ in range(len(data['bottom_size'])):
            self.element_is_visible(Locators.BOTTOM_SIZE_FIELD).send_keys(Keys.BACKSPACE)
        for _ in range(len(data['shoes_size'])):
            self.element_is_visible(Locators.SHOES_SIZE_FIELD).send_keys(Keys.BACKSPACE)
        for b in range(len(data['brands'])):
            delete_brand_button = (By.XPATH, '//li[@title="' + data['brands'][b] + '"]/button')
            self.element_is_visible(delete_brand_button).click()

    def delete_folder(self, data, driver):
        # Locators
        folder_hover_locator = (By.XPATH, '//span[text()="' + data['name'] + '"]/ancestor::a')
        trash_button_locator = (By.XPATH, '//span[text()="' + data['name'] + '"]/ancestor::a/div/img[3]')
        delete_confirmation_locator = (By.XPATH, '//*[@id="btn-delete-folder"]')

        # Hover to folder item and push Delete
        actions = ActionChains(driver)
        actions.move_to_element(self.element_is_visible(folder_hover_locator))
        actions.click(self.presence_of_element_located(trash_button_locator))
        actions.perform()
        self.element_to_be_clickable(delete_confirmation_locator).click()

    def if_folder_exists(self, data, driver):
        return len(driver.find_elements(By.XPATH, '//span[text()="' + data['name'] + '"]/ancestor::a')) > 0

    def get_folder_name_in_form(self):
        return self.element_is_visible(Locators.FOLDER_NAME_FIELD).get_attribute('value')

    def get_folder_user_id_in_form(self):
        return self.element_is_visible(Locators.USER_ID_FIELD).get_attribute('value')

    def cancel_folder_creation_button(self):
        return self.element_to_be_clickable(Locators.CANCEL_BUTTON).click()

    def is_popup_new_folder_visible(self):
        return self.element_is_visible(Locators.POPUP_FOLDER_FORM)

    def close_button_folder_creation(self):
        return self.element_is_visible(Locators.CLOSE_POPUP_BUTTON).click()

    # def is_folder_fields_equals(self, data):
    #     user_id = self.element_is_visible((By.XPATH, '//span[text()="' + data['name'] + '"]/ancestor::a')).get_attribute('data-user-id')
    #     gender = ast.literal_eval(self.element_is_visible((By.XPATH, '//span[text()="' + data['name'] + '"]/ancestor::a')).get_attribute('data-gender'))
    #     top_size = ast.literal_eval(self.element_is_visible((By.XPATH, '//span[text()="' + data['name'] + '"]/ancestor::a')).get_attribute('data-top-sizes'))
    #     bottom_size = ast.literal_eval(self.element_is_visible((By.XPATH, '//span[text()="' + data['name'] + '"]/ancestor::a')).get_attribute('data-bottom-sizes'))
    #     shoes_size = ast.literal_eval(self.element_is_visible((By.XPATH, '//span[text()="' + data['name'] + '"]/ancestor::a')).get_attribute('data-shoes-sizes'))
    #     brands = ast.literal_eval(self.element_is_visible((By.XPATH, '//span[text()="' + data['name'] + '"]/ancestor::a')).get_attribute('data-brands'))
    #
    #     # Change data from DOM
    #     gender = [s.lower() for s in gender]
    #     gender = ['Male' if s == 'male' else s for s in gender]
    #     gender = ['Female' if s == 'female' else s for s in gender]
    #     gender = [s.replace('kid_girls', 'Kids Girls') for s in gender]
    #     gender = [s.replace('kid_boys', 'Kids Boys') for s in gender]
    #     gender = [s.replace('teen_boys', 'Teens Boys') for s in gender]
    #     gender = [s.replace('teen_girls', 'Teens Girls') for s in gender]
    #     gender = [s.replace('toddler_boys', 'Toddlers Boys') for s in gender]
    #     gender = [s.replace('toddler_girls', 'Toddlers Girls') for s in gender]
    #     top_size = [s.replace(' ', '').upper() for s in top_size]
    #     bottom_size = [s.replace(' ', '').upper() for s in bottom_size]
    #     shoes_size = [s.replace(' ', '').upper() for s in shoes_size]
    #
    #     folder = {
    #         'name': data['name'],
    #         'user_id': user_id,
    #         'gender': gender,
    #         'top_size': top_size,
    #         'bottom_size': bottom_size,
    #         'shoes_size': shoes_size,
    #         'brands': brands,
    #         }
    #
    #     return folder == data
