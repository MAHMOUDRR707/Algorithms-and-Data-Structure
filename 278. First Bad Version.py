#time:log(n)
#link:https://leetcode.com/problems/first-bad-version/
class Solution:
    def firstBadVersion(self, n):
        left = 1
        right = n 
        while (left<= right):
            mid =  (left+right)//2
            if left==right :
                return left
            if (isBadVersion(mid)==True):
                 right =  mid
            if(isBadVersion(mid) == False):
                left = mid+1
