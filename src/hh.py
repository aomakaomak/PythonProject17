import requests
from src.parser import Parser

class HH(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self, file_worker):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []
        super().__init__(file_worker)

    def load_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
        return self.vacancies

if __name__ == "__main__":
    file_worker = "dsf"
    hh1 = HH(file_worker)
    print(hh1)
    print(type(hh1))

    print(hh1.file_worker)
    print(hh1.vacancies)

    response = hh1.load_vacancies("менеджер")

    print(type(response))
    print(response[0])





