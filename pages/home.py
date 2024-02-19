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
    
    @property
    def product_item(self):
        return self.page.locator("#tbodyid > div:nth-child(1) > div > div > h4 > a")

    def submit_login_form(self, user: dict):
        self.login_menu_button.click()
        self.username_field.fill(user["username"])
        self.password_field.fill(user["password"])
        self.login_button.click()

    def go_to_home(self):
        self.page.goto("https://www.demoblaze.com/")

    def select_product(self):
        self.product_item.click()