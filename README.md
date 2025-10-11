# 🧠 Анализатор вакансий HH.ru

## 🚀 Что делает проект

Консольное приложение, которое:
- Ищет вакансии на [hh.ru](https://hh.ru) по ключевому слову;  
- Нормализует данные (зарплата, ссылка, требования);  
- Показывает **топ-N вакансий по зарплате**;  
- Сохраняет результаты в JSON-файл.

---

## ⚙️ Установка

```bash
git clone https://github.com/yourusername/hh-analyzer.git
cd hh-analyzer
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate на Windows
pip install -r requirements.txt
```

---

## ▶️ Запуск

```bash
python -m src.main
```

Пример работы:
```
Введите ключевое слово для поиска на hh.ru: Python
Введите количество вакансий для вывода (топ N по зарплате): 3

— Топ-3 по зарплате для «Python» —
1. Senior Python Developer — 300000 ₽ | https://hh.ru/vacancy/12345
2. Middle Python Engineer — 250000 ₽ | https://hh.ru/vacancy/67890
3. Junior Python Dev — 180000 ₽ | https://hh.ru/vacancy/11111

✅ Топ-3 вакансий сохранён в файл: data/top_3_Python.json
```

---

## 🧩 Архитектура

```
src/
├── hh.py                  # Работа с API hh.ru
├── parser.py              # Базовый парсер
├── work_with_vacancies.py # Модель вакансии
├── save_to_json_file.py   # Нормализация и сохранение JSON
├── utils.py               # get_top_n_for_keyword()
└── main.py                # main_function() — CLI-интерфейс
```

---

## 🧪 Тесты

Тесты написаны с использованием `pytest`.

Запуск:
```bash
pytest -v
```

---

## 📄 Пример JSON

```json
[
  {
    "name": "Senior Python Developer",
    "salary": 300000,
    "requirement": "Django, REST, Docker",
    "link": "https://hh.ru/vacancy/12345"
  }
]
```

---

## 🧠 Зависимости

- `requests` — работа с API  
- `pytest` — тестирование  
- `unittest.mock` — мокирование  
- `heapq` — выбор топ-N  
