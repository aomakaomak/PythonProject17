import pytest

from src.work_with_vacancies import Work_with_vacancies

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
def vacancy_dict1():
    return {
        "name": "Manager",
        "link": "some link1",
        "salary": 200000,
        "requirement": "some requirement 1",
    }


@pytest.fixture
def vacancy2_dict2():
    return {
        "name": "Manager",
        "link": "some link 2",
        "salary": 300000,
        "requirement": "some requirement 2",
    }