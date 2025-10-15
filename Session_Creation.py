from http import client
from pydoc import cli
import time
import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--remote-allow-origins=*")

# Load env variable
load_dotenv()

url = os.getenv("URL")
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
driver_path = os.getenv("DRIVER")

# url = os.getenv("URL_prod")
# email = os.getenv("EMAIL_prod")
# password = os.getenv("PASSWORD_prod")

service_obj = Service(driver_path)

driver = webdriver.Chrome(service=service_obj, options=options)

driver.maximize_window()
driver.implicitly_wait(5)

wait = WebDriverWait(driver, 30)
quick_wait = WebDriverWait(driver, 1)
actions = ActionChains(driver)

# ======================================================================================================================
# ------------------------------------Please add the necessary infos here-----------------------------------------------
# ======================================================================================================================

# target_portal = "AUTO's live."
target_portal = "Session Automation Portal 001"
new_webcast_title = "Automated Webcast Title - 001!!!"

# ======================================================================================================================
# ------------------------------------------------Thank You!------------------------------------------------------------
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

# search the portal
search_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search portal']")))
search_box.click()
search_box.send_keys(target_portal)

edit_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Edit']")))
driver.execute_script("arguments[0].click();", edit_btn)

# validate
portal_title = wait.until(EC.presence_of_element_located((By.XPATH, "(//p[@class='branding-information-text mt-1'])[1]")))
portal_title_text = portal_title.text
print(f"portal_title_text: {portal_title_text}")
assert "Portal" in portal_title_text 

# ======================================================================================================================

# Click Session button
time.sleep(2)
session_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Sessions')]")))
driver.execute_script("arguments[0].click();", session_btn)

# validation
session_title = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='webcast-summary-title']")))
session_title_text = session_title.text
print(f"session_title_text: {session_title_text}")
assert "Live" in session_title_text

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
webcast_title.send_keys(new_webcast_title)

time.sleep(3)

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

time.sleep(3)
wait.until(EC.presence_of_element_located((By.ID, "swal2-html-container")))

# ======================================================================================================================

def find_and_activate_session(driver: webdriver.Chrome, target_event_name: str):
    wait = WebDriverWait(driver, 15)
    
    def get_webcast_summaries():
        return wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "webcast-summary"))
        )

    try:
        webcast_summaries = get_webcast_summaries()
        print(f"Event summaries found: {len(webcast_summaries)}")
    except Exception as e:
        print(f"Could not find any webcast summary. Error: {e}")
        return

    for summary in webcast_summaries:
        try:
            webcast_name = summary.find_element(
                By.XPATH,
                ".//div[contains(@class, 'webcast-summary-event-name')]//div[contains(@class, 'webcast-summary-background')]"
            )
            current_webcast = webcast_name.text.strip()
            print(f"Checking webcast: {current_webcast}")

            if current_webcast.strip().casefold() == target_event_name.strip().casefold():
                print(f"✅ Match Found for webcast '{target_event_name}'")

                # Click Activate
                activate_btn = WebDriverWait(summary, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, ".//div[contains(@class, 'webcast-summary-activate')]//button")
                    )
                )
                activate_btn.click()
                print("Clicked the 'Activate' button.")

                # Wait for popup and close/confirm it
                wait.until(EC.presence_of_element_located((By.ID, "swal2-html-container")))
                print("Popup detected after Activate.")
                time.sleep(2)

                # 🔁 Re-locate the summary after DOM update
                webcast_summaries = get_webcast_summaries()
                for updated_summary in webcast_summaries:
                    try:
                        updated_name = updated_summary.find_element(
                            By.XPATH,
                            ".//div[contains(@class, 'webcast-summary-event-name')]//div[contains(@class, 'webcast-summary-background')]"
                        ).text.strip()

                        if updated_name.strip().casefold() == target_event_name.strip().casefold():
                            manage_button = WebDriverWait(updated_summary, 10).until(
                                EC.element_to_be_clickable(
                                    (By.XPATH, ".//div[contains(@class, 'webcast-manage-column')]//button")
                                )
                            )
                            manage_button.click()
                            print("🎯 Clicked the 'Manage' button successfully.")
                            return
                    except Exception:
                        continue
        except Exception as e:
            print(f"Error while processing a webcast summary: {e}")
    
find_and_activate_session (driver, new_webcast_title)

webcast_managment_page = wait.until(EC.presence_of_element_located((By.XPATH, "//div[normalize-space()='Configure your webcast']")))
webcast_managment_page_title = webcast_managment_page.text
print(f"webcast_managment_page_title: {webcast_managment_page_title}")
assert "Configure" in webcast_managment_page_title

# ======================================================================================================================

# preview webcast slide upload
time.sleep(1)
content_btn = wait.until(EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Content'])[1]")))
driver.execute_script("arguments[0].click();", content_btn)

slide_upload = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='file'])[1]")))
driver.execute_script("arguments[0].style.display = 'block';", slide_upload)
driver.execute_script("arguments[0].click();", slide_upload)
slide_upload.send_keys(r"C:\Users\Tulip\OneDrive - TulipTech LTD\Desktop\Test_Slides\9 page - Project Timeline Presentation.pdf")

# preview save button 
preview_save_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save']")))
driver.execute_script("arguments[0].click();", preview_save_btn)

#  wait for the popup to 
time.sleep(5)
wait.until(EC.presence_of_element_located((By.ID, "swal2-html-container")))

# change to live page
status_dropdown = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@title='Preview']")))
status_dropdown.click()

# choose live
status_live = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Live')]")))
status_live.click()

# live webcast slide upload
time.sleep(1)
content_btn = wait.until(EC.presence_of_element_located((By.XPATH, "(//button[normalize-space()='Content'])[1]")))
driver.execute_script("arguments[0].click();", content_btn)

slide_upload = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='file'])[1]")))
driver.execute_script("arguments[0].style.display = 'block';", slide_upload)
driver.execute_script("arguments[0].click();", slide_upload)
slide_upload.send_keys(r"C:\Users\Tulip\OneDrive - TulipTech LTD\Desktop\Test_Slides\9 page - Project Timeline Presentation.pdf")

# live save button
live_save_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save']")))
live_save_btn.click()

#  wait for the popup to 
time.sleep(5)
wait.until(EC.presence_of_element_located((By.ID, "swal2-html-container")))

# change to preview page
status_dropdown = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='status']")))
status_dropdown.click()

# choose live
status_live = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@id='status_list_0'])[1]")))
status_live.click()

#preview video upload.
video_upload = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@type='file'])[2]")))
driver.execute_script("arguments[0].style.display = 'block';", video_upload)
driver.execute_script("arguments[0].click();", video_upload)
video_upload.send_keys(r"C:\Users\Tulip\OneDrive - TulipTech LTD\Desktop\Test_Videos\Em Beihold - Numb Little Bug (Official Lyric Video).mp4")

# preview save button 
preview_save_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save']")))
driver.execute_script("arguments[0].click();", preview_save_btn)

#  wait for the popup to 
time.sleep(5)
wait.until(EC.presence_of_element_located((By.ID, "swal2-html-container")))








time.sleep(5)