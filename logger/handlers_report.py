from base_report import BaseReport

class HandlersReport(BaseReport):
    """
    Отчёт по состоянию ручек API. Статистика выводится по каждому уровню логирования.
    """

    def generate(self):
        """
        Генерация отчёта для статистики по ручкам.
        """
        # Выводим заголовок
        print(f"{'HANDLER':<20} {'DEBUG':>7} {'INFO':>7} {'WARNING':>9} {'ERROR':>7} {'CRITICAL':>10}")
        print("-" * 60)

        # Выводим данные по каждому handler
        for line in self.format_handler_data():
            print(line)

        # Суммируем уровни логирования
        debug_sum, info_sum, warning_sum, error_sum, critical_sum = self.sum_each_log_level()
        total_requests = self.sum_total_requests()

        # Выводим итоговые данные
        print(f"{'TOTAL':<20} {debug_sum:>7} {info_sum:>7} {warning_sum:>9} {error_sum:>7} {critical_sum:>10}")
        print(f'\nTOTAL REQUESTS: {total_requests}')