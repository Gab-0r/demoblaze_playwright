from playwright.async_api import Page

class Cart:
    def __init__(self, page: Page):
        self.page = page

    @property
    def place_order_button(self):
        return self.page.locator("#page-wrapper > div > div.col-lg-1 > button")
    
    @property
    def place_order_name(self):
        return self.page.locator("#name")
    
    @property
    def place_order_country(self):
        return self.page.locator("#country")
    
    @property
    def place_order_city(self):
        return self.page.locator("#city")

    @property
    def place_order_credit_card(self):
        return self.page.locator("#card")
    
    @property
    def place_order_month(self):
        return self.page.locator("#month")
    
    @property
    def place_order_year(self):
        return self.page.locator("#year")
    
    @property
    def purchase_button(self):
        return self.page.locator("#orderModal > div > div > div.modal-footer > button.btn.btn-primary")

    @property
    def purchase_complete_msg(self):
        return self.page.wait_for_selector("body > div.sweet-alert.showSweetAlert.visible > h2")

    def click_place_order(self):
        self.place_order_button.click()

    def fill_place_order_form(self, userData: dict):
        self.place_order_name.fill(userData["name"])
        self.place_order_country.fill(userData["country"])
        self.place_order_city.fill(userData["city"])
        self.place_order_credit_card.press_sequentially(userData["credit_card"])
        self.place_order_month.press_sequentially(userData["month"])
        self.place_order_year.press_sequentially(userData["year"])

    def click_purchase_button(self):
        self.purchase_button.click()

    