#problem link : https://codeforces.com/contest/253/problem/B
#time : o(n**2)

n =  int(input())
z =  list(map(int,input().split()))
x =  min(z)
y = 0
L =0
z= sorted(z)
for i in range(n):
    while( 2*z[L]<z[i]):
	    L+=1
    y = max(y,i-L+1)
print(n-y)
