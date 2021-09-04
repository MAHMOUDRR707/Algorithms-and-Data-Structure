#problem link : https://codeforces.com/problemset/problem/158/B


import math as mt 
n = int(input())
z =  list(map(int,input().split()))
x = z.count(4)
x_2 =  z.count(2)
if x_2 %2 == 0 :
    x+=x_2//2
else :
    x+=(x_2//2)
    x_2 = 1
x_3 = z.count(3)
x_1 =  z.count(1)
if x_1 == x_3 :
    x+=x_3
elif x_3 > x_1 :
    x+=x_3
    if x_1 ==1 and x_2:
        x+= 1
    else :
        x+=(mt.ceil(x_1/4))
print(x)
        
    
