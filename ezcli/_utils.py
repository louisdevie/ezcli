def split_int(a, b, min=0):
	bounds = [round(i*a/b) for i in range(b)] + [a]
	deltas = [max(min, bounds[i+1]-bounds[i]) for i in range(b)]
	return deltas

def auto_line_break(text, max_width):
	words = text.split(' ')
	lines = list()

	current_line = words.pop(0)
	for word in words:
		if len(current_line) + len(word) + 1 <= max_width:
			current_line += ' ' + word
		else:
			lines.append(current_line)
			current_line = word

	lines.append(current_line)

	return lines