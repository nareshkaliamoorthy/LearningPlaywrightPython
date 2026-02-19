import re

from playwright.sync_api import Page, expect



class Org_Hrm_Home_Page:

    def __init__(self, page: Page):
        self.page = page
        self.leave_menu = page.get_by_role("link", name="Leave", exact=True)
        self.from_date = page.locator("div.oxd-input-group", has=page.locator("label", has_text="From Date")).locator("input")
        self.to_date = page.locator("div.oxd-input-group", has=page.locator("label", has_text="To Date")).locator("input")
        self.leave_status_drop_down = page.locator("div.oxd-input-group", has=page.locator("label", has_text="Show Leave with Status")).locator("div.oxd-select-text-input")
        self.leave_status_options = page.locator("div.oxd-input-group", has=page.locator("label", has_text="Show Leave with Status"))
        self.leave_type_drop_down = page.locator("div.oxd-input-group", has=page.locator("label", has_text="Leave Type")).locator("div.oxd-select-text-input")
        self.leave_type_options = page.locator("div.oxd-input-group", has=page.locator("label", has_text="Leave Type"))
        self.employee_name = page.get_by_placeholder("Type for hints...")
        self.sub_unit = page.locator("div.oxd-input-group", has=page.locator("label",has_text="Sub Unit")).locator("div.oxd-select-text-input")
        self.past_emp_radio_btn = page.locator("div.oxd-grid-item",has=page.locator("p", has_text="Include Past Employees")).locator("span.oxd-switch-input")
        self.reports_menu = page.locator("span.oxd-topbar-body-nav-tab-item", has_text="Reports")
        self.reports_menu_leave_entl = page.get_by_role("link", name="Leave Entitlements and Usage Report")
        self.reports_menu_my_leave_entl = page.get_by_role("menuitem", name="My Leave Entitlements and Usage Report")
        self.header = page.locator("div.header-wrapper")




    def click_on_leave_menu(self):
        self.leave_menu.click()
        expect(self.page).to_have_url(re.compile("leave"))
        #expect(self.to_date).to_have_value("2026-31-12", timeout=15000)
        expect(self.to_date).to_have_value(re.compile(".+"))
        #self.page.wait_for_load_state("networkidle")

    def click_on_left_menu(self,menu_name):
        directory_menu = self.page.locator("span.oxd-text", has_text=menu_name)
        directory_menu.click()
        expect(self.page).to_have_url(re.compile("directory"))


    def enter_from_date(self,from_date):
        self.from_date.fill(from_date)
        expect(self.from_date).to_have_value(from_date)
        print("from date")

    def enter_to_date(self,to_date):
        self.to_date.fill(to_date)
        expect(self.to_date).to_have_value(to_date)

    def click_leave_status_drop_down(self):
        self.leave_status_drop_down.click()

    def get_leave_status_list(self):
        options = self.leave_status_options.get_by_role("option").all_inner_texts()
        print("options:",options)

    def click_on_leave_type_drop_down(self):
        self.leave_type_drop_down.click()

    def get_leave_type_options(self):
        leave_type_options = self.leave_type_options.get_by_role("option").all_inner_texts()
        print(leave_type_options)

    def select_leave_type(self, leave_type):
        self.leave_type_options.get_by_role("option", name=leave_type).click()
        self.page.wait_for_timeout(5000)
        drop_down_value = self.leave_type_drop_down
        expect(drop_down_value).to_have_text(leave_type)

    def enter_employee_name(self, name):
        self.employee_name.fill(name)
        self.page.get_by_text("Hind hinda").click()
        expect(self.employee_name).to_have_value(re.compile(name))

    def click_on_sub_unit_drop_down(self):
        self.sub_unit.click()

    def select_sub_unit(self,sub_unit):
        sub_unit_options = self.page.locator("div.oxd-input-group", has=self.page.locator("label",has_text="Sub Unit")).get_by_role("option").all_inner_texts()
        self.page.get_by_text(sub_unit).click()
        expect(self.sub_unit).to_have_text(sub_unit)
        print(sub_unit_options)

    def click_on_employees_radio_btn(self):
        self.past_emp_radio_btn.click()
        print(self.past_emp_radio_btn.get_attribute("class"))
        self.past_emp_radio_btn.click()
        print(self.past_emp_radio_btn.get_attribute("class"))

    def select_any_option_from_reports_menu(self):
        self.reports_menu.click()
        self.reports_menu_my_leave_entl.click()
        self.page.wait_for_timeout(5000)
        my_leave_entl_pg = self.page.get_by_role("heading", name="My Leave Entitlements and Usage Report")
        expect(my_leave_entl_pg).to_be_visible()

    def get_data_from_my_leave_entl_tbl(self):
        sections = self.page.locator("revogr-data[type='rgRow']")
        left_section_rows = sections.nth(0).locator("div.rgRow")
        right_section_rows = sections.nth(1).locator("div.rgRow")
        all_values = sections.all_text_contents()
        print(all_values)
        print(left_section_rows.all_text_contents())
        print(right_section_rows.all_text_contents())

        for s, left_row in enumerate(left_section_rows.all_text_contents()):
            if left_row == "CAN - Bereavement":
                row_value = right_section_rows.all_text_contents()[s]
                print("its corresponding values:", row_value)





