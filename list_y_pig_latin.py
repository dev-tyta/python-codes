#! python3
# list_y_pig_latin.py  - Adds bullet points to start

import pyperclip

text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '*' + lines[i]
text = '\n'.join(lines)

pyperclip.copy(text)
