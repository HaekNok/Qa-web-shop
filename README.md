# QA Web Shop Test Automation Suite

Фреймворк автоматизации тестирования UI (Playwright) и REST API (Requests) на базе Pytest.

## Стек технологий
- Python 3.10+
- Pytest
- Playwright
- Requests

## Структура репозитория
```text
qa-web-shop/
├── tests/
│   ├── ui/          # UI сценарии (авторизация, каталог, корзина)
│   └── api/         # API проверки (GET/POST endpoints reqres.in)
├── pages/           # Page Object классы
├── utils/           # Конфигурация и тестовые данные
├── conftest.py      # Фикстуры браузера и API клиента
├── pytest.ini       # Маркеры и параметры запуска
└── requirements.txt # Список зависимостей
```

## Установка окружения
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

## Запуск тестов
```bash
# Все тесты
pytest

# Только UI тесты
pytest -m ui

# Только API тесты
pytest -m api

# Подробный вывод
pytest -v -s
```
