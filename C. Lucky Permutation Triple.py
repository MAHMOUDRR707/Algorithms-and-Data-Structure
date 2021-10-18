#problem  link : https://codeforces.com/contest/304/problem/C
#time : o(n)
n = int(input())
z =  list(range(n))
if n&1 :
    print(*z)
    print(*z)
    for i in range(n):
        print((z[i]+z[i])%n,end = " ")
else :
    print(-1)
