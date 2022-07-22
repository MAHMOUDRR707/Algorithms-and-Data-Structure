# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        more = []
        less = []
        final = []
        cur  = head
        while cur :
            if cur.val < x :
                less.append(cur.val)
            else :
                more.append(cur.val)
            cur  = cur.next
            
        res =  finall=  ListNode()
        final =  less + more
        for i in final : 
            res.next = ListNode(i)
            res =  res.next
      
        return finall.next
