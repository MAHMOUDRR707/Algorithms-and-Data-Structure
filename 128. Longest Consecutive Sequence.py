class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        x =  0 
        max_x = 0
        n = len(nums)
        nums.sort()
        if not nums :
            return 0
        for i  in range(1,n):
            if  nums[i]- nums[i-1] == 1 :
                x +=1
            elif nums[i] == nums[i-1] :
                continue
            else :
                x = 0
            max_x =  max(x,max_x)
        return (max_x+1)
