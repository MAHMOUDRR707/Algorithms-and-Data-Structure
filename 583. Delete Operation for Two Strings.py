class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n =  len(word2)
        m =  len(word1)
        z = [[0  for i in range(n+1)]for j in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1] :
                    z[i][j] = z[i-1][j-1] +1 
                else :
                     z[i][j] = max(z[i][j-1] , z[i-1][j])
        return(n+m - 2 *z[-1][-1])
    
