from selenium import webdriver
import time

URL = "https://connectstudio-portal-dev.world-television.com/689eef0849bb55397eefffaa/session/689f225ff37f425de7e498d8?isNewSession=true"

driver = webdriver.Chrome()

# open full window
driver.maximize_window()

# Open first tab
driver.get(URL)

# Open 49 more tabs
for i in range(1, 5):
    driver.execute_script(f"window.open('{URL}', '_blank');")
    time.sleep(2)  # slight delay to avoid overwhelming your browser

print("✅ 50 tabs opened successfully!")

# Optional: Keep them open for observation
time.sleep(60)

driver.quit()
