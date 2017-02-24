from functools import wraps


def decorator_name(f):
	#@wraps(f) 
	def decorated(*args, **kwargs):
		if not can_run:
			return 'Function will not run'
		return f(*args, ** kwargs)

	return decorated



@decorator_name
def func():	
	return 'Function will run'

can_run = True

print (func())
print func.__name__
