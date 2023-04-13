#!/usr/bin/python3
"""
2-append_write.py
writes text to the last line of a file
"""


def append_write(filename="", text=""):
    """Writes text text into file filename"""
    with open(filename, 'a', encoding='utf-8') as myfile:
        return myfile.write(text)
