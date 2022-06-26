class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        z = []
        n = len(nums1)
        m =  len(nums2)
        for i in range(n) :
            index =  nums2.index(nums1[i])
            x = 0
            for j in range(index,m):
                if nums2[j] > nums1[i] :
                    z.append(nums2[j])
                    x= 1 
                    break
            if x != 1 :
                z.append(-1)
        print(z)
                    
        return (z)
