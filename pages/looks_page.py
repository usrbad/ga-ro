from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from conftest import driver
from pages.base_page import BasePage
from locators.looks_locators import FoldersLocators as Locators

class LooksPage(BasePage):

    def new_folder_button(self):
        self.element_is_visible(Locators.ADD_FOLDER_BUTTON).click()

    def create_folder(self, data):
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
        self.element_is_visible(Locators.SAVE_BUTTON).click()

    def delete_folder(self, data, driver):
        driver.implicitly_wait(5)

        folder_hover = driver.find_element(By.XPATH, '//span[text()="' + data['name'] + '"]/ancestor::a')
        button_delete = driver.find_element(By.XPATH, '//span[text()="' + data['name'] + '"]/ancestor::a/div/img[3]')
        delete_confirmation = driver.find_element(By.XPATH, '//*[@id="btn-delete-folder"]')

        # Наводим курсор на папку и кликаем по кнопке Удалить
        actions = ActionChains(driver)
        actions.move_to_element(folder_hover)
        actions.click(button_delete)
        actions.perform()
        delete_confirmation.click()
        # self.element_is_visible(Locators.DELETE_CONFIRMATION_BUTTON).click()

    def if_folder_exists(self, data, driver):
        return len(driver.find_elements(By.XPATH, '//span[text()="' + data['name'] + '"]/ancestor::a')) > 0