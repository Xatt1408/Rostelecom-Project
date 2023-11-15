import pytest
from settings import *

''' АВТОРИЗАЦИЯ. МЕНЮ ВЫБОРА ТИПА АУТЕНТИФИКАЦИИ '''
## Test 1
def test_option_tab_phone_authorization(browser, auth_page):
    """ Проверка, что возможен выбор типа аутентификации по номеру телефона """
    auth_page.go_to_site()
    auth_page.tab_phone_click()
    element = auth_page.tab_find_field_description()
    assert element.text == "Мобильный телефон"

## Test 2
def test_option_tab_email_authorization(browser, auth_page):
    """ Проверка, что возможен выбор типа аутентификации по адресу электронной почты """
    auth_page.go_to_site()
    auth_page.tab_email_click()
    element = auth_page.tab_find_field_description()
    assert element.text == "Электронная почта"

## Test 3
def test_option_tab_ls_authorization(browser, auth_page):
    """ Проверка, что возможен выбор типа аутентификации по лицевому счету """
    auth_page.go_to_site()
    auth_page.tab_ls_click()
    element = auth_page.tab_find_field_description()
    assert element.text == "Лицевой счёт"

## Test 4
def test_option_tab_login_authorization(browser, auth_page):
    """ Проверка, что возможен выбор типа аутентификации по логину """
    auth_page.go_to_site()
    auth_page.tab_login_click()
    element = auth_page.tab_find_field_description()
    assert element.text == "Логин"

## Test 5
@pytest.mark.parametrize('username', [valid_email, valid_phone, valid_login, valid_account],
                         ids=['email', 'phone', 'login', 'ls'])
def test_automatic_tab_authorization(browser, auth_page, username):
    """ Проверка, что при вводе номера телефона/почты/логина/лицевого счета таб выбора типа аутентификации меняется
    автоматически """
    auth_page.go_to_site()
    auth_page.clear_fields()
    auth_page.enter_name(username)
    auth_page.password_click()
    if username == valid_phone:
        assert auth_page.tab_find_field_description().text == "Мобильный телефон"
    elif username == valid_email:
        assert auth_page.tab_find_field_description().text == "Электронная почта"
    elif username == valid_login:
        assert auth_page.tab_find_field_description().text == "Логин"
    else:
        assert auth_page.tab_find_field_description().text == "Лицевой счёт"


''' АВТОРИЗАЦИЯ. ПОЗИТИВНЫЕ СЦЕНАРИИ АВТОРИЗАЦИИ '''
## Test 6
def test_by_phone_authorization(browser, auth_page):
    """ Проверка авторизации по номеру телефона зарегистрированного в системе пользователя """
    auth_page.go_to_site()
    auth_page.tab_phone_click()
    auth_page.clear_fields()
    auth_page.enter_name(valid_phone)
    auth_page.enter_password(valid_password)
    auth_page.auth_btn_click()
    assert auth_page.get_relative_link() == '/account_b2c/page'
    assert auth_page.find_user_account_title().text == "Учетные данные"
    auth_page.exit_of_user_account()

## Test 7
def test_by_email_authorization(browser, auth_page):
    """ Проверка авторизации по адресу электронной почты зарегистрированного в системе пользователя """
    auth_page.go_to_site()
    auth_page.tab_email_click()
    auth_page.clear_fields()
    auth_page.enter_name(valid_email)
    auth_page.enter_password(valid_password)
    auth_page.auth_btn_click()
    assert auth_page.get_relative_link() == '/account_b2c/page'
    assert auth_page.find_user_account_title().text == "Учетные данные"
    auth_page.exit_of_user_account()

## Test 8
def test_by_login_authorization(browser, auth_page):
    """ Проверка авторизации по логину зарегистрированного в системе пользователя """
    auth_page.go_to_site()
    auth_page.tab_login_click()
    auth_page.clear_fields()
    auth_page.enter_name(valid_login)
    auth_page.enter_password(valid_password)
    auth_page.auth_btn_click()
    assert auth_page.get_relative_link() == '/account_b2c/page'
    assert auth_page.find_user_account_title().text == "Учетные данные"
    auth_page.exit_of_user_account()

## Test 9
def test_by_ls_authorization(browser, auth_page):
    """ Проверка авторизации по лицевому счету зарегистрированного в системе пользователя """
    auth_page.go_to_site()
    auth_page.tab_ls_click()
    auth_page.clear_fields()
    auth_page.enter_name(valid_account)
    auth_page.enter_password(valid_password)
    auth_page.auth_btn_click()
    assert auth_page.get_relative_link() == '/account_b2c/page'
    assert auth_page.find_user_account_title().text == "Учетные данные"
    auth_page.exit_of_user_account()

''' АВТОРИЗАЦИЯ. НЕГАТИВНЫЕ СЦЕНАРИИ АВТОРИЗАЦИИ '''
## Test 10
def test_invalid_password_tab_phone_in_authorization(browser, auth_page):
    """ Проверка, что авторизация по номеру телефона не проходит при вводе недействительного пароля, отображается
    сообщение об ошибке """
    auth_page.go_to_site()
    auth_page.tab_phone_click()
    auth_page.clear_fields()
    auth_page.enter_name(valid_phone)
    auth_page.enter_password(other_password1)
    auth_page.auth_btn_click()
    error = auth_page.find_the_error_message()
    assert error.text == "Неверный логин или пароль"

## Test 11
def test_invalid_password_tab_email_in_authorization(browser, auth_page):
    """ Проверка, что авторизация по адресу электронной почты не проходит при вводе недействительного пароля,
    отображается сообщение об ошибке """
    auth_page.go_to_site()
    auth_page.tab_email_click()
    auth_page.clear_fields()
    auth_page.enter_name(valid_email)
    auth_page.enter_password(other_password1)
    auth_page.auth_btn_click()
    error = auth_page.find_the_error_message()
    assert error.text == "Неверный логин или пароль"

## Test 12
def test_invalid_phone_format_in_authorization(browser, auth_page):
    """ Проверка, что авторизация не проходит при вводе номера телефона незарегистрированного в системе пользователя,
    отображается сообщение об ошибке """
    auth_page.go_to_site()
    auth_page.tab_phone_click()
    auth_page.clear_fields()
    auth_page.enter_name(other_phone)
    auth_page.enter_password(valid_password)
    auth_page.auth_btn_click()
    error = auth_page.find_the_error_message()
    assert error.text == "Неверный логин или пароль"

## Test 13
def test_invalid_email_format_in_authorization(browser, auth_page):
    """ Проверка, что авторизация не проходит при вводе email незарегистрированного в системе пользователя, отображается
   сообщение об ошибке """
    auth_page.go_to_site()
    auth_page.tab_email_click()
    auth_page.clear_fields()
    auth_page.enter_name(other_email)
    auth_page.enter_password(valid_password)
    auth_page.auth_btn_click()
    error = auth_page.find_the_error_message()
    assert error.text == "Неверный логин или пароль"

''' АВТОРИЗАЦИЯ. ПЕРЕХОД ПО ССЫЛКАМ. '''
## Test 14
def test_go_to_the_password_recovery_form(browser, auth_page):
    """ Проверка, что осуществлен переход к форме 'Восстановление пароля' """
    auth_page.go_to_site()
    auth_page.clear_fields()
    auth_page.forgot_password_click()
    element = auth_page.find_password_recovery_form()
    assert element.text == "Восстановление пароля"

## Test 15
def test_go_to_the_registration_form(browser, auth_page, regis_page):
    """ Проверка,что осуществлен переход к форме 'Регистрация' """
    auth_page.go_to_site()
    auth_page.auth_regis_click()
    element = regis_page.download_regis_page()
    assert element.text == "Регистрация"

## Test 16
def test_go_to_the_user_agreement(browser, auth_page):
    """ Проверка, что осуществлен переход к пользовательскому соглашению """
    auth_page.go_to_site()
    auth_page.clear_fields()
    auth_page.user_agreement_click()
    all_windows = browser.window_handles
    browser.switch_to.window(all_windows[1])
    assert len(all_windows) == 2
    assert browser.title == 'User agreement'

## Test 17
def test_go_to_the_vk_for_authorization(browser, auth_page):
    """ Проверка, что осуществлен переход для авторизации через 'ВКонтакте' """
    auth_page.go_to_site()
    auth_page.clear_fields()
    auth_page.auth_vk_click()
    current_url = auth_page.get_current_url()
    assert 'vk' in current_url

## Test 18
def test_go_to_the_ok_for_authorization(browser, auth_page):
    """ Проверка, что осуществлен переход для авторизации через 'Одноклассники' """
    auth_page.go_to_site()
    auth_page.clear_fields()
    auth_page.auth_ok_click()
    current_url = auth_page.get_current_url()
    assert 'ok' in current_url

## Test 19
def test_go_to_the_mail_ru_for_authorization(browser, auth_page):
    """ Проверка, что осуществлен переход для авторизации через 'Майл.ру' """
    auth_page.go_to_site()
    auth_page.clear_fields()
    auth_page.auth_mail_ru_click()
    current_url = auth_page.get_current_url()
    assert 'mail' in current_url

## Test 20
def test_go_to_the_ya_for_authorization(browser, auth_page):
    """ Проверка, что осуществлен переход для авторизации через 'Яндекс' """
    auth_page.go_to_site()
    auth_page.clear_fields()
    auth_page.auth_ya_click() # click не проходит, переход не осуществлен
    current_url = auth_page.get_current_url()
    assert 'yandex' in current_url