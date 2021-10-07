#problem link :https://codeforces.com/contest/810/problem/B
#time: o(n)
n,m =  map(int,input().split())
x = 0
y =[]
for i in range(n):
    k,l =   list(map(int,input().split()))
    x+=min(k,l)
    y.append((min(2*k,l)-min(k,l)))
y.sort(reverse =  True)
for i in range(m) :
    x+=y[i]
print(x)
      
    
