#link  :  https://codeforces.com/contest/614/problem/A
#time :  o(logk(n))

n,m,k = map(int,input().split())
z = []
x = 1
while x< n :
    x *=  k

while x<=  m  :
    z.append(x)
    x *= k

if z ==[] :
    print(-1)
else :
    print(*z)
