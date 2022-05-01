class Solution:
    def removeDuplicates(self, nums: List[int]):
        x = 0 
        n =  len(nums)
        z =[]
        m =  n-1
        i = 0
        while i <n :
            print(nums,n,i)
            if nums[i] not in z :
                z.append(nums[i])
                x +=1
                i += 1
            else :
                nums.pop(i)
                n -=1
                
                
        #another solution
        for j in range(n):
            
            if nums[i] !=  nums[j] :
                i+=1
                nums[i] =  nums[j]
           
           
        
        return i+1
