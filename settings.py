#данные для авторизации
u_name = "vika"
u_phone = "+79917628006"
u_email = "sacor53735@upshopt.com"
u_pass = "tt66yy77"

#список url
base_page_url = "https://martichelli.ru/"
catalog_page_url = f"{base_page_url}catalog"
catalog_dresses_page_url = f"{base_page_url}catalog/Platya"
auth_page_url = f"{base_page_url}user/login"
register_page_url = f'{base_page_url}user/register'
user_profile = f"{base_page_url}user/settings"
search_page_url = f"{base_page_url}search"
contact_page_url = f'{base_page_url}page/Kontakty'
table_size_page_url = f'{base_page_url}page/Razmernaya-setka'
delivery_page_url = f'{base_page_url}page/%D0%94%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D0%BA%D0%B0'
#delivery_page_url = f'{base_page_url}page/' + str('Доставка'.encode("utf-8"))
business_page_url = f'{base_page_url}page/Usloviya-sotrudnichestva'
compare_page_url = f'{base_page_url}compare'
shop_cart_page_url = f'{base_page_url}cart'
product_page_url = f'{base_page_url}goods/s3246?from=OTMz&mod_id=250699829'

#значение для поиска
seach_value = 'шорты'


#функции для генерации значений
def generate_string(count):
    txt = ''
    for i in range(count):
        txt += 'm'
    return txt

def russian_chars():
   return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

# Здесь мы взяли 20 популярных китайских иероглифов
def chinese_chars():
   return '的一是不了人我在有他这为之大来以个中上们'

def special_chars():
   return '|\/!@#$%^&*()-_=+`~?"№;:[]{}'

