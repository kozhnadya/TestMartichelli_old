#тестируем страницу с товарами "Платье"
from pages.catalog_dresses_page import CatalogDressesPage
from pages.locators import ProductPageLocators

# проверяем наличие у товаров фото, наименования, цены
def test_catalog_dresses_page(browser):
    page = CatalogDressesPage(browser)
    images = page.get_product_images()
    names = page.get_product_names()
    rtl_prices = page.get_product_rtl_prices()
    prices = page.get_product_prices()
    for i in range(len(images)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert rtl_prices[i].text != ''
        assert prices[i].text != ''

#проверяем что товар соответствует категории страницы
def test_check_name_product(browser):
    page = CatalogDressesPage(browser)
    names = page.get_product_names()
    for i in range(len(names)):
        assert "платье" in (names[i].text).lower()


#тестируем сортировку "Дорогие-Дешевые"
def test_sort_expensive_to_cheap(browser):
    page = CatalogDressesPage(browser)
    page.sort_expensive_to_cheap()
    prices = page.get_product_prices()
    for i in range(len(prices)-1):
        assert int(prices[i].text.replace(' ', '')) >= int(prices[i+1].text.replace(' ',''))


#тестируем сортировку "Дешевые-Дорогие"
def test_sort_expensive_to_cheap(browser):
    page = CatalogDressesPage(browser)
    page.sort_cheap_to_expensive()
    prices = page.get_product_prices()
    for i in range(len(prices)-1):
        assert int(prices[i].text.replace(' ', '')) <= int(prices[i+1].text.replace(' ',''))

#тест на соответствие ссылки карточки с товаром
def test_click_product_link(browser):
    page = CatalogDressesPage(browser)
    #image_links = page.get_product_image_links()
    names = page.get_product_names()
    for i in range(len(names)):
        image_links = page.get_product_image_links()
        names = page.get_product_names()
        #проверяем что ссылки изображения и наименования равны
        assert image_links[i].get_attribute('href') == names[i].get_attribute('href')
        crt_name = names[i].text
        image_links[i].click()
        prd_name = page.find_element(locator=ProductPageLocators.prd_name)
        # проверяем наименование на странице товара соответствует
        # наименованию на карточке
        assert crt_name.lower() == (prd_name.text).lower()
        page.driver.back()






