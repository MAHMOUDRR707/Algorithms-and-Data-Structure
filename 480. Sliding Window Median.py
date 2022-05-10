class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        n = len(nums)
        x = []
        med = k//2
        for i in range(n-k+1):
            z =  nums[i:i+k]
            z.sort()
            if k%2 == 0 :    
                x.append((z[med]+z[med-1])/2)
            else :
                x.append(z[med])
        return x
