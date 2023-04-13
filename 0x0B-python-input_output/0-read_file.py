#!/usr/bin/python3
"""
0-read_file.py
reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """Reads a file and print to stdout"""
    with open(filename, 'r', encoding='utf-8') as myfile:
        for line in myfile:
            print(line, end="\n")
