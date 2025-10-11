from abc import ABC, abstractmethod


class Parser(ABC):
    """Абстрактный класс для получения вакансий"""

    def __init__(self, file_worker):
        self.file_worker = file_worker

    @abstractmethod
    def load_vacancies(self, keyword):
        """Метод для получения вакансий"""
        pass
