import pytest
import allure
from pages.order_page import OrderPage
from pages.main_page import MainPage
class TestOrder:

    @pytest.mark.parametrize("button_add_order, first_name, last_name, adress, tel_number, comment", [
        #Набор - верхняя кнопка
        ("header_button", "Бутон", "Цветков", "Москва, ул. Булкина 1", "89991112233", "Написать"),
        #Набор - нижняя кнопка
        ("button_main_page", "Оливье", "Мимозова", "СПб, Пышкина 10", "89992223344", "Позвонить"),
    ])

    @allure.title('Проверка позитивного сценария оформления заказа')
    @allure.description('Оформление заказа по нажатию на кнопку Заказать в шапке или на главной странице')
    def test_add_order(self, driver, button_add_order, first_name, last_name, adress, tel_number, comment):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open_main_page()
        main_page.load_main_page()
        main_page.cockie_check()

        if button_add_order == "header_button":
            main_page.click_order_button_header()
        if button_add_order == "button_main_page":
            main_page.scroll_in_order_button()
            main_page.click_order_button_main_page()

        order_page.loading_first_order_page()
        order_page.fill_first_page_form_order(first_name, last_name, adress, tel_number)
        order_page.click_next_button()
        order_page.loading_second_order_page()
        order_page.fill_second_page_form_order(comment)
        order_page.click_order_button()
        order_page.click_button_confirm_order()

        assert "Заказ оформлен" in order_page.get_text_header_success_order_modal()
