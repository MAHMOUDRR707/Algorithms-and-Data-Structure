class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        max_ =  nums.index(max(nums))  
        min_ =  nums.index(min(nums)) 
        x =  min(max(min_,max_)+1 , n - min(max_,min_) , n-max(max_,min_)+min(max_,min_)+1)
        return x
