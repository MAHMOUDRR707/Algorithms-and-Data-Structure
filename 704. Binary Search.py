#link:https://leetcode.com/problems/binary-search/submissions/
#time:o(log(n))
class Solution:
    def search(self, nums, target) :
        mid =  len(nums)//2
        x =  nums[mid]         
        if x == target : 
           return mid
        elif target < x :
            y = self.left_search(nums[:mid],target)
            
            if y is not None :
              return y
            else : 
                return -1
        else :
           y = self.right_search(nums[mid:],target)
           if y is not None:
              return y+mid
           else : 
                return -1
    
    def left_search(self,nums,target):
        y = 0
        for i in range(len(nums)):
            if nums[i] ==  target :
                y = i 
                return y
    
    def right_search(self,nums,target):
        y = 0
        for i in range(len(nums)):
            if nums[i] ==  target :
                y = i 
                return y
    
