from selenium.webdriver.common.by import By


class AuthPageLocators:
    auth_email = (By.ID, "email")
    auth_pass = (By.ID, "sites_client_pass")
    auth_btn = (By.ID, "send2")
    error_mess = (By.CLASS_NAME, "warning")
    invalid_input_mess = (By.XPATH, '//label[@class="invalidInput"]')

class MainPageLocators:
    prd_sale_tab = (By.XPATH, '//*[@id="producttabs"]//*[@data-href="pdt-sale"]')
    prd_new_tab = (By.XPATH, '//*[@id="producttabs"]//*[@data-href="pdt-new"]')
    prd_best_tab = (By.XPATH, '//*[@id="producttabs"]//*[@data-href="pdt-best"]')

    prd_sale_images = (By.XPATH, '//*[@class="pdt-sale pdt-content active"]//*[@class="product-image2"]//img')
    prd_sale_names = (By.XPATH, '//*[@class="pdt-sale pdt-content active"]//*[@class="product-name"]/a')
    prd_sale_retail_price = (By.XPATH, '//*[@class="pdt-sale pdt-content active"]//*[@class="price rtl-price RUB"]')
    prd_sale_trade_price = (By.XPATH, '//*[@class="pdt-sale pdt-content active"]//*[@class="price RUB"]//*[@class="num"]')

    prd_new_images = (By.XPATH, '//*[@class="pdt-new pdt-content active"]//*[@class="product-image2"]//img')
    prd_new_names = (By.XPATH, '//*[@class="pdt-new pdt-content active"]//*[@class="product-name"]/a')
    prd_new_retail_price = (By.XPATH, '//*[@class="pdt-new pdt-content active"]//*[@class="price rtl-price RUB"]')
    prd_new_trade_price = (By.XPATH, '//*[@class="pdt-new pdt-content active"]//*[@class="price RUB"]//*[@class="num"]')
    prd_new_ico = (By.XPATH, '//*[@class="pdt-new pdt-content active"]//*[@class="ico-new"]')

    prd_best_images = (By.XPATH, '//*[@class="pdt-best pdt-content active"]//*[@class="product-image2"]//img')
    prd_best_names = (By.XPATH, '//*[@class="pdt-best pdt-content active"]//*[@class="product-name"]/a')
    prd_best_price = (By.XPATH, '//*[@class="pdt-best pdt-content active"]//*[@class="price RUB"]//*[@class="num"]')
    prd_best_ico = (By.XPATH, '//*[@class="pdt-best pdt-content active"]//*[@class="ico-best"]')


class UserProfileLocators:
    u_prf_message = (By.CLASS_NAME, "message success")


class CatalogPageLocators:
    catalog_name = (By.XPATH, '//*[@class="cat-name"]')


class SearchLocators:
    search_txt = (By.XPATH, '//*[@id="search_mini_form"]//input[@type="text"]')
    search_btn = (By.XPATH, '//*[@id="search_mini_form"]//button')
    search_res_title = (By.XPATH, '//*[@id="main"]//h1[@class="title"]')


class ProductLocators:
    prd_images = (By.XPATH, '//*[@class="product-image2"]//img')
    prd_image_links = (By.XPATH, '//*[@class="product-image2"]/a')
    prd_names = (By.XPATH, '//*[@class="product-name"]/a')
    prd_rtl_price = (By.XPATH, '//*[@class="price rtl-price RUB"]')
    prd_price = (By.XPATH, '//*[@class="price RUB"]//*[@class="num"]')
    limit_page = (By.XPATH, '//*[@class="toolbar"]//*[@name="per_page"]//option')
    toolbar_sort = (By.XPATH, '//*[@class="toolbar"]//*[@class="sort-by"]//*[@name="goods_search_field_id"]')

class ProductPageLocators:
    prd_name = (By.XPATH, '//*[@class="product-name"]//*[@itemprop="name"]')
    shop_cart_btn = (By.XPATH, '//*[@class="add-to-cart"]//*[@class="add-cart button button2"]')
    shop_cart_count = (By.CLASS_NAME, 'cart-count')
    input_count = (By.XPATH, '//*[@class="inputText quantity"]')

class HeaderLocators:
    #links
    compare_link = (By.XPATH, '//*[@class = "block compare  "]')
    shop_cart_link = (By.XPATH, '//*[@class = "block cart  "]')
    logo_link = (By.XPATH, '//*[@class="logo col-md-2 col-xs-6"]')
    catalog_link = (By.XPATH, '//*[@id="header"]//*[@class="header-middle"]//*[contains(text(), "Каталог")]')
    contacts_link = (By.XPATH, '//*[@id="header"]//*[@class="header-middle"]//*[contains(text(), "Контакты")]')
    table_size_link = (By.XPATH, '//*[@class="header-middle"]//*[contains(text(), "Таблица размеров")]')
    business_link = (By.XPATH, '//*[@class="header-middle"]//*[contains(text(), "Условия сотрудничества")]')
    delivery_link = (By.XPATH, '//*[@id="header"]//*[@class="header-middle"]//*[contains(text(), "Оплата и доставка")]')

    #buttons
    callback_btn = (By.XPATH, '//*[@id="header"]//*[@class="button button3"]')

class CallbackLocators:
    callback_win = (By.ID, 'fancybox-callback')
    callback_title = (By.XPATH, '//*[@id="fancybox-callback"]/*[@class="title"]')


class ShopCartLocators:
    catalog_link = (By.LINK_TEXT, 'каталога')
    clear_cart = (By.XPATH, '//*[@class="button col-left"]')
    mess_clear_cart = (By.CLASS_NAME, 'success')
    product_table = (By.CLASS_NAME, 'container')
    products = (By.XPATH, '//*[@class="cart-products-list"]/li')

