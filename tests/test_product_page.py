import time
from pages.product_page import ProductPage

#позитивный тест добавления товара в корзину
def test_add_in_shop_cart(browser):
    page = ProductPage(browser)
    old_cart_count = page.get_shop_cart_count()
    inpt_count = page.get_input_count_value()
    print(inpt_count)
    page.click_shop_cart()
    time.sleep(3)
    new_cart_count = page.get_shop_cart_count()
    assert new_cart_count == (old_cart_count + inpt_count)

#негативный тест добавления недопустимого кол-ва товаров в корзину
def test_add_in_shop_cart_negative(browser):
    page = ProductPage(browser)
    old_cart_count = page.get_shop_cart_count()
    #вводим значение больше допустимого
    inpt_count = page.enter_input_count_value(1001)
    time.sleep(5)
    print(inpt_count)
    page.click_shop_cart()
    time.sleep(3)
    new_cart_count = page.get_shop_cart_count()
    #проверяем что кол-во товара в корзине не изменилось
    assert new_cart_count == old_cart_count