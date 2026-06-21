import allure
from pages.main_page import MainPage

class TestQuestions:

    @allure.title('Соответствие текста ответа первому вопросу FAQ')
    @allure.description('Проверка, что текст раскрывшегося элемента аккордеона соответствует своему вопросу')
    def test_question_one(self, driver):
        page = MainPage(driver) 
        page.open_main_page()
        page.load_main_page()
        page.scroll_in_accordion()
        page.click_faq_question_one()
        text = page.get_text_answer_one()
        assert text == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.title('Соответствие текста ответа второму вопросу FAQ')
    @allure.description('Проверка, что текст раскрывшегося элемента аккордеона соответствует своему вопросу')
    def test_question_two(self, driver):
        page = MainPage(driver) 
        page.open_main_page()
        page.load_main_page()
        page.scroll_in_accordion()
        page.click_faq_question_two()
        text = page.get_text_answer_two()
        assert text == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    @allure.title('Соответствие текста ответа третьему вопросу FAQ')
    @allure.description('Проверка, что текст раскрывшегося элемента аккордеона соответствует своему вопросу')
    def test_question_three(self, driver):
        page = MainPage(driver) 
        page.open_main_page()
        page.load_main_page()
        page.scroll_in_accordion()
        page.click_faq_question_three()
        text = page.get_text_answer_three()
        assert text == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'    

    @allure.title('Соответствие текста ответа четвертому вопросу FAQ')
    @allure.description('Проверка, что текст раскрывшегося элемента аккордеона соответствует своему вопросу')
    def test_question_four(self, driver):
        page = MainPage(driver) 
        page.open_main_page()
        page.load_main_page()
        page.scroll_in_accordion()
        page.click_faq_question_four()
        text = page.get_text_answer_four()
        assert text == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @allure.title('Соответствие текста ответа пятому вопросу FAQ')
    @allure.description('Проверка, что текст раскрывшегося элемента аккордеона соответствует своему вопросу')
    def test_question_five(self, driver):
        page = MainPage(driver) 
        page.open_main_page()
        page.load_main_page()
        page.scroll_in_accordion()
        page.click_faq_question_five()
        text = page.get_text_answer_five()
        assert text == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    @allure.title('Соответствие текста ответа шестому вопросу FAQ')
    @allure.description('Проверка, что текст раскрывшегося элемента аккордеона соответствует своему вопросу')
    def test_question_six(self, driver):
        page = MainPage(driver) 
        page.open_main_page()
        page.load_main_page()
        page.scroll_in_accordion()
        page.click_faq_question_six()
        text = page.get_text_answer_six()
        assert text == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'    

    @allure.title('Соответствие текста ответа седьмому вопросу FAQ')
    @allure.description('Проверка, что текст раскрывшегося элемента аккордеона соответствует своему вопросу')
    def test_question_seven(self, driver):
        page = MainPage(driver) 
        page.open_main_page()
        page.load_main_page()
        page.scroll_in_accordion()
        page.click_faq_question_seven()
        text = page.get_text_answer_seven()
        assert text == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    @allure.title('Соответствие текста ответа восьмому вопросу FAQ')
    @allure.description('Проверка, что текст раскрывшегося элемента аккордеона соответствует своему вопросу')
    def test_question_eight(self, driver):
        page = MainPage(driver) 
        page.open_main_page()
        page.load_main_page()
        page.scroll_in_accordion()
        page.click_faq_question_eight()
        text = page.get_text_answer_eight()
        assert text == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
        