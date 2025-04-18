import pytest
from logger.log_parser import *
from base_report import BaseReport
from handlers_report import HandlersReport



class FakeReport(BaseReport):
    def generate(self):
        return "foo"
    

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


def test_sum_each_log_level(sample_stats):
    report = FakeReport(sample_stats)
    result = report.sum_each_log_level()
    assert result == (8, 16, 6, 3, 1)  # DEBUG, INFO, WARNING, ERROR, CRITICAL


def test_sum_total_requests(sample_stats):
    report = FakeReport(sample_stats)
    result = report.sum_total_requests()
    assert result == 34  # сумма всех чисел кроме строк (имён)


def test_format_handler_data(sample_stats):
    report = FakeReport(sample_stats)
    formatted = report.format_handler_data()

    assert isinstance(formatted, list)
    assert len(formatted) == 2
    assert "handler_one" in formatted[0]
    assert "handler_two" in formatted[1]


