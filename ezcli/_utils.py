from re import compile as regex

import sys
cmd, *argv = sys.argv
argc = len(argv)

def split_int(a, b, min=0):
	bounds = [round(i*a/b) for i in range(b)] + [a]
	deltas = [max(min, bounds[i+1]-bounds[i]) for i in range(b)]
	return deltas

def auto_line_break(text, max_width):
	words = text.split(' ')
	lines = list()

	current_line = str()
	for word in words:
		if len(current_line) + len(word) <= max_width:
			current_line += word + ' '
		elif len(word) <= max_width:
			lines.append(current_line)
			current_line = word + ' '
		else:
			offset = end = max_width - len(current_line)
			lines.append(current_line + word[:offset])
			for i in range(len(word)//max_width - 1):
				start = i*max_width + offset
				end = (i+1)*max_width + offset
				lines.append(word[start:end])
			current_line = word[end:] + ' '

	lines.append(current_line)

	return lines

def strip(val):
	if val.startswith('='):
		val = val[1:]
	if val.startswith('"'):
		val = val[1:]
	if val.endswith('"'):
		val = val[:-1]

	return val