
# dictionary of linked lists
from stack import Stack
from queue import queue

class Graph:
	table = {}
	visited = {}
	s = Stack()
	
	# constructor - graph provided 
	def __init__(self, t):
		self.table = t
		for node in self.table:
			self.visited[node] = False

	# add node - first el + neighbours
	def addNode(self, l):
		self.table[l[0]] = l[1:]

	# O()
	def dfs(self, start, target):
		#print(start)

		# return on visited nodes
		if self.visited[start] is False:
			self.visited[start] = True
			if target in self.table[start]:
				print("found: " + target)
				return target
			else:
				for node in self.table[start]:
					if(self.visited[node] is False):
						#print(self.table[start])
						self.dfs(node, target) 
	
	def stackDFS(self, start, target):
		if(self.visited[start] != True):
			self.visited[start] = True
			for node in self.table[start]:
				self.s.push(node)
			while self.s.isEmpty() != True:
				_temp = self.s.pop()
				# if(_temp == target):
				# 	print("found: " + str(_temp))
				# 	return _temp
				self.stackDFS(_temp, target)


	def bfs(self, start, target):
		q = queue()
		q.enqueue(start)
		while not q.isEmpty():
			node = q.dequeue()
			if(node == target):
				print('found: ' + str(node))
				return
			for n in self.table[node]:
				q.enqueue(n)

# test
a = {
	'A' : ['B', 'C'],
	'B' : ['D', 'E'],
	'C' : ['F', 'G'],
	'D' : ['A'],
	'E' : ['A'],
	'F' : ['B'],
	'G' : ['C']
}
g = Graph(a)
x = g.bfs('A', 'G')