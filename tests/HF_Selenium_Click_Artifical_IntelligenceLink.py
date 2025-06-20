
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize the Chrome driver in headful mode
chrome_options = Options()
chrome_options.add_argument('--start-maximized')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    # Visit the specified URL
    driver.get('https://learn.microsoft.com/en-us')
    
    # Wait for the page to load
    time.sleep(10)  # Using sleep to wait for the page to load
    
    # Scroll down to find 'Artificial Intelligence' and click the link
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)  # Give some time for the page to load more content
    
    ai_link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Artificial Intelligence')
    ai_link.click()
    
    # Wait for the page to load
    time.sleep(10)  # Using sleep to wait for the new page to load
    
    # Print the page title
    print(driver.title)
finally:
    # Quit the browser
    driver.quit()
