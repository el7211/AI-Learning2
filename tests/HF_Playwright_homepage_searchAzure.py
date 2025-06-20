
import playwright.sync_api

def run(playwright):
    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto("https://learn.microsoft.com/en-us")
    page.wait_for_load_state('networkidle')
    page.wait_for_timeout(10000)
    search_box = page.query_selector('//*[@id="welcome-page-search-form-autocomplete-input"]')
    search_box.fill("Azure")
    search_box.press("Enter")
    page.wait_for_load_state('networkidle')
    page.screenshot(path='screenshots/002.png', full_page=True)
    context.close()
    browser.close()

with playwright.sync_api.sync_playwright() as playwright:
    run(playwright)
