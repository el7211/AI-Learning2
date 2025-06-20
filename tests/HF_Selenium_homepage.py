
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from agents.tool import detect_language

def main():
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    lang_codes = ['zh-cn', 'ja-jp', 'fr-fr', 'de-de']
    
    try:
        for lang in lang_codes:
            url = f"https://learn.microsoft.com/{lang}"
            driver.get(url)
            
            # Wait for the page to load
            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "title")))
            
            # Get the page title and detect its language
            title = driver.title
            detected_language = detect_language(text=title)
            
            print(f"URL: {url}")
            print(f"Page title: {title}")
            print(f"Detected language: {detected_language}\n")
            
            # Sleep for a second to be polite (optional)
            time.sleep(1)
    
    finally:
        # Quit the WebDriver
        driver.quit()

main()
