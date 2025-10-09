import builtins
from unittest.mock import MagicMock

import src.main as main_mod


def test_main_function_empty_keyword(monkeypatch, capsys):
    # Подменяем два ввода: первый — пустая строка
    inputs = iter(["   "])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    # Запускаем
    main_mod.main_function()

    # Проверяем вывод
    captured = capsys.readouterr().out
    assert "Пустой запрос." in captured


def test_main_function_invalid_n(monkeypatch, capsys):
    # Первый ввод — keyword, второй — нечисловой N
    inputs = iter(["Python", "abc"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    main_mod.main_function()

    captured = capsys.readouterr().out
    assert "Нужно ввести число." in captured


def test_main_function_no_results(monkeypatch, capsys):
    # Подменяем ввод корректными значениями
    inputs = iter(["Python", "3"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    # Мокаем get_top_n_for_keyword -> пусто
    monkeypatch.setattr(main_mod, "get_top_n_for_keyword", lambda kw, n: [])

    main_mod.main_function()

    captured = capsys.readouterr().out
    assert "Ничего не найдено." in captured


def test_main_function_happy_path(monkeypatch, capsys, sample_vacancies):
    """
    Полный сценарий:
    - вводим kw="Python", n=2
    - get_top_n_for_keyword возвращает 2 вакансии (ссылки совпадают с alternate_url в sample_vacancies)
    - HH.load_vacancies возвращает sample_vacancies
    - Save_to_json_file.save_vacancies_in_file вызывается с ожидаемым путем
    - В выводе корректный список и сообщение о сохранении
    """
    # 1) Подменяем ввод
    inputs = iter(["Python", "2"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    # 2) Готовим данные для top-N (совпадение по ссылкам с sample_vacancies)
    top_vacancies = [
        {
            "name": "Python Developer",
            "salary": 150000,
            "link": "https://hh.ru/vacancy/123",
        },
        {"name": "Data Analyst", "salary": 120000, "link": "https://hh.ru/vacancy/456"},
    ]
    monkeypatch.setattr(main_mod, "get_top_n_for_keyword", lambda kw, n: top_vacancies)

    # 3) Мокаем HH: экземпляр с load_vacancies -> sample_vacancies
    hh_instance = MagicMock()
    hh_instance.load_vacancies.return_value = sample_vacancies
    HH_mock_cls = MagicMock(return_value=hh_instance)
    monkeypatch.setattr(main_mod, "HH", HH_mock_cls)

    # 4) Мокаем Save_to_json_file: хотим отследить raw, путь и вызов save_vacancies_in_file
    saved_payload = {"path": None, "raw_selected": None}

    class SaveSpy:
        def __init__(self, raw):
            # сохраним "сырые" отобранные вакансии для проверки
            saved_payload["raw_selected"] = raw

        def save_vacancies_in_file(self, path):
            saved_payload["path"] = path

    monkeypatch.setattr(main_mod, "Save_to_json_file", SaveSpy)

    # 5) Запускаем функцию
    main_mod.main_function()

    # 6) Проверяем печать
    out = capsys.readouterr().out
    assert "— Топ-2 по зарплате для «Python» —" in out
    # строки списка
    assert "1. Python Developer — 150000 ₽ | https://hh.ru/vacancy/123" in out
    assert "2. Data Analyst — 120000 ₽ | https://hh.ru/vacancy/456" in out
    # сообщение о сохранении
    assert "✅ Топ-2 вакансий сохранён в файл: data/top_2_Python.json" in out

    # 7) Проверяем, что HH вызван ожидаемо
    HH_mock_cls.assert_called_once_with(file_worker=None)
    hh_instance.load_vacancies.assert_called_once_with("Python")

    # 8) Проверяем, что в Save_to_json_file попали только те «сырые» вакансии,
    # которые соответствуют top_links (по alternate_url)
    assert isinstance(saved_payload["raw_selected"], list)
    selected_links = {v.get("alternate_url") for v in saved_payload["raw_selected"]}
    assert selected_links == {"https://hh.ru/vacancy/123", "https://hh.ru/vacancy/456"}

    # 9) Проверяем путь сохранения
    assert saved_payload["path"] == "data/top_2_Python.json"
