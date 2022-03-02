#link:https://codeforces.com/contest/1641/problem/A
#time: o(nlog(n))
t =  int(input())
for i in range(t):
    n,x =  map(int,input().split())
    z  = (list(map(int,input().split())))
    z.sort()
    v ={(j):z.count(j) for i,j in enumerate(z)}
    y = 0
    for i in (z):
        if v[(i)] != 0 :
            v[(i)] -=1
            if (i * x in z  ) and v[(i*x)] != 0 :
                v[(i*x)] -=1

            else:
                y+=1
    print(y)
