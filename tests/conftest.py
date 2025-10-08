import pytest

from src.work_with_vacancies import Work_with_vacancies

from src.save_to_json_file import Save_to_json_file

@pytest.fixture
def first_vacancy():
    return Work_with_vacancies(name="Manager", link="some link 1", salary=200000, requirement="some requirement 1")

@pytest.fixture
def second_vacancy():
    return Work_with_vacancies(name="Supervisor", link="some link 2", salary=300000, requirement="some requirement 2")

@pytest.fixture
def vacancy_without_salary():
    return Work_with_vacancies(name="Without salary", link="some link 3", salary="", requirement="some requirement 3")

@pytest.fixture
def data_list():
    return Save_to_json_file([1, 2, 3])

@pytest.fixture
def sample_vacancies():
    return [
        {
            "name": "Python Developer",
            "experience": 3,
            "alternate_url": "https://hh.ru/vacancy/123",
            "salary": {"from": 150000},
            "snippet": {"requirement": "Опыт с Django и REST API"},
        },
        {
            "name": "Data Analyst",
            "experience": 5,
            "alternate_url": "https://hh.ru/vacancy/456",
            "salary": None,
            "snippet": {"requirement": "SQL, Power BI"},
        },
    ]

# @pytest.fixture
# def vacancy_dict1():
#     return {
#         "name": "Manager",
#         "link": "some link1",
#         "salary": 200000,
#         "requirement": "some requirement 1",
#     }
#
#
# @pytest.fixture
# def vacancy2_dict2():
#     return {
#         "name": "Manager",
#         "link": "some link 2",
#         "salary": 300000,
#         "requirement": "some requirement 2",
#     }