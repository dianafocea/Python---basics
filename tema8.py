
"""
https://phptravels.net/
"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

chrome = webdriver.Chrome()
chrome.maximize_window()

chrome.get('https://phptravels.net/')

# asteptam ca pagina sa se incarce
sleep(3)

# gasim butonul de Got it pt cookies si dam click pe el > luam element-ul folosind CSS dupa id
chrome.find_element(By.CSS_SELECTOR, 'button#cookie_stop').click()

# dam click pe input-ul de search pentru City Name > luam elementul dupa numele CLASEI
chrome.find_element(By.CLASS_NAME, 'selection').click()

# Gasim input-ul de search si scriem in el caracterele "ist" > luam elementele folosind XPATH dupa atributul aria-controls = valoarea select2-hotels_city-results
hotels_search_field = chrome.find_element(By.XPATH, '//input[@aria-controls="select2-hotels_city-results"]')
hotels_search_field.send_keys("ist")
sleep(2)

# Gasim prima afisare de rezultat "Istanbul" > luam primul child de tip li al lui ul
first_city_option = chrome.find_element(By.XPATH, '//ul[@class="select2-results__options"]/child::li[1]')
sleep(1)
first_city_option.click()

# selectam ultima zi din calendarul de Checkin > luam primul copil al ultimului copil al lui tbody
chrome.find_element(By.NAME, 'checkin').click()
chrome.find_element(By.XPATH, '//tbody/*[last()]/*').click()
sleep(2)

# dam click pe dropdown-ul de Travellers
chrome.find_element(By.CLASS_NAME, 'travellers').click()

# gasim input-urile dupa NAME, stergem ce valori sunt introduse si introducem numarul de camere si adulti
chrome.find_element(By.NAME, 'roomInput').clear()
chrome.find_element(By.NAME, 'roomInput').send_keys('3')
chrome.find_element(By.NAME, 'adults').clear()
chrome.find_element(By.NAME, 'adults').send_keys('6')


# gasim butonul de Search dupa ID si dam click pe el
chrome.find_element(By.ID, 'submit').click()
sleep(2)

# in momentul acesta suntem pe pagina https://phptravels.net/hotels/en/usd/istanbul/02-10-2022/03-10-2022/3/6/0/US

# gasim toate butoanele rezultatelor de Details si le salvam intr-o lista > luam elementele dupa css, folosind tag-ul a cu clasa more_details
images = chrome.find_elements(By.CSS_SELECTOR, 'a.more_details')
images[0].click()
sleep(2)

# in momentul acesta suntem pe pagina https://phptravels.net/hotel/en/usd/istanbul/tria-hotel-istanbul-special/29/02-10-2022/03-10-2022/3/6/0/1/US/0/0/

# deschidem a 3-a imagine din pagina folosind tag-ul ei, iar apoi o inchidem de pe butonul X
chrome.find_elements(By.TAG_NAME, 'img')[3].click()
sleep(1)
chrome.find_element(By.XPATH, '//button[@title="Close"]').click()

# luam elementul a folosind PARTIAL LINK TEXT si dam click pe el
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Amenit').click()
sleep(10)
# luam elementul a folosind LINK TEXT si dam click pe el
rooms_link = chrome.find_element(By.LINK_TEXT, 'Rooms')
coordinates = rooms_link.location_once_scrolled_into_view       # returns dict of X, Y coordinates
chrome.execute_script('window.scrollTo({}, {});'.format(coordinates['x'], coordinates['y']))

rooms_link.click()
sleep(1)

# gasim dupa nume elementul pt cantitatea camerei si selectam valoarea 2
chrome.find_elements(By.NAME, 'room_quantity')[0].click()
chrome.find_element(By.CSS_SELECTOR, 'option[value="2"]').click()

# dam click pe butonul BOOK NOW
chrome.find_element(By.CLASS_NAME, 'ladda-button').click()
sleep(1)

# in momentul acesta suntem pe pagina https://phptravels.net/hotels/booking

# gasim input-ul de firstname dupa atributul name folosind |
chrome.find_element(By.XPATH, '//input[@name="first-name"] | //input[@name="firstname"]').send_keys('Mihai')

# gasim inputul cu placeholder "Email" iar apoi din parinte in parinte si apoi luam text-ul labelului din ultimul parinte
email_label = chrome.find_element(By.XPATH, '//input[@placeholder="Email"]/parent::div/parent::div/label').text
assert email_label == "Email"

# gasim urmatorul frate de la li-ul cu text-ul 2 rooms si verificam ca span-ul lui este Room Price
next_field = chrome.find_element(By.XPATH, '//li[text()="2 Rooms"]/following-sibling::li/span').text
assert next_field == "Room Price:"


# folosim functie sa gasim elemente dupa text() si daca sa dam click pe ele sau nu
def check_element_displayed_by_text(tag, expected_text, is_click):
    element = chrome.find_element(By.XPATH, f'//{tag}[text()="{expected_text}"]')
    element.is_displayed()
    if is_click:
        element.click()

# gasim elemente dupa text complet sau partial folosind XPATH
chrome.find_element(By.XPATH, '//span[contains(text(), "Rooms Qua")]').is_displayed()
check_element_displayed_by_text("li", "2 Rooms", False)
check_element_displayed_by_text("li", "1 Nights ", False)
check_element_displayed_by_text("button", "Confirm Booking", True)

sleep(5)

chrome.quit()