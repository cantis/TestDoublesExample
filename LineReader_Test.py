"""Test the LineReader module."""

import pathlib
from pathlib import Path
from unittest.mock import MagicMock, mock_open, patch

from LineReader import read_from_file


def test_returns_correct_string(monkeypatch) -> None:
    """Test that the function returns the correct string from the file."""
    # arrange
    mock_file = MagicMock()
    mock_file.readline.return_value = 'test line'
    monkeypatch.setattr(pathlib.Path, 'open', mock_file)

    # act
    result = read_from_file('test.txt')

    # assert
    mock_file.assert_called_once_with('test.txt', 'r')
    assert result == 'test line'


def test_path_open() -> None:
    """Test that the function returns the correct string from the file."""
    # Arrange
    mock_data = 'mock file content'
    m_open = mock_open(read_data=mock_data)
    file_path = 'dummy_path.txt'

    # Act
    with patch('pathlib.Path.open', m_open):
        with Path(file_path).open() as f:
            result = f.read()

    # Assert
    assert result == mock_data