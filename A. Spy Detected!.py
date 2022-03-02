# link :https://codeforces.com/contest/1645/problem/A
#time: o(nlog(n))
t = int(input())
for i in range(t):
    n =  int(input())
    z =list(map(int,input().split()))
    y =z
    b = sorted(z,key = lambda x:z.count(x))
    print(y.index(b[0])+1)
