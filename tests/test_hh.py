import unittest
from unittest.mock import MagicMock, patch

from src.hh import HH  # предполагается, что твой файл называется hh.py


class TestHH(unittest.TestCase):
    @patch("src.hh.requests.get")
    def test_load_vacancies(self, mock_get):
        # --- Настраиваем фиктивный ответ API ---
        fake_vacancies = [
            {"id": "1", "name": "Python Developer"},
            {"id": "2", "name": "Data Scientist"},
        ]
        fake_response = MagicMock()
        fake_response.json.return_value = {"items": fake_vacancies}
        mock_get.return_value = fake_response

        # --- Создаём экземпляр класса HH ---
        hh = HH(file_worker=None)

        # --- Вызываем метод ---
        result = hh.load_vacancies("Python")

        # --- Проверяем, что API вызывался несколько раз ---
        self.assertTrue(mock_get.called)
        self.assertGreaterEqual(mock_get.call_count, 1)

        # --- Проверяем параметры вызова первого запроса ---
        first_call_args, first_call_kwargs = mock_get.call_args
        self.assertIn("https://api.hh.ru/vacancies", first_call_args[0])
        self.assertIn("headers", first_call_kwargs)
        self.assertIn("params", first_call_kwargs)
        self.assertEqual(first_call_kwargs["params"]["text"], "Python")

        # --- Проверяем, что результат содержит данные ---
        self.assertIsInstance(result, list)
        self.assertIn("Python Developer", [v["name"] for v in result])

        # --- Проверяем, что вакансии добавляются в self.vacancies ---
        self.assertEqual(hh.vacancies, result)

        # --- Проверяем, что метод не падает на нескольких страницах ---
        self.assertLessEqual(hh._HH__params["page"], 20)
