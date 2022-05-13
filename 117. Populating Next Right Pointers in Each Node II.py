"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        cur = root
        while root:
            dummy =  Node()
            temp =  dummy 
            while root:
                if root.left :
                    dummy.next  = root.left 
                    dummy = dummy.next
                if root.right :
                    dummy.next =  root.right
                    dummy =  dummy.next
                root = root.next 
            root = temp.next
        return cur
