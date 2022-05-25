from itertools import permutations

class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0 :
            return 0
        x =  False
        if num < 0 :
            x = True
        num =  str(num)
       
        if x:
            num =  num[1:]
            num = "".join(sorted(num,reverse =  True))
            num = - int(num)
            return num
        num = (sorted(num))
        #print(num)
        x =  num.count("0")
        y = num.pop(x)
        num.insert(0,y)
    
        num =  "".join(num)
        return int(num)
