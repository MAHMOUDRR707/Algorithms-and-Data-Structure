#link:https://leetcode.com/problems/maximum-subarray/submissions/
#time:o(n)
class Solution:
    def maxSubArray(self, nums) :
        n =  len(nums)
        x ,max_x = nums[0],nums[0]
        for i in range(1,n):
            if x < 0 :
                x = 0
            x += nums[i]
            max_x = max(max_x,x)

        return max_x
