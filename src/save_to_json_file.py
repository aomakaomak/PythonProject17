import json
from typing import List

from src.file_worker import File_worker
from src.hh import HH


class Save_to_json_file(File_worker):
    """Класс для работы со спарсенными данными"""

    def __init__(self, data: List):
        self.data = data

    def vacancies_with_our_attributes(self):
        """Формируем список словарей на основе определенных нами атрибутов"""
        vacancy_list = []
        for vacancy in self.data:
            if vacancy.get("salary"):
                salary = vacancy.get("salary").get("from")
            else:
                salary = 0
            vacancy_dict = {
                "name": vacancy.get("name"),
                "link": vacancy.get("alternate_url"),
                "salary": salary,
                "requirement": vacancy.get("snippet").get("requirement"),
            }
            vacancy_list.append(vacancy_dict)

        return vacancy_list

    def save_vacancies_in_file(self, file_path):
        """Сохраняем в json файл"""
        data_with_attr = self.vacancies_with_our_attributes()
        with open(file_path, "a", encoding="UTF-8") as f:
            json.dump(data_with_attr, f, indent=4, ensure_ascii=False)

    def filter_from_file(self, *args, **kwargs):
        pass

    def del_vacancy(self, *args, **kwargs):
        pass


# if __name__ == "__main__":
#     hh = HH("dskfj")
#     response = hh.load_vacancies("менеджер")
#     # print(type(response))
#     # print(response[0])
#
#     # vacancy_list = Save_to_json_file(response)
#     # vacancy_list_with_attr = vacancy_list.vacancies_with_our_attributes()
#     # print(vacancy_list_with_attr)
#
#     response_json = Save_to_json_file(response)
#     response_json.save_vacancies_in_file("data/my_vacancies.json")
