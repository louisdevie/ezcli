from sys import stdout

from . import _layout
 
def print_in_cols(*values, layout='-*'):
    layout = _layout.parse_layout(layout, len(values))
    print(layout)
    layout = _layout.calculate_layout(layout)
    print(layout)
    for row in rows:
        for i, cell in enumerate(row):
            stdout.write(cell)
            stdout.write(' '*(layout[i]-len(cell)))
        stdout.write('\n')