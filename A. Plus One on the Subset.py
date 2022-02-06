#link  :  https://codeforces.com/contest/1624/problem/A
#time : o(1)
n =  int(input())
for i in range(n):
    m =  int(input())
    z =  list(map(int,input().split()))
    x,y = min(z),max(z)
    print(y-x)
