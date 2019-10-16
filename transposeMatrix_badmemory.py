class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        
        # pre-initialize output matrix
        output = [[0]*len(A) for i in range(len(A[0]))]
        
        # translate elements from A to Output
        for row in range(len(A)):
            for col in range(len(A[0])):
                output[col][row] = A[row][col]
                
        return output
    

    # lessons
    '''
    A different approach is to modify A directly.
    One can swap each element with the inverse element; 
    but, if you do this element-by-element in the normal order,
    you will end up with no changes. Each element will be swapped,
    then reached again in its new position & swapped back
    to its orignial position.
    So you'd need to create a new swap-order.
    '''