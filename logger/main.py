from logger.log_parser import get_log_files, parse_log_statuses
from report_factory import ReportFactory


def main():
    # Получаем аргументы командной строки
    args = get_log_files()
    
    # Читаем все логи
    all_handler_stats = []
    for path in args.log_files:
        stats = parse_log_statuses(path)
        all_handler_stats.extend(stats)

    # Получаем нужный отчёт
    report = ReportFactory.get_report(args.report, all_handler_stats)
    report.generate()

if __name__ == "__main__":
    main()