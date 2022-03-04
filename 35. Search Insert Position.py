#link:https://leetcode.com/problems/search-insert-position/submissions/
#time:o(log(n))
class Solution:
    def searchInsert(self, List, target) :
        l = 0
        n = len(List)
        r = n 
        while (1):
            mid =  (r+l)//2

            if r == l :
                return l
            if target ==  List[mid]:
                return mid 
            if target < List[mid] :
                r =  mid
            if target > List[mid] :
                l =  mid +1
            
            
        
