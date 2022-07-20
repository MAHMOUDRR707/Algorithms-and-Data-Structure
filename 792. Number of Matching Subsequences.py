class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        """""
        n =  len(s)
        z=  {}
        for i in range(n):
            if s[i]  not in z :
                z[s[i]] = 1
            else :
                z[s[i]] += 1
        result = 0
        #print(z)
        for i in words :
            x = {}
            res = 0 
            for j in i : 
                if j not  in x :
                    x[j] = 1 
                else :
                    x[j] += 1 
            #print(x)
            for k,j in x.items():
                if k not in z   :
                    res -= 1
                else :
                    if j  > z[k] :
                        res -=1 
                    else :
                        res +=1 
            #print(res)
            if res ==  len(set(i)) :
                result  += 1
        return(result)
                    
        """""
        @lru_cache
        def issequence(word,s):
            if not s :
                return True
            index = 0 
            for i  in range(len(s)):
                if word[index]  ==  s[i] :
                    index += 1
                if index ==  len(word):
                    return True
            return False
        result  =  []
        for j in words :  
            if issequence(j,s):
                result.append(j)
        return (len(result))
                
    
        
