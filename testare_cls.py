import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random

class Verify(unittest.TestCase):
    driver = webdriver.Chrome()


    HOME_PAGE_URL = 'https://the-internet.herokuapp.com'
    FORM_AUTH_LINK = (By.LINK_TEXT, "Form Authentication")
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Forgot Password")
    BASIC_AUTH_LINK = (By.LINK_TEXT, "Basic Auth")


    def setUp(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.set_page_load_timeout(5)

    def tearDown(self):
        self.driver.quit()

    def test_navigate_to_home_page(self):
        self.driver.get(*self.HOME_PAGE_URL)


    def test_click_form_auth(self):
        self.driver.find_element(*self.FORM_AUTH_LINK).click()

    def test_click_forgot_password(self):
        self.driver.find_element(*self.FORGOT_PASSWORD_LINK).click()

    def test_click_basic_auth(self):
        self.driver.find_element(*self.BASIC_AUTH_LINK).click()












