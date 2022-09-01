#тестирование Шапки на различных страницах сайта
import pytest
from pages.header import Header
from pages.search_page import SearchPage
from pages.locators import CallbackLocators
import settings
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#тестирование поиска на разных страницах сайта
#тестирование ввода данных для поиска
@pytest.mark.parametrize('v_url',
                         [settings.base_page_url,
                          settings.catalog_page_url,
                          settings.contact_page_url,
                          settings.table_size_page_url,
                          settings.delivery_page_url,
                          settings.business_page_url,
                          settings.auth_page_url,
                          settings.register_page_url,
                          settings.search_page_url,
                          settings.compare_page_url,
                          settings.shop_cart_page_url],
                         ids=['from main page',
                              'from catalog page',
                              'from contact page',
                              'from table_size page',
                              'from delivery page',
                              'from business page',
                              'from login page',
                              'from register page',
                              'from search page',
                              'from compare page',
                              'from shop_cart page'])
@pytest.mark.parametrize('v_value',
                         ['',
                          settings.generate_string(255),
                          settings.generate_string(1001),
                          settings.russian_chars(),
                          settings.russian_chars().upper(),
                          settings.chinese_chars(),
                          settings.special_chars(),
                          '1234567890'],
                         ids=['empty',
                              '255 simbols',
                              'more than 1000 symbols',
                              'russian',
                              'RUSSIAN',
                              'chinese',
                              'specials',
                              'digit']
                         )
def test_work_search(browser, v_url, v_value):
    page = SearchPage(browser, url=v_url)
    page.enter_search(value=v_value)
    page.click_search_button()
    #проверяем что перешли на страницу поиска
    assert settings.search_page_url in page.driver.current_url

#тестирование ссылки "Сравнение"
@pytest.mark.parametrize('v_url',
                         [settings.base_page_url,
                          settings.catalog_page_url,
                          settings.contact_page_url,
                          settings.table_size_page_url,
                          settings.delivery_page_url,
                          settings.business_page_url,
                          settings.auth_page_url,
                          settings.register_page_url,
                          settings.search_page_url,
                          settings.shop_cart_page_url],
                         ids=['from main page',
                              'from catalog page',
                              'from contact page',
                              'from table_size page',
                              'from delivery page',
                              'from business page',
                              'from login page',
                              'from register page',
                              'from search page',
                              'from shop_cart page'])
def test_click_compare_link(browser, v_url):
    page = Header(browser, url=v_url)
    page.click_compare_link()
    #проверяем что перешли на страницу "Сравнение"
    assert page.driver.current_url == settings.compare_page_url

#тест ссылки "Корзина"
@pytest.mark.parametrize('v_url',
                         [settings.base_page_url,
                          settings.catalog_page_url,
                          settings.contact_page_url,
                          settings.table_size_page_url,
                          settings.delivery_page_url,
                          settings.business_page_url,
                          settings.auth_page_url,
                          settings.register_page_url,
                          settings.search_page_url,
                          settings.compare_page_url],
                         ids=['from main page',
                              'from catalog page',
                              'from contact page',
                              'from table_size page',
                              'from delivery page',
                              'from business page',
                              'from login page',
                              'from register page',
                              'from search page',
                              'from compare page'])
def test_click_shop_cart_link(browser, v_url):
    page = Header(browser, url=v_url)
    page.click_shop_cart_link()
    # проверяем что перешли на страницу "Корзина"
    assert page.driver.current_url == settings.shop_cart_page_url

#тест ссылки логотипа
@pytest.mark.parametrize('v_url',
                         [settings.base_page_url,
                          settings.catalog_page_url,
                          settings.contact_page_url,
                          settings.table_size_page_url,
                          settings.delivery_page_url,
                          settings.business_page_url,
                          settings.auth_page_url,
                          settings.register_page_url,
                          settings.search_page_url,
                          settings.compare_page_url,
                          settings.shop_cart_page_url],
                         ids=['from main page',
                              'from catalog page',
                              'from contact page',
                              'from table_size page',
                              'from delivery page',
                              'from business page',
                              'from login page',
                              'from register page',
                              'from search page',
                              'from compare page',
                              'from shop_cart page'])
def test_click_logo_link(browser, v_url):
    page = Header(browser, url=v_url)
    page.click_logo_link()
    # проверяем что перешли на главную страницу
    assert page.driver.current_url == settings.base_page_url

#тест ссылки "Каталог"
@pytest.mark.parametrize('v_url',
                         [settings.base_page_url,
                          settings.catalog_page_url,
                          settings.contact_page_url,
                          settings.table_size_page_url,
                          settings.delivery_page_url,
                          settings.business_page_url,
                          settings.auth_page_url,
                          settings.register_page_url,
                          settings.search_page_url,
                          settings.compare_page_url,
                          settings.shop_cart_page_url],
                         ids=['from main page',
                              'from catalog page',
                              'from contact page',
                              'from table_size page',
                              'from delivery page',
                              'from business page',
                              'from login page',
                              'from register page',
                              'from search page',
                              'from compare page',
                              'from shop_cart page'])
def test_click_catalog_link(browser, v_url):
    page = Header(browser, url=v_url)
    page.click_catalog_link()
    # ожидаем загрузку заголовка на странице Каталога
    wait = WebDriverWait(page.driver, 10).until(EC.title_is("Каталог товаров"))
    # Проверяем, что мы оказались на странице Каталога
    assert page.driver.current_url == settings.catalog_page_url

#тест ссылки "Доставка и оплата"
@pytest.mark.parametrize('v_url',
                         [settings.base_page_url,
                          settings.catalog_page_url,
                          settings.contact_page_url,
                          settings.table_size_page_url,
                          settings.delivery_page_url,
                          settings.business_page_url,
                          settings.auth_page_url,
                          settings.register_page_url,
                          settings.search_page_url,
                          settings.compare_page_url,
                          settings.shop_cart_page_url],
                         ids=['from main page',
                              'from catalog page',
                              'from contact page',
                              'from table_size page',
                              'from delivery page',
                              'from business page',
                              'from login page',
                              'from register page',
                              'from search page',
                              'from compare page',
                              'from shop_cart page'])
def test_click_delivery_link(browser, v_url):
    page = Header(browser, url=v_url)
    page.click_delivery_link()
    # проверяем что перешли на страницу Доставка
    assert page.driver.current_url == settings.delivery_page_url

#тест ссылки "Контакты"
@pytest.mark.parametrize('v_url',
                         [settings.base_page_url,
                          settings.catalog_page_url,
                          settings.contact_page_url,
                          settings.table_size_page_url,
                          settings.delivery_page_url,
                          settings.business_page_url,
                          settings.auth_page_url,
                          settings.register_page_url,
                          settings.search_page_url,
                          settings.compare_page_url,
                          settings.shop_cart_page_url],
                         ids=['from main page',
                              'from catalog page',
                              'from contact page',
                              'from table_size page',
                              'from delivery page',
                              'from business page',
                              'from login page',
                              'from register page',
                              'from search page',
                              'from compare page',
                              'from shop_cart page'])
def test_click_contacts_link(browser, v_url):
    page = Header(browser, url=v_url)
    page.click_contacts_link()
    # проверяем что перешли на страницу Контакты
    assert page.driver.current_url == settings.contact_page_url

#тест ссылки "Таблица размеров"
@pytest.mark.parametrize('v_url',
                         [settings.base_page_url,
                          settings.catalog_page_url,
                          settings.contact_page_url,
                          settings.table_size_page_url,
                          settings.delivery_page_url,
                          settings.business_page_url,
                          settings.auth_page_url,
                          settings.register_page_url,
                          settings.search_page_url,
                          settings.compare_page_url,
                          settings.shop_cart_page_url],
                         ids=['from main page',
                              'from catalog page',
                              'from contact page',
                              'from table_size page',
                              'from delivery page',
                              'from business page',
                              'from login page',
                              'from register page',
                              'from search page',
                              'from compare page',
                              'from shop_cart page'])
def test_click_table_size_link(browser, v_url):
    page = Header(browser, url=v_url)
    page.click_table_size_link()
    # проверяем что перешли на страницу Таблица размеров
    assert page.driver.current_url == settings.table_size_page_url

#тест ссылки "Условия сотрудничества"
@pytest.mark.parametrize('v_url',
                         [settings.base_page_url,
                          settings.catalog_page_url,
                          settings.contact_page_url,
                          settings.table_size_page_url,
                          settings.delivery_page_url,
                          settings.business_page_url,
                          settings.auth_page_url,
                          settings.register_page_url,
                          settings.search_page_url,
                          settings.compare_page_url,
                          settings.shop_cart_page_url],
                         ids=['from main page',
                              'from catalog page',
                              'from contact page',
                              'from table_size page',
                              'from delivery page',
                              'from business page',
                              'from login page',
                              'from register page',
                              'from search page',
                              'from compare page',
                              'from shop_cart page'])
def test_click_business_link(browser, v_url):
    page = Header(browser, url=v_url)
    page.click_business_link()
    # проверяем что перешли на страницу Таблица размеров
    assert page.driver.current_url == settings.business_page_url


#@pytest.mark.parametrize('v_url', [settings.base_page_url], ids=['from main page'])
@pytest.mark.parametrize('v_url',
                         [settings.base_page_url,
                          settings.catalog_page_url,
                          settings.contact_page_url,
                          settings.table_size_page_url,
                          settings.delivery_page_url,
                          settings.business_page_url,
                          settings.auth_page_url,
                          settings.register_page_url,
                          settings.search_page_url,
                          settings.compare_page_url,
                          settings.shop_cart_page_url],
                         ids=['from main page',
                              'from catalog page',
                              'from contact page',
                              'from table_size page',
                              'from delivery page',
                              'from business page',
                              'from login page',
                              'from register page',
                              'from search page',
                              'from compare page',
                              'from shop_cart page'])
def test_click_callback_btn(browser, v_url):
    page = Header(browser, url=v_url)
    page.click_callback_btn()
    assert page.find_element(locator=CallbackLocators.callback_title).text == "Обратный звонок".upper()
