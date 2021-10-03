#problem link : https://codeforces.com/contest/16/problem/B
#time :  o(n)
a,b = map(int,input().split())
z={}
for i in range(b):
    x,y = map(int,input().split())
    z[x] = y 
z = {k: v for k, v in sorted(z.items(), key=lambda item: item[1], reverse =  True)}
m = 0
n= a
for i,j in z.items() :
    m +=  min(n,i)*j
    n -= min(n,i)
    
print(m)
    
    
