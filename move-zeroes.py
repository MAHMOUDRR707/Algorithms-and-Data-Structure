#link:https://leetcode.com/problems/move-zeroes/
#time:o(n)

class Solution:
    def moveZeroes(self, nums) :
        x = 0 
        z =  []
        n =  len(nums)
        for i in range(n):
            if nums[i] == 0 :
                x+=1
            else :
                z.append(nums[i])
        for j in range(x):
            z.append(0)
        for i in range(n):
            nums[i] = z[i]
