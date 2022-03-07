#time:o(log(n))
#link:https://leetcode.com/problems/merge-sorted-arra
class Solution:
    def merge(self, nums1, m, nums2, n) :
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] =  nums2
        nums1.sort()
        
