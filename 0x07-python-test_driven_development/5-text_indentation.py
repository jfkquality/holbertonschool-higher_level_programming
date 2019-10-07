#!/usr/bin/python3
def text_indentation(text):
    # Find min of position of finding ',', '.' and ';'
    # Extract substring to that index + 1. Use slicing
    # Repeat until end of string/text

    start = 0
    question = 0
    dot = 0
    colon = 0
    position = 0

    if not isinstance(text, (str)):
        raise TypeError("text must be a string")

    while (position != len(text) and start != len(text) + 2):
        question = text.find('?', start)
        if question == -1:
            question = len(text)
        dot = text.find('.', start)
        if dot == -1:
            dot = len(text)
        colon = text.find(':', start)
        if colon == -1:
            colon = len(text)
        position = min(question, dot, colon)

        print(text[start:position + 1], end='')
        if (position != len(text) and start != len(text) + 2):
            print('\n')

        start = position + 2
