#link : https://codeforces.com/contest/365/problem/A
#time :  o(n)

n,m =  map(int,input().split())
y = 0
z = [i  for i in range(m+1)]
for i in range(n):
    x =  set(input())
    v = 0
    for j in x :
        if int(j) in z :
            v+=1
    if v ==  m+1 :
        y+=1
print(y)
    
