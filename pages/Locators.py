from selenium.webdriver.common.by import By

class RegisLocators:
    """ Локаторы страницы регистрации """
    LOCATOR_REGIS_TITLE = (By.CSS_SELECTOR, 'h1[class ="card-container__title"]')
    LOCATOR_REGIS_FORM = (By.CSS_SELECTOR, '.rt-input__placeholder')

    LOCATOR_REGIS_NAME = (By.CSS_SELECTOR, 'input[name="firstName"]')
    LOCATOR_REGIS_LASTNAME = (By.CSS_SELECTOR, 'input[name="lastName"]')
    LOCATOR_REGIS_REGION = (By.XPATH, '//input[@autocomplete="new-password"]'[0])
    LOCATOR_REGIS_ADDRESS = (By.ID, 'address')
    LOCATOR_REGIS_PASSWORD = (By.ID, 'password')
    LOCATOR_REGIS_PASSWORD_CONFIRM = (By.ID, 'password-confirm')
    LOCATOR_REGIS_PASSWORD_EYE = (By.CSS_SELECTOR, 'svg.rt-eye-icon.rt-input__eye[aria-hidden="true"]')

    LOCATOR_REGIS_BTN_REGISTER = (By.XPATH, '//button[@name="register"]')

    LOCATOR_REGIS_META_ERROR = (By.CSS_SELECTOR, '.rt-input-container__meta--error')
    LOCATOR_REGIS_ERROR_PASSWORD = (By.CSS_SELECTOR, 'div.new-password-container__password>span.rt-input-container__meta--error')
    LOCATOR_REGIS_ERROR_REPEAT_USER = (By.CSS_SELECTOR, 'h2.card-modal__title')

    LOCATOR_REGIS_AGREEMENT = (By.CSS_SELECTOR, 'a.rt-link.rt-link--orange[target="_blank"]')

class AuthLocators:
    """ Локаторы страницы авторизации """
    LOCATOR_AUTH_TAB_PHONE = (By.ID, 't-btn-tab-phone')
    LOCATOR_AUTH_TAB_EMAIL = (By.ID, 't-btn-tab-mail')
    LOCATOR_AUTH_TAB_LOGIN = (By.ID, 't-btn-tab-login')
    LOCATOR_AUTH_TAB_LS = (By.ID, 't-btn-tab-ls')
    LOCATOR_AUTH_TAB_FIELD = (By.CSS_SELECTOR, 'span.rt-input__placeholder')

    LOCATOR_AUTH_NAME = (By.ID, 'username')
    LOCATOR_AUTH_PASSWORD = (By.ID, 'password')
    LOCATOR_AUTH_FORGOT_PASSWORD = (By.ID, 'forgot_password')
    LOCATOR_AUTH_PASSWORD_RECOVERY = (By.CSS_SELECTOR, '.card-container__title')

    LOCATOR_AUTH_BTN = (By.XPATH, '//*[@id= "kc-login"]')
    LOCATOR_AUTH_USER_ACCOUNT = (By.CSS_SELECTOR, '.card-title')
    LOCATOR_AUTH_EXIT_USER_ACCOUNT = (By.ID, 'logout-btn')

    LOCATOR_AUTH_META_ERROR = (By.CSS_SELECTOR, '.rt-input-container__meta--error')
    LOCATOR_AUTH_ERROR_MESSAGE = (By.ID, 'form-error-message')

    LOCATOR_AUTH_REGIS = (By.XPATH, '//a[@id="kc-register"]')
    LOCATOR_AUTH_AGREEMENT = (By.CSS_SELECTOR, 'a.rt-link.rt-link--orange[target="_blank"]')

    LOCATOR_AUTH_VK = (By.ID, 'oidc_vk')
    LOCATOR_AUTH_OK = (By.ID, 'oidc_ok')
    LOCATOR_AUTH_MAIL_RU = (By.ID, 'oidc_mail')
    LOCATOR_AUTH_YA = (By.ID, 'oidc_ya')