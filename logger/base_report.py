from abc import ABC, abstractmethod
from collections import defaultdict
from typing import List, Dict

class BaseReport(ABC):
    """
    Базовый класс для создания отчётов. Все отчёты должны наследовать этот класс.
    """
    
    def __init__(self, stats: List[Dict[str, int]]):
        """
        Инициализация с данными.
        :param stats: Статистика по логам (каждый элемент - это словарь с данными по handler)
        """
        self.stats = stats

    @abstractmethod
    def generate(self):
        """
        Метод для генерации отчёта. Должен быть реализован в каждом конкретном отчёте.
        """
        pass

    def sum_each_log_level(self) -> tuple:
        """
        Суммирует значения каждого уровня логирования по всем handler.
        """
        levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
        return tuple(sum(handler[level] for handler in self.stats) for level in levels)

    def sum_total_requests(self) -> int:
        """
        Суммирует общее количество запросов.
        """
        total_requests = sum(
            sum(value for value in handler_stats.values() if not isinstance(value, str))
            for handler_stats in self.stats
        )
        return total_requests

    def format_handler_data(self):
        """
        Форматирует данные для вывода в отчёт.
        Возвращает строку для каждого handler в формате: 
        "handler_name  DEBUG INFO WARNING ERROR CRITICAL"
        """
        result = []
        for handler in self.stats:
            result.append(f"{handler['handler']:<20} "
                           f"{handler['DEBUG']:>7} "
                           f"{handler['INFO']:>7} "
                           f"{handler['WARNING']:>9} "
                           f"{handler['ERROR']:>7} "
                           f"{handler['CRITICAL']:>10}")
        return result