class Solution:
    def childHeightDiff(self, root):
        if root is None:
            return 0
        else:
            # compute height of node's LEFT & RIGHT SUBTREE
            l = self.childHeightDiff(root.left)
            r = self.childHeightDiff(root.right)
            
            # check height-balance
            if abs(l-r)>1:
                return False
            else:
                if l is False or r is False:
                    return False
                # compute HEIGHT of curr-node
                return max(l, r)+1
        return True
    
    def isBalanced(self, root: TreeNode) -> bool:
        # empty tree is "balanced"
        if root is None:
            return True
        return self.childHeightDiff(root)
        
        # algorithm is same as MAX-HEIGHT OF BT => O(n) ???
        # space complexity => O(log[n]) => stack will at-most contain NODES in path of max-height