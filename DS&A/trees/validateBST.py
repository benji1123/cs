class Solution(object):
    def isValidBST(self, root):
        # stack
        s = []
        prev = float('-inf')
        # in order-traversal
        while s or root:
            while root:
                s.append(root)
                root = root.left
            root = s.pop()
            # if not in order => BST = false
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right
        return True