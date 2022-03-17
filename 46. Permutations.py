#link:https://leetcode.com/problems/permutations/
#time : o(1)
from itertools import permutations 
class Solution:
    def permute(self, nums):
        z = permutations(nums)
        return z
