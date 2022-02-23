#link: https://codeforces.com/contest/278/problem/A
#time:o(1)
n =  int(input())
z =  list(map(int,input().split()))
l =  list(map(int,input().split()))
s,t = min(l),max(l)
x = sum(z[s-1:t-1])
y =  (sum(z[:s-1]) + sum(z[t-1:]))
print(min(x,y))
