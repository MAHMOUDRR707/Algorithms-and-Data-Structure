#link :  https://codeforces.com/contest/90/problem/B
#time : o(n**2)


n,m =  map(int,input().split())
z = [ ["" for i in range(m)] for j in range(n)]
col = [ [] for j in range(n)]
row = []
for i in range(n) :
    x = list(input())
    row.append(x)
    for j in range(m) :
        z[i][j] =  x[j]
        col[j].append(x[j])

x =[]
for i in range(n):
    for j in range(m):
        y =  z[i][j]
        if row[i].count(y) == 1 and col[j].count(y) == 1 :
            print(y,end ="")


        
