def divide(numerator,divider, nik):
	return numerator/divider

def decorate(function_to_decorate):
	def _decorate(num, div):
		if div == 0:
			return 0
		else:
			return function_to_decorate(num,div)
	return _decorate



divide = decorate(divide)

print divide(4,2)
