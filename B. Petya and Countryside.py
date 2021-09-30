#problem link : https://codeforces.com/contest/66/problem/B
#time :  O(n**2)
n =  int(input())
z=  list(map(int,input().split()))
up , down , max_z = 0,0,1
s = 1
for i in  range(n):
    down ,  up = i,i
    s = 1
    while down > 0  and z[down] >=  z[down-1] :
        s+=1
        down-=1
    while up < n-1 and z[up] >=  z[up+1] :
        s+=1
        up+=1
    max_z =  max(s,max_z)
print(max_z)
