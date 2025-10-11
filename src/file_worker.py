from abc import ABC, abstractmethod


class FileWorker(ABC):
    """Абстрактный класс для сохранения списка вакансий"""

    @abstractmethod
    def save_vacancies_in_file(self, *args, **kwargs):
        """Сохранение вакансий в файл"""
        pass

    @abstractmethod
    def filter_from_file(self, *args, **kwargs):
        """Фильтрация вакансий"""
        pass

    @abstractmethod
    def del_vacancy(self, *args, **kwargs):
        """Удаление вакансий"""
        pass
