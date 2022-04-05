#link : https://leetcode.com/problems/pascals-triangle-ii/submissions/#link:

#time:o(n**2)

class Solution:
    def getRow(self, r) :
        z = [[1],[1,1]]
        if r < 2  :
            return z [r]
        
        for i in range(2,r+1):
            x =  [1]*(i+1)
            z.append(x)
            for j in range(1,i):
                z[i][j] = (z[i-1][j] +z[i-1][j-1])
        
        return z[-1]
