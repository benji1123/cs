class Solution(object):
    def maxDepth(self, root):
        # depth = # nodes in path != height
        if root is None:
            # return [0] not [1] because this Node d.n.e
            return 0
        
        leftChildH = self.maxDepth(root.left)
        rightChildH = self.maxDepth(root.right)
        return max(leftChildH, rightChildH)+1
        
        # time complexity => O(n)
        # space complexity => O(log[n])