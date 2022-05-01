class Solution:
    def combinationSum(self, nums: List[int], target: int) :
        
        start = 0 
        z = []
        rest = target
        ans = []
        n = len(nums)
        def dfs(start,z,rest):
            if rest == 0 :
                ans.append(z[:])
                return
            
            for i in range(start,n):
                x =  nums[i]
                val =  rest - x 
                if val >=0 :
                    dfs(i,z+[x],val)
            
        dfs(0,z,rest)
        return ans
