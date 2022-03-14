#link:https://leetcode.com/problems/implement-queue-using-stacks/
#time:o(1)
class MyQueue:

    def __init__(self):
        self.items = []
    def push(self, x) :
        self.items.insert(0,x)

    def pop(self) :
        return  self.items.pop()

    def peek(self) :
        return self.items[-1]

    def empty(self):
        if self.items == [] :
            return True
        return False
