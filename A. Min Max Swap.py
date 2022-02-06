#time : o(n)
#link : https://codeforces.com/contest/1631/problem/A
n =  int(input())
for _ in  range(n):
    x =  int(input())
    a =  list(map(int,input().split()))
    b =  list(map(int,input().split()))
    y = 0
    for i in range(x):
        if a[i] < b[i] :
            y = b[i]
            b[i] = a[i]
            a[i] = y
            
    print(max(a)*max(b))
