#класс страницы "Поиск"

from pages.base_page import BasePage
from pages.locators import SearchLocators
from settings import search_page_url


class SearchPage(BasePage):
    def __init__(self, driver, url=search_page_url):
        super().__init__(driver, url=url)
        self.go_to_site()

    #вводим в поле ввода поиска
    def enter_search(self, value):
        seach_box = self.find_element(locator=SearchLocators.search_txt)
        print(seach_box.get_attribute("value"))
        seach_box.send_keys(value)

    #нажимаем на кнопку поиска
    def click_search_button(self):
        seach_btn = self.find_element(locator=SearchLocators.search_btn)
        seach_btn.click()
