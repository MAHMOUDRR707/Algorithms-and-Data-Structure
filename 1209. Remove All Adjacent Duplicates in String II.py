class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        x = ''
        a  = [["lol",0]]
        for i in s  :
            if i == a[-1][0] :
                a[-1][1] +=1
                if a[-1][1] >= k : 
                    while  i == a[-1][0] :
                        a.pop()
            else :
                n = len(a)
                a.insert(n,[i,1])
                    
        n = len(a)
        print(a)
        for i in range(1,n):
            x+=a[i][0] *a[i][1]
        return x
