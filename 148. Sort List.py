# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import collections
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur =  head 
        z = []
        while cur :
            z.append(cur.val)
            cur = cur.next
        n = len(z)
        z.sort()
        z =  collections.deque(z)
        res = head
        while res :
            res.val =  z.popleft()
            res =res.next
        return head
