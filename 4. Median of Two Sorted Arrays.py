#link:https://leetcode.com/problems/median-of-two-sorted-arrays/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) :
        n =  len(nums1)
        m =  len(nums2)
        
        z = []*(m+n)
        z[:n] =  nums1
        z[n:m] =  nums2 
        x = (m+n)
        print(z)
        z.sort()
        if x%2 == 0 :
            x //=2
            return (z[x]+z[x-1])/2
        else :
            x//=2
            return z[x]
