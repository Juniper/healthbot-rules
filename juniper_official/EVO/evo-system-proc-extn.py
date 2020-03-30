def kb_convert(size_value, **kwargs):
	if not size_value[-1].isalpha():
		return float(size_value)
	else:
		n = float(size_value[:-1])
		c = size_value[-1].lower()
		if c == 'm':
			return float(n * 1000)
		elif c == 'g':
			return float(n * 1000000)
		else :
			return float(n)
