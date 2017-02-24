class Node(self):
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next_node = next_node
	
	def get_data(self):
		return self.data

	def get_next(self):
		return self.next_node
	
	def set_next(self, next_node):
		self.next_node = next_node


def insert(self,data):
	new_node = Node(data)
	new_node.set_next(self.head)
	self.head=  new_node

def search(self, data):
	
