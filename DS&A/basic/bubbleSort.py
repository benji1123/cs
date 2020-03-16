# compression of files can use SORTING , ex:
	# group equal pixels together
	# compressed file is a count of each group of pixels

l = [5,2,4,6,1,3]

# sort in increasing order
for iteration in range(len(l)):
	for index in range(len(l)-1):
		if l[index] > l[index+1]:
			# swap
			l[index], l[index+1] = l[index+1], l[index]
print(l)