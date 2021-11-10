#problem link : https://codeforces.com/contest/1607/problem/C
#time : o(n)

n = int(input())
for i in range(n):
    m =  int(input())
    x = list(map(int,input().split()))
    x = sorted(x)
    if m == 1 :
        print(x[0])
 
    else :
        z =  x[0]
        for i in range(1,m):
               z =  max(z,x[i] -x[i-1])
        print(z)
            
