class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        z =  set()
        y = 0 
        l = 0
        max_ = -100000000000000
        for i in range(n):
            x =  nums[i]
            if x  in z :
                max_ =  max(max_,y)
                for j in range(l,i):
                    if x != nums[j]:
                        y -= nums[j]
                        z.remove(nums[j])
                    else :
                        l =  j+1
                        break
            else :
                z.add(x)
                y+=x
        return (max(y,max_))
