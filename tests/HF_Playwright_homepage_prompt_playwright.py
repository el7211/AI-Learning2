import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from agents.tool import detect_language

from playwright.sync_api import sync_playwright


def main():
    lang_codes = ['zh-cn', 'ja-jp', 'fr-fr', 'de-de']
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        try:
            for lang in lang_codes:
                url = f'https://learn.microsoft.com/{lang}'
                page.goto(url)
                page_title = page.title()
                print(f'Title for {url}: {page_title}')
                detected_lang = detect_language(page_title)
                print(f'Detected Language for {url}: {detected_lang}')
        finally:
            browser.close()

if __name__ == '__main__':
    main()
