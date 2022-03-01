#link : https://leetcode.com/problems/container-with-most-water/
#time: o(n)
class Solution:
    def maxArea(self, height) :
        '''''
        z = 0
        max_z = 0
        for i in range(0,len(height)):
            for j in range(i+1,len(height)):
               z = min(height[i],height[j]) * (abs(j-i))
               max_z =  max(z,max_z)
        return (max_z)
        '''''
        
        l,r = 0,len(height)-1 
        
        z ,max_z = 0,0
        while l != r :
            z =  min(height[l],height[r])*(r-l) 
            max_z =  max(z,max_z)
            if height[l] > height[r] :
                r -= 1 
            else :
                l +=1 
        return  max_z
