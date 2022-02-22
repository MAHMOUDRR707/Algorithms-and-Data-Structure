#link: https://codeforces.com/contest/1635/problem/B
#time:o(n)
n =  int(input())
for _ in range(n):
    m =  int(input())
    z =  list(map(int,input().split()))
    x = 0
    for i in range(1,m-1):
        if z[i] > z[i-1]  and z[i] > z[i+1] :
            x +=1 
            z[i+1] =  z[i]
            if i !=  m-2  :
                z[i+1] =  max(z[i+1],z[i+2])
    print(x)
    print(*z)
