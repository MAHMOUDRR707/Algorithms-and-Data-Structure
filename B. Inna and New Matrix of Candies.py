#problem link : https://codeforces.com/contest/400/problem/B
#time : o(n)
m,n = map(int,input().split())
z = [["" for j in range(n)] for i in range(m)]

for i in range(m) :
    x =  list(input())
    z[i] =  x
x = set()
y = False
for i in range(m):
    if z[i].index('G') > z[i].index( "S"):
        y =  True
    else :
        x.add(z[i].index('S') - z[i].index( "G"))

if y :
    print(-1)
else :
    print(len(x))
