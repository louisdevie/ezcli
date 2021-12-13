def split_int(a, b, min=0):
	bounds = [round(i*a/b) for i in range(b)] + [a]
	deltas = [max(min, bounds[i+1]-bounds[i]) for i in range(b)]
	return deltas