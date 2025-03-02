# JWT Authentication Service

Этот проект представляет собой сервис для авторизации пользователей с использованием JWT (JSON Web Token). Сервис включает в себя регистрацию, вход в систему и обновление токенов.

## Требования

Перед тем, как запустить проект, убедись, что у тебя установлены следующие компоненты:
- Docker

## Шаги для запуска

1. **Создай файл `.env` в корне проекта:**

   В файле `.env` нужно указать параметры для подключения к базе данных и секретные ключи для генерации токенов. Пример содержимого файла:

   ```
   DB_HOST=db
   DB_PORT=5432
   DB_NAME=auth_db
   DB_USER=auth_user
   DB_PASS=auth_password
   ACCESS_SECRET_KEY=secret_access
   REFRESH_SECRET_KEY=secret_refresh
   ```

   - `DB_HOST`: Хост для подключения к базе данных (в Docker-сетке это будет `db`).
   - `DB_PORT`: Порт для подключения к PostgreSQL (по умолчанию `5432`).
   - `DB_NAME`: Имя базы данных.
   - `DB_USER`: Имя пользователя базы данных.
   - `DB_PASS`: Пароль пользователя базы данных.
   - `ACCESS_SECRET_KEY`: Секретный ключ для создания access токенов.
   - `REFRESH_SECRET_KEY`: Секретный ключ для создания refresh токенов.

2. **Запуск с использованием Docker Compose:**

   После того как `.env` файл создан, ты можешь запустить проект с помощью Docker Compose:

   ```bash
   docker compose up
   ```

   Эта команда:
   - Соберет все контейнеры (если это необходимо).
   - Запустит контейнер с PostgreSQL (база данных) и с FastAPI-приложением.

3. **Доступ к API:**

   После того как контейнеры запустятся, API будет доступно по адресу:

   ```
   http://localhost:8000
   ```

   Документация по API будет доступна по адресу:

   ```
   http://localhost:8000/docs
   ```

   Для использования сервисов авторизации и работы с JWT, см. документацию по эндпоинтам.

## Структура файлов

- `docker-compose.yml` — файл конфигурации для Docker Compose.
- `Dockerfile` — описание Docker-образа для приложения.
- `main.py` — главный файл для запуска FastAPI-приложения.
- `api/` — директория с файлами для роутеров и схем.
- `db/` — директория с файлами для работы с базой данных.
- `core/` — директория с основными утилитами, такими как генерация JWT-токенов.
- `.env` — файл для конфигурации окружения.
