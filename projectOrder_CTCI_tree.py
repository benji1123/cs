# edges => (a,d) (f,b) (b,d) (f,a) (d,c)
# projects => a b c d e f
# proper order => f e a b d c

# build a directed graph

edges = [['a','d'], ['f','b'], ['b','d'], ['f','a'], ['d','c']]

# adjacency list = vector of vectors
# adjList = {}
# for edge in edges:
# 	if edge[0] in adjList:
# 		adjList[edge[0]].append(edge[1])
# 	else:
# 		adjList[edge[0]] = [edge[1]]

# we need a 'min-heap' => this will be the case anytime there is ambiguity about which node to start @

# pseudocode


class node:
	data = None
	children = None
	def __init__(self, d, child):
		self.data = d
		self.children = [child]

ht = {}
for edge in edges:

	# check if prj is in HT
	if edge in ht:
		ht[edge[0]].children.append(edge[1])
	ht[edge[0]] = node(edge[0], edge[1])

