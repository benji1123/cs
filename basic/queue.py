
class node():
	data = None
	next = None   # closer to front of queue
	prev = None	  # closer to back of queue

	def __init__(self, d):
		self.data = d

class queue(): 	# O(1)
	front = None
	back = None
	def __init__(self):
		front, back = None, None


	def isEmpty(self):
		if self.front is None:
			return True
		return False


	def enqueue(self, d):
		# create node as PREV of 'back'
		# set as new 'back'
		if (self.front is None):
			self.front = node(d)
			self.back = self.front
			return

		self.back.prev = node(d)
		self.back.prev.next = self.back
		self.back = self.back.prev


	def dequeue(self): # O(1)
		# set 'prev' of front as new front
		# set next of new-front as None
		if(self.front is None):
			print('queue already empty')
			return
		elif(self.front == self.back):
			_temp = self.front.data
			self.front, self.back = None, None
			return _temp

		_temp = self.front.data
		self.front = self.front.prev
		self.front.next = None
		return _temp


	def printQueue(self): # O(n)
		p = self.front
		while p is not None:
			print(p.data)
			p=p.prev