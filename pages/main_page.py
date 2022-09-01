#класс Главной страницы

from pages.base_page import BasePage
from pages.locators import MainPageLocators
from settings import base_page_url


class MainPage(BasePage):
    #pass
    def __init__(self, driver):
        super().__init__(driver, url=base_page_url)
        self.go_to_site()


    # нажатие на ссылку "Доставка и оплата"
    def click_on_the_help_button(self):
        button = self.find_element(locator=MainPageLocators.button_help)
        return button.click()

    # переход во вкладку "Товары на главной"
    def click_on_product_sale(self):
        tab = self.find_element(locator=MainPageLocators.prd_sale_tab)
        tab.click()
        return tab

    # открытие вкладку "Новинки"
    def click_on_product_new(self):
        tab = self.find_element(locator=MainPageLocators.prd_new_tab)
        tab.click()
        return tab

    # открытие вкладку "Хиты продаж"
    def click_on_product_best(self):
        tab = self.find_element(locator=MainPageLocators.prd_best_tab)
        tab.click()
        return tab

    #получить список товаров из вкладки "Товары на главном"
    def get_list_of_products_sale(self):
        images = self.find_elements(locator=MainPageLocators.prd_sale_images)
        names = self.find_elements(locator=MainPageLocators.prd_sale_names)
        retail_price = self.find_elements(locator=MainPageLocators.prd_sale_retail_price)
        trade_price = self.find_elements(locator=MainPageLocators.prd_sale_trade_price)
        return images, names, retail_price, trade_price

    # получить список товаров из вкладки "Новинки"
    def get_list_of_products_new(self):
        images = self.find_elements(locator=MainPageLocators.prd_new_images)
        names = self.find_elements(locator=MainPageLocators.prd_new_names)
        retail_price = self.find_elements(locator=MainPageLocators.prd_new_retail_price)
        trade_price = self.find_elements(locator=MainPageLocators.prd_new_trade_price)
        ico = self.find_elements(locator=MainPageLocators.prd_new_ico)
        return images, names, retail_price, trade_price, ico

    # получить список товаров из вкладки "Хит продаж"
    def get_list_of_products_best(self):
        images = self.find_elements(locator=MainPageLocators.prd_best_images)
        names = self.find_elements(locator=MainPageLocators.prd_best_names)
        price = self.find_elements(locator=MainPageLocators.prd_best_price)
        ico = self.find_elements(locator=MainPageLocators.prd_best_ico)
        return images, names, price, ico