class Solution:
    def longestValidParentheses(self, s: str) -> int:
        x = 0
        max_x = 0
        stack = [-1]
        n = len(s)
        for j in range(n) :
            i = s[j]
            if i == "(":
                stack.insert(0,j)
            else :
                stack.pop(0)
                if   not stack :
                    stack.insert(0,j)
                else :
                    x = j-stack[0]
                    print(x)
                    max_x =  max(max_x,x)
        
        return max_x
