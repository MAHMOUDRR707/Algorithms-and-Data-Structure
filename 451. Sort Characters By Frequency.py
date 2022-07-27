class Solution:
    def frequencySort(self, s: str) -> str:
        res = {}
        for i in s :
            if i in res :
                res[i] +=1 
            else :
                res[i] = 1 
        
        res=  dict(sorted(res.items(),key =  lambda x:x[0]))
        res=  dict(sorted(res.items(),key =  lambda x:x[1],reverse = True))
        x = ""
        for i,j in res.items() :
            x += (i)*j
        return x
