#!/usr/bin/python3
"""THIS IS 5-text_indentation MODULE"""


def text_indentation(text):
    """PRINTS WITH 2 NEW LINES AFTER CHARACTERS ., ? and :"""

    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for a in text:
        if flag == 0:
            if a == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if a == '?' or a == '.' or a == ':':
                print(a)
                print()
                flag = 0
            else:
                print(a, end="")
                
