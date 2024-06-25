"""Demonstrate how to mock the open function in the pathlib module."""
import pathlib
from pathlib import Path
from unittest.mock import MagicMock

from _pytest.monkeypatch import MonkeyPatch

mock_file = MagicMock()
mock_file.readline.return_value = 'test line'
MonkeyPatch.setattr(pathlib,'Path.open', mock_file)

print(pathlib.Path.open('test.txt', 'r').readline())  # noqa: T201
