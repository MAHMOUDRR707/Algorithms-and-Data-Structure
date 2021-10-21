#problem  link : https://codeforces.com/contest/699/problem/B
#time : o(n**2)
n,m =  map(int,input().split())
x = []
y = []
A = [[0 for i in range(m)]for j in range(n)]
z = 0
total = 0
for i in range(n) :
    v =  input()
    total +=  v.count("*")
    x.append(v.count("*"))
    for j in  range(m) :
     A[i][j] = v[j]
     
for j in range(m):
    mm = 0
    for i in range(n) :
        if A[i][j] == "*" :
            mm+= 1
    y.append(mm)

b = ""
def pro(n,m,A,x,y):
 for i in range(n):
  for j in range(m):
    z =  x[i] +y[j]
    if A[i][j] == "*":
        z-=1
    if z ==  total :
        b = "YES"
        i,j = i+1,j+1
        print(b)
        print(i,j)
        return
 print("NO")
pro(n,m,A,x,y)
        

