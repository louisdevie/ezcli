from re import compile as _re

REGEX_FIXED_COLUMN = _re(r'\d+')
REGEX_RELATIVE_COLUMN = _re(r'\d\d?%')
REGEX_FRACTIONAL_COLUMN = _re(r'-+')

CHARACTERS = 'char'
RELATIVE = 'rel'
FRACTIONAL = 'frac'

def parse_layout(layout, ncols):
	before = list()
	after = list()
	repeat = None

	isafter = False
	for col in layout.split(' '):
		if col.endswith('*'):
			if not isafter:
				repeat = parse_layout_column(col[:-1])
				isafter = True
			else:
				raise ValueError('there can only be one repeating column')
		else:
			if isafter:
				after.append(parse_layout_column(col))
			else:
				before.append(parse_layout_column(col))

	nabs = len(before) + len(after)
	nrpt = ncols - nabs
	if nrpt < 0:
		raise ValueError(f'the layout describe {nabs} columns but only {n} were given')
	else:
		return before + [repeat]*nrpt + after
			
def parse_layout_column(col):
	if REGEX_FIXED_COLUMN.fullmatch(col):
		width = int(col)
		unit = CHARACTERS

	elif REGEX_RELATIVE_COLUMN.fullmatch(col):
		width = int(col[:-1])
		unit = RELATIVE

	elif REGEX_FRACTIONAL_COLUMN.fullmatch(col):
		width = len(col)
		unit = FRACTIONAL

	else:
		raise ValueError(f'invalid column width {col}')

	return width, unit
	
def calculate_layout(l):
	width = os.get_terminal_size()[0]
	leftover = width
	nauto = 0
	calc = list()
	for w, u in l:
		if u == 'fixed':
			calc.append(w)
			leftover -= calc[-1]
		elif u == 'relative':
			calc.append(int(w*width/100))
			leftover -= calc[-1]
		elif u == 'auto':
			calc.append([w])
			nauto += w
	autowidth = _split_int(leftover, nauto, 1)
	i = 0
	for j in range(len(calc)):
		if isinstance(calc[j], list):
			n, = calc[j]
			calc[j] = sum(autowidth[i:i+n])
			i += n
	return calc