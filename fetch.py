from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import json

def fetch_page(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        try:
            page.goto(url, timeout=60000)
            page.wait_for_load_state("networkidle")

            # Get the page content
            content = page.content()

            soup = BeautifulSoup(content, features="html.parser")

            items = soup.find_all('div', {'data-cy': 'l-card'}, limit = 10)

            json_arr = []

            for item in items:
                href = 'https://www.olx.ua' + item.find('a').get('href', '')
                description = item.find('h4').text
                dict = {"description": description, "href": href}
                json_arr.append(dict)
            
            print(json.dumps(json_arr, ensure_ascii=False))

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            browser.close()
