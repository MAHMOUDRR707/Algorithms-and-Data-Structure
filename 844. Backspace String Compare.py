#time :o(n)
#link: https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) :
        x,y = [],[]
        for i in range(0,len(s)):
            if s[i] == '#'  and x:
                x.pop()
            else :
                if s[i].isalpha():
                    x.append(s[i])
        

        for j in range(len(t)):
            if t[j] == '#' and y:
                y.pop()
            else :
                if t[j].isalpha():
                    y.append(t[j])
        print(x,y)
        if x == y :
            return True
        return False
