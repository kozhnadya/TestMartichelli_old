#тестирование результатов поиска
from pages.search_page import SearchPage
from pages.locators import SearchLocators, ProductLocators
import settings


def test_results_seach(browser):
    page = SearchPage(browser)
    page.enter_search(settings.seach_value)
    page.click_search_button()
    #проверяем что в заголовке результата содержится текст поиска
    assert settings.seach_value in page.find_element(locator=SearchLocators.search_res_title).text

    images = page.find_elements(locator=ProductLocators.prd_images)
    names = page.find_elements(locator=ProductLocators.prd_names)
    price = page.find_elements(locator=ProductLocators.prd_price)
    limit_value = int(page.find_element(locator=ProductLocators.limit_page).text)
    #проверяем кол-во товаров на странице с лимитом товаров на странице
    assert limit_value == len(images)
    #проверяем наличие у товара фото, наименования, цены
    for i in range(limit_value):
        assert images[i].get_attribute("src") != ''
        assert names[i].text != ''
        assert price[i].text != ''







