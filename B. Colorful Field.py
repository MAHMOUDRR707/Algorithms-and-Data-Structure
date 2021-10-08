#problem link :  https://codeforces.com/contest/79/problem/B
#time : o(n**2)

n,m,x,y =  map(int,input().split())
z = [[0 for i in range(m)] for j in range(n)]

for i in range(x):
    a,b =  map(int,input().split())
    z[a-1][b-1] = "Waste"
v = 0 
for i in range(n) :
    for j in range(m):
        if v == 3:
            v = 0
        if z[i][j] == "Waste":
            continue
        else :
            if v == 0 :
                z[i][j] = "Carrots"
            elif v == 1 :
                z[i][j] = "Kiwis"
            elif v == 2 :
                z[i][j] = "Grapes"
            v+=1
            
            
for i in range(y):
    a,b  =  map(int,input().split())
    print(z[a-1][b-1])
