class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        x =  sorted(nums)
        if x == nums :
            return  0
        n =  len(nums)
        i,j = -1,-1
        start = 0
        end  = n-1
        while  (i == -1 or j == -1):
            
            if x[start] != nums[start] and i == -1:
                    i = start
                    print(i)
            if x[end] != nums[end] and j == -1:
                    j = end
            
            start +=1 
            end -=1
        print(i,j)
        return j-i+1
