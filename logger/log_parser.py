import os
import argparse
from collections import defaultdict
from typing import List, Dict

def parse_log_statuses(file_path: str) -> List[Dict[str, int]]:
    """
    Парсит лог-файл и возвращает статистику по уровням логирования.
    :param file_path: Путь к лог-файлу.
    :return: Список словарей с данными по каждому handler.
    """
    stats = defaultdict(lambda: {
        'DEBUG': 0,
        'INFO': 0,
        'WARNING': 0,
        'ERROR': 0,
        'CRITICAL': 0
    })
    
    try:
        with open(file_path) as f:
            for line in f:
                try:
                    parts = line.split()
                    if not any(i in parts for i in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']):
                        continue
                    
                    handler = parts[5]
                    level = parts[2]
                    
                    if level in stats[handler]:
                        stats[handler][level] += 1
                except Exception as e:
                    print(f"Ошибка при обработке строки: {line.strip()}. Ошибка: {e}")
                    continue
        
        return [{'handler': k, **v} for k, v in stats.items()]
    except FileNotFoundError as e:
        print(f"Файл {file_path} не был найден.")
        return []


def get_log_files():
    """
    Получает список лог-файлов из аргументов командной строки.
    :return: Аргументы командной строки.
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

    parser = argparse.ArgumentParser(description="Анализ логов и генерация отчётов")
    parser.add_argument("log_files", nargs="+", help="Список лог-файлов для анализа")
    parser.add_argument("--report", type=str, help="Тип отчёта (например, handlers)")
    return parser.parse_args()