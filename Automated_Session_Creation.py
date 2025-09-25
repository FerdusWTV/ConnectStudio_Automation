from http import client
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

# click the client
client_box = 



time.sleep(5)