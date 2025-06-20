
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize the Chrome browser in headful mode
chrome_options = ChromeOptions()
chrome_options.add_argument("--start-maximized")  # Maximize the window when it opens

# Set up the Chrome driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

# Load the Microsoft Learn main page
driver.get("https://learn.microsoft.com/en-us")

# Wait for the page to load (using time.sleep as a simple alternative)
time.sleep(10)

# Scroll down to find 'Artificial Intelligence' and click the link
artificial_intelligence_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Artificial Intelligence')]")
driver.execute_script("arguments[0].scrollIntoView();", artificial_intelligence_link)
time.sleep(5)  # Wait for the element to be clickable
artificial_intelligence_link.click()

# Wait for the new page to load (using time.sleep as a simple alternative)
time.sleep(10)

# Scroll up to the top of the page
driver.execute_script("window.scrollTo(0, 0);")

# Assert the page title
expected_title = "AI learning hub - Start your AI learning journey, and build practical AI skills to use right away. | Microsoft Learn"
assert driver.title == expected_title, f"Expected title not found. Found: {driver.title}"

# Quit the driver
driver.quit()
