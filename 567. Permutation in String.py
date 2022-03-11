#link:https://leetcode.com/problems/permutation-in-string/
#time: o(n)
import re
class Solution:
    def checkInclusion(self, s1, s2):
        n =  len(s1)
        m = len(s2)
        z ={}
        for i in s1 :
            if i in z.keys():
                z[i] += 1
            else :
                z[i] = 1
                
        for i in range(m):
            if s2[i] in z:
                z[s2[i]] -= 1
            if i >= n and s2[i-n] in z :
                z[s2[i-n]]  += 1
            
            if all([z[x] == 0 for x in z ])  :
                return True
                
        return False

"""
import re
class Solution:
    def checkInclusion(self, s1, s2):
        n =  len(s1)
        m = len(s2)
        x = 0
        for i in range(m):
            if s2[i] in s1:
                for j in range(n):
                    if s2[i+j] in s1 :
                        x += 1
                if x == n :
                    return True
                else :
                    x = 0
        return False
"""
