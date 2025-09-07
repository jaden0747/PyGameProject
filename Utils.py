def map_value(in_min, in_max, out_min, out_max, value):
	"""
	Maps a value from one range to another.
	"""
	if in_max - in_min == 0:
		raise ValueError("Input range cannot be zero.")
	return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
