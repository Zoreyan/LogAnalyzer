import tempfile
import os
from log_parser import parse_log_statuses


def test_parse_log_statuses_valid_lines():
    log_content = """
    2025-04-16 12:27:26,637 INFO django.server: "GET /api/v1/dashboard/ HTTP/1.1" 200 5219
    2025-04-16 12:28:48,387 DEBUG django.server: "GET /api/v1/dashboard/ HTTP/1.1" 200 5219
    2025-04-16 12:29:00,388 ERROR django.request: "POST /api/v1/orders/ HTTP/1.1" 500 80559
    2025-04-16 12:29:01,001 WARNING django.server: "GET /api/v1/dashboard/ HTTP/1.1" 200 5219
    2025-04-16 12:29:01,643 CRITICAL django.core: "CRITICAL FAILURE"
    """.strip()

    with tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8") as tmp:
        tmp.write(log_content)
        tmp_path = tmp.name

    stats = parse_log_statuses(tmp_path)
    os.remove(tmp_path)

    expected = {
        "django.server": {
            "DEBUG": 1,
            "INFO": 1,
            "WARNING": 1,
            "ERROR": 0,
            "CRITICAL": 0
        },
        "django.request": {
            "DEBUG": 0,
            "INFO": 0,
            "WARNING": 0,
            "ERROR": 1,
            "CRITICAL": 0
        },
        "django.core": {
            "DEBUG": 0,
            "INFO": 0,
            "WARNING": 0,
            "ERROR": 0,
            "CRITICAL": 1
        }
    }

    for item in stats:
        handler = item["handler"]
        for level in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']:
            assert item[level] == expected[handler][level]


def test_parse_log_statuses_file_not_found(capfd):
    stats = parse_log_statuses("nonexistent.log")
    out, _ = capfd.readouterr()
    assert stats == []
    assert "не был найден" in out