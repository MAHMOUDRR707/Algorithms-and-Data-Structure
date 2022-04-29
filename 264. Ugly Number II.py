class Solution:
    def nthUglyNumber(self, n: int) -> int:
        x1,x2,x3 = 0,0,0
        ugly = 0
        z =[1]
        for i in range(n-1):
            ugly =  min(z[x1]*2,z[x2]*3,z[x3]*5)
            z.append(ugly)
            if ugly == z[x1] * 2 :
                x1 +=1
            if ugly == z[x2] * 3 :
                x2 +=1
            if ugly == z[x3] * 5 :
                x3 +=1 
        return z[-1]
