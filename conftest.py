import os.path
import re

import pytest
from playwright.sync_api import sync_playwright, expect

AUTH_FILE = "auth/auth.json"
expect.set_options(timeout=15000)

def generate_auth_state():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        page.get_by_placeholder("Username").fill("Admin")
        page.get_by_placeholder("Password").fill("admin123")
        page.get_by_role("button", name="Login").click()
        page.wait_for_url(re.compile("dashboard"))
        context.storage_state(path=AUTH_FILE)
        browser.close()


@pytest.fixture(scope="session")
def browser():
    if not os.path.exists(AUTH_FILE):
        print("Generating AUTH File..")
        generate_auth_state()
        print("AUTH File generated successfully in ",AUTH_FILE)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="session")
def context(browser):
    context = browser.new_context(storage_state=AUTH_FILE)
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()


