class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        z = {}
        for i in set(nums):
            x =  nums.count(i)
            if x > 2 :
                z[i] = x
        n = len(nums)-1
        y = 0
        i = 0
        while n > 0:
            if nums[i] in z :
                if z[nums[i]] > 2 :
                        z[nums[i]] -=1
                        nums[i] = 100000
                        y+=1
            n-=1
            i+=1
        n = len(nums)
        return n-y
