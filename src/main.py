from src.hh import HH
from src.work_with_vacancies import Work_with_vacancies
from src.save_to_json_file import Save_to_json_file

import heapq

def main_function():

    keyword = input("Введите ключевое слово: ")
    quantity = int(input("Введите количество вакансий с максимальной зп: "))

    file_worker = "any"
    hh = HH(file_worker)
    response = hh.load_vacancies(keyword)

    # vacancy_list = []
    # for vacancy in response:
    #     if vacancy > min(vacancy_list):
    #         vacancy_list.append(vacancy)

    response_for_compare = Work_with_vacancies(response)

    top5 = heapq.nlargest(quantity, response_for_compare)
    return top5





if __name__ == "__main__":
    print(main_function())


