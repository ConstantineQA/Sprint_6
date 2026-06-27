import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage

class TestLogo:

    @allure.title('Переход на ya.ru после клика на логотип Яндекс')
    @allure.description('ya.ru открывается в новой вкладке после клика на логотип Яндекс')
    def test_click_logo_ya(self, driver):
        page = MainPage(driver)
        page.open_main_page()
        page.load_main_page()
        page.click_logo_yandex()
        page.open_link_new_tab()
        assert 'https://ya.ru/' in page.get_current_url()

    @allure.title('Переход на главную Яндекс Самокат по клику на логотип Самокат')
    @allure.description('Главная https://qa-scooter.education-services.ru/ открывается в этой же вкладке послек клика на логотип Самокат')
    def test_click_logo_ya_samokat(self, driver):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        order_page.open_order_page()
        order_page.loading_first_order_page()
        main_page.click_logo_ya_samokat()
        assert main_page.get_current_url() == MainPage.URL
