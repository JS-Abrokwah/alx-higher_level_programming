#!/usr/bin/python3
"""
1-write_file.py
writes text into file
"""


def write_file(filename="", text=""):
    """Writes text text into file filename"""
    with open(filename, 'w', encoding='utf-8') as myfile:
        return myfile.write(text)
