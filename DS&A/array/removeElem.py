'''
we're going to take a 2 pointer approach:
 > traverse from the start of the array (l)
 > traverse from the tail of the array (r)

The traversal will end when these two pointers meet at some arbitrary point.
On the way to the arbitrary point, the left-pointer will look for '2s' and the right-pointer will look for 'non-2s' and we'll swap them.
At the end of traversal, we will return the index of the left-pointer plus 1; 
'''

arr = [1,1,0,0,4,0,5,6,7]
target = 0

l, r = 0, len(arr)-1			
while l < r:
	if l<r and arr[l] != target:
		l += 1
	if l<r and arr[r] == target:
		r -= 1
	if arr[l] == target and arr[r] != target:
		print(arr)
		arr[l], arr[r] = arr[r], arr[l]

print(arr)
print(l+1)