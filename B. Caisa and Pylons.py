#problem link : https://codeforces.com/contest/463/problem/B
# time : o(n)
n = int(input())
z = list(map(int,input().split()))
dol = 0
cur  = 0
for i in range(n) :
    if z[i] > cur:
    
      dol +=  abs(z[i]-cur)
      cur =  z[i]
     
print(dol)
