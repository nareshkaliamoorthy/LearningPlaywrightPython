from playwright.sync_api import sync_playwright

def test_handling_tables():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.ag-grid.com/example/")
        page.wait_for_selector("div.ag-row")
        rows = page.locator("div.ag-row")
        row_values = rows.all_text_contents()
        print(rows.count())
        print(row_values)
        page.wait_for_timeout(5000)

