class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        x = False
        n = len(nums)
        middle = -100000000000000
        stack = []
        for i in range(n-1,-1,-1):
            if nums[i] < middle :
                return True
            while stack and stack[-1] < nums[i]:
                middle =  stack[-1]
                stack.pop()
            
            stack.append(nums[i])         
        return False
