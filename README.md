# CI/CD Pipeline

Настроен полный CI/CD пайплайн в `.gitlab-ci.yml`:

### Линтеры
- ruff — проверка Python-кода
- hadolint — проверка Dockerfile

### Сборка образов
- build_dev — сборка development-образа через Kaniko с зависимостями для тестирования
- build_prod — сборка production-образа через Kaniko

### Тестирование
- unit_tests — запуск unit-тестов в development-контейнере
- integration_tests — запуск интеграционных тестов (проверка работы с реальным API ЦБ РФ, сервисного слоя и фильтрации валют)

### Деплой
- deploy — ручной деплой на сервер через SSH (только ветка master)
  - Pull нового образа
  - Запуск через `docker-compose.hardened.yml`

# Упаковка приложения в Докер

## 1. Dockerfile
Разработан `Dockerfile` на базе `python:3.12-slim` с многоэтапной сборкой (multi-stage).
- **base** — установка Poetry и зависимостей
- **development** — установка всех зависимостей (включая dev), копирование тестов
- **production** — только основные зависимости, без dev-пакетов

## 2. Docker compose
Разработан `docker-compose.yml`. Он задает сервис "app", который запускает команду "python main.py". Сервис работает в режиме только для чтения и использует tmpfs для временных файлов. Также задаются переменные окружения и проброс портов.
Затем создан новый файл `docker-compose.hardened.yml` с новыми настройками безопасности: ограничение прав доступа, отключение привилегий, ограничение ресурсов, отключение коммуникации между контейнерами.

Также приложение загружено на docker hub: https://hub.docker.com/repository/docker/volodyagg/client_server_app

## 3. sbom.json и trivy-report.json
Файл `trivy-report.json` содержит результаты сканирования, в ходе которого была выявлена критическая проблема:
`CVE-2024-47874` в пакете `starlette` версии `0.27.0` - уязвимость парсера `multipart/form-data`. Хакер мог отправить специально сформированный запрос, который заставлял сервер бесконечно обрабатывать данные, полностью съедая ресурсы CPU. Благодаря обновлению `fastapi` до версии `0.135.1` версия `starlette` была поднята до безопасной. Повторный анализ подтвердил отсутствие критических уязвимостей. Уязвимость описана в FINDINGS.md

Файл `sbom.json` содержит полный перечень всех установленных библиотек в формате CycloneDX, их точных версий и хеш-сумм.

## 4. Создан .dockerignore файл

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



