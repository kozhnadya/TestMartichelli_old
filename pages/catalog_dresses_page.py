#класс страницы с товарами "Платье"
from pages.base_page import BasePage
from pages.locators import ProductLocators
from settings import catalog_dresses_page_url
from selenium.webdriver.support.ui import Select


class CatalogDressesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, url=catalog_dresses_page_url)
        self.go_to_site()

    #получить фото товара
    def get_product_images(self):
        return self.find_elements(locator=ProductLocators.prd_images)

    # получить ссылку с фото товара
    def get_product_image_links(self):
        return self.find_elements(locator=ProductLocators.prd_image_links)

    # получить наименвоание товара
    def get_product_names(self):
        return self.find_elements(locator=ProductLocators.prd_names)

    # получить розничную цену товара
    def get_product_rtl_prices(self):
        return self.find_elements(locator=ProductLocators.prd_rtl_price)

    # получить оптовую цену товара
    def get_product_prices(self):
        return self.find_elements(locator=ProductLocators.prd_price)

    #сортировка товаров  по типу от Дорогого к дешевым
    def sort_expensive_to_cheap(self):
        sort = Select(self.find_element(ProductLocators.toolbar_sort))
        sort.select_by_visible_text("цене: Дорогие — Дешевые")

    #сортировка товаров по типу от Дешевого к дорогому
    def sort_cheap_to_expensive(self):
        sort = Select(self.find_element(ProductLocators.toolbar_sort))
        sort.select_by_visible_text("цене: Дешевые — Дорогие")

