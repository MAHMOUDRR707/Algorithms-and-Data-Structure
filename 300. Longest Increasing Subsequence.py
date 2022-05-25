class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #n = len(nums)
        #num = sorted(list(set(nums)))
        #m = len(num)
        #dp =  [[-1 for i in range(m+1)]for i in range(n+1)]
        
        #for i in range(n+1):
            #for j in range(m+1):
                
              #  if i== 0 or j == 0 :
             #       dp[i][j] = 0 
                    
            #    elif nums[i-1] == num[j-1]:
           #         dp[i][j] = dp[i-1][j-1] + 1
                
          #      else :
         #           dp[i][j] =  max(dp[i][j-1],dp[i-1][j])
                
        #return dp[-1][-1]
        
        n = len(nums)
        dp =  [1 for i in range(n)]
        maxmuim = 1
        for i in range(1,n):
            for j in range(0,i):
                
                if nums[i] >  nums[j] and dp[i] < dp[j] +1  :
                    dp[i] = dp[j] +1 
                    maxmuim =  max(maxmuim, dp[i])
        return (maxmuim)
