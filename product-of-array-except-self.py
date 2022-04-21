#link:https://leetcode.com/problems/product-of-array-except-self/
#time:o(n)
from itertools import combinations
import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        x = 1
        y = nums.count(0) 
        if y > 1 :
            return [0]*n
        elif y == 1 :
            nums =  combinations(nums,n-1)
            for i in nums:
                ans.append(np.prod(i))
            ans = ans[::-1]
        else :
            for i in range(n):
                x *= nums[i]
            for i in range(n):
                   ans.append((x//nums[i]))
        return ans
