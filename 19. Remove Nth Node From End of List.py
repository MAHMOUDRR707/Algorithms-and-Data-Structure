#link:https://leetcode.com/problems/remove-nth-node-from-end-of-list/
#time:o(n)
class Solution:
    def removeNthFromEnd(self, head, n):
        l = 0 
        cur = head 
        while cur :
            l += 1 
            cur = cur.next
            
        y = l - n
        if  y ==0:
            return head.next
        x = 1
        cur  =  head
        while cur :
            if x == y:
                cur.next =  cur.next.next
                break
            x += 1 
            cur = cur.next
        
        return head
