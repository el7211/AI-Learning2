
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


def perform_browser_operations():
    # Initialize the ChromeDriver using webdriver-manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Step 1 & 2: Open the Chrome browser and visit the URL
        driver.get("https://learn.microsoft.com/en-us")

        # Step 3: Maximize the webpage and wait for the page to load
        driver.maximize_window()
        WebDriverWait(driver, 10).until(EC.title_contains("Microsoft Learn"))

        # Step 4: Wait 10 seconds, find the search box, input 'Azure' and click Search
        time.sleep(10)  # Wait for 10 seconds
        search_box = driver.find_element(By.XPATH, '//*[@id="welcome-page-search-form-autocomplete-input"]')

        search_box.send_keys("Azure")
        search_box.send_keys(Keys.RETURN)

        # Step 5: Wait for the page to load
        time.sleep(10)  # Wait for 10 seconds
        # Step 6: Take a screenshot and save it
        driver.save_screenshot('002.png')
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    perform_browser_operations()