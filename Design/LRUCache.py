'''
Motivation: this is the most popular Microsoft question
Thurs 3AM, 19 Sept 2019
Tests Passed: 4 of 18
'''

# NODE: dll
class node:
    key = 0
    value = 0
    nextNode = None
    prevNode = None

    def __init__(self, key, data, n, p):
        self.key = key
        self.value = data

class dll:
    head = None
    tail = None
    def __init__(self):
        self.head = None
        self.tail = None
    
    def addNode(self, key, value):
        n = node(key, value, None, None)
        # the dll is empty
        if self.head is None:
            self.head = n
            self.tail = n
            
        # the dll has 1 node
        elif self.head == self.tail:
            self.head.nextNode = n
            n.prevNode = self.head
            self.tail = n
        else: # the dll has 2+ nodes
            self.tail.nextNode = n
            n.prevNode = self.tail
            self.tail = n 
        return n # return node into dict
    
    
    def deleteNode(self, n):
        # Base Case 
        if self.head is None or n is None: 
            return 
          
        # If node to be deleted is head node 
        if self.head == n: 
            self.head = n.nextNode
  
        # Change next only if node to be deleted is NOT 
        # the last node 
        if n.nextNode is not None: 
            n.nextNode.prevNode = n.prevNode
      
        # Change prev only if node to be deleted is NOT  
        # the first node 
        if n.prevNode is not None: 
            n.prevNode.nextNode = n.nextNode
            
class LRUCache(object):
    
    # .........................................
    keys = {}           # dict stores dll-nodes
    capacity = 0        # cache size
    linkedList = None
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.linkedList = dll()
              
    # get val from the dict O(1)
    def get(self, key):
        if key in self.keys: 
            _val = self.keys[key].value            # get node's val with: _val = dict[key].value
            # re-position accessed-node to tail 
            self.linkedList.deleteNode(self.keys[key])
            self.keys.pop(key) 
            self.keys[key] = self.linkedList.addNode(key, _val)
            return _val
        else: return -1
        
   #insert new key with dict O(1)
    def put(self, key, value):
        if key not in self.keys:
            # cache @ capacity -> remove last-accessed item
            if len(self.keys) == self.capacity:
                _key = self.linkedList.head.key
                self.linkedList.deleteNode(self.linkedList.head)    # delete node  
                self.keys.pop(_key)                                 # delete dict-entry
            self.keys[key] = self.linkedList.addNode(key, value)
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
