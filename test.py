from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.set_page_load_timeout(60)
driver.get("https://www.google.com")



# ========================================================



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def find_and_interact_with_event(driver: webdriver.Chrome, target_event_name: str):
    """
    Searches for an event by name and clicks the Activate and Manage buttons.

    Args:
        driver: The Selenium WebDriver instance.
        target_event_name: The name of the event to find (e.g., 'Automated Webcast Title').
    """
    # Use a wait for the main container of all summaries to be present
    # The parent container for all events appears to be a list of elements with class 'webcast-summary'
    try:
        # Wait for at least one event summary to be visible
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "webcast-summary"))
        )

        # 1. Locate all event summary elements (all containers)
        event_summaries = driver.find_elements(By.CLASS_NAME, "webcast-summary")
        print(f"Found {len(event_summaries)} total event summaries.")

    except Exception as e:
        print(f"Could not find event summaries. Error: {e}")
        return

    # 2. Iterate through them
    for summary in event_summaries:
        try:
            # 3. Find and extract the event name
            # The name is inside 'webcast-summary-background' which is inside 'webcast-summary-event-name'
            event_name_element = summary.find_element(
                By.XPATH,
                ".//div[contains(@class, 'webcast-summary-event-name')]//div[contains(@class, 'webcast-summary-background')]"
            )
            current_event_name = event_name_element.text.strip()
            print(f"Checking event: '{current_event_name}'")

            # 4. Compare the extracted name with your target name
            if current_event_name == target_event_name:
                print(f"MATCH FOUND for event: '{target_event_name}'")

                # 5. Perform the required clicks

                # Clicks 1: The button under 'webcast-summary-activate'
                # Find the button element within the current summary element
                activate_button = summary.find_element(
                    By.XPATH,
                    ".//div[contains(@class, 'webcast-summary-activate')]//button"
                )
                activate_button.click()
                print("Clicked the 'Activate' button.")

                # Wait for potential update/change after the first click if necessary,
                # otherwise directly proceed to the next click.
                # If the UI takes time to update, uncomment the line below.
                # time.sleep(1)

                # Clicks 2: The button under 'webcast-manage-column'
                # Find the button element within the current summary element
                manage_button = summary.find_element(
                    By.XPATH,
                    ".//div[contains(@class, 'webcast-manage-column')]//button"
                )
                manage_button.click()
                print("Clicked the 'Manage' button.")

                # 6. Stop the iteration
                return  # Exit the function after successful interaction

        except Exception as e:
            # Continue to the next summary if a particular summary element is malformed or throws an error
            print(f"Error processing one event summary: {e}")
            continue

    print(f"Target event '{target_event_name}' was not found in the list.")

# --- Example Usage ---

# 1. Setup your driver (make sure the driver executable is in your PATH or specify its path)
# driver = webdriver.Chrome() # Example for Chrome
# driver.get("YOUR_WEBPAGE_URL")

# 2. Define the target name
# target_name = "Automated Webcast Title" # Use the exact text you are looking for

# 3. Call the function
# find_and_interact_with_event(driver, target_name)