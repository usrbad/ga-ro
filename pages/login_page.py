from pages.base_page import BasePage
from locators.login_locators import LoginPageLocators as Locators

class LoginPage(BasePage):

    def submit_login(self, email, password):
        self.element_is_visible(Locators.EMAIL).send_keys(email)
        self.element_is_visible(Locators.PASSWORD).send_keys(password)
        self.element_is_visible(Locators.LOGIN_BUTTON).click()
        return
