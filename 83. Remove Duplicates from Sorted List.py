#link:https://leetcode.com/problems/remove-duplicates-from-sorted-list/
#time: o(n)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        cur  = head 
        if cur is None:
            return head
        after = cur.next
        while after :
            if after.val ==  cur.val :
                while after.val == cur.val:
                    after = after.next
                    if after is None:
                        break
                cur.next = after
            else:
                cur  = after
                after = after.next
        return head
