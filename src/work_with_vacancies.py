from src.hh import HH


class WorkWithVacancies:
    """Класс для валидации и сравнения вакансий по з/п"""

    __slots__ = ("name", "link", "salary", "requirement")

    def __init__(self, name, link, salary, requirement):

        self.name = name
        self.link = link
        self.salary = self.validate(salary)
        self.requirement = requirement

    @staticmethod
    def validate(salary: int):
        """Проверяем, что указана зп"""
        if not salary:
            return 0
        else:
            return salary

    def __eq__(self, other):
        """Реализуем методы сравнения"""
        return self.salary == other.salary

    def __lt__(self, other):
        """Реализуем методы сравнения"""
        return self.salary < other.salary

    def __gt__(self, other):
        """Реализуем методы сравнения"""
        return self.salary > other.salary

    def __repr__(self):
        """Формируем представление"""
        return f"{self.name} ({self.salary} руб.)"


# if __name__ == "__main__":
#
#     hh2 = HH("ewjfi")
#     response = hh2.load_vacancies("менеджер")
#     vacancy2 = response[0]
#     print(vacancy2)
#     print(type(vacancy2))
#
#     name = vacancy2.get("name")
#     link = vacancy2.get("alternate_url")
#     salary = vacancy2["salary"]["from"]
#     requirement = vacancy2["snippet"]["requirement"]
#
#     print(name)
#     print(link)
#     print(salary)
#     print(requirement)
#
#     vacancy3 = response[1]
#     print(vacancy3["salary"]["from"])
#
#
#
#     name5 = vacancy3.get("name")
#     link5 = vacancy3.get("alternate_url")
#     salary5 = vacancy3["salary"]["from"]
#     requirement5 = vacancy3["snippet"]["requirement"]
#
#     vacancy4 = Work_with_vacancies(name, link, salary, requirement)
#     vacancy5 = Work_with_vacancies(name5, link5, salary5, requirement5)
#
#     print(vacancy4.salary)
#     print(vacancy5.salary)
#
#     if vacancy4 < vacancy5:
#         print("vacancy4 < vacancy5")
#     else:
#         print("vacancy4 > vacancy5")
#
#
# #
#
#
