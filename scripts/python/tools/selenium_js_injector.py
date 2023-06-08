from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to your Chrome driver executable
driver = webdriver.Chrome(
    "C:\\Users\\sergi\\PycharmProjects\\Cartuli-AI-Assitant\\scripts\\python\\lib\\chromedriver.exe")

# Load the website
driver.get('https://www.sloppylopez.com')

# Inject and execute JavaScript code
with open('scripts/clickAllElements.js', 'r') as file:
    script_code = file.read()

driver.execute_script(script_code)

# Wait for the script execution to complete
timeout = 10  # Adjust the timeout as needed
clickable_elements_locator = (By.CSS_SELECTOR, 'a, button, input[type="button"], input[type="submit"], [role="button"], [onclick]')
WebDriverWait(driver, timeout).until(EC.presence_of_all_elements_located(clickable_elements_locator))

# Capture and print the console output
console_logs = driver.get_log('browser')
for log in console_logs:
    print(f'[{log["level"]}] {log["message"]}')

# Close the browser
driver.quit()
