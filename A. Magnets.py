#time :  o(1)
#link: https://codeforces.com/problemset/problem/344/A 

n =   int(input())
y =0
z = 0
for i in range(n):
    x =  int(input())
    if y !=  x :
        z+= 1
    y = x
print(z)
