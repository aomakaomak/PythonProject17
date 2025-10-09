from abc import ABC, abstractmethod


class File_worker(ABC):

    @abstractmethod
    def save_vacancies_in_file(self, *args, **kwargs):
        pass

    @abstractmethod
    def filter_from_file(self, *args, **kwargs):
        pass

    @abstractmethod
    def del_vacancy(self, *args, **kwargs):
        pass
