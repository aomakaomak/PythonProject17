import unittest
from unittest.mock import MagicMock, patch

from src.utils import get_top_n_for_keyword  # допустим, функция в файле top_n.py


class TestGetTopNForKeyword(unittest.TestCase):
    @patch("src.utils.SaveToJsonFile")
    @patch("src.utils.HH")
    def test_get_top_n_for_keyword(self, mock_hh_class, mock_save_class):
        # --- 1. Настраиваем мок HH ---
        mock_hh = MagicMock()
        mock_hh.load_vacancies.return_value = [{"id": 1}, {"id": 2}, {"id": 3}]
        mock_hh_class.return_value = mock_hh

        # --- 2. Настраиваем мок Save_to_json_file ---
        mock_save = MagicMock()
        mock_save.vacancies_with_our_attributes.return_value = [
            {"id": 1, "salary": 100000},
            {"id": 2, "salary": 200000},
            {"id": 3, "salary": 150000},
        ]
        mock_save_class.return_value = mock_save

        # --- 3. Вызываем тестируемую функцию ---
        result = get_top_n_for_keyword("Python", 2)

        # --- 4. Проверяем, что вернулись 2 вакансии ---
        self.assertEqual(len(result), 2)

        # --- 5. Проверяем, что отсортированы по зарплате убыванию ---
        self.assertGreaterEqual(result[0]["salary"], result[1]["salary"])

        # --- 6. Проверяем, что функция использует правильные классы ---
        mock_hh.load_vacancies.assert_called_once_with("Python")
        mock_save.vacancies_with_our_attributes.assert_called_once()
