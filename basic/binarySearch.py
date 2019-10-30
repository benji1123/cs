x = [1,2,3,4,5,6,7]

def binSearch(arr, l, r, target):
	if(l<r):
		c = (l+r)//2
		if(arr[c] == target):
			return c
		# too big
		if(target < arr[c]):
			return binSearch(arr,l,c-1,target)
		# too small
		else:
			return binSearch(arr,c+1,r,target)
	return -1



x = [1,2,3,4,5,6,7]
print(binSearch(x, 0, len(x)-1, 6))
