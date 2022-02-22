#link :https://codeforces.com/contest/1635/problem/A
#time :o(n)
n = int(input())
for i in range(n):
    m = int(input())
    z  = list(map(int,input().split()))
    x  =0 
    for j in range(m):
        x |=  z[j]
    print(x)
