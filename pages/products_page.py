from playwright.sync_api import Page
from utils.test_data import BASE_URL


class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.inventory_items = page.locator(".inventory_item")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")

    def open(self):
        self.page.goto(f"{BASE_URL}/inventory.html")
        return self

    def is_loaded(self) -> bool:
        return self.inventory_items.first.is_visible()

    def get_items_count(self) -> int:
        return self.inventory_items.count()

    def add_product(self, name: str):
        item = self.inventory_items.filter(has_text=name)
        item.get_by_role("button", name="Add to cart").click()

    def remove_product(self, name: str):
        item = self.inventory_items.filter(has_text=name)
        item.get_by_role("button", name="Remove").click()

    def open_cart(self):
        self.cart_link.click()