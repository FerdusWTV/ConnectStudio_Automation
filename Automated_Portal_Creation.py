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

wait = WebDriverWait(driver, 10)
quick_wait = WebDriverWait(driver, 1)
actions = ActionChains(driver)

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
welcome = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'header-title'))).text
print(f'Login successful: {welcome}')
assert 'Welcome' in welcome

# ======================================================================================================================

create_portal_btn = driver.find_element(By.XPATH, "//div[contains(text(),'Create Portal')]")
portal_btn_text = create_portal_btn.text
print(f"portal_btn_text: {portal_btn_text}")

# ======================================================================================================================

# click the create portal btn
driver.find_element(By.XPATH, "//li[@class='show']").click()

# ======================================================================================================================
# branding page fillup

# select organization
wait.until(EC.presence_of_element_located((By.ID, "rc_select_0"))).click()
org_menu = driver.find_element(By.XPATH, "//div[@class='rc-virtual-list-holder']")
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", org_menu)
driver.find_element(By.XPATH, "//div[@title='Automated Test ORG']").click()

# select client
driver.find_element(By.ID, "rc_select_1").click()
client_menu = driver.find_element(By.CLASS_NAME, "rc-virtual-list-holder-inner")
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", client_menu)
driver.find_element(By.XPATH, "//div[contains(text(),'Automated client 002')]").click()

# Template style (optional)
driver.find_element(By.XPATH, "//div[@data-testid='template-style']").click()
time.sleep(1)
template = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@title='Material - popular user experience style comprised of 3D elements']")))
template.click()


# header menu logo
logo = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='file'])[1]")))
driver.execute_script("arguments[0].scrollIntoView(true);", logo)
driver.execute_script("arguments[0].style.display = 'block';", logo)
logo.send_keys("C:/Users/Tulip/OneDrive - TulipTech LTD/Desktop/Test_Logos/logo007.png")
#crop logo & set
logo_set_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Set']")))
logo_set_button.click()


# favicon upload
time.sleep(1)
favicon = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='file'])[1]")))
driver.execute_script("arguments[0].scrollIntoView(true);", favicon)
driver.execute_script("arguments[0].style.display = 'block';", favicon)
favicon.send_keys("C:/Users/Tulip/OneDrive - TulipTech LTD/Desktop/Test_Logos/New_folder/favicon_32.png")


# registration email image
time.sleep(1)
reg_email_image = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='file'])[1]")))
driver.execute_script("arguments[0].scrollIntoView(true);", reg_email_image)
driver.execute_script("arguments[0].style.display = 'block';", reg_email_image)
reg_email_image.send_keys("C:/Users/Tulip/OneDrive - TulipTech LTD/Desktop/Test_Logos/download.png")
#crop logo & set
# time.sleep(1)
reg_set_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Set']")))
reg_set_button.click()


# Registration, Login page logo
time.sleep(1)
reg_logo = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='file'])[1]")))
driver.execute_script("arguments[0].scrollIntoView(true);", reg_logo)
driver.execute_script("arguments[0].style.display = 'block';", reg_logo)
reg_logo.send_keys("C:/Users/Tulip/OneDrive - TulipTech LTD/Desktop/Test_Logos/logo007.png")
#crop logo & set
# time.sleep(1)
reg_logo_set_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Set']")))
reg_logo_set_button.click()


# ============================================================================================================

# # background color (NN)
# bg_color = driver.find_element(By.CLASS_NAME, 'choose-font-color-input')
# driver.execute_script("arguments[0].scrollIntoView(true);", bg_color)
# driver.execute_script("arguments[0].click();", bg_color)
# # write color hex
# color_hex = driver.find_element(By.CLASS_NAME, "rcp-fields-element-input")
# new_value = "#8af8eb"
# driver.execute_script("arguments[0].click();", color_hex)
# driver.execute_script("arguments[0].value = arguments[1];", color_hex, new_value)

# ============================================================================================================

wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='home-page']")))
time.sleep(10)

# ============================================================================================================

# save button
save_btn = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Save & Next']")))
save_btn_name = save_btn.text
print(f"save_btn_name: {save_btn_name}")
driver.execute_script("arguments[0].scrollIntoView(true);", save_btn)
time.sleep(1)
driver.execute_script("arguments[0].click();", save_btn) #click save btn

### branding save confirmation
# time.sleep(10)
# wait.until(EC.presence_of_element_located((By.ID, "swal2-html-container")))

# home_title = driver.find_element(By.XPATH, "//p[@class='general-info-title']").text
# print(f"home_title: {home_title}")



time.sleep(5)