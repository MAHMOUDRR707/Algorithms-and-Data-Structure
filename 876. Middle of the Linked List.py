#link:https://leetcode.com/problems/middle-of-the-linked-list/
#time:o(n)
# Definition for singly-linked list.
'''''
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
'''''
class Solution(): 
     def middleNode(self, head) :
        cur  =  head 
        x = 1
        while cur.next  :
            cur  =  cur.next
            x +=1
        x = x//2
        y = 0
        cur  = head
        while y < x :
            cur = cur.next
            y += 1
        return cur
   
