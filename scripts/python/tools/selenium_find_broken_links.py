from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tools.logger import logger


def change_element_color(driver, element, response_code):
    try:
        if response_code is not None and 200 <= response_code < 400:
            element_color = 'green'
        else:
            element_color = 'red'

        driver.execute_script("arguments[0].style.backgroundColor = '{}';".format(element_color), element)
    except Exception as e:
        logger(e)
        pass


def click_elements(url):
    driver = webdriver.Chrome(
        "C:\\Users\\sergi\\PycharmProjects\\Cartuli-AI-Assitant\\scripts\\python\\lib\\chromedriver.exe")
    driver.get(url)

    wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed

    elements = wait.until(
        EC.presence_of_all_elements_located((By.XPATH, "//a | //button")))  # Add other element types as needed
    logger(elements)
    for element in elements:
        try:
            logger(element.id)
            # Open element in a new window
            driver.execute_script("window.open(arguments[0].getAttribute('href'))", element)

            # Switch to the newly opened window
            driver.switch_to.window(driver.window_handles[-1])

            logger("Clicked!!!!!!")

            # Wait for the page to load and retrieve the performance entries
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'body'))
            )
            response_code = driver.execute_script(
                "var entries = window.performance.getEntries();"
                "if (entries.length > 0 && entries[0].response) {"
                "   return entries[0].response.status;"
                "} else {"
                "   return null;"
                "}"
            )

            # if response_code is not None:
            change_element_color(driver, element, response_code)

            # Close the current window
            driver.close()

            # Switch back to the original window
            driver.switch_to.window(driver.window_handles[0])
        except Exception as e:
            # logger(e)
            pass

    driver.quit()


url = "https://sloppylopez.com/"
click_elements(url)
