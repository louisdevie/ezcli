from sys import stdout
from itertools import zip_longest

from . import _layout
from . import _utils

class Indentation:
    value = 0

_INDENT = Indentation()
 
def print_in_cols(*values, layout='-*'):
    layout = _layout.parse_layout(layout, len(values))
    print(layout)
    layout = _layout.calculate_layout(layout)
    print(layout)

    rows = zip_longest(*[_utils.auto_line_break(col, layout[i]) for i, col in enumerate(values)], fillvalue='')

    for row in rows:
        for i, cell in enumerate(row):
            stdout.write(' ')
            stdout.write(cell)
            stdout.write(' '*(layout[i]-len(cell)))
        stdout.write('\n')

def simple_message(text):
    for line in text.split('\n'):
        stdout.write(' '*(1+_INDENT.value*2) + line + '\n')

def blank_lines(n=1):
    stdout.write('\n'*n)

def indent(levels=1):
    _INDENT.value += levels

def unindent(levels=1):
    _INDENT.value -= levels