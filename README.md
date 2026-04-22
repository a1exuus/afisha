# Пародия на Яндекс.Афишу

Простое Django-приложение для управления мероприятиями и местами. Разработано для локального запуска и обучения.

## Требования

*   **Python**: 3.10 – 3.13
*   **OS**: Windows / Linux / macOS
*   **База данных**: SQLite (встроена, настройка не требуется)

## Быстрый старт

### 1. Клонирование и подготовка
```bash
# Клонируй репозиторий (если есть)
git clone <repository_url>
cd <project_folder>

# Создай виртуальное окружение
python -m venv venv

# Активируй окружение
# Для Windows (CMD):
venv\Scripts\activate
# Для Windows (PowerShell):
venv\Scripts\Activate.ps1
# Для Linux/macOS:
source venv/bin/activate
```

### 2. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 3. Настройка окружения (.env)
В корне проекта создай файл `.env` (или скопируй `.env.example`, если есть).
Проект использует библиотеку `environs`, поэтому настройки читаются автоматически.

**Пример минимального `.env`:**
```bash
# Секретный ключ (сгенерируй свой: https://djecrety.ir/)
SECRET_KEY=django-insecure-change-me-please

# Режим отладки (True для разработки)
DEBUG=True

# Разрешённые хосты
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 4. Применение миграций и сборка статики
```bash
# Применяем миграции БД
python manage.py migrate

# Собираем статические файлы (CSS, JS, Admin)
python manage.py collectstatic --noinput
```

### 5. Создание суперпользователя (Администратора)
```bash
python manage.py createsuperuser
# Следуй инструкциям в терминале (логин, email, пароль)
```

### 6. Запуск сервера разработки
```bash
python manage.py runserver
```
Открой в браузере:
*   Сайт: [http://127.0.0.1:8000](http://127.0.0.1:8000)
*   Админ-панель: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## Наполнение данными

### Способ 1: Через админ-панель
1.  Зайди в `/admin`.
2.  Авторизуйся под суперпользователем.
3.  Используй разделы **Places** и **PlaceImage** для ручного добавления контента.

### Способ 2: Загрузка из JSON (Команда управления)
Для массового импорта данных предусмотрена кастомная команда `load_place`.

**Синтаксис:**
```bash
python manage.py load_place <URL_к_JSON_файлу> (ОБЯЗАТЕЛЬНО RAW!)
```

**Пример:**
```bash
python manage.py load_place http://mysite.com/data/places.json
```

**Требования к формату JSON:**
```json
[
  {
    "title": "Название мероприятия или места",
    "imgs": [
      'картинка1.url',
      'картинка2.url',
      ...
    ],
    "description_short": "Краткое описание",
    "description_long": "Полное описание",
    "coordinates": {
        "lng": 55.75,
        "lat": 37.61
    }
  }
]
```

---

## Полезные команды

| Команда | Описание |
|---------|----------|
| `python manage.py runserver` | Запустить локальный сервер |
| `python manage.py migrate` | Применить миграции БД |
| `python manage.py makemigrations` | Создать новые миграции при изменении моделей |
| `python manage.py collectstatic --noinput` | Собрать статику в `STATIC_ROOT` |
| `python manage.py createsuperuser` | Создать аккаунт администратора |
| `python manage.py shell` | Открыть интерактивную консоль Django |
| `python manage.py load_place <url>` | Загрузить места из JSON |

---

## Важно для разработки

1.  **Безопасность**: Никогда не коммить файл `.env` в Git. В репозитории должен лежать только шаблон `.env.example`.
2.  **SQLite**: Эта БД подходит только для разработки. При высоких нагрузках или множественных записях возможны блокировки файла.
3.  **Статика**: На `DEBUG=True` Django сам раздает статику. При переключении в `DEBUG=False` потребуется настройка Nginx или WhiteNoise.
4.  **SECRET_KEY**: Убедись, что в `.env` указан уникальный сложный ключ. Не используй дефолтные значения из примеров.

---

## Структура проекта (кратко)

```
├── manage.py
├── requirements.txt      # Зависимости
├── .env                  # Локальные настройки (не в git!)
├── db.sqlite3            # Файл базы данных
├── places/               # Основное приложение
│   ├── models.py         # Модели (Place, PlaceImage)
│   ├── admin.py          # Настройки админки
│   └── management/
│       └── commands/
│           └── load_place.py  # Команда импорта
└── config/               # Настройки проекта
    ├── settings.py       # Общие настройки + environs
    └── urls.py
```