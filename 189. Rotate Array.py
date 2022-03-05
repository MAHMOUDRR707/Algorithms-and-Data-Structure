#link:https://leetcode.com/problems/rotate-array/
#time:o(n)
class Solution:
    def rotate(self, nums, k):
        n =  len(nums)
        z =[0]*n
        for i in range(n):
            n_index = (k+i)%n
            z[n_index] = nums[i]
        for i in range(n):
            nums[i] = z[i]
        return nums
        
