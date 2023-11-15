import pytest
from selenium import webdriver
from pages.auth_page import AuthPage
from pages.regis_page import RegistrationPage

@pytest.fixture(scope='session')
def browser():
   driver = webdriver.Chrome(r'C:\Users\Xatt\PycharmProjects\chromedriver.exe')
   driver.maximize_window()
   driver.implicitly_wait(5)
   yield driver
   driver.quit()

@pytest.fixture(scope='session')
def auth_page(browser):
   auth_page = AuthPage(browser)
   return auth_page

@pytest.fixture(scope='session')
def regis_page(browser):
   regis_page = RegistrationPage(browser)
   return regis_page