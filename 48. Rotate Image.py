#link:https://leetcode.com/problems/rotate-image/
#time:o(1)
import numpy as np
class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix =  np.array(matrix)
        matrix = matrix[::-1]
        matrix = matrix.transpose()
        matrix = matrix.tolist()
        print(matrix)

