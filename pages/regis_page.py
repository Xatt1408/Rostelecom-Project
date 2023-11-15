from .base_page import BasePage
from .Locators import RegisLocators

class RegistrationPage(BasePage):
    def enter_name(self, value):
        return self.find_element(RegisLocators.LOCATOR_REGIS_NAME).send_keys(value)

    def clear_the_name_field(self):
        return self.find_element(RegisLocators.LOCATOR_REGIS_NAME).clear()

    def enter_lastname(self, value):
        return self.find_element(RegisLocators.LOCATOR_REGIS_LASTNAME).send_keys(value)

    def clear_the_lastname_field(self):
        return self.find_element(RegisLocators.LOCATOR_REGIS_LASTNAME).clear()

    def enter_address(self, value):
        return self.find_element(RegisLocators.LOCATOR_REGIS_ADDRESS).send_keys(value)

    def clear_the_address_field(self):
        return self.find_element(RegisLocators.LOCATOR_REGIS_ADDRESS).clear()

    def enter_password(self, value):
        return self.find_element(RegisLocators.LOCATOR_REGIS_PASSWORD).send_keys(value)

    def clear_the_password_field(self):
        return self.find_element(RegisLocators.LOCATOR_REGIS_PASSWORD).clear()

    def enter_password_confirm(self, value):
        return self.find_element(RegisLocators.LOCATOR_REGIS_PASSWORD_CONFIRM).send_keys(value)

    def clear_the_password_confirm_field(self):
        return self.find_element(RegisLocators.LOCATOR_REGIS_PASSWORD_CONFIRM).clear()

    def click_btn_register(self):
        return self.find_element(RegisLocators.LOCATOR_REGIS_BTN_REGISTER).click()

    def download_regis_page(self):
        return self.find_element(RegisLocators.LOCATOR_REGIS_TITLE)

    def content_of_the_registration_form(self):
        all_list = self.find_elements(RegisLocators.LOCATOR_REGIS_FORM)
        return [x.text for x in all_list]

    def empty_fields_in_the_registration_form(self):
        return self.find_elements(RegisLocators.LOCATOR_REGIS_META_ERROR)

    def find_the_error_password(self):
        return self.find_element(RegisLocators.LOCATOR_REGIS_ERROR_PASSWORD)

    def find_the_error_message(self):
        return self.find_element(RegisLocators.LOCATOR_REGIS_META_ERROR)

    def find_repeat_user(self):
        return self.find_element(RegisLocators.LOCATOR_REGIS_ERROR_REPEAT_USER)

    def click_icon_eye(self):
        return self.find_element(RegisLocators.LOCATOR_REGIS_PASSWORD_EYE).click()

    def user_agreement_click(self):
        return self.find_element(RegisLocators.LOCATOR_REGIS_AGREEMENT).click()