def solution1(tree, target):

	s, min = [], float('inf')
	
	# s (stack) is initially empty
	# after all elements are poppoed from Stack, the tree has been traversed
	while s or tree:
	
		# LEFT
		while(tree):
			s.append(tree)
			tree = tree.left
		tree = s.pop()
		
		# CURR
		if abs(target - tree.value) < abs(target - min):
			min = tree.value
		
		# RIGHT
		tree = tree.right 
	return min


def solution2(tree, target, closest = float('inf')):
		if tree is None:
		return closest
	
	if abs(tree.value - target) < abs(closest - target):
		closest = tree.value
		
	if target < tree.value:
		return solution2(tree.left, target, closest)
	
	else:
		return solution2(tree.right, target, closest)