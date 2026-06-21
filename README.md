# Sprint_6
## UI тесты для sprint_6

### Основная информация о проекте
1. Автотесты написаны для учебного сервиса Яндекс Самокат (https://qa-scooter.education-services.ru/).
2. Основа для написания автотестов: pytest, selenium.
3. Команда для запуска: pytest -v

### Перечень файлов

1. conftest.py - фикстуры
2. pages/main_page.py - локаторы и методы страницы https://qa-scooter.education-services.ru/. Здесь же элементы из шапки
3. pages/order_page.py - локаторы и методы https://qa-scooter.education-services.ru/order для флоу оформления заказа
4. tests/test_logo.py - тесты на переходы по клику на логотипы в шапке 
5. tests/test_questions.py - тесты для проверки соответствия текстов ответов вопросам из блока FAQ
6. tests/test_order.py - тесты позитивного сценария оформления заказа
7. allure-report/- отчет о тестировании
8. requirmements.txt - зависимости

### Перечень тестов
**test_logo.py**
1. test_click_logo_ya - Проверка перехода на ya.ru в новой вкладке после клика на логотип Яндекс.
2. test_click_logo_ya_samokat - Проверка перехода в текущей вкладке на главную Яндекс Самокат по клику на логотип Самокат

**test_questions.py**

Тесты для всех вопросов из перечня FAQ. проверяется соответствие текстов ответов вопросам из блока FAQ.
1. test_question_one
2. test_question_two
3. test_question_three
4. test_question_four
5. test_question_five
6. test_question_six
7. test_question_seven
8. test_question_eight

**test_order.py**
1. test_add_order - параметризированный тест с наборами тестовых пользовательских данных. Запускается через две точки входа - кнопка Заказать в шапке и на главной сервиса.

### Запуск тестов

```bash
1. Запуск тестов с сохранением результатов
pytest --alluredir=allure-results
```
```bash
2. Генерация html отчета
allure generate allure-results --clean -o allure-report 
```
```bash
3. Проверка отчета локально
allure open allure-report 
```