#time : o(n)
# link : https://codeforces.com/contest/1237/problem/B

n = int(input())
z= list(map(int,input().split()))
y= list(map(int,input().split()))
m = -1
yy =[0]*n
zz=[0]*n
x = 0
for i in  range(n):
    
    yy[y[i]-1] = i
for i in range(n):
    zz[i] = yy[z[i]-1]
for i in range(n) :
    if zz[i] > m :
        m =  zz[i]
    else :
        x+=1
print(x)
