import requests

from src.file_worker import FileWorker
from src.parser import Parser


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self, file_worker: FileWorker):
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies = []
        super().__init__(file_worker)

    @property
    def vacancies(self):
        """Геттер отдает нам вакансии"""
        return self.__vacancies

    def load_vacancies(self, keyword: str):
        """Получаем список вакансий по ключевому слову"""
        self.__params["text"] = keyword
        while self.__params.get("page") != 20:
            response = requests.get(
                self.__url, headers=self.__headers, params=self.__params
            )
            try:
                response.raise_for_status()
            except requests.HTTPError:
                print(f"Ошибка при запросе: {getattr(response, 'status_code', 'unknown')}")
                break

            vacancies = response.json()["items"]
            self.vacancies.extend(vacancies)
            self.__params["page"] += 1
        return self.vacancies






# if __name__ == "__main__":
#     file_worker = "dsf"
#     hh1 = HH(file_worker)
#     print(hh1)
#     print(type(hh1))
#
#     print(hh1.file_worker)
#     print(hh1.vacancies)
#
#     response = hh1.load_vacancies("менеджер")
#
#     print(type(response))
#     print(response[0])
