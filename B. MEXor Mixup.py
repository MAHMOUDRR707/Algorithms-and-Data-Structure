#link : https://codeforces.com/contest/1567/problem/B
#time :o(1)
t  = int(input())
for i in range(t):
    x,y =  map(int,input().split())
    z = 0
    
    if x%4 == 1:
        z = x-1
    elif x%4 == 2 :
        z = 1
    elif x%4 == 3 :
        z = x
    else :
        z = 0


    if z == y  :
        print(x)
    elif (z^y) !=  x:
        print(x+1)
    else :
        print(x+2)
