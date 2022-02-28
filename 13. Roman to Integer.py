#link : https://leetcode.com/problems/roman-to-integer/
#time :o(n)
class Solution:
    def romanToInt(self, s) :
        d = 0
        z= {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'DM':-1000,'CD':-200,'CM':-200,'XC':-20,'IV':-2,'IX':-2,'XL':-20,'VX':-10}
        for i,j  in z.items():
            x =  s.count(i)
            d += x*j
        return d

z =  input()
s =  solution(z)
print(s)
