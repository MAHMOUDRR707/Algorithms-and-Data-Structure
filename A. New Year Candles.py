#link :  https://codeforces.com/problemset/problem/379/A
# time :  o(n)
x, y =  map(int,input().split())
z = 0
while(x >= y ):
    z+= y
    x -= y
    x+=1
print(z+x)
