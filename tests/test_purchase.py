from pages.cart import Cart
from pages.home import Home
from pages.product import Product
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

class TestPurchase:
    def test_purchase_product(self, page: Page):
        home_page = Home(page)
        product_page = Product(page)
        cart_page = Cart(page)

        home_page.go_to_home()
        home_page.submit_login_form(user)
        home_page.select_product()
        product_page.add_product_to_cart()
        product_page.go_to_cart()
        cart_page.click_place_order()
        cart_page.fill_place_order_form(place_order)
        cart_page.click_purchase_button()

        is_purchase_complete_visible = cart_page.purchase_complete_msg.is_visible()

        assert is_purchase_complete_visible, "complete purchase message is not displayed"