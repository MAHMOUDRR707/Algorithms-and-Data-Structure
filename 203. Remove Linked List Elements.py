#link:https://leetcode.com/problems/remove-linked-list-elements/
#time:o(n)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head, val):
        while head and head.val == val :
            head = head.next
        
        if head is None:
            return head
        prev = head
        cur = prev.next
        
        while cur :
            if cur.val ==  val :
               cur  = cur.next
               prev.next = cur
            else :
                cur = cur.next
                prev = prev.next
            
        
        return head
