# тестирование страницы авторизации на сайте

import pytest
from pages.auth_page import AuthPage
import settings


#позитивный тест на авторизацию
def test_auth_page(browser):
    page = AuthPage(browser)
    page.enter_email(settings.u_email)
    page.enter_pass(settings.u_pass)
    assert page.get_error_message.text == ''
    page.click_auth_btn()
    # ожидаем загрузку страницы личного кабинета
    assert page.get_relative_link() == settings.user_profile.replace(settings.base_page_url, '')


#негативный тест на авторизацию
#проверка вводом различных значений в поле ввода
@pytest.mark.parametrize('n_email',
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
@pytest.mark.parametrize('n_pass',
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
def test_auth_page_negativ(browser, n_email, n_pass):
    page = AuthPage(browser)
    page.enter_email(n_email)
    page.enter_pass(n_pass)
    page.click_auth_btn()
    #проверяем что остались на сайте авторизации
    assert page.get_relative_link() == settings.auth_page_url.replace(settings.base_page_url, '')
