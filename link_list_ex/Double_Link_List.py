class Node(object):
	
	def __init__(self,data, next, prev):
		self.data = data
		self.next = next
		self.prev = prev



class DoubleList(object):
	
	root_head = None
	head = None

	def show(self):
		print 'showing the complete link list data'
		current_node = self.root_head
		while current_node is not None:	
			print current_node.data, "-->"
			current_node = current_node.next
		print None

	def append(self,data):
		new_node = Node(data,None,None)
		if self.root_head is None:
			self.root_head = self.head = new_node
		else: 
			new_node.next = None
			new_node.prev = self.head
			self.head.next = new_node
			
		self.head = new_node		
		
		
	def remove(self,data):

		current_node = self.root_head
		privous_node = self.root_head
		while current_node is not None:
			if current_node.data == data:	
				if current_node == self.root_head:
					self.root_head = current_node.next		
				else:
					privous_node.next = current_node.next
				break
			privous_node = current_node
			current_node = current_node.next
		if current_node == None:
			print ' Data not found to remove'
					
		



	def search(self, search_data):
		print 'now searching the link list for the data'

		current_node = self.root_head
		while current_node is not None:
			if current_node.data == search_data:
				print 'data found'
				break
			current_node = current_node.next

		if current_node == None:
			print ' Data Not found'

s= DoubleList()
s.append(2)
s.append(4)
s.append(13)
s.append(12)
s.show()
#s.search(3)
#s.search(2)
#s.remove(2)

s.show()
