#problem link : https://codeforces.com/contest/445/problem/A
#time : o(n**2)

n,m =  map(int,input().split())
z = []
for i in range(n):
    z.append(list(input()))
x = 0
for i in range(n):
    for j in range(m):
        if z[i][j] == "." :
         if (i+j)%2 == 0 :
            z[i][j] = "W"
         else:
            z[i][j] = "B"
x = ""
for i in range(n):
    for j in range(m):
        x += z[i][j]
    print(x)
    x = "" 
