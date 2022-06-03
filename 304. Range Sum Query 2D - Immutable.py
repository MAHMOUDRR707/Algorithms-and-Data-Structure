# 304. Range Sum Query 2D - Immutable
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix  =  matrix
        self.z = matrix
        n = len(matrix)
        m =  len(matrix[0])
        for i in range(n):
            for j in range(1,m):
                self.z[i][j] += self.z[i][j-1]
        print(self.z)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        x =  0
        i =  row1 
        while i <=  row2 :
            if col1-1 >=  0 :
                x += self.z[i][col2] - self.z[i][col1-1]  
            else :
                x+= self.z[i][col2]
            i+=1
        return(x)
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
