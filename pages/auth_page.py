#класс страницы авторизации
import selenium.common.exceptions
from pages.base_page import BasePage
from pages.locators import AuthPageLocators
from settings import auth_page_url


class AuthPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, url=auth_page_url)
        self.go_to_site()


    def enter_email(self, value):
        box_email = self.find_element(locator=AuthPageLocators.auth_email)
        box_email.send_keys(value)

    def enter_pass(self, value):
        box_pass = self.find_element(locator=AuthPageLocators.auth_pass)
        box_pass.send_keys(value)

    def click_auth_btn(self):
        btn_sign_on = self.find_element(locator=AuthPageLocators.auth_btn)
        try:
            btn_sign_on.click()
        except selenium.common.exceptions.ElementClickInterceptedException:
            print("Кнопка 'Войти' недоступна для нажатия")

    def get_error_message(self):
        return self.find_element(locator=AuthPageLocators.error_mess)

    def get_invalid_input_message(self):
        return self.find_element(locator=AuthPageLocators.invalid_input_mess)
