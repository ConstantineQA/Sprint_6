from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    #найти элемент
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    #клик на элемент
    def click_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator)).click()

    #ввод данных в поле
    def send_keys_to_element(self, locator, text):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator)).send_keys(text)

    #получить текст
    def get_text(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator)).text

    #ожидание
    def wait_for_visible(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))
    
    #скролл к элементу
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    #открыть ссылку
    def open_url(self, url):
        self.driver.get(url)

    #получить текущий URL 
    def get_current_url(self):
        return self.driver.current_url
    
    #открыть ссылку в новой вкладке
    def switch_to_new_tab(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(expected_conditions.url_changes('about:blank'))