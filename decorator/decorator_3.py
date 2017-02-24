from functools import wraps 

def logit(logfile='out.log'):
	def logging_decorator(func):
		
		@wraps(func)
		def wrapped_function(*args, **kwargs):
			log_string = func.__name__ + 'was called'
			print log_string
			with open(logfile, 'a') as F_file:
				F_file.write(log_string + '\n')
		return wrapped_function	
	return logging_decorator



@logit()

def my_func():
	pass

my_func()
