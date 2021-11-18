#link  : https://codeforces.com/contest/1557/problem/B
#time:o(n)
t  = int(input())
for i in range(t):
    n,m = map(int,input().split())
    z =  list(map(int,input().split()))
    zz  = sorted(z)
    y = {}
    x= 1
    yy = {}
    for j in range(n):
        y[z[j]] = j
    for j in range(n):
        yy[zz[j]] = j
    for j in range(n-1):
        if y[zz[j]]+1 != y[zz[j+1]] :
            x+=1
    if x <=  m :
        print("YES")
    else :
        print("NO")
