#link : https://codeforces.com/contest/439/problem/A
#time :o(n)

n,m =  map(int,input().split())
z = list(map(int,input().split()))
s = 0
x = 0
for i in range(n):
    s+=  z[i]
    


if s +(n-1)*10<=  m :
    x =  m-s
    x =  x //5 
    print(x)
else :
    print(-1)
