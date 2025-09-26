from http import client
from pydoc import cli
import time
import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

service_obj = Service("C:/Users/Tulip/Downloads/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)
driver.maximize_window()
driver.implicitly_wait(5)

# Load env variable
load_dotenv()

url = os.getenv("URL")
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

# url = os.getenv("URL_prod")
# email = os.getenv("EMAIL_prod")
# password = os.getenv("PASSWORD_prod")

wait = WebDriverWait(driver, 30)
quick_wait = WebDriverWait(driver, 1)
actions = ActionChains(driver)

# ======================================================================================================================

# login form
driver.get(url)
driver.find_element(By.ID, 'email').send_keys(email)
driver.find_element(By.ID, 'password').send_keys(password)
driver.find_element(By.CLASS_NAME, 'login-button').click()
time.sleep(5)

# login validation wait
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'swal2-container')))

# ======================================================================================================================

# dashboard page validation
welcome = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'header-title'))).text
print(f'Login successful: {welcome}')
assert 'Welcome' in welcome

# ======================================================================================================================

# click the organizaton button
org_btn = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'Organization')])[1]")))
org_btn_text = org_btn.text
print(f"org_btn_text: {org_btn_text}")
driver.execute_script("arguments[0].click();", org_btn)

org_page = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='page-header-title']")))
org_page_title = org_page.text
assert "Organizations" in org_page_title

# ======================================================================================================================

# click the page button
btn_13 = wait.until(EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='13']")))
driver.execute_script("arguments[0].scrollIntoView(true);", btn_13)
driver.execute_script("arguments[0].click();", btn_13)

# ======================================================================================================================

# click the organization card
org_arrow = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='org-card-arrow'])[8]")))
org_name = driver.find_element(By.XPATH, "//h6[normalize-space()='Automated Test ORG']").text
print(f"org_name: {org_name}")
driver.execute_script("arguments[0].click();", org_arrow)

# ======================================================================================================================

# portal_page = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='con-title']")))
# portal_page_title = portal_page.text
# print(f"portal_page_title: {portal_page_title}")
# assert "Portals" in portal_page_title

# click the client
client_box = wait.until(EC.presence_of_element_located((By.XPATH, "//tbody/tr[3]/td[3]")))
client_name = driver.find_element(By.XPATH, "//td[normalize-space()='Automated client 002']").text
print(f"client_name: {client_name}")
driver.execute_script("arguments[0].scrollIntoView(true);", client_box)
driver.execute_script("arguments[0].click();", client_box)

# ======================================================================================================================

# click the portal edit button
portal_edit_btn = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='portal-action-button'][normalize-space()='Continue Editing'])[1]")))
driver.execute_script("arguments[0].scrollIntoView(true);", portal_edit_btn)
driver.execute_script("arguments[0].click();", portal_edit_btn)

# ======================================================================================================================

# click the sessions button of the portal
time.sleep(5)
session_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Sessions')]")))
driver.execute_script("arguments[0].click();", session_btn)

# ======================================================================================================================

# Click Schedule Webcast Button 
webcast_creation_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='session-button-group-right']")))
webcast_creation_btn.click()

# Click the Create New Webcast button
new_webcast_btn = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='stream-modal-container h-full'])[1]")))
driver.execute_script("arguments[0].click();", new_webcast_btn)

# ======================================================================================================================

# Create New Webcast form fillup (setp-1)
webcast_title = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='streamName']")))
webcast_title.send_keys("Automated Webcast Title!!!")

# time.sleep(5)
# next buttton-1
webcast_title_next_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Next']")))
driver.execute_script("arguments[0].click();", webcast_title_next_btn)

# Date select calendar (Step-2)
webcast_date = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Select date']")))
webcast_date.click()
# select date
select_webcast_date = wait.until(EC.presence_of_element_located((By.XPATH, "//div[normalize-space()='25']")))
driver.execute_script("arguments[0].click();", select_webcast_date)

# select webcast time 
webcast_time = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Select time']")))
webcast_time.click()
#select time
select_webcast_time = wait.until(EC.presence_of_element_located((By.XPATH, "//ul[@data-type='hour']//div[@class='ant-picker-time-panel-cell-inner'][normalize-space()='03']")))
driver.execute_script("arguments[0].click();", select_webcast_time)

# select webcast duration
webcast_duration = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Select duration']")))
webcast_duration.click()
#select duration
select_webcast_duration = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='ant-picker-time-panel-cell-inner'][normalize-space()='01'])[3]")))
driver.execute_script("arguments[0].click();", select_webcast_duration)

# time.sleep(5)
# next button-2
next_btn_2 = wait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Next']")))
driver.execute_script("arguments[0].click();", next_btn_2)

# step-3
signal = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='acquisitionSignal']")))
driver.execute_script("arguments[0].style.display = 'block';", signal)
driver.execute_script("arguments[0].click();", signal)

# time.sleep(5)
# next button-3
next_btn_3 = wait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Next']")))
driver.execute_script("arguments[0].click();", next_btn_3)

# create webcast btn
next_btn_3 = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='save-button d-flex flex-row justify-items-center']")))
driver.execute_script("arguments[0].click();", next_btn_3)

wait.until(EC.presence_of_element_located((By.ID, "swal2-html-container")))

# webcast creation validation
webcast_title_validation = wait.until(EC.presence_of_element_located((By.XPATH, "//div[normalize-space()='Automated Webcast Title!!!']")))
webcast_title_validation_text = webcast_title_validation.text
print(f"webcast_title_validation_text: {webcast_title_validation}")
assert "Automated" in webcast_title_validation_text

# ======================================================================================================================

# Activate Webcast
activate_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@role='switch']")))
driver.execute_script("arguments[0].click();", activate_btn)

# Activate Webcast validation
wait.until(EC.presence_of_element_located((By.ID, "swal2-html-container")))

# Manage webcast
driver.find_element(By.XPATH, "//button[normalize-space()='Manage']").click()

# Manage webcast validation
webcast_manage_page = wait.until(EC.presence_of_element_located((By.XPATH, "//div[normalize-space()='Configure your webcast']")))
webcast_manage_page_title = webcast_manage_page.text
print(f"webcast_manage_page_title: {webcast_manage_page_title}")
assert "Configure" in webcast_manage_page_title

# ======================================================================================================================









time.sleep(5)