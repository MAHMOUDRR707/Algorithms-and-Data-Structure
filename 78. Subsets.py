#link:https://leetcode.com/problems/subsets/
#time:o(n)

from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        z =[]
        n = len(nums)
        for i in range(n+1):
            for j in (combinations(nums,i)):
                z.append(list(j))
        return z
                
