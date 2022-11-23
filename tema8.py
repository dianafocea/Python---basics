# Tema 8 - SELECTORS

from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

chrome = webdriver.Chrome()
chrome.maximize_window()

# Exerciții obligatorii - grad de dificultate: Usor spre Mediu
# Alege unul sau mai multe din sugestiile de site-uri de mai jos
# - https://www.phptravels.net/
# - http://automationpractice.com/index.php    # link---> invalid
# - https://formy-project.herokuapp.com/
# - https://the-internet.herokuapp.com/
# - https://www.techlistic.com/p/selenium-practice-form.html
# - jules.app
# Alege câte 3 elemente din fiecare tip de selector din următoarele categorii:
# ● Id
chrome.get("https://formy-project.herokuapp.com/form")
chrome.find_element(By.ID, 'first-name').send_keys('Diana')
chrome.find_element(By.ID, 'last-name').send_keys('Focea')
chrome.find_element(By.ID, 'job-title').send_keys('QA Engineer')
#
# # ● Link text
#
chrome.get('https://the-internet.herokuapp.com/')
chrome.find_element(By.LINK_TEXT, "Dynamic Loading").click()
chrome.find_element(By.LINK_TEXT, "Example 2: Element rendered after the fact").click()
chrome.find_element(By.LINK_TEXT, "Elemental Selenium").click()

# ● Parțial link text

chrome.get('https://the-internet.herokuapp.com/')
chrome.find_element(By.PARTIAL_LINK_TEXT, "Codes").click()
chrome.find_element(By.PARTIAL_LINK_TEXT, "5").click()
chrome.find_element(By.PARTIAL_LINK_TEXT, "here").click()

# ● Name  select2-search__field

chrome.get("https://phptravels.net")
chrome.find_element(By.CLASS_NAME, "form-control autocomplete-airport yes").click()
chrome.find_element(By.CLASS_NAME, "form-control autocomplete-airport yes").clear()

sleep(2)

# ● Tag*
# ● Class name*
# ● Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)
# observație:
# - Probabil nu vei găsi un singur website care să cuprindă toate variantele
# de mai sus, astfel că îți recomandăm să folosești mai multe site-uri
#
# - Opțional: La tag și class name vei folosi find elementS! - salvează în listă.
# Interactionează cu un element la alegere din listă.
# Pentru xpath identifică elemente după criteriile de mai jos:
# ● 3 după atribut valoare
# ● 3 după textul de pe element
# ● 1 după parțial text
# ● 1 cu SAU, folosind pipe |
# ● 1 cu *
# ● 1 în care le iei ca pe o listă de xpath și în python ajunge 1 element, deci
# cu (xpath)[1]
# ● 1 în care să folosești parent::
# ● 1 în care să folosești fratele anterior sau de după (la alegere)
# ● 1 funcție ca și cea de la clasă prin care să pot alege eu prin parametru cu
# ce element vreau să interacționez.
# Exerciții extra - Opțional
# https://www.automatetheplanet.com/most-exhaustive-xpath-locators-cheat-sheet/