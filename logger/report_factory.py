from handlers_report import HandlersReport
from base_report import BaseReport

class ReportFactory:
    """
    Фабрика для создания отчётов.
    Позволяет добавить новые отчёты в будущем.
    """
    
    reports = {
        "handlers": HandlersReport,
        # Другие отчеты
    }

    @classmethod
    def get_report(cls, report_name: str, stats) -> BaseReport:
        """
        Создаёт отчёт по имени.
        :param report_name: Название отчёта.
        :param stats: Статистика для отчёта.
        :return: Объект отчёта.
        """
        report_class = cls.reports.get(report_name)
        if report_class is None:
            raise ValueError(f"Отчёт с названием '{report_name}' не найден.")
        return report_class(stats)