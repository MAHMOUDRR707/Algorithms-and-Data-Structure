#problem link : https://codeforces.com/contest/289/problem/A
#time :  o(n)
n,m =  map(int,input().split())
z =set()
for i in range(n):
    a,b =  map(int,input().split())
    for j in range(a,b+1):
        z.add(j)


l  = len(z)
if l > m and l%m !=  0 :
    x =  l%m
    print(m-x)
elif l>=m  and l%m == 0 :
    print(0)
else :
    print(m-l)
