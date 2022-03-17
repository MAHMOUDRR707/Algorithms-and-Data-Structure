#link : https://leetcode.com/problems/letter-case-permutation/
#time:o(n*n*m)
from itertools import permutations
class Solution:
    def letterCasePermutation(self, s) :
        n =  len(s) 
        m =  1 << n
        z = []
        x = set()
        s = s.lower()
        for i in range(m):
            z =  [k for k in s]
            for j in range(n):
                if ((i>>j) &1) == 1:
                    z[j] =  s[j].upper()
            temp = ''
            for k in z :
                temp += k
            
            x.add(temp)
        return x
        
