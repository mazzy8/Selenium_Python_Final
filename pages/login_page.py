from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        cur_url = self.browser.current_url
        assert 'login' in cur_url, 'Fail in url, string login not find'

    def should_be_login_form(self):
        a = self.is_element_present(*LoginPageLocators.LOGIN_EMAIL)
        b = self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD)
        assert all((a, b)), 'Fail in login form'

    def should_be_register_form(self):
        a = self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL)
        b = self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD)
        c = self.is_element_present(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD)
        assert all((a, b, c)), 'Fail in registration form'
