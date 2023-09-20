from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_in_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_in_url(self):
        assert "login" in self.browser.current_url, "Страница логина отсутствует"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_LOCATOR), "форма логина отсутствует"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_LOCATOR), "форма регистраци отсутствует"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_LOCATOR)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_LOCATOR)
        accept_password_field = self.browser.find_element(*LoginPageLocators.ACCEPT_PASSWORD_LOCATOR)
        email_field.send_keys(email)
        password_field.send_keys(password)
        accept_password_field.send_keys(password)

