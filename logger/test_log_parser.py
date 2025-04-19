from log_parser import parse_log_statuses, get_log_files
import sys
from unittest import mock
import pytest

def test_parse_log_statuses_file_not_found(capfd):
    stats = parse_log_statuses("nonexistent.log")
    out, _ = capfd.readouterr()
    assert stats == []
    assert "не был найден" in out




def test_get_log_files_parses_args_correctly():
    test_args = ["script_name", "logs/log1.txt", "logs/log2.txt", "--report", "handlers"]

    with mock.patch.object(sys, 'argv', test_args):
        args = get_log_files()
        assert args.log_files == ["logs/log1.txt", "logs/log2.txt"]
        assert args.report == "handlers"