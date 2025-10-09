from heapq import nlargest

from src.hh import HH
from src.save_to_json_file import Save_to_json_file
from src.work_with_vacancies import Work_with_vacancies


def get_top_n_for_keyword(keyword: str, n: int):
    """Функция для отбора топ-вакансий по з/п"""
    hh = HH(file_worker=None)
    raw = hh.load_vacancies(keyword)  # вакансии уже отфильтрованы HH по keyword
    normalized = Save_to_json_file(raw).vacancies_with_our_attributes()
    # по желанию можно отбросить вакансии без з/п:
    normalized = [v for v in normalized if (v.get("salary") or 0) > 0]
    return nlargest(n, normalized, key=lambda v: v.get("salary", 0))
