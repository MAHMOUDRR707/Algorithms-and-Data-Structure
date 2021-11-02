#problem  link : https://codeforces.com/contest/376/problem/B
#time : o(n)
n,m  = map(int,input().split())

z = {str(i+1):0 for i in range(n)}
y = {str(i+1):0 for i in range(n)}
x  =0
for i in range(m):
    a,b,c =  map(int,input().split())
    z[str(a)] += c
    y[str(b)] += c
for i in range(n):
    if z[str(i+1)] < y[str(1+i)]:
        x+= ( y[str(1+i)] - z[str(1+i)])

print(x)
