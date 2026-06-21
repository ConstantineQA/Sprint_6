from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure

class MainPage:

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
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть главную страницу')
    def open_main_page(self):
        self.driver.get(self.URL)

    @allure.step('Загрузка главной страницы')
    def load_main_page(self):
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(self.ACCORDION_FAQ))
    
    @allure.step('переход в новую вкладку')
    def open_link_new_tab(self):
        WebDriverWait(self.driver,10).until(expected_conditions.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(expected_conditions.url_changes('about:blank'))
    
    @allure.step('Принять условия использования кук')
    def cockie_check(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.COCKIE))
        self.driver.find_element(*self.COCKIE).click()

    #Логотипы
    @allure.step('Клик на логотип Яндекс')
    def click_logo_yandex(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.LOGO_YANDEX))
        self.driver.find_element(*self.LOGO_YANDEX).click()
    
    @allure.step('Клик на лготип Яндекс Самокат')
    def click_logo_ya_samokat(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.LOGO_YA_SAMOKAT))
        self.driver.find_element(*self.LOGO_YA_SAMOKAT).click()

    #Оформление заказа
    @allure.step('Клик на кнопку Заказать в шапке')
    def click_order_button_header(self):
        self.driver.find_element(*self.ORDER_BUTTON_HEADER).click()

    @allure.step('Клик на кнопку Заказать на главной странице')
    def click_order_button_main_page(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.ORDER_BUTTON))
        self.driver.find_element(*self.ORDER_BUTTON).click()

    @allure.step('Скролл до кнопки Заказать на главной странице')
    def scroll_in_order_button(self):
        element = self.driver.find_element(*self.CONTAINER_FOR_ORDER_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)   
    
    #FAQ
    @allure.step('Скролл главной страницы к аккордиону FAQ')
    def scroll_in_accordion(self):
        element = WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(self.ACCORDION_FAQ))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step('Клик на первый вопрос в FAQ')
    def click_faq_question_one(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.ACCORDION_ITEM_ONE))
        self.driver.find_element(*self.ACCORDION_ITEM_ONE).click()
    
    @allure.step('Клик на второй вопрос в FAQ')
    def click_faq_question_two(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.ACCORDION_ITEM_TWO))
        self.driver.find_element(*self.ACCORDION_ITEM_TWO).click()

    @allure.step('Клик на третий вопрос в FAQ')
    def click_faq_question_three(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.ACCORDION_ITEM_THREE))
        self.driver.find_element(*self.ACCORDION_ITEM_THREE).click()

    @allure.step('Клик на четвертый вопрос в FAQ')
    def click_faq_question_four(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.ACCORDION_ITEM_FOUR))
        self.driver.find_element(*self.ACCORDION_ITEM_FOUR).click()

    @allure.step('Клик на пятый вопрос в FAQ')
    def click_faq_question_five(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.ACCORDION_ITEM_FIVE))
        self.driver.find_element(*self.ACCORDION_ITEM_FIVE).click()

    @allure.step('Клик на шестой вопрос в FAQ')
    def click_faq_question_six(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.ACCORDION_ITEM_SIX))
        self.driver.find_element(*self.ACCORDION_ITEM_SIX).click()

    @allure.step('Клик на седьмой вопрос в FAQ')
    def click_faq_question_seven(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.ACCORDION_ITEM_SEVEN))
        self.driver.find_element(*self.ACCORDION_ITEM_SEVEN).click()

    @allure.step('Клик на восьмой вопрос в FAQ')
    def click_faq_question_eight(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.ACCORDION_ITEM_EIGHT))
        self.driver.find_element(*self.ACCORDION_ITEM_EIGHT).click()
    
    @allure.step('Получить текст ответа первого вопроса')
    def get_text_answer_one(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.ANSWER_FAQ_ONE))
        return self.driver.find_element(*self.ANSWER_FAQ_ONE).text
    
    @allure.step('Получить текст ответа второго вопроса')
    def get_text_answer_two(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.ANSWER_FAQ_TWO))
        return self.driver.find_element(*self.ANSWER_FAQ_TWO).text
    
    @allure.step('Получить текст ответа третьего вопроса')
    def get_text_answer_three(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.ANSWER_FAQ_THREE))
        return self.driver.find_element(*self.ANSWER_FAQ_THREE).text
    
    @allure.step('Получить текст ответа четвертого вопроса')
    def get_text_answer_four(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.ANSWER_FAQ_FOUR))
        return self.driver.find_element(*self.ANSWER_FAQ_FOUR).text
    
    @allure.step('Получить текст ответа пятого вопроса')
    def get_text_answer_five(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.ANSWER_FAQ_FIVE))
        return self.driver.find_element(*self.ANSWER_FAQ_FIVE).text
    
    @allure.step('Получить текст ответа шестого вопроса')
    def get_text_answer_six(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.ANSWER_FAQ_SIX))
        return self.driver.find_element(*self.ANSWER_FAQ_SIX).text
    
    @allure.step('Получить текст ответа седьмого вопроса')
    def get_text_answer_seven(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.ANSWER_FAQ_SEVEN))
        return self.driver.find_element(*self.ANSWER_FAQ_SEVEN).text
    
    @allure.step('Получить текст ответа восьмого вопроса')
    def get_text_answer_eight(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.ANSWER_FAQ_EIGHT))
        return self.driver.find_element(*self.ANSWER_FAQ_EIGHT).text
