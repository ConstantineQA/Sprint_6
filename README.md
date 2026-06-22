# Sprint_6
## UI тесты для sprint_6

### Основная информация о проекте
1. Автотесты написаны для учебного сервиса Яндекс Самокат (https://qa-scooter.education-services.ru/).
2. Основа для написания автотестов: pytest, selenium.
3. Команда для запуска: pytest -v

### Перечень файлов

1. conftest.py - фикстуры
2. pages/base_page - общие базовые методы
3. pages/main_page.py - локаторы и методы страницы https://qa-scooter.education-services.ru/. Здесь же элементы из шапки
4. pages/order_page.py - локаторы и методы https://qa-scooter.education-services.ru/order для флоу оформления заказа
5. tests/test_logo.py - тесты на переходы по клику на логотипы в шапке 
6. tests/test_questions.py - тесты для проверки соответствия текстов ответов вопросам из блока FAQ
7. tests/test_order.py - тесты позитивного сценария оформления заказа
8. tests/data.py - переменные с текстами ответов на вопросы FAQ
9. allure-report/- отчет о тестировании
11. requirmements.txt - зависимости

### Перечень тестов
**test_logo.py**
1. test_click_logo_ya - Проверка перехода на ya.ru в новой вкладке после клика на логотип Яндекс.
2. test_click_logo_ya_samokat - Проверка перехода в текущей вкладке на главную Яндекс Самокат по клику на логотип Самокат

**test_questions.py**
1. test_question Проверка соответствия текстов ответов вопросам из блока FAQ.

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