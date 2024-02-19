from pages.home import Home
from pages.product import Product
from pages.cart import Cart
import time
from playwright.async_api import Page

user = {
    "username":"test",
    "password":"test"
}

place_order = {
    "name": "Gabriel Orozco",
    "country": "Colombia",
    "city": "Medellín",
    "credit_card":"123",
    "month":"02",
    "year":"2024"
}

class TestLogin:
    def test_valid_login(self, page: Page):
        home_page = Home(page)
        home_page.go_to_home()
        home_page.submit_login_form(user)

        is_welcome_visible = home_page.welcome_msg.is_visible()

        assert is_welcome_visible, "Welcome message is not displayed or the user is not logged"


