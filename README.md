# Webproject: Contacts on Any GET

Простое веб-приложение на стандартной библиотеке Python (`http.server`):
любой `GET`-запрос возвращает страницу `contacts.html`.

## Что реализовано

- Обработчик `do_GET` всегда отдает `contacts.html`.
- Маршрут не ограничен: `/`, `/abc`, `/orders/1` и любой другой `GET` возвращают ту же страницу.
- Верстка использует удаленные ресурсы Bootstrap CDN.
- Проект запускается через Poetry.

## Требования

- Python 3.10+
- Poetry

## Установка

```powershell
poetry install
```

## Запуск

```powershell
poetry run python app.py
```

После запуска сервер доступен по адресу `http://localhost:8080`.

## Проверка

Откройте в браузере:

- `http://localhost:8080/`
- `http://localhost:8080/anything`
- `http://localhost:8080/test/path`

Или проверьте через PowerShell:

```powershell
curl http://localhost:8080/
curl http://localhost:8080/anything
curl http://localhost:8080/test/path
```

Во всех случаях должна вернуться страница контактов.

## Структура проекта

- `app.py` - HTTP-сервер и обработка `GET`
- `contacts.html` - страница контактов
- `pyproject.toml` - конфигурация Poetry
