#link:https://leetcode.com/problems/permutations-ii/
#time:o(n)
from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n =  len(nums)
        z =[]
        x =  permutations(nums,n)
        for i in x :
            if list(i) not in z :
                z.append(list(i))
        return((z))
