#link: https://leetcode.com/problems/reshape-the-matrix/
#time:o(1)
import numpy as np
class Solution:
    def matrixReshape(self, mat, r, c):
        mat =  np.array(mat)
        n,m =  np.shape(mat)
        if n*m  !=  r*c :
            mat = mat.tolist()
            return mat
        mat =  np.reshape(mat,(r,c))
        mat = mat.tolist()
        return (mat)

## Another solution

class Solution:
    def matrixReshape(self, mat, r, c):
        n,m =  len(mat),len(mat[0])
        if n*m  != r*c :
            return mat
        z =[j for i in mat for j in i]
        x =[]
        for i in range(r):
            y =[]
            for j in range(c):
                y.append(z.pop(0))
            x.append(y)
        return x
