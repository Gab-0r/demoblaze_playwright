from playwright.async_api import Page

class Product:
    def __init__(self, page: Page):
        self.page = page
    
    @property
    def add_to_cart_button(self):
        return self.page.locator("#tbodyid > div.row > div > a")
    
    @property
    def cart_menu_button(self):
        return self.page.locator("#cartur")

    def add_product_to_cart(self):
        self.add_to_cart_button.click()

    def go_to_cart(self):
        self.cart_menu_button.click()