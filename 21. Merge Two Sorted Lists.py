#link: https://leetcode.com/problems/merge-two-sorted-lists/
#time:o(n)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        z =[]
        cur =  list1
        cur2 =  list2
        curr = head =  ListNode()
        while cur2 and cur :
            if cur2.val >  cur.val :
                curr.next = cur
                cur,curr =  cur.next,cur
            else :
                curr.next =  cur2
                cur2,curr=  cur2.next , cur2
        if cur or cur2 :
            curr.next =  cur  if cur else  cur2
        return head.next
