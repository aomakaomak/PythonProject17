from abc import ABC, abstractmethod

from src.file_worker import FileWorker


class Parser(ABC):
    """Абстрактный класс для получения вакансий"""

    def __init__(self, file_worker: FileWorker):
        self.file_worker = file_worker

    @abstractmethod
    def load_vacancies(self, keyword: str):
        """Метод для получения вакансий"""
        pass
