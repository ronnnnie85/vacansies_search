# 💼 Вакансии HH.ru – Поиск и Работа с API

## 📌 Описание проекта

Проект представляет собой консольное приложение на Python для поиска и фильтрации вакансий с платформы [hh.ru](https://hh.ru), используя публичное API. Программа позволяет:

- 🔍 Выполнять поиск вакансий по ключевому слову
- 📊 Сохранять и фильтровать вакансии по зарплате, описанию и другим критериям
- 🧹 Удалять, сортировать и просматривать вакансии
- 💾 Хранить вакансии в JSON-файле
- ✅ Покрытие тестами 76%

Проект построен с соблюдением **ООП**, принципов **SOLID**, с покрытием **модульными тестами**.

---

## 🛠️ Используемый стек

- Python 3.10+
- [HH API](https://github.com/hhru/api/)
- `requests`, `json`
- `pytest`, `coverage`
- Poetry (управление зависимостями)

---

## 📂 Структура проекта

```
Vacansies_search_hh/
│
├── data/                      # Хранение вакансий
├── htmlcov/                   # HTML-отчет по тестированию
│
├── src/
│   ├── config.py              # Параметры запроса
│   ├── head_hunter_api.py     # HeadHunterAPI - загрузка данных с hh.ru
│   ├── json_saver.py          # JsonSaver - работа с JSON-файлом
│   ├── parser.py              # Parser (ABC) - абстрактный класс API
│   ├── saver.py               # Saver (ABC) - абстрактный класс файлового хранилища
│   ├── user_interaction.py    # UserInteraction - консольный интерфейс
│   ├── vacancies_processing.py# VacProcessing - фильтрация/сортировка
│   └── vacancy.py             # Vacancy - модель вакансии
│
├── tests/
│   └── test_*.py              # Покрытие основных классов
│
├── .coverage
├── .flake8
├── .gitignore
├── main.py                    # Точка входа
├── poetry.lock
├── pyproject.toml
└── README.md
```

---

## 🧩 Классы и их функциональность

### `Parser (ABC)`
- `load_data` – загрузка вакансий.
- `__get_request` – отправка запроса к API.

### `HeadHunterAPI(Parser)`
- Получение данных с платформы hh.ru.
- Обрабатывает пагинацию, возвращает список словарей вакансий.

### `Saver (ABC)`
- `add_vacancy` – добавление вакансии в хранилище.
- `get_vacancy` – получение по ID.
- `delete_vacancy` – удаление по ID.

### `JsonSaver(Saver)`
- Работа с JSON-файлом вакансий (`data/vacancies.json`).
- Проверка на дубли, сериализация/десериализация объектов.

### `Vacancy`
- Атрибуты: `job_title`, `link`, `salary`, `description`, `id`.
- Магические методы сравнения вакансий по зарплате: `__lt__`, `__eq__`, `__ge__` и т.д.
- Метод `cast_to_object_list` – преобразование API-данных в объекты.
- Метод `cast_to_dict` – для сериализации.

### `VacProcessing`
- `get_top_vacancies` – топ N по зарплате.
- `filter_vacancies` – по ключевому слову.
- `get_vacancies_by_salary` – по диапазону.
- `sort_vacancies`, `print_vacancies` – сортировка и вывод.

### `UserInteraction`
- CLI-интерфейс пользователя.
- Поддерживает пошаговый сценарий: поиск, фильтрация, сортировка, повтор запроса.

---

## ⚙️ Установка и запуск

```bash
git clone https://github.com/your-username/Vacansies_search_hh.git
cd Vacansies_search_hh

poetry install
poetry run python main.py
```

---

## 🧪 Тестирование

```bash
poetry run pytest --cov=src tests/
poetry run coverage html
```

---

## 📌 Пример использования

```text
Введите ключевое слово для поиска вакансий: Python

Выберите метод поиска:
1) Найти топ вакансий
2) Найти вакансии по слову из описания
3) Найти вакансии по диапазону зарплат
4) Отсортировать вакансии по зарплате
5) Выход
```

---

## 📜 Лицензия

MIT License. Проект доступен для свободного использования.

