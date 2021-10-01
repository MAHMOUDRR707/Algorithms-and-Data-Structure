#problem link :  https://codeforces.com/contest/268/problem/A
#time: o(n)
n =  int(input())
x,y = [],[]
for i in range(n):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)
z= 0
for i in range(n):
    if x[i] in y :
        z+= y.count(x[i])
print(z)
