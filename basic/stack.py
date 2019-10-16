
class Node:
    data = 0
    prev = None
    def __init__(self, d):
        self.data = d

class Stack:
    top = None
    def __init__(self):
        self.top = None

    def push(self, d):
        n = Node(d)
        n.prev = self.top
        self.top = n

    def pop(self):
        _temp = self.top
        self.top = self.top.prev
        return _temp

    def printStack(self):
        p = self.top
        while p != None:
            print(p.data)
            p = p.prev

    def isEmpty(self):
        if self.top is None:
            return True
        return False

# s = Stack()
# s.push(5)
# s.push(8)
# s.push(70)
# s.printStack()
# print("pop")
# s.pop()
# s.printStack()
        



