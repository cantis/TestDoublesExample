"""A module for reading lines from a file."""

from pathlib import Path


def read_from_file(filename: str) -> str:
    """Read a file and return the first line."""
    with Path.open(filename, 'r') as file:
        return file.readline()
    # infile = open(filename, 'r')
    # line = infile.readline()
    # return line
