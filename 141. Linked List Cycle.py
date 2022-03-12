#link :https://leetcode.com/problems/linked-list-cycle/
#time:o(n)
class Solution:
    def hasCycle(self, head) :
        cur = head
        val =  head
        while val is not None and val.next is not None:
            cur  =  cur.next
            val =  val.next.next
            if val == cur :
                return True
        return False
            
