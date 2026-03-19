# Currency Service — Домашнее задание №2

Сервис на FastAPI, который предоставляет актуальные курсы валют с помощью API Центрального Банка РФ.

`GET /info`

Возвращает информацию о версии, названии сервиса и авторе.
*Данные берутся из переменных окружения (.env).*

`GET /info/currency`

**Параметры:**
* `date` (optional): Дата в формате `YYYY-MM-DD`.
* `currency` (optional): Код валюты (например, `eur`).

**Логика обработки:**
* Если `date` не указан — выдаются данные на текущий день.
* Если `currency` не указан — выдается полный список всех валют в ключе `currencies`.

### Технологи
* **Python 3.12+**
* **FastAPI**
* **Requests**
* **ElementTree**
* **Pyproject.toml**

### Старт

1. Установка зависимостей:
   Все необходимые библиотеки подтянутся из файла конфигурации:
   ```
   pip install .
   ```

2. Настройка переменных окружения:
    Создайте файл .env в корне проекта:
    ```
    PORT=8000
    VERSION=1.0.0
    AUTHOR=v.laptev
    ```

# Hello!
### My name is Vadimir, nice to meet you. I am:
- HSE.Student 2 course
- Based in Moscow
- Python is a main language
- DevOps in the near future
- Music enjoyer (RnB, Trap)
- Reach me at: [Telegram](https://t.me/itwastoohard) | [GitHub](https://github.com/VolodyaGG)

## Literraly me ...
``` Python
if (coffee.empty()):
    code.stop()
```



