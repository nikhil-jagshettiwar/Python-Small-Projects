from functools import wraps
def a_new_decorator(a_func):
	@wraps(a_func)
	def wrapTheFunction():
		print("I am printint this BEFORE executin the a_func")

		a_func()

		print ('I am printing this AFTER executing the a_func')	
	
	return wrapTheFunction



@a_new_decorator
def a_function_requiring_decoration():
	print (' I am now in actual decorator function')


print (a_function_requiring_decoration.__name__)
#a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
a_function_requiring_decoration()
