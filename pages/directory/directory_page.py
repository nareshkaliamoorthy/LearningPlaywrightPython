from unittest import expectedFailure

from playwright.sync_api import Page, expect


class Org_Hrm_Directory_Page:

    def __init__(self, page: Page):
        self.page = page

    def get_dir_card(self, name):
        return self.page.locator("p.oxd-text", has_text = name)


    def click_on_directory(self, card_name):
        card = self.scroll_to_card(card_name)
        # card = self.get_dir_card(card_name)
        # card.scroll_into_view_if_needed()
        card.click()
        directory_sidebar_card = self.page.locator("div.orangehrm-corporate-directory-sidebar", has = self.page.locator("p", has_text=card_name))
        expect(directory_sidebar_card).to_be_visible()
        self.page.wait_for_timeout(5000)

    def scroll_to_card(self,card_name):
        container = self.page.locator("div.orangehrm-container")

        for x in range (15):
            card = self.page.locator("p.orangehrm-directory-card-header", has_text=card_name)

            if card.count() > 0:
                card.first.scroll_into_view_if_needed()
                return card.first

            container.evaluate("el => el.scrollTop += 500")
            self.page.wait_for_timeout(1000)
        raise Exception ("Scroll failed",{card_name})




