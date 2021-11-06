# link : https://codeforces.com/contest/165/problem/A
#time : o(n**2)
n = int(input())
z = []
s = 0
for i in range(n):
    x,y =  map(int,input().split())
    z.append((x,y))

for i in range(n):
    x,y  =  z[i]
    left = 0
    right = 0
    up = 0
    down = 0
    for j in range(n):
        if z[j] == z[i] :
            continue
        c1,c2 =  z[j]
        if c1 ==  x  and y >c2  :
            down = 1
        elif c1 ==  x  and y <c2  :
            up = 1
             
        elif c1 >  x  and y ==c2  :
            right = 1
        elif c1 <  x  and y ==c2  :
            left = 1
    if left and right and down and up :
        s+=1
print(s)
