#link: https://leetcode.com/problems/two-sum/
#time: o(n)
class Solution:
    def twoSum(self, nums, target) :
        n =  len(nums)
        s = 0
        z = {}
        for i in range(n):
            s =  target - nums[i]
            if s  in z :
                return [z[s],i]
            else :
                z[nums[i]] = i
        
