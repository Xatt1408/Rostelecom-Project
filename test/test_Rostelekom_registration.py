import pytest
from settings import *

''' РЕГИСТРАЦИЯ. ФОРМАТ ПОЛЕЙ ФОРМЫ РЕГИСТРАЦИИ '''
## Test 1
def test_content_of_the_registration_form(browser, auth_page, regis_page):
   """ Проверка, что форма регистрации содержит все обязательные поля в соответствии с требованиями """
   auth_page.open_the_regis_form()
   elements = regis_page.content_of_the_registration_form()
   assert "Имя" and "Фамилия" and "Регион" and "E-mail или мобильный телефон" and "Пароль" and "Подтверждение пароля" in elements

## Test 2
@pytest.mark.parametrize('invalid_name', [invalid_name1, invalid_name2, invalid_name3, invalid_name4, invalid_name5, invalid_name6],
                         ids=["1 char", "31 chars", "50 chars", "english", "numbers", "special"])
def test_invalid_format_of_the_name_field_in_the_registration_form(browser, auth_page, regis_page, invalid_name):
    """" Проверка, что поле "Имя" не принимает формат отличный от требований, отображается сообщение об ошибке """
    auth_page.open_the_regis_form()
    regis_page.clear_the_name_field()
    regis_page.enter_name(invalid_name)
    regis_page.click_btn_register()
    error = regis_page.find_the_error_message()
    assert error.text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

## Test 3
@pytest.mark.parametrize('invalid_name', [invalid_name1, invalid_name2, invalid_name3, invalid_name4, invalid_name5, invalid_name6],
                         ids=["1 char", "31 chars", "50 chars", "english", "numbers", "special"])
def test_invalid_format_of_the_lastname_field_in_the_registration_form(browser, auth_page, regis_page, invalid_name):
    """" Проверка, что поле "Фамилия" не принимает формат отличный от требований, отображается сообщение об ошибке """
    auth_page.open_the_regis_form()
    regis_page.clear_the_lastname_field()
    regis_page.enter_lastname(invalid_name)
    regis_page.click_btn_register()
    error = regis_page.find_the_error_message()
    assert error.text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

## Test 4
@pytest.mark.parametrize('invalid_phone', [invalid_phone1, invalid_phone2], ids=["phone without +7", "letters"])
def test_invalid_format_of_the_phone_field_in_the_registration_form(browser, auth_page, regis_page, invalid_phone):
   """" Проверка,что поле "Мобильный телефон" не принимает формат данных отличный от маски ввода, отображается
   сообщение об ошибке """
   auth_page.open_the_regis_form()
   regis_page.clear_the_address_field()
   regis_page.enter_address(invalid_phone)
   regis_page.click_btn_register()
   error = regis_page.find_the_error_message()
   assert error.text == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"

## Test 5
@pytest.mark.parametrize('invalid_email', [invalid_email1, invalid_email2], ids=["email without @", "email without domain"])
def test_invalid_format_of_the_email_field_in_the_registration_form(browser, auth_page, regis_page, invalid_email):
    """" Проверка,что поле "Email" не принимает формат данных отличный от маски ввода example@email.ru,
    отображается сообщение об ошибке """
    auth_page.open_the_regis_form()
    regis_page.clear_the_address_field()
    regis_page.enter_address(invalid_email)
    regis_page.click_btn_register()
    error = regis_page.find_the_error_message()
    assert error.text == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"

## Test 6
@pytest.mark.parametrize('invalid_password', [invalid_password1, invalid_password2, invalid_password3, invalid_password4,
                                              invalid_password5, invalid_password6, invalid_password7],
                         ids=["7 chars", "21 chars", "35 chars", "9 chars without capital letter",
                              "9 chars without lowercase letter", "8 chars without number/special", "9 chars cyrillic"])

def test_invalid_format_of_the_password_field_in_the_registration_form(browser, auth_page, regis_page, invalid_password):
    """" Проверка, что поле "Пароль" не принимает формат данных отличный от требований, отображается сообщение об ошибке """
    auth_page.open_the_regis_form()
    regis_page.clear_the_password_field()
    regis_page.click_icon_eye()
    regis_page.enter_password(invalid_password)
    regis_page.click_btn_register()
    if invalid_password == invalid_password1:
        assert regis_page.find_the_error_password().text == "Длина пароля должна быть не менее 8 символов"
    elif invalid_password == invalid_password2 or invalid_password == invalid_password3:
        assert regis_page.find_the_error_password().text == "Длина пароля должна быть не более 20 символов"
    elif invalid_password == invalid_password4:
        assert regis_page.find_the_error_password().text == "Пароль должен содержать хотя бы одну заглавную букву"
    elif invalid_password == invalid_password5:
        assert regis_page.find_the_error_password().text == "Пароль должен содержать хотя бы одну строчную букву"
    elif invalid_password == invalid_password6:
        assert regis_page.find_the_error_password().text == "Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру"
    else:
        assert regis_page.find_the_error_password().text == "Пароль должен содержать только латинские буквы"

''' РЕГИСТРАЦИЯ. НЕГАТИВНЫЕ СЦЕНАРИИ. ОТПРАВКА ФОРМЫ '''
## Test 7
def test_repeat_email_in_the_registration_form(browser, auth_page, regis_page):
   """ Проверка, что повторная регистрация по email невозможна,отображается сообщение о существовании учетной записи """
   auth_page.open_the_regis_form()
   regis_page.enter_name(valid_name)
   regis_page.enter_lastname(valid_lastname)
   regis_page.enter_address(valid_email)
   regis_page.enter_password(valid_password)
   regis_page.enter_password_confirm(valid_password)
   regis_page.click_btn_register()
   message = regis_page.find_repeat_user()
   assert message.text == "Учётная запись уже существует"

## Test 8
def test_repeat_phone_in_the_registration_form(browser, auth_page, regis_page):
   """ Проверка, что повторная регистрация по номеру телефона невозможна,отображается сообщение о существовании учетной записи """
   auth_page.open_the_regis_form()
   regis_page.enter_name(other_name1)
   regis_page.enter_lastname(other_name2)
   regis_page.enter_address(valid_phone)
   regis_page.enter_password(other_password1)
   regis_page.enter_password_confirm(other_password1)
   regis_page.click_btn_register()
   message = regis_page.find_repeat_user()
   assert message.text == "Учётная запись уже существует"

## Test 9
def test_empty_field_email_in_the_registration_form(browser, auth_page, regis_page):
    """" Проверка, что регистрация невозможна без email/номера телефона, отображается сообщение о необходимости заполнения поля """
    auth_page.open_the_regis_form()
    regis_page.enter_name(other_name2)
    regis_page.enter_lastname(other_name1)
    regis_page.enter_password(other_password2)
    regis_page.enter_password_confirm(other_password2)
    regis_page.click_btn_register()
    error = regis_page.find_the_error_message()
    assert error.text == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"

## Test 10
def test_empty_field_password_in_the_registration_form(browser, auth_page, regis_page):
    """" Проверка, что регистрация невозможна без указания пароля, отображается сообщение о необходимости заполнения поля """
    auth_page.open_the_regis_form()
    regis_page.enter_name(other_name3)
    regis_page.enter_lastname(other_name3)
    regis_page.enter_address(valid_phone)
    regis_page.click_btn_register()
    error = regis_page.find_the_error_message()
    assert error.text == "Длина пароля должна быть не менее 8 символов"

## Test 11
def test_invalid_format_of_the_password_confirm_field_in_the_registration_form(browser, auth_page, regis_page):
    """" Проверка, что регистрация невозможна без подтверждения пароля, отображается сообщение об ошибке """
    auth_page.open_the_regis_form()
    regis_page.enter_name(other_name4)
    regis_page.enter_lastname(other_name4)
    regis_page.enter_address(other_email)
    regis_page.enter_password(other_password1)
    regis_page.enter_password_confirm(other_password2)
    regis_page.click_btn_register()
    error = regis_page.find_the_error_message()
    assert error.text == "Пароли не совпадают"

## Test 12
def test_empty_fields_in_the_registration_form(browser, auth_page, regis_page):
   """" Проверка,что невозможно зарегистрироваться с пустыми полями формы,отображаются сообщения о необходимости заполнения полей """
   auth_page.open_the_regis_form()
   regis_page.click_btn_register()
   error = regis_page.empty_fields_in_the_registration_form()
   assert len(error) == 5

''' РЕГИСТРАЦИЯ. ПЕРЕХОД ПО ССЫЛКАМ '''
## Test 13
def test_go_to_the_user_agreement(browser, auth_page, regis_page):
   """ Проверка, что осуществлен переход к пользовательскому соглашению """
   auth_page.open_the_regis_form()
   regis_page.user_agreement_click()
   all_windows = browser.window_handles
   browser.switch_to.window(all_windows[1])
   assert len(all_windows) == 2
   assert browser.title == 'User agreement'