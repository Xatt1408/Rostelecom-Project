import os
from dotenv import load_dotenv
load_dotenv()

# Базовая страница Ростелекома
base_url = "https://b2c.passport.rt.ru"

# Личная инфа зарегистрированного пользователя
valid_name = 'Михаил'
valid_lastname = 'Кобцев'
valid_login = os.getenv('valid_login')
valid_email = os.getenv('valid_email')
valid_phone = os.getenv('valid_phone')
valid_password = os.getenv('valid_password')
# Лицевой счет зарегистрированного пользователя
valid_account = os.getenv('valid_account')

# Информация незарегистрированного пользователя
other_name1 = 'Яна' # 3 символа
other_name2 = 'Яр' # 2 символа
other_name3 = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчш' # 29 символов
other_name4 = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшf' # 30 символов

other_phone = '+79885195941'
other_email = 'fable5969@gmail.com'

other_password1 = 'Ggv423е4ееsfdg23t3gerge5r5h4' # 19 символов
other_password2 = 'ewg24g4g23r12r1r1243f3f43tggw' # 20 символов

# Невалидные значения для проверки полей ввода
invalid_name1 = 'P' # 1 символ
invalid_name2 = 'dsg42wtg24gfdgfdht45hrdfbdfhgrwhw2rgrfbsdv' # 31 символ
invalid_name3 = 'fsgreabbervfdzgveraf43wf23fdsdsgbfdbdbgb3423' # 50 символов
invalid_name4 = 'Karla' # латиница
invalid_name5 = '1254325' # числа
invalid_name6 = '!#!2@#$#><>??}' # спецсимволы

invalid_phone1 = '9875748382485' # номер без +7
invalid_phone2 = 'nomertelefon'  # строка

invalid_email1 = 'dgjfhgei.ru' # email без @
invalid_email2 = 'fdggerr@' # email без домена

invalid_password1 = '56ghTlo' # 7 символов
invalid_password2 = 'ewg24g4g23r12r1r1243f3f43tggw1' # 21 символ
invalid_password3 = 'dsg42wtg24gfdgfdht45hrdfbdfhgrwhw2rgrfbsdvfsds' # 35 символов
invalid_password4 = 'dgj5834f' # 9 символов, без заглавной буквы
invalid_password5 = 'GJGIRIVFKF' # 9 символов, без строчной буквы
invalid_password6 = 'dsfGKGK' # 8 символов, без цифры/без спецсимвола
invalid_password7 = 'Помо351р' # 9 символов, кириллица