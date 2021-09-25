#problem link : https://www.hackerrank.com/challenges/larrys-array/problem
#time: O(n**2)

n =  int(input())
for i in range(n):
    x = int(input())
    y =  list(map(int,input().split()))
    z = 0
    for j in range(len(y)):
        for k in range(j+1,len(y)):
            if y[j] > y[k]:
                z+=1
    if  z%2 == 0:
        print("YES")
    else :
        print("NO")
            
