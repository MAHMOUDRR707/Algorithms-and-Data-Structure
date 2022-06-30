class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort() 
        n = len(nums)
        x =  nums[(n-1)//2]
        y = 0
        for i in nums : 
            if i != x :
                y += abs(x-i)
        return (y)
