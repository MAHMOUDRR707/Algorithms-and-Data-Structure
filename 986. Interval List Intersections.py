#link :https://leetcode.com/problems/interval-list-intersections/
#time: o(n)
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]):
        n  =  len(firstList)
        m =  len(secondList)
        ans = []
        i,j = 0 , 0
        while i< n  and  m >  j :
            
            x =  max(firstList[i][0],secondList[j][0])
            y  =  min (firstList[i][1],secondList[j][1])
            
            if y >= x:
                ans.append([x,y])
            
            if  firstList[i][1] > secondList[j][1] :
                j += 1 
            else :
                i += 1
        return ans
            
