

# merge 2 sorted lists
# increasing order
'''
comparing a pair of numbers & inserting the smaller value into our list.
the two numbers will consist of one number from each sorted input list.
when we insert a number, the pointer in that list will move to the next element 
'''
def merge(l1, l2):
	p1, p2 = 0, 0
	l3 = []
	while (p1 < len(l1) and p2 < len(l2)):
		
		if l1[p1] < l2[p2]:
			l3.append(l1[p1])
			p1 += 1
		else:
			l3.append(l2[p2])
			p2 += 1
	# add remanent elements
	while (p1 < len(l1)):
		l3.append(l1[p1])
		p1 += 1

	while (p2 < len(l2)):
		l3.append(l2[p2])
		p2 += 1
	return l3

list = [1,2,6,2,44,32]
string = "aasdasdasd"
l = 0
r = 6


# break a list down to its halves, then merge them back
def sort(list):
	
	if(len(list) < 2):
		return list
		
	# split
	m = len(list)//2
	leftSubArr = sort(list[:m]) 
	rightSubArr = sort(list[m:])
	return merge(leftSubArr, rightSubArr)

x = sort(string)
print(x)