
from stack import Stack
from queue import queue

# use nodes for "leaves"
class node:
	left = None
	right = None
	data = 0
	numDescendents = 0
	def __init__(self, d):
		self.data = d

# smaller children on left
# larger on right
class bst:
	head = None
	s = Stack()

	def __init__(self, leaves):
		print('created tree')
		# add leafs into BST
		for leaf in leaves:
			self.head = self.insert(self.head, leaf)

	def getHead(self):
		return self.head

	def insert(self, ref, d):
		# return a new node
		if ref is None:
			return node(d)
		# initialize left-child
		elif(d <= ref.data):
			ref.left = self.insert(ref.left, d)
		# initialize right-child
		else:
			ref.right = self.insert(ref.right, d)
		# return root-node with all children
		return ref

	def dfs(self, start, target):
		if start.data == target:
			print("found: " + str(target))
			return target
		elif target < start.data:
			self.dfs(start.left, target)
		else:
			self.dfs(start.right, target)

l = [1, 0, 2, 3]
b = bst(l)
b.dfs(b.getHead(), 3)
