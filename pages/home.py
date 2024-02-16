from playwright.async_api import Page

class Home:
    def __init__(self, page: Page):
        self.page = page

    @property
    def login_menu_button(self):
        return self.page.locator("#login2")
    
    @property
    def username_field(self):
        return self.page.locator("#loginusername")
    
    @property
    def password_field(self):
        return self.page.locator("#loginpassword")

    @property
    def login_button(self):
        return self.page.get_by_role("button", name="Log in")
    
    @property
    def welcome_msg(self):
        return self.page.wait_for_selector("#nameofuser")

    def submit_login_form(self):
        self.login_menu_button.click()
        self.username_field.fill("test")
        self.password_field.fill("test")
        self.login_button.click()

    def go_to_home(self):
        self.page.goto("https://www.demoblaze.com/")

        