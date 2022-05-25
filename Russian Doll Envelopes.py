class Solution:
    def maxEnvelopes(self, envelops: List[List[int]]) -> int:
        #envelops = [[i,j] for i,j in sorted(envelops, key = lambda item:[item[0],-item[1]])]
        #n = len(envelops)
        #dp = [1 for i in range(n+1)]
        #max_ = 1 
        #for i in range(n+1):
            #for j in range(i+1):
                
          #      if  envelops[i-1][0] > envelops[j-1][0] and envelops[i-1][1] > envelops[j-1][1] and dp[i] < dp[j] +1 :
           #         dp[i] =  dp[j] + 1
         #           max_ = max(max_,dp[i])
        #print(dp)
        #return (max_)
        envelops = [[i,j] for i,j in sorted(envelops, key = lambda item:[item[0],-item[1]])]
        res =  []
        
        for i ,j in enumerate(envelops):
            x = bisect_left(res,j[1])
            if x ==  len(res):
                res.append(j[1])
            else :
                res[x] =  j[1]
        return len(res)
