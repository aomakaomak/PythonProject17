def test_work_with_vacancies_init(first_vacancy):
    assert first_vacancy.name == "Manager"
    assert first_vacancy.link == "some link 1"
    assert first_vacancy.salary == 200000
    assert first_vacancy.requirement == "some requirement 1"


def test_work_with_vacancies_init_without_salary(vacancy_without_salary):
    assert vacancy_without_salary.name == "Without salary"
    assert vacancy_without_salary.link == "some link 3"
    assert vacancy_without_salary.salary == 0
    assert vacancy_without_salary.requirement == "some requirement 3"


def test_work_with_vacancies_equal(first_vacancy, second_vacancy):
    assert first_vacancy.__lt__(second_vacancy) == True
    assert first_vacancy.__gt__(second_vacancy) == False
    assert first_vacancy.__eq__(second_vacancy) == False
