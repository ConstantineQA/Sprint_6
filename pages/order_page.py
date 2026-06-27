from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
from pages.base_page import BasePage
import allure

class OrderPage(BasePage):
    
    #Страница
    URL ='https://qa-scooter.education-services.ru/order'
    
    #Локаторы
    #Первая страница оформления заказа
    FIRST_NAME_INPUT = (By.XPATH, "//input[contains(@placeholder,'Имя')]")
    LAST_NAME_INPUT = (By.XPATH, "//input[contains(@placeholder,'Фамилия')]")
    ADDRESS_INPUT = (By.XPATH, "//input[contains(@placeholder,'Адрес')]")
    METRO_STATION_INPUT = (By.XPATH, "//input[contains(@placeholder,'метро')]")
    FIRST_METRO_STATION = (By.XPATH, "//ul[@class='select-search__options']/li[1]")
    TELEPHONE_NUMBER_INPUT = (By.XPATH, "//input[contains(@placeholder,'Телефон')]")
    NEXT_BUTTON = (By.XPATH, "//button[text() = 'Далее']")
    
    #Вторая страница оформления заказа
    DATE_PICKER_INPUT = (By.XPATH, "//div[contains(@class,'react-datepicker')]/input")
    ARROW_WRAPPER = (By.XPATH, "//div[@class='Dropdown-arrow-wrapper']/span")
    WRAPPER_OPTION = (By.XPATH, "//div[@class='Dropdown-menu']/div[1]")
    COLOR = (By.ID, "grey")
    COMMENT = (By.XPATH, "//input[contains(@placeholder,'Комментарий')]")
    ORDER_BUTTON_MIDDLE = (By.XPATH, "//button[contains(@class,'Button_Middle') and text()= 'Заказать']")

    #Кнопка подтверждения заказа
    BUTTON_CONFIRM_ORDER = (By.XPATH, "//button[text()='Да']")

    #Заголовок модального окна об успешном оформлении заказа
    SUCCESS_MODAL_HEADER = (By.XPATH, "//div[contains(@class, 'Order_Modal')]/div[contains(@class, 'Order_ModalHeader')]")
    
    #Методы
    @allure.step('Открыть страницу заказа')
    def open_order_page(self):
        self.open_url(self.URL)

    @allure.step('Загрузка первой страницы оформления заказа')
    def loading_first_order_page(self):
        self.wait_for_visible(self.NEXT_BUTTON, timeout=5)

    @allure.step('Заполнение первой страницы оформления заказа')
    def fill_first_page_form_order(self, first_name, last_name, address, tel_number):
        self.send_keys_to_element(self.FIRST_NAME_INPUT, first_name)
        self.send_keys_to_element(self.LAST_NAME_INPUT, last_name)
        self.send_keys_to_element(self.ADDRESS_INPUT, address)
        self.click_element(self.METRO_STATION_INPUT)
        self.wait_for_visible(self.FIRST_METRO_STATION)
        self.click_element(self.FIRST_METRO_STATION)
        self.send_keys_to_element(self.TELEPHONE_NUMBER_INPUT, tel_number)
        
    @allure.step('Клик на кнопку Далее')    
    def click_next_button(self):
        self.click_element(self.NEXT_BUTTON)

    @allure.step('Загрузка второй страницы оформления заказа')
    def loading_second_order_page(self):
        self.wait_for_visible(self.ORDER_BUTTON_MIDDLE, timeout=3)

    @allure.step('Заполнение второй страницы формы оформления заказа')
    def fill_second_page_form_order(self, comment):
        date = (datetime.now() + timedelta(days=3)).strftime("%d.%m.%Y")
        self.send_keys_to_element(self.DATE_PICKER_INPUT, date)
        self.click_element(self.ARROW_WRAPPER)
        self.click_element(self.WRAPPER_OPTION)
        self.click_element(self.COLOR)
        self.send_keys_to_element(self.COMMENT, comment)

    @allure.step('Клик на кнопку Заказать на втором экране формы')
    def click_order_button(self):
        self.click_element(self.ORDER_BUTTON_MIDDLE)

    @allure.step('Подтверждение заказа на кнопку Да')
    def click_button_confirm_order(self):
        self.click_element(self.BUTTON_CONFIRM_ORDER)

    @allure.step('Получение уведомления об успешном оформлении заказа')
    def get_text_header_success_order_modal(self):
        self.wait_for_visible(self.SUCCESS_MODAL_HEADER, timeout=10)
        return self.get_text(self.SUCCESS_MODAL_HEADER)
    