#link:https://leetcode.com/problems/ransom-note/
#time:o(n)
class Solution:
    def canConstruct(self, ransomNote, magazine) :
        z = {}
        for i in  magazine :
            if i in z.keys():
                z[i] +=1 
            else :
                z[i] = 1 
        for i in ransomNote :
            if i not in z.keys() :
                return False
            if z[i] <= 0 :
                return False
            else :
                z[i] -= 1 
        return True
