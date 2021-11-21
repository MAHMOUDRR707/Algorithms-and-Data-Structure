#link : https://codeforces.com/contest/1569/problem/A
#time:o(n)
t =  int(input())
for i in range(t):
    n =  int(input())
    z =  list(input())
    l,r = -1,-1
    for j in range(n-1) :
        if z[j] != z[j+1] :
            l = j+1
            r = j+2
    print(l,r)
