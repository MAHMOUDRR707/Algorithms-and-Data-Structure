#link :  https://codeforces.com/contest/716/problem/A
#time: o(n)

n , m =  map(int, input().split())
z =  list(map(int,input().split()))
x = 1 
for i in range(1,n):
    if z[i]-z[i-1] <= m :
        x+=1
    else:
        x = 1


print(x)
