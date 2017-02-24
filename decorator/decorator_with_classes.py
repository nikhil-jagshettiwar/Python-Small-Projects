class logit(object):
	def __init__(self,logfile= 'outlog.log'):
		self.logfile = logfile


	def __call__(self, func):
		log_string = func.__name__ + 'was called'
		print log_string
		# opening the logfile and appending
		with open(self.logfile, 'a') as FD:
			FD.write(log_string + '\n')
		self.notify()

	def notify(self):
		pass


@logit()
def foo():
	pass


class email_logit(logit):
	''' 
	A logit implentation for sending the emails to admins when the logit function called
	'''
	
	def __init__(self, email = 'nikhil@imgtec.com', *args, **kwargs):
		self.email = email
		super(email_logit, self).__init__(*args, **kwargs)

	
	def notify(self):
		pass
	
