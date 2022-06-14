class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n =  len(text1)
        m = len(text2)
        z = [[0 for i in range(n+1)] for i  in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[j-1] == text2[i-1] :
                    z[i][j] =  z[i-1][j-1] +1 
                else :
                    z[i][j] =  max(z[i][j-1],z[i-1][j])
        return z[-1][-1]
