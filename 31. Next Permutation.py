class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        start = 0 
        var = 0
        x =  sorted(nums,reverse =True)
        if x == nums :
                z = nums[:][::-1]
                nums[:] = z[:]
        else :
         for i in range(n-2,-1,-1) :
            x = nums[i+1]
            if x > nums[i]:
                var =  nums[i]
                start = i
                break
         end = n-1
         for i in range(start+1,n):
            if nums[i] <= var :
                break
            else :
                before =  nums[i]
                end = i 
         nums[start] , nums[end] =  nums[end] , nums[start]
         index =  min(start,end)
         z  = nums[start+1:][::-1]
         nums[start+1:] = z
