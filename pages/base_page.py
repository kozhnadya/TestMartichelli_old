from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse


#базовый класс для некоторой абстрактной страницы
class BasePage(object):

    #нужны объект веб-драйвера, адрес страницы и время ожидания элементов
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.base_url = url
        self.driver.implicitly_wait(timeout)

    #возвращает короткий адрес текущей страницы
    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path

    #запускает страницу сайта
    def go_to_site(self):
        return self.driver.get(self.base_url)

    #поиск элемента по локатору
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")
    #поиск списка элементов по локатору
    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")