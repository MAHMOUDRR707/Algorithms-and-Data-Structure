#time : o(n)
#link : https://codeforces.com/contest/227/problem/B
n = int(input())
x = list(map(int,input().split()))
m =  int(input())
y =  list(map(int,input().split()))
f = 0
s = 0
for i in range(m):
    f += (x.index(y[i])+1)
x =  x[::-1]

for i in range(m):
    s+= (x.index(y[i])+1)
print(f,s)
