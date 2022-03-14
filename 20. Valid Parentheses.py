#link:https://leetcode.com/problems/valid-parentheses/
#time :o(n)
class Solution:
    def isValid(self, s) :
        z = [] 
        n =  len(s)
        x =  {'(':')','[':']','{':'}'}

        for i  in range(n):
            if s[i]  in x :
                z.append(s[i])
            else :
                if z == [] or x[z.pop()] != s[i]:
                    
                    return False
        if z != []:
            return False
        return True
