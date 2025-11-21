Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers
Реализованные сценарии
Созданы юнит-тесты, покрывающие классы Burger, Bun и Ingredient

Процент покрытия: 89% (отчет: htmlcov/index.html)

Структура проекта
text
qa-python-Diplom1/
├── praktikum/          # пакет, содержащий код программы
│   ├── __init__.py
│   ├── bun.py
│   ├── burger.py
│   └── ingredient.py
├── tests/              # пакет, содержащий тесты
│   ├── __init__.py
│   ├── conftest.py
│   ├── data.py
│   └── test_Burger.py
└── requirements.txt
Запуск автотестов
Установка зависимостей

bash
pip install -r requirements.txt
Запуск автотестов и создание HTML-отчета о покрытии

bash
pytest --cov=praktikum --cov-report=html
Просмотр отчета о покрытии

bash
start htmlcov/index.html