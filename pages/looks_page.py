from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tests.conftest import driver
from pages.base_page import BasePage
from locators.looks_locators import FoldersLocators as Locators

class LooksPage(BasePage):

    def new_folder_button(self):
        self.element_is_visible(Locators.ADD_FOLDER_BUTTON).click()

    def fill_folder_fields(self, data):
        self.element_is_visible(Locators.FOLDER_NAME_FIELD).send_keys(data['name'])
        self.element_is_visible(Locators.USER_ID_FIELD).send_keys(data['user_id'])
        for g in data['gender']:
            self.element_is_visible(Locators.GENDER_FIELD).send_keys(g)
            self.element_is_visible(Locators.GENDER_FIELD).send_keys(Keys.RETURN)
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

    def delete_folder(self, data, driver):
        # Locators
        folder_hover_locator = (By.XPATH, '//span[text()="' + data['name'] + '"]/ancestor::a')
        trash_button_locator = (By.XPATH, '//span[text()="' + data['name'] + '"]/ancestor::a/div/img[3]')
        delete_confirmation_locator = (By.XPATH, '//*[@id="btn-delete-folder"]')

        # Наводим курсор на папку и кликаем по кнопке Удалить
        actions = ActionChains(driver)
        actions.move_to_element(self.element_is_visible(folder_hover_locator))
        actions.click(self.presence_of_element_located(trash_button_locator))
        actions.perform()
        self.element_to_be_clickable(delete_confirmation_locator)

    def if_folder_exists(self, data, driver):
        return len(driver.find_elements(By.XPATH, '//span[text()="' + data['name'] + '"]/ancestor::a')) > 0

    def get_folder_name_in_form(self, data):
        return self.element_is_visible(Locators.FOLDER_NAME_FIELD).get_attribute('value')

    def get_folder_user_id_in_form(self, data):
        return self.element_is_visible(Locators.USER_ID_FIELD).get_attribute('value')