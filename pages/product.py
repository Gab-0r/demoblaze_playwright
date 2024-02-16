from playwright.async_api import Page

class Product:
    def __init__(self, page: Page):
        self.page = page

    def add_to_cart_button(self):
        return self.page.locator("#tbodyid > div.row > div > a")
