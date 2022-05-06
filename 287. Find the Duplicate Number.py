class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 0 
        right =  len(nums) - 1
        n = len(nums)
        z = {}
        for i in range(n) :
            if nums[i] in z  :
                return nums[i]
            z[nums[i]] = 1
        return 0
