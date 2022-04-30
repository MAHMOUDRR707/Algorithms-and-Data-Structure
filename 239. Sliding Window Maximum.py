class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n =  len(nums)
        result = []
        z = deque()
        for i in range(n) :
            while  z  and  z[0][0]< i-k +1:
                z.popleft()
            while z and z[-1][1] <= nums[i]:
                z.pop()
            z.append((i,nums[i]))
            if i >= k-1 :
                result.append(z[0][1])
           
           # result.append(max(nums[i:i+k]))
        return result
