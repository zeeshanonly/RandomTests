from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import winsound
import time

last_name = "John"
first_name = "Doe"
email = "john.doe@gmail.com"
passportNo = "HH1234567"
telephoneNo = "03012344567"

def fillField(fieldID:str, value: str):
    # Function to fill text fileds as per the data provided in the arguments
    text_field = driver.find_element(By.ID, fieldID)
    text_field.clear()
    text_field.send_keys(value)

def fillAllFields(ln = last_name, fn = first_name, em = email, passNo = passportNo, tn = telephoneNo):
    # Function to fill all text fields on the form
    lnID = "appointment_newAppointmentForm_lastname"
    fnID = "appointment_newAppointmentForm_firstname"
    emID = "appointment_newAppointmentForm_email"
    rpemID = "appointment_newAppointmentForm_emailrepeat"
    passNoID = "appointment_newAppointmentForm_fields_0__content"
    tnID = "appointment_newAppointmentForm_fields_2__content"

    textList = [ln, fn, em, em, passNo, tn]
    IDList = [lnID, fnID, emID, rpemID, passNoID, tnID]

    for fieldText, fieldID in zip(textList, IDList):
        fillField(fieldID, fieldText)

    # Selecting citizenship (Default is pakistani)
    citizenshipField = driver.find_element(By.ID, "appointment_newAppointmentForm_fields_1__content")
    citizenshipDropdown = Select(citizenshipField)
    options = citizenshipDropdown.options
    citizenshipDropdown.select_by_index(1)

def playBeep(duration = 5): #Plays a beep for duration (seconds)
    frequency = 1000  # Frequency in Hertz (Hz)
    spacingTime = 0.5
    for i in range(0, int(duration/spacingTime)):
        winsound.Beep(frequency, int(spacingTime*1000))
        time.sleep(spacingTime)
# Launch a Chrome browser instance
driver = webdriver.Chrome()

# Open the website with the form
driver.get("https://service2.diplo.de/rktermin/extern/appointment_showForm.do?locationCode=isla&realmId=108&categoryId=1600")

# Find the "Masters appointments" option in the form

while True:
    options_field = driver.find_element(By.ID, "appointment_newAppointmentForm_fields_3__content")
    dropdown = Select(options_field)
    options = dropdown.options
    if not "Master students" in options[3].text:
        time.sleep(1)
        driver.refresh()
    else:
        playBeep()
        dropdown.select_by_index(3)
        fillAllFields()
        while True:
            pass

# Close the browser
driver.quit()
