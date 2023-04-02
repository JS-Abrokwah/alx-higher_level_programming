#!/usr/bin/python3

def text_indentation(text):
    """
    Prints the input text with 2 new lines after each of the characters '.', '?' and ':'
    
    Args:
        text (str): The text to be indented
    
    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    special_chars = set(['.', '?', ':'])
    lines = []
    line_start = 0
    for i in range(len(text)):
        if text[i] in special_chars:
            lines.append(text[line_start:i+1].strip())
            lines.append("")
            line_start = i+1
    
    # Add the last line to the list of lines
    lines.append(text[line_start:].strip())
    
    # Print the lines with indentation
    for line in lines:
        if line == lines[-1]:
            print(line, end="")
        else:
            print(line)
