#link:https://codeforces.com/contest/1638/problem/A
#time: o(n)
n = int(input())
for _ in range(n):
    m =  int(input())
    z = list(map(int,input().split()))
    x = []
    for i in range(m):
        if z[i] != i+1 :
            for j in range(i+1,m):
                if z[j] ==  i+1 :
                    break
            x =  z[i:j+1]
            z[i:j+1] = x[::-1]
            break
    print(*z)
            
