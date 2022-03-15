#link:https://leetcode.com/problems/climbing-stairs/
#time: o(n)
class Solution:
    def climbStairs(self, n):
        if n == 1 :
            return  1
        z =[1,2]
        for i in range(2,n):
            z.append(z[i-2]+z[i-1])
        return z[-1]
