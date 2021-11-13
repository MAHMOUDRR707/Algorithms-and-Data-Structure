#link  : https://codeforces.com/contest/1605/problem/A
#time : o(1)

n = int(input())
for i in range(n):
     a,b,c =  map(int,input().split())
     if (a+b+c)%3 :
         print(1)
     else :
         print(0)
     
     
