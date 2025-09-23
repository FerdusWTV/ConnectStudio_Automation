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

# Create Portal Button
create_portal_btn = driver.find_element(By.XPATH, "//div[contains(text(),'Create Portal')]")
portal_btn_text = create_portal_btn.text
print(f"portal_btn_text: {portal_btn_text}")

# click the create portal btn
driver.find_element(By.XPATH, "//li[@class='show']").click()

# ======================================================================================================================
# branding page fillup

# select organization
org_menu_box = wait.until(EC.presence_of_element_located((By.ID, "rc_select_0")))
org_menu_box.click()
org_menu = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='rc-virtual-list-holder']")))
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

# ============================================================================================================

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
time.sleep(1)
reg_set_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Set']")))
reg_set_button.click()


# Registration, Login page logo
time.sleep(1)
reg_logo = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='file'])[1]")))
driver.execute_script("arguments[0].scrollIntoView(true);", reg_logo)
driver.execute_script("arguments[0].style.display = 'block';", reg_logo)
reg_logo.send_keys("C:/Users/Tulip/OneDrive - TulipTech LTD/Desktop/Test_Logos/logo007.png")
#crop logo & set
time.sleep(1)
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
# time.sleep(10)

# ============================================================================================================

# save button
save_btn = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Save & Next']")))
save_btn_name = save_btn.text
print(f"Branding_save_btn_name: {save_btn_name}")
driver.execute_script("arguments[0].scrollIntoView(true);", save_btn)
time.sleep(1)
driver.execute_script("arguments[0].click();", save_btn) #click save btn

### branding save confirmation
time.sleep(5)
wait.until(EC.presence_of_element_located((By.ID, "swal2-html-container")))

# ============================================================================================================

## optional if the home page is not automatically clicked enable this
# home_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Home')]")))
# driver.execute_script("arguments[0].click();", home_btn)

# wait for the branding info to get saved in the local storage
time.sleep(10)

# ============================================================================================================

# Home page access validation
home_title = driver.find_element(By.XPATH, "//p[@class='general-info-title']").text
print(f"home_title: {home_title}")
assert "General" in home_title
# ============================================================================================================





# ==================================================================================================================================================
# ==================================================================================================================================================





##### Home Home Home Home Home #####

# Title
title = driver.find_element(By.XPATH, "//input[@id='eventName']")
title.send_keys("This is a Automated Title! Please read this!!!")

# # Subtitle (NN)
# subtitle = driver.find_element(By.XPATH, "//input[@id='subTitle']")
# subtitle.send_keys("This is a automated subtitle!!!")

# ============================================================================================================

# Portal Opening date
opening_date = driver.find_element(By.XPATH, "//input[@name='date']")
opening_date.click()
today_btn = driver.find_element(By.XPATH, "(//a[normalize-space()='Today'])[1]")
today_btn.click()

# Portal Closing date
closing_date = driver.find_element(By.XPATH, "//input[@name='closingDate']")
closing_date.click()
#closing date
time.sleep(1)
date_close = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[normalize-space()='Today'])[2]")))
date_close.click()

# ============================================================================================================

# Event Introduction
time.sleep(5) #to prevent from the page to crash as it is a p tag that take some time to load and take the data.
# intro = driver.find_element(By.XPATH, "//div[@class='ql-editor ql-blank']//p")
intro = driver.find_element(By.XPATH, "//div[@class='ql-editor ql-blank']")
intro.send_keys("This is a Automated Event Introduction. Please read this intro!!! If you can see this than the script is working correctly!!!")

# ============================================================================================================

# # Homepage Button Label(optional)
# home_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='homepageButton']")))
# driver.execute_script("arguments[0].scrollIntoView(true);", home_btn)
# home_btn.send_keys("Download Resources")

# ============================================================================================================

# # Homepage Image
# home_image = driver.find_element(By.XPATH, "//input[@type='file']")
# driver.execute_script("arguments[0].scrollIntoView(true);", home_image)
# driver.execute_script("arguments[0].style.display = 'block';", home_image)
# home_image.send_keys("C:/Users/Tulip/OneDrive - TulipTech LTD/Desktop/Test_Logos/download.png")
# # set btn
# home_image_set_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Set']")))
# home_image_set_button.click()

# ============================================================================================================

# Home page save button
home_save_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save & Next']")))
home_save_btn_name = home_save_btn.text
print(f"home_page_save_btn_name: {home_save_btn_name}")
driver.execute_script("arguments[0].scrollIntoView(true);", home_save_btn)
time.sleep(5)
driver.execute_script("arguments[0].click();", home_save_btn) #click save btn

# Home page save confirmation
# time.sleep(5)
wait.until(EC.presence_of_element_located((By.ID, "swal2-html-container")))

# ============================================================================================================

# Regsitration page validation
reg_title = driver.find_element(By.XPATH, "//p[@class='user-management-title']").text
print(f"Registration_page_title: {reg_title}")
assert "Access" in reg_title

# ============================================================================================================






# ==================================================================================================================================================
# ==================================================================================================================================================





##### Registration Registration Registration Registration #####

# Enable registration
reg_require_btn = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='checkbox'])[1]")))
driver.execute_script("arguments[0].style.display = 'block';", reg_require_btn)
driver.execute_script("arguments[0].click();", reg_require_btn)

# ============================================================================================================

# Save registration page
reg_page_save_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save & Next']")))
reg_save_btn_name = reg_page_save_btn.text
print(f"reg_page_save_btn_name: {reg_save_btn_name}")
driver.execute_script("arguments[0].scrollIntoView(true);", reg_page_save_btn)
driver.execute_script("arguments[0].click();", reg_page_save_btn)

# Registration page save confirmation
# time.sleep(5)
# wait.until(EC.presence_of_element_located((By.ID, "swal2-html-container")))

# ============================================================================================================

# Sessions Page access confirmation
session_title = driver.find_element(By.XPATH, "//div[@class='webcast-summary-title']").text
print(f"session_Page_Title: {session_title}")
assert "Live" in session_title

# ============================================================================================================





# ==================================================================================================================================================
# ==================================================================================================================================================





##### Session Session Session Session #####


# ============================================================================================================

# Save Session Page
session_page_save_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save & Next']")))
session_page_save_btn_name = session_page_save_btn.text
print(f"session_page_save_btn_name: {session_page_save_btn}")
driver.execute_script("arguments[0].scrollIntoView(true);", session_page_save_btn)
driver.execute_script("arguments[0].click();", session_page_save_btn)

# # Session page save confirmation
# time.sleep(5)
# wait.until(EC.presence_of_element_located((By.ID, "swal2-html-container")))

# speaker page validation
speaker_page = wait.until(EC.presence_of_element_located((By.XPATH, "//p[@class='our-speaker-title']")))
speaker_page_title = speaker_page.text
print(f"speaker_page_title: {speaker_page_title}")
assert "Event" in speaker_page_title

# ============================================================================================================






# ==================================================================================================================================================
# ==================================================================================================================================================






##### Speaker Speaker Speaker Speaker #####

speaker_enable_button = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='checkbox']")))
driver.execute_script("arguments[0].scrollIntoView(true);", speaker_enable_button)
driver.execute_script("arguments[0].style.display = 'block';", speaker_enable_button)
driver.execute_script("arguments[0].click();", speaker_enable_button)
time.sleep(3)
driver.execute_script("arguments[0].click();", speaker_enable_button)

# ============================================================================================================

# speaker page save button
speaker_save_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save & Next']")))
driver.execute_script("arguments[0].scrollIntoView(true);", speaker_save_btn)
driver.execute_script("arguments[0].click();", speaker_save_btn)

# ============================================================================================================

#speaker page save validation
agenda_title = wait.until(EC.presence_of_element_located((By.XPATH, "//p[@class='agenda-title']")))
agenda_page_title = agenda_title.text
print(f"agenda_title: {agenda_page_title}")
assert "Event" in agenda_page_title










time.sleep(5)