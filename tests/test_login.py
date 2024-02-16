from pages.home import Home
import time
from playwright.async_api import Page

class TestLogin:
    def test_valid_login(self, page: Page):
        home_page = Home(page)
        home_page.go_to_home()
        home_page.submit_login_form()

        is_welcome_visible = home_page.welcome_msg.is_visible()

        assert is_welcome_visible, "Welcome message is not displayed or the user is not logged"

        time.sleep(2)

    # def test_purchase_product(self, page: Page):
    #     home_page = Home(page)


