#link :https://leetcode.com/problems/pascals-triangle/
#time: o(n**2)
class Solution:
    def generate(self, n) :
        z =[]
        for i in range(n):
            x =[1] * (i+1)
            z.append(x)
            for j in range(1,len(z[i])-1):
                z[i][j] = (z[i-1][j]+ z[i-1][j-1])
        return z
