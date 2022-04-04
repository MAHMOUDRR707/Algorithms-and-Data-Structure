#link:https://leetcode.com/problems/merge-intervals/
#time:o(n)
class Solution:
    def merge(self, intervals: List[List[int]]):
        first , last = [],[]
        intervals.sort()
        ans = [intervals[0]]
        n =  len(intervals)
        for i in range(1,n) :
            end =  ans[-1][1]
            if end >=  intervals[i][0]:
                ans[-1][1] =  max(end,intervals[i][1])    
            else :
                ans.append(intervals[i])
        return ans
