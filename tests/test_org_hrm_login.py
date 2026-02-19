#https://opensource-demo.orangehrmlive.com
from playwright.sync_api import Page

from pages.directory.directory_page import Org_Hrm_Directory_Page
from pages.org_hrm_home_page import Org_Hrm_Home_Page
from pages.org_hrm_login_page import Org_Hrm_Login_Page


def tst_login(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    # login_page = Org_Hrm_Login_Page(page)
    # login_page.enter_username("Admin")
    # login_page.enter_password("admin123")
    # login_page.click_login_btn(page)
    home_page = Org_Hrm_Home_Page(page)
    home_page.click_on_left_menu("Directory")
    directory_page = Org_Hrm_Directory_Page(page)
    directory_page.click_on_directory("Amelia Brown")
    #directory_page.click_on_directory("savina dulvin dulvin")

    # home_page.click_on_leave_menu()
    # # home_page.enter_from_date("2026-14-02")
    # # home_page.enter_to_date("2026-15-02")
    # # home_page.click_leave_status_drop_down()
    # # home_page.get_leave_status_list()
    # # home_page.click_on_leave_type_drop_down()
    # # home_page.get_leave_type_options()
    # # home_page.select_leave_type("CAN - FMLA")
    # # # home_page.enter_employee_name("Ahmed")
    # # home_page.click_on_sub_unit_drop_down()
    # # home_page.select_sub_unit("TechOps")
    # # home_page.click_on_employees_radio_btn()
    # home_page.select_any_option_from_reports_menu()
    # home_page.get_data_from_my_leave_entl_tbl()


    page.wait_for_timeout(2000)







