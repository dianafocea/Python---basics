# fisier pt verificare cod
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select



# 3 selectors by ID

chrome = webdriver.Chrome()                       # lansam browersul de chrome
chrome.get("https://phptravels.net/visa")              # navigam la link-ul respectiv prin metoda get
chrome.find_element(By.ID, "currency").click()  # click pe moneda actuala
sleep(1)
chrome.find_element(By.ID, "languages").click() # click pe limba aleasa
sleep(1)
chrome.find_element(By.ID, "ACCOUNT").click()   # click pe numele de cont
sleep(1)
chrome.quit()
# --------------------------------------------------------------------------------------------------------
# 3 selectors by LINK TEXT

chrome = webdriver.Chrome()                           # lansam browersul de chrome
chrome.get("https://formy-project.herokuapp.com")     # navigam la url respectiv
chrome.find_element(By.LINK_TEXT, "Buttons").click()
sleep(1)
chrome.find_element(By.LINK_TEXT, "Form").click()
sleep(1)
chrome.find_element(By.ID, "logo").click()
sleep(1)
chrome.find_element(By.LINK_TEXT, "Key and Mouse Press").click()
sleep(1)
chrome.quit()
# --------------------------------------------------------------------------------------------------------
# 3 selectors by PARTIAL LINK TEXT

chrome = webdriver.Chrome()
chrome.get("https://the-internet.herokuapp.com")
chrome.find_element(By.PARTIAL_LINK_TEXT, "File D").click()     # deschidem linkul File Download
sleep(1)
chrome.back()                                                   # navigam inapoi
chrome.find_element(By.PARTIAL_LINK_TEXT, "Key").click()        # deschidem Key Presses
sleep(1)
chrome.find_element(By.PARTIAL_LINK_TEXT, "Element").click()    # deschidem link-ul spre pagina Elemental Selennium
sleep(5)
chrome.quit()
# --------------------------------------------------------------------------------------------------------
# 3 selectors by NAME

chrome = webdriver.Chrome()
chrome.get("https://www.techlistic.com/p/selenium-practice-form.html")
chrome.find_element(By.ID,'ez-accept-all').click()                          # confirmam cookie-ul

chrome.find_element(By.NAME, "firstname").send_keys("Cristi")
chrome.find_element(By.NAME, "lastname").send_keys("Popescu")
chrome.find_element(By.NAME, "continents").click()
sleep(5)
chrome.quit()
# --------------------------------------------------------------------------------------------------------
# 3 selectors by TAG (we use find elementS - saved on the list)

chrome = webdriver.Chrome()
chrome.get("https://www.techlistic.com/p/selenium-practice-form.html")
chrome.find_element(By.ID,'ez-accept-all').click()                          # confirmam cookie-ul

keyboard_list = chrome.find_elements(By.TAG_NAME, "input")
keyboard_list[0].send_keys("Gabi")
keyboard_list[1].send_keys("Coman")
keyboard_list[11].send_keys("12.11.2022")
sleep(4)
chrome.quit()
# --------------------------------------------------------------------------------------------------------
# 3 selectors by CLASSS (we use find elementS - saved on the list)

chrome = webdriver.Chrome()
chrome.get("https://phptravels.net/signup")

keyboard_class = chrome.find_elements(By.CLASS_NAME, "form-control")
keyboard_class[0].send_keys("Adi")
keyboard_class[1].send_keys("Popa")
keyboard_class[2].send_keys("0345123132")
keyboard_class[3].send_keys("office@travelRO.com")
sleep(5)
chrome.quit()
# --------------------------------------------------------------------------------------------------------
# 3 selectors by CSS (1 by ID, 1 by CLASS, 1 by attribute=partial_value)

chrome = webdriver.Chrome()
chrome.maximize_window()
chrome.get("https://phptravels.net/")

chrome.find_element(By.CSS_SELECTOR, "#checkin").click()        # dupa id (folosim #)
sleep(1)
chrome.find_element(By.CSS_SELECTOR, ".checkout").click()       # dupa clasa (folosim .)
sleep(1)
chrome.find_element(By.CSS_SELECTOR, "input[placeholder*='your email']").send_keys("office@romania.ro")
sleep(5)
chrome.quit()
# --------------------------------------------------------------------------------------------------------
# XPATH
# 3 by attribut value

chrome = webdriver.Chrome()
chrome.get("https://formy-project.herokuapp.com/autocomplete")

chrome.find_element(By.XPATH, "//input[@id='autocomplete']").send_keys("office@romania.ro")
chrome.find_element(By.XPATH, "//input[@id='locality']").send_keys("Cluj")
chrome.find_element(By.XPATH, "//input[@id='administrative_area_level_1']").send_keys("Romania")
sleep(3)

# 3 by text of elements
chrome.get("https://formy-project.herokuapp.com/buttons")
chrome.find_element(By.XPATH, "//button[contains(text(), 'Primary')]").click()
sleep(0.5)
chrome.find_element(By.XPATH, "//button[contains(text(), 'Success')]").click()
sleep(0.5)
chrome.find_element(By.XPATH, "//button[contains(text(), 'Info')]").click()
sleep(0.5)

# 1 by partial text
chrome.find_element(By.XPATH, "//button[contains(text(), 'War')]").click()
sleep(0.5)

# 1 with OR(SAU), using pipes |  (primul gasit dintre variante)
chrome.find_element(By.XPATH, "//button[contains(text(), 'NuExista1')] | //button[contains(text(), 'Middle')] | //button[contains(text(), 'NuExista2')]").click()
sleep(1)

# 1 with *
chrome.get("https://formy-project.herokuapp.com/form")
chrome.find_element(By.XPATH, "//*[@id='job-title']").send_keys("QA Automation")
sleep(1)

# 1 which you take them as an xpath list and then in python is sent 1 element, so with (xpath)[1]
chrome.find_element(By.XPATH, '(//input[@class="form-control"])[4]').click()
sleep(1)

# 1 in which to use parent::
parent_text = chrome.find_element(By.XPATH,"//label[contains(text(), 'First name')]/parent::strong").text
print(parent_text)
sleep(1)

# 1 in which to use the brother before or after (your choice)
chrome.find_element(By.XPATH,"//label[contains(text(), 'First name')]/parent::strong/following-sibling::input").send_keys("CRISTI")
sleep(1)

# 1 function like the one in the class through which I can choose by parameter which element I want to interact with.

chrome.get("https://www.techlistic.com/p/selenium-practice-form.html")
chrome.find_element(By.ID,'ez-accept-all').click()
def checkbox(name,input_id):
    chrome.find_element(By.XPATH, f"//input[@name='{name}']")
    chrome.find_element(By.XPATH, f"//input[@id='{input_id}']").click()

checkbox("profession","profession-1")
checkbox("tool","tool-2")
sleep(5)
chrome.quit()
