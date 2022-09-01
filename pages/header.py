#класс шапки сайта
from pages.base_page import BasePage
from pages.locators import HeaderLocators


class Header(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url=url)
        self.go_to_site()

    # нажатие на ссылку "Сравнение"
    def click_compare_link(self):
        self.find_element(locator=HeaderLocators.compare_link).click()

    # нажатие на ссылку "Корзина"
    def click_shop_cart_link(self):
        self.find_element(locator=HeaderLocators.shop_cart_link).click()

    # нажатие на Логотип сайта
    def click_logo_link(self):
        self.find_element(locator=HeaderLocators.logo_link).click()

    # нажатие на ссылку "Каталог"
    def click_catalog_link(self):
        self.find_element(locator=HeaderLocators.catalog_link).click()

    # нажатие на ссылку "Контакты"
    def click_contacts_link(self):
        self.find_element(locator=HeaderLocators.contacts_link).click()

    # нажатие на ссылку "Таблица размеров"
    def click_table_size_link(self):
        self.find_element(locator=HeaderLocators.table_size_link).click()

    # нажатие на ссылку "Условия сотрудничества"
    def click_business_link(self):
        self.find_element(locator=HeaderLocators.business_link).click()

    # нажатие на ссылку "Доставка и оплата"
    def click_delivery_link(self):
        self.find_element(locator=HeaderLocators.delivery_link).click()

    # нажатие на кнопку "Обратная связь"
    def click_callback_btn(self):
        self.find_element(locator=HeaderLocators.callback_btn).click()
