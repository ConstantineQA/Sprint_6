import pytest
import allure
from pages.order_page import OrderPage
from pages.main_page import MainPage
class TestOrder:

    @allure.title('Проверка позитивного сценария оформления заказа')
    @allure.description('Оформление заказа по нажатию на кнопку Заказать')
    @pytest.mark.parametrize("button_type, first_name, last_name, address, tel_number, comment", [
        ("header", "Бутон", "Цветков", "Москва, ул. Булкина 1", "89991112233", "Написать"),
        ("main", "Оливье", "Мимозова", "СПб, Пышкина 10", "89992223344", "Позвонить"),
    ])
    def test_add_order(self, driver, button_type, first_name, last_name, address, tel_number, comment):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open_main_page()
        main_page.load_main_page()
        main_page.cockie_check()
        main_page.click_order_button(button_type)

        order_page.loading_first_order_page()
        order_page.fill_first_page_form_order(first_name, last_name, address, tel_number)
        order_page.click_next_button()
        order_page.loading_second_order_page()
        order_page.fill_second_page_form_order(comment)
        order_page.click_order_button()
        order_page.click_button_confirm_order()

        assert "Заказ оформлен" in order_page.get_text_header_success_order_modal()
