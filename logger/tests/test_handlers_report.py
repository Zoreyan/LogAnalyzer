import pytest
from handlers_report import HandlersReport


@pytest.fixture
def sample_stats():
    return [
        {
            "handler": "handler_one",
            "DEBUG": 2,
            "INFO": 4,
            "WARNING": 1,
            "ERROR": 1,
            "CRITICAL": 0
        },
        {
            "handler": "handler_two",
            "DEBUG": 6,
            "INFO": 12,
            "WARNING": 5,
            "ERROR": 2,
            "CRITICAL": 1
        }
    ]


def test_generate_output(sample_stats, capfd):
    report = HandlersReport(sample_stats)
    report.generate()

    out, err = capfd.readouterr()
    assert "HANDLER" in out
    assert "handler_one" in out
    assert "handler_two" in out
    assert "TOTAL" in out
    assert "TOTAL REQUESTS" in out

    # Проверим суммы
    assert "8" in out     # DEBUG
    assert "16" in out    # INFO
    assert "6" in out     # WARNING
    assert "3" in out     # ERROR
    assert "1" in out     # CRITICAL
    assert "34" in out    # total requests