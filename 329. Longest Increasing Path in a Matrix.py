class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix ) == 0  :
            return  0
        longestpath = 0 
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        n = len(matrix)
        m = len(matrix[0])
        cashe = [[0 for i in range(m)] for i in range(n)]
        
        def longestFunction(matrix,cashe,n,m,i,j):
            if cashe[i][j] > 0 :
                return cashe[i][j]
            maxmuim = 0 
            for k in directions :
                x = i +  k[0]
                y = j + k[1]
                if  x < n and y < m  and x > -1 and y > -1   and matrix[x][y] > matrix[i][j]:
                    longest =  longestFunction(matrix,cashe,n,m,x,y)
                    maxmuim = max(longest, maxmuim)
            cashe[i][j] =  maxmuim +1 
            return cashe[i][j]
                    
        for i in range(n):
            for j in range(m):
                longest =  longestFunction(matrix,cashe ,n,m,i,j)
                longestpath =  max(longest,longestpath)
        return longestpath
