
# Tema 9 - VERIFICATORI
# Exerciții obligatorii - grad de dificultate: Usor spre Mediu

from selenium import webdriver
import unittest
from unittest import TestCase
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Implementează o clasă Login care să moștenească unittest.TestCase
# Gasește elementele în partea de sus folosind ce selectors dorești:
# - setUp()
# - Driver
# https://the-internet.herokuapp.com/
# Click pe Form Authentication

# tearDown()
# Quit browser
#
class Login(unittest.TestCase):
    chrome = webdriver.Chrome()
    chrome.maximize_window()

    FORM_LINK = (By.LINK_TEXT, "Form Authentication")
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login"]/button/i')
    ATTR_BUTTON = (By.LINK_TEXT, "Elemental Selenium")
    ID_FIELD = (By.ID, "username")
    PASS_FIELD = (By.ID, "password")
    LOGIN_ERROR = (By.XPATH, '//*[@id="flash"]')


    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)
        self.chrome.get("https://the-internet.herokuapp.com/")
        self.chrome.find_element(*self.FORM_LINK).click()


    def tearDown(self):
        self.chrome.quit()


# ● Test 1
# - Verifică dacă noul url e corect
    def test_page_iscorrect(self):
        actual_title = self.chrome.title
        expected_title = "The Internet"
        self.assertEqual(actual_title, expected_title, "Title incorrect")


# ● Test 2
# - Verifică dacă page title e corect
    def test_page_title(self):
        actual_title = self.chrome.title
        expected_title = "The Internet"
        self.assertEqual(actual_title, expected_title, "Title incorrect")

# ● Test 3
# - Verifică textul de pe elementul xpath=//h2 e corect
    def test_xpath_h2_iscorrect(self):
        actual_h2title = self.chrome.title
        expected_h2title = "The Internet"
        self.assertEqual(actual_h2title, expected_h2title, "h2 title incorrect")

# ● Test 4
# - Verifică dacă butonul de login este displayed
    def test_button_isdisplayed(self):
        btn = self.chrome.find_element(*self.LOGIN_BUTTON)
        self.assertTrue(btn.is_displayed(), 'Butonul nu este displayed')

# ● Test 5
# - Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect
    def test_href_attribute_iscorrect(self):
        actual = self.chrome.find_element(*self.ATTR_BUTTON).get_attribute('href')
        expected = 'http://elementalselenium.com/'
        self.assertEqual(actual, expected, 'The attribute value is not correct')

# ● Test 6
# - Lasă goale user și pass
# - Click login
# - Verifică dacă eroarea e displayed

#         btn = self.chrome.find_element(*self.LOGIN_BUTTON)
#         self.assertTrue(btn.is_displayed(), 'Butonul nu este displayed')

    def test_login_eroor_isdisplayed(self):
        id_login = self.chrome.find_element(*self.ID_FIELD).send_keys("")
        pass_login = self.chrome.find_element(*self.PASS_FIELD).send_keys("")
        login = self.chrome.find_element(*self.LOGIN_BUTTON).click()
        login_error = self.chrome.find_element(*self.LOGIN_ERROR)
        self.assertTrue(login_error.is_displayed()), 'Login error not displayed'


# ● Test 7
# - Completează cu user și pass invalide
# - Click login
# - Verifică dacă mesajul de pe eroare e corect
# - Este și un x pus acolo extra așa că vom folosi soluția de mai jos
# expected = 'Your username is invalid!'
# self.assertTrue(expected in actual, 'Error message text is
# incorrect')
# ● Test 8
# - Lasă goale user și pass
# - Click login
# - Apasă x la eroare
# - Verifică dacă eroarea a dispărut
# ● Test 9
# - Ia ca o listă toate //label
# - Verifică textul ca textul de pe ele să fie cel așteptat (Username și
# Password)
# - Aici e ok să avem 2 asserturi
#
# ● Test 10
# - Completează cu user și pass valide
# - Click login
# - Verifică ca noul url CONTINE /secure
# - Folosește un explicit wait pentru elementul cu clasa ’flash succes’
# - Verifică dacă elementul cu clasa=’flash succes’ este displayed
#
# - Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’
# ● Test 11
# - Completează cu user și pass valide
# - Click login
# - Click logout
# - Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login
#
# Exerciții Opționale - grad de dificultate: Mediu spre greu: may need Google
# ● Test 12 - brute force password hacking
# - Completează user tomsmith
# - Găsește elementul //h4
# - Ia textul de pe el și fă split după spațiu. Consideră fiecare cuvânt ca o
# potențială parolă.
# - Folosește o structură iterativă prin care să introduci rând pe rând
# parolele și să apeși pe login.
# - La final testul trebuie să îmi printeze fie
# ‘Nu am reușit să găsesc parola’
# ‘Parola secretă este [parola]’