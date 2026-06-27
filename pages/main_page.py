from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class MainPage(BasePage):

    #Страница
    URL = 'https://qa-scooter.education-services.ru/'

    #Локаторы
    #Кнопки оформления заказа
    ORDER_BUTTON_HEADER = (By.XPATH, "//div[contains(@class,'Header_Nav')]/button[contains(@class,'Button_Button')]")
    CONTAINER_FOR_ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Home_FinishButton')]")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Home_FinishButton')]//button[text()='Заказать']")

    #Аккордион и кнопки с вопросами
    ACCORDION_FAQ = (By.XPATH, "//div[contains(@class,'Home_FAQ')]/div[@class='accordion']")
    ACCORDION_ITEM_ONE = (By.ID, "accordion__heading-0") 
    ACCORDION_ITEM_TWO = (By.ID, "accordion__heading-1")
    ACCORDION_ITEM_THREE = (By.ID, "accordion__heading-2")
    ACCORDION_ITEM_FOUR = (By.ID, "accordion__heading-3")
    ACCORDION_ITEM_FIVE = (By.ID, "accordion__heading-4")
    ACCORDION_ITEM_SIX = (By.ID, "accordion__heading-5")
    ACCORDION_ITEM_SEVEN = (By.ID, "accordion__heading-6")
    ACCORDION_ITEM_EIGHT = (By.ID, "accordion__heading-7")

    #Ответы в аккордионе
    ANSWER_FAQ_ONE = (By.ID, "accordion__panel-0")
    ANSWER_FAQ_TWO = (By.ID, "accordion__panel-1")
    ANSWER_FAQ_THREE = (By.ID, "accordion__panel-2")
    ANSWER_FAQ_FOUR = (By.ID, "accordion__panel-3")
    ANSWER_FAQ_FIVE = (By.ID, "accordion__panel-4")
    ANSWER_FAQ_SIX = (By.ID, "accordion__panel-5")
    ANSWER_FAQ_SEVEN = (By.ID, "accordion__panel-6")
    ANSWER_FAQ_EIGHT = (By.ID, "accordion__panel-7")
    
    #Логотипы в шапке
    LOGO_YANDEX = (By.XPATH, "//a[contains(@class,'Header_LogoYandex')]")
    LOGO_YA_SAMOKAT = (By.XPATH, "//a[contains(@class,'Header_LogoScooter')]")
    
    #кнопка принятия условий использования кук 
    COCKIE = (By.ID, "rcc-confirm-button")

    #методы
    @allure.step('Открыть главную страницу')
    def open_main_page(self):
        self.open_url(self.URL)

    @allure.step('Загрузка главной страницы')
    def load_main_page(self):
        self.wait_for_visible(self.ACCORDION_FAQ)
    
    @allure.step('переход в новую вкладку')
    def open_link_new_tab(self):
        self.switch_to_new_tab()
    
    @allure.step('Принять условия использования кук')
    def cockie_check(self):
        self.click_element(self.COCKIE)

    #Логотипы
    @allure.step('Клик на логотип Яндекс')
    def click_logo_yandex(self):
        self.click_element(self.LOGO_YANDEX)
    
    @allure.step('Клик на лготип Яндекс Самокат')
    def click_logo_ya_samokat(self):
        self.click_element(self.LOGO_YA_SAMOKAT)

    #Оформление заказа
    @allure.step('Клик на кнопку Заказать')
    def click_order_button(self, button_type):
        if button_type == "header":
            self.click_element(self.ORDER_BUTTON_HEADER)
        elif button_type == "main":
            self.scroll_to_element(self.CONTAINER_FOR_ORDER_BUTTON)
            self.click_element(self.ORDER_BUTTON)

    @allure.step('Скролл до кнопки Заказать на главной странице')
    def scroll_in_order_button(self):
        self.scroll_to_element(self.CONTAINER_FOR_ORDER_BUTTON)   
    
    # #FAQ
    @allure.step('Скролл главной страницы к аккордиону FAQ')
    def scroll_in_accordion(self):
        self.wait_for_visible(self.ACCORDION_FAQ)
        self.scroll_to_element(self.ACCORDION_FAQ)
