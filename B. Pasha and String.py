#link:https://codeforces.com/contest/525/problem/B
#time:o(n)
z =  list(input())
n = len(z)
a =  int(input())
b =  list(map(int,input().split()))
for i in range(a):
    x = b[i]
    y =  n - b[i]+1
    v = z[x-1:y]
    z[x-1:y] = v[::-1]
    
for i in z :
    print(i,end='')
