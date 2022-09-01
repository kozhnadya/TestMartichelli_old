#тестирование страницы Корзины

from pages.shop_cart_page import ShopCartPage
import test_product_page
from selenium.common.exceptions import TimeoutException

def test_click_clear_shop_cart(browser):
    #добавила два товар в корзину
    for i in range(2):
        test_product_page.test_add_in_shop_cart(browser)
    page = ShopCartPage(browser)
    #проверяем что корзина не пустая
    products = page.get_list_products()
    assert len(products) > 0
    #нажимаем кнопку "Очистить корзину"
    page.click_clear_cart()
    #потверждаем очистку в окне потверждения
    page.driver.switch_to_alert().accept()
    try:
        products = page.get_list_products()
        assert False
    except TimeoutException:
        print('shop_cart_is_empty')
        return True

