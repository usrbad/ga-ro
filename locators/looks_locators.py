from selenium.webdriver.common.by import By

class FoldersLocators:
    ADD_FOLDER_BUTTON = (By.XPATH, '//*[@id="button-add-folder"]')
    POPUP_FOLDER_FORM = (By.XPATH, '//*[@id="popup-add-new-folder"]')
    FOLDER_NAME_FIELD = (By.XPATH, '//*[@id="folder-name"]')
    USER_ID_FIELD = (By.XPATH, '//*[@id="user-id"]')
    GENDER_FIELD = (By.XPATH, '//span[@class="tagify__input" and @data-placeholder="Select gender"]')
    TOP_SIZE_FIELD = (By.XPATH, '//span[@class="tagify__input" and @data-placeholder="Select top size"]')
    BOTTOM_SIZE_FIELD = (By.XPATH, '//span[@class="tagify__input" and @data-placeholder="Select bottom size"]')
    SHOES_SIZE_FIELD = (By.XPATH, '//span[@class="tagify__input" and @data-placeholder="Select shoes size"]')
    BRAND_FIELD = (By.XPATH, '//span[@class="select2-selection select2-selection--multiple"]')
    BRAND_CONFIRM = (By.XPATH, '//li[@class="select2-results__option select2-results__option--selectable select2-results__option--highlighted"]')
    SAVE_BUTTON = (By.XPATH, '//*[@id="btn-save-folder"]')
    CANCEL_BUTTON = (By.XPATH, '//*[@id="btn-cancel-new-folder"]')
    CLOSE_POPUP_BUTTON = (By.XPATH, '//*[@id="close-icon"]')
    DELETE_CONFIRMATION_BUTTON = (By.XPATH, '//*[@id="btn-delete-folder"]')
    DELETE_CANCEL_BUTTON = (By.XPATH, '//*[@id="btn-delete-cancel"]')
    DELETE_FOLDER_POPUP = (By.XPATH, '//*[@id="popup-delete-folder"]')
