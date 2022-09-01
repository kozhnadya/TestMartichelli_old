# тестирование Главной страницы сайта
from pages.main_page import MainPage


#проверка карточек товара во вкладке "Товары на главной"
def test_open_product_sale_tab(browser):
    page = MainPage(browser)
    #переходим во вкладку "Товары на главной"
    tab = page.click_on_product_sale()
    #проверяем, что вкладка активна
    assert "active" in tab.get_attribute("class")
    images, names, rtl_price, trd_price = page.get_list_of_products_sale()
    #проверка, что у каждой карточки товара есть фото, наименование, розничная цена, оптовая цена
    for i in range(len(images)):
        assert images[i].get_attribute("src") != ''
        assert names[i].text != ''
        assert rtl_price[i].text != ''
        assert trd_price[i].text != ''

#проверка карточек товара во вкладке "Новинки"
def test_open_product_new_tab(browser):
    page = MainPage(browser)
    #переходим во вкладку "Новинки"
    tab = page.click_on_product_new()
    #проверяем, что вкладка активна
    assert "active" in tab.get_attribute("class")
    images, names, rtl_price, trd_price, ico = page.get_list_of_products_new()
    #проверка, что у каждой карточки товара есть фото, наименование, розничная цена, оптовая цена, значок "Новинка"
    for i in range(len(images)):
        assert images[i].get_attribute("src") != ''
        assert names[i].text != ''
        assert rtl_price[i].text != ''
        assert trd_price[i].text != ''
        assert ico[i].text != 'Новинка'


#проверка карточек товара во вкладке "Хит продаж"
def test_open_product_best_tab(browser):
    page = MainPage(browser)
    #переходим во вкладку "Хит продаж"
    tab = page.click_on_product_best()
    #проверяем, что вкладка активна
    assert "active" in tab.get_attribute("class")
    images, names, price, ico = page.get_list_of_products_best()
    #проверка, что у каждой карточки товара есть фото, наименование, цена, значок "Хит"
    for i in range(len(images)):
        assert images[i].get_attribute("src") != ''
        assert names[i].text != ''
        assert price[i].text != ''
        assert ico[i].text != 'Хит'


