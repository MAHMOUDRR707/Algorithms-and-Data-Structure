#link : https://codeforces.com/contest/439/problem/B
#time : o(n)
n,m = map(int,input().split())
z =  list(map(int,input().split()))
z = sorted(z)
s = 0
for i in z :
    s  +=  m* i
    if m == 1 :
        continue
    else :
        m-=1
print(s)
