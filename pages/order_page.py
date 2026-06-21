from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from datetime import datetime, timedelta
import allure

class OrderPage:
    
    #Страница
    URL ='https://qa-scooter.education-services.ru/order'
    
    #Локаторы
    #Первая страница оформления заказа
    FIRST_NAME_INPUT = (By.XPATH, "//input[contains(@placeholder,'Имя')]")
    LAST_NAME_INPUT = (By.XPATH, "//input[contains(@placeholder,'Фамилия')]")
    ADRESS_INPUT = (By.XPATH, "//input[contains(@placeholder,'Адрес')]")
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
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть страницу заказа')
    def open_order_page(self):
        self.driver.get(self.URL)

    @allure.step('Загрузка первой страницы оформления заказа')
    def loading_first_order_page(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.NEXT_BUTTON))

    @allure.step('Заполнение первой страницы оформления заказа')
    def fill_first_page_form_order(self, frirst_name, last_name, adress, tel_number):
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(frirst_name)
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*self.ADRESS_INPUT).send_keys(adress)
        self.driver.find_element(*self.METRO_STATION_INPUT).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.FIRST_METRO_STATION))
        self.driver.find_element(*self.FIRST_METRO_STATION).click()
        self.driver.find_element(*self.TELEPHONE_NUMBER_INPUT).send_keys(tel_number)
        
    @allure.step('Клик на кнопку Далее')    
    def click_next_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.NEXT_BUTTON))
        self.driver.find_element(*self.NEXT_BUTTON).click()

    @allure.step('Загрузка второй страницы оформления заказа')
    def loading_second_order_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.ORDER_BUTTON_MIDDLE))

    @allure.step('Заполение второй страницы формы оформления заказа')
    def fill_second_page_form_order(self, comment):
        date = (datetime.now() + timedelta(days=3)).strftime("%d.%m.%Y")
        self.driver.find_element(*self.DATE_PICKER_INPUT).send_keys(date)
        self.driver.find_element(*self.ARROW_WRAPPER).click()
        self.driver.find_element(*self.WRAPPER_OPTION).click()
        self.driver.find_element(*self.COLOR).click()
        self.driver.find_element(*self.COMMENT).send_keys(comment)

    @allure.step('Клик на кнопку Заказать на втором экране формы')
    def click_order_button(self):
        self.driver.find_element(*self.ORDER_BUTTON_MIDDLE).click()

    @allure.step('Подтверждение заказа на кнопку Да')
    def click_button_confirm_order(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.BUTTON_CONFIRM_ORDER))
        self.driver.find_element(*self.BUTTON_CONFIRM_ORDER).click()

    @allure.step('Получение уведомления об успешном оформлении заказа')
    def get_text_header_success_order_modal(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.SUCCESS_MODAL_HEADER))
        return self.driver.find_element(*self.SUCCESS_MODAL_HEADER).text
    