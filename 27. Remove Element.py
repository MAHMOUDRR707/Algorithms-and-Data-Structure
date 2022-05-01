class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        x = 0
        res =[]
        m =  n-1
        def swap(index,m):
            nums[index],  nums[m] = nums[m] , nums[index]
        
        z =  nums.count(val)
        for i in range(n-z):
            if nums[i] == val:
                while nums[m] == val :
                    m-=1
                swap(i,m)
            
            x+=1
            
        return x
