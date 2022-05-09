class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        z ={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res = []
        n = len(digits)
        if n == 0:
            return res
        def help(x,dig):
            if x ==  n :
                res.append(dig)
                return 
            
            for i in z[digits[x]]:
                help(x+1,dig+i)
            
        help(0,'')
        return res
