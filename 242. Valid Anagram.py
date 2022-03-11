#linlk:https://leetcode.com/problems/valid-anagram/
#time:o(n)
class Solution:
    def isAnagram(self,s, t):
        if len(s) !=  len(t):
            return False
        z = {}
        for i in  s :
            if i in z.keys():
                z[i] +=1 
            else :
                z[i] = 1 
        for i in t :
            if i not in z.keys() :
                return False
            if z[i] <= 0 :
                return False
            else :
                z[i] -= 1 
        return True
