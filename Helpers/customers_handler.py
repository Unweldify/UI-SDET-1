"""Этот файл отвечает за логику выбора клиента для удаления."""
from typing import List


class CustomerHandler:
    """Класс для методов логики выбора."""

    @staticmethod
    def get_avg_len(names: List[str]) -> float:
        """
        Метод находит среднее арифметическое длины имён.

        :param names: Список имён.
        :return: Среднее арифметическое, число с плавающей точкой.
        """
        name_lengths = [len(name) for name in names]
        avg = sum(name_lengths) / len(name_lengths)
        return avg

    @staticmethod
    def get_closest_avg(names: List[str], avg: float) -> str:
        """
        Метод находит имя, длина которого близка к параметру avg (сред. арифметическое).

        :param names: Список имён.
        :param avg: Среднее арифметическое, число с плавающей точкой.
        :return: Найденное имя, строка.
        """
        closest_avg = min(names, key=lambda name: abs(len(name) - avg))
        return closest_avg
