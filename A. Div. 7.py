#time :  o(n)
#link : https://codeforces.com/contest/1633/problem/A
n =  int(input())
for i in range(n):
    x = int(input())
    if x%7 == 0 :
        print(x)
    else :
        x = x -  x%10
        while (x%7 !=0) :
             x+=1
        print(x)
