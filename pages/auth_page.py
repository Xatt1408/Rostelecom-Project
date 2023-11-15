from .base_page import BasePage
from .Locators import AuthLocators

class AuthPage(BasePage):
    def tab_phone_click(self):
        return self.find_element(AuthLocators.LOCATOR_AUTH_TAB_PHONE).click()

    def tab_email_click(self):
        return self.find_element(AuthLocators.LOCATOR_AUTH_TAB_EMAIL).click()

    def tab_login_click(self):
        return self.find_element(AuthLocators.LOCATOR_AUTH_TAB_LOGIN).click()

    def tab_ls_click(self):
        return self.find_element(AuthLocators.LOCATOR_AUTH_TAB_LS).click()

    def tab_find_field_description(self):
        return self.find_element(AuthLocators.LOCATOR_AUTH_TAB_FIELD)

    def enter_name(self, value):
        return self.find_element(AuthLocators.LOCATOR_AUTH_NAME).send_keys(value)

    def clear_the_name_field(self):
        return self.find_element(AuthLocators.LOCATOR_AUTH_NAME).clear()

    def enter_password(self, value):
        return self.find_element(AuthLocators.LOCATOR_AUTH_PASSWORD).send_keys(value)

    def password_click(self):
        return self.find_element(AuthLocators.LOCATOR_AUTH_PASSWORD).click()

    def clear_the_password_field(self):
        return self.find_element(AuthLocators.LOCATOR_AUTH_PASSWORD).clear()

    def clear_fields(self):
        return self.find_elements(AuthLocators.LOCATOR_AUTH_NAME and AuthLocators.LOCATOR_AUTH_PASSWORD).clear()

    def forgot_password_click(self):
        return self.find_element(AuthLocators.LOCATOR_AUTH_FORGOT_PASSWORD).click()

    def find_password_recovery_form(self):
        return self.find_element(AuthLocators.LOCATOR_AUTH_PASSWORD_RECOVERY)

    def auth_btn_click(self):
        return self.find_element(AuthLocators.LOCATOR_AUTH_BTN).click()

    def find_the_error_message(self):
        return self.find_element(AuthLocators.LOCATOR_AUTH_ERROR_MESSAGE)

    def find_user_account_title(self):
        return self.find_element(AuthLocators.LOCATOR_AUTH_USER_ACCOUNT)

    def exit_of_user_account(self):
        return self.find_element(AuthLocators.LOCATOR_AUTH_EXIT_USER_ACCOUNT).click()

    def user_agreement_click(self):
        return self.find_element(AuthLocators.LOCATOR_AUTH_AGREEMENT).click()

    def auth_vk_click(self):
        return self.find_element(AuthLocators.LOCATOR_AUTH_VK).click()

    def auth_ok_click(self):
        return self.find_element(AuthLocators.LOCATOR_AUTH_OK).click()

    def auth_mail_ru_click(self):
        return self.find_element(AuthLocators.LOCATOR_AUTH_MAIL_RU).click()

    def auth_ya_click(self):
        return self.find_element(AuthLocators.LOCATOR_AUTH_YA).click()

    def auth_regis_click(self):
        return self.find_element(AuthLocators.LOCATOR_AUTH_REGIS).click()

    def open_the_regis_form(self):
        self.go_to_site()
        return self.auth_regis_click()