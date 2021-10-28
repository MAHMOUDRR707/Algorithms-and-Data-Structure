#problem link : https://codeforces.com/contest/580/problem/B
#time : o(n**2)

n,m =  map(int,input().split())
z = {}
l,r =0,0
for i in range(n):
    a,b =  map(int,input().split())
    z[i] = [a,b]

x = 0
max_x = 0
z = dict(sorted(z.items(),  key=lambda x: (x[1][0],x[1][1])))


while r<n :
    if  ( abs(z[r][0] - z[l][0]) >= m) :
        max_x = max(x,max_x)
        x-=z[l][1]
        l+=1
    else :
      x += z[r][1]
      r+=1
    max_x = max(x,max_x)

print(max_x)
