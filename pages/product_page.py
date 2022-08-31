from settings import product_page_url
from pages.base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.keys import Keys

class ProductPage(BasePage):
    def __init__(self, driver, url=product_page_url):
        super().__init__(driver, url=url)
        self.go_to_site()

    def click_shop_cart(self):
        btn = self.find_element(locator=ProductPageLocators.shop_cart_btn)
        btn.click()

    def get_shop_cart_count(self):
        return int(self.find_element(locator=ProductPageLocators.shop_cart_count).text)

    def get_input_count_value(self):
        return int(self.find_element(locator=ProductPageLocators.input_count).get_attribute('value'))

    def enter_input_count_value(self, value):
        inp_count = self.find_element(locator=ProductPageLocators.input_count)
        inp_count.click()
        inp_count.send_keys(Keys.CONTROL+'a')
        inp_count.send_keys(Keys.DELETE)
        inp_count.send_keys(value)
        return self.get_input_count_value()


