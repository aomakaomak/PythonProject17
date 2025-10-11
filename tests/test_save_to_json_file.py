from src.save_to_json_file import SaveToJsonFile


def test_save_to_json_file_init(data_list):
    assert data_list.data == [1, 2, 3]


def test_vacancies_with_our_attributes(sample_vacancies):

    saver = SaveToJsonFile(sample_vacancies)
    result = saver.vacancies_with_our_attributes()

    assert isinstance(result, list)
    assert result[0]["salary"] == 150000
    assert result[1]["salary"] == 0
    assert result[0]["name"] == "Python Developer"
    assert result[1]["requirement"] == "SQL, Power BI"
