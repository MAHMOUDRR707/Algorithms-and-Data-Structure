class Solution:
    def maxOperations(self, nums: List[int], k: int):
        z =  []
        x = 0
        n =  len(nums)
        i = 0
        left = 0 
        right = n-1
        nums.sort()
        while left < right :   
            y  =  nums[left] + nums[right]
            if  y == k :
                x+=1
                left +=1 
                right -=1
            if y >k :
                right -=1
            if  y < k :
                left += 1
        ##another solution
        for i in range(n):
            if nums[i] > k :
                break
            y = k- nums[i]
            for j in range(i+1,n) :
                if nums[j] == y :
                    if i not in z  and j not in z  and i != j:
                        z.append(i)
                        z.append(j)
                        x += 1 
                        break             
        return x
