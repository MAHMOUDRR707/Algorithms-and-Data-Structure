class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        x =  1 << k
        z  = set()
        #print(x)
        for i in range(k,n+1):
            y =  s[i-k:i]
            if y not in z :
                z.add(y)
                x -= 1 
                #print(z,x)
                if x == 0 :
                    return True
