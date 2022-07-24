class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num = list(set(nums))
        #num.sort(key =  lambda x: nums.count(x),reverse = True)
        res = {}
        for i in nums :
            if i in  res :
                res[i] += 1
            else :
                res[i] = 1 
                
        res  = dict(sorted(res.items(),key =  lambda x :x[1],reverse = True))
        return list(res.keys())[:k]
