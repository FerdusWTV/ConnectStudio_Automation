import time
import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import EC as EC
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:/Users/Tulip/Downloads/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)
driver.maximize_window()
driver.implicitly_wait(5)

# load env variable
load_dotenv()

url = os.getenv("URL")
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

wait = WebDriverWait(driver, 10)
quick_wait = WebDriverWait(driver, 3)

# ======================================================================================================================

# login form
driver.get(url)
driver.find_element(By.ID, 'email').send_keys(email)
driver.find_element(By.ID, 'password').send_keys(password)
driver.find_element(By.CLASS_NAME, 'login-button').click()
time.sleep(5)

#login validation wait
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'swal2-container')))

# ======================================================================================================================

#dashboard page validation
welcome = driver.find_element(By.CLASS_NAME, 'header-title').text
print(f'Login successfully: {welcome}')
assert 'Welcome' in welcome

# ======================================================================================================================

#org page access validation
driver.find_element(By.XPATH, "//li[3]").click()
org_text = driver.find_element(By.CLASS_NAME, "page-header-title").text
print(f'Accessed Organization Page successfully: {org_text}')
assert 'All Organizations' in org_text

# ======================================================================================================================

# #Total Page count
# total_page = driver.find_element(By.CSS_SELECTOR, "aside[class='children'] li:nth-child(10)").text
# print(f"Total Organization Page: {total_page}")

# # Targeted org page switch
# for i in range(13):
#     element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[aria-label='Next page']")))
#     driver.execute_script("arguments[0].scrollIntoView(true);", element)
#     time.sleep(1)
#     element.click()
#     print(i)

# ======================================================================================================================

#new org create btn
create_org_btn = driver.find_element(By.CLASS_NAME, "save-button").text
driver.find_element(By.CLASS_NAME, "save-button").click()
print(f'create_org_btn: {create_org_btn}')

## org form fillup

# Org Name
org_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='text']:nth-child(2)")))
org_name.send_keys('Automated_Test_ORG')

#org Logo
org_logo = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']")))
org_logo.send_keys("C:/Users/Tulip/OneDrive - TulipTech LTD/Desktop/Test_Logos/wtv.png")

#org Template
driver.find_element(By.ID, "rc_select_1").click()
temp = wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Modern - popular user experience style comprised of 3D elements']")))
temp.click()


# Wait for the modal body
modal_body = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ant-modal-body")))

# Scroll to bottom of modal
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal_body)

# Wait for the button to be clickable
save_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.connect-studio-small-save-button")))

# Click the button
# save_button.click()

time.sleep(5)