import re

from playwright.sync_api import Page, expect


class Org_Hrm_Login_Page:

    def __init__(self, page: Page):
        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.login_btn = page.get_by_role("button", name="Login")

    def enter_username(self,username):
        self.username.fill(username)
        #assert self.username.inner_text() == username
        expect(self.username).to_have_value(username)

    def enter_password(self,password):
        self.password.fill(password)
        #assert self.password.inner_text() == password
        expect(self.password).to_have_value(password)

    def click_login_btn(self, page: Page):
        self.login_btn.click()
        expect(page).to_have_url(re.compile("dashboard"), timeout=15000)
        #page.wait_for_load_state("networkidle")


