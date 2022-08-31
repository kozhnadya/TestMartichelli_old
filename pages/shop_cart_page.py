from settings import shop_cart_page_url, catalog_dresses_page_url
from .base_page import BasePage
from .locators import ShopCartLocators

class ShopCartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, url=shop_cart_page_url)
        self.go_to_site()

    def click_catalog_link(self):
        self.find_element(locator=ShopCartLocators.catalog_link).click()

    def click_clear_cart(self):
        self.find_element(locator=ShopCartLocators.clear_cart).click()

    def add_product_to_shop_cart(self):
        new_win = f'window.open({catalog_dresses_page_url})'
        self.driver.execute_script(new_win)

    def get_mess_clear_cart(self):
        mess = self.find_element(locator=ShopCartLocators.mess_clear_cart).text
        return mess

    def get_products(self):
        return self.find_elements(locator=ShopCartLocators.products)
