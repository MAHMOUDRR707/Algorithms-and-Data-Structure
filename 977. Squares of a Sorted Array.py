#time:o(nlog(n))
#link:https://leetcode.com/problems/squares-of-a-sorted-array/
class Solution:
    def sortedSquares(self, nums):
        z =[]
        for i in nums :
            z.append(i*i)
        z.sort()
        return z


##### Another solution #####

#time : o(n)
class Solution:
    def sortedSquares(self, nums):
        r = 0
        n = len(nums)
        z =[]
        for i in range(n) :
            if nums[r] <0 :
              nums[r] = abs(nums[r])
              r += 1        
        l = r-1
        while(l>=0 and r<n): 
            
            if nums[l] < nums[r] :
                z.append(nums[l]**2)
                l -=1
            else :
                z.append(nums[r]**2)
                r += 1
        for i in range(r,n):
            z.append(nums[i]**2)
        for i in range(l,-1,-1):
            z.append(nums[i]**2)
        
        return z
