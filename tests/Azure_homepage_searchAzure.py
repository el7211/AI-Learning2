
from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        context = browser.new_context(no_viewport=True)
        page = context.new_page()
        page.goto("https://learn.microsoft.com/en-us")
        page.wait_for_load_state('load')
        time.sleep(5)
        search_box = page.wait_for_selector('xpath=//*[@id="welcome-page-search-form-autocomplete-input"]')
        search_box.fill("Azure")
        search_box.press("Enter")
        page.wait_for_load_state('load')
        page.screenshot(path="tests/screenshots/002.png")
        browser.close()

if __name__ == "__main__":
    run()
