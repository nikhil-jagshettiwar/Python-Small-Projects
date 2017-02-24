def logging(func):
	def Actual_logging(*args, **kwargs):
		print 'I am in Actual_loggin function'
		print reduce(lambda x,y : x*y , args) 
		print 'args present are :', args , kwargs
		
		print func(*args, **kwargs)	
	
	return Actual_logging


@logging
def foo(*args,**kwargs):
	return 'hello i am in foo function now'



foo(2,3,5,6)

