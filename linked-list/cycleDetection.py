class Solution(object):
    def hasCycle(self, head):
        if head is None:
            return False
        
        # a fast-rate-of-change (fast ptr) intersects with slow-rate-of-change (slow-ptr) 
        # if it starts AFTER it; and not before --- basically, it catches up
        slow, fast = head, head.next
        
        while slow is not fast:
            # check fast.next to prevent null-ptr error
            if slow is None or fast is None or fast.next is None:
                return False
            fast = fast.next.next
            slow = slow.next
        return True