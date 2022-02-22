#link : https://codeforces.com/contest/1637/problem/B
#time:o(n)
t = int(input())
for i in range(t):
    n =  int(input())
    z =  list(map(int,input().split()))
    x = 0
    for i in range(n):
        if z[i] ==0 :
          x+=  2  * (n-i) * (i+1)
        else :
            x+=  (n-i) * (i+1)
    print(x)
