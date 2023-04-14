#!/usr/bin/python3

"""
inserts a line of text to a file, after each line
containing a specific string (see example)
"""


def append_after(filename="", search_string="", new_string=""):
    """append new_string after line of filename that contains
    search_string"""

    new_text = ""
    with open(filename) as myfile:
        for line in myfile:
            new_text += line
            if search_string in line:
                new_text += new_string

    with open(filename, 'w') as editablefile:
        editablefile.write(new_text)
