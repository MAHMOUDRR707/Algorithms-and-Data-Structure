class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        z =  [[0 for i in range(n)] for i in range(m)]
        
        z[0][0] =  1
        
        for i in range(1,n):
            z[0][i] = 1
        for i in range(1,m):
            z[i][0] = 1 
        #print(z)
        
        for i in range(1,m):
            for j in range(1,n):
                z[i][j] = z[i-1][j] + z[i][j-1]
        print(z)
        
        return z[m-1][n-1]
