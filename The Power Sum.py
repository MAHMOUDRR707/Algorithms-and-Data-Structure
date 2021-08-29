#problem link : https://www.hackerrank.com/challenges/the-power-sum/problem
import math as mt

def powerSum(X, N):
    # Write your code here
    y =  int(mt.pow(X,1/N))
    z= [1]+[0]*X
    for i in range(1,y+1):
        s = i**N
        for j in range(X,s-1,-1):
            z[j] += z[j-s]
    print(z)
    return z[-1]



X = int(input().strip())

N = int(input().strip())

result = powerSum(X, N)

print(result)
