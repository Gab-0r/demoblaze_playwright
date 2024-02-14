import re
import time
from playwright.async_api import Page, expect

def test_purchase(page: Page):
    page.goto("https://www.demoblaze.com/")
    page.get_by_role("link", name="Log in").click()
    page.locator("#loginusername").fill("test")
    page.locator("#loginpassword").fill("test")
    page.get_by_role("button", name="Log in").click()
    page.locator("#tbodyid > div:nth-child(1)").click()
    page.locator("#tbodyid > div.row > div > a").click()
    page.locator("#cartur").click()
    page.get_by_role("button", name="Place Order").click()
    page.locator("#name").fill("Gabriel")
    page.locator("#country").fill("Colombia")
    page.locator("#city").fill("Medellín")
    page.locator("#card").press_sequentially("123")
    page.locator("#month").press_sequentially("02")
    page.locator("#year").press_sequentially("2024")
    page.get_by_role("button", name="Purchase").click()    

    expect(page.locator("body > div.sweet-alert.showSweetAlert.visible")).to_be_visible()

    time.sleep(2)
    