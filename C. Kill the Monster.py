#link : https://codeforces.com/contest/1633/problem/C
#time :  O(n)
import math as mt 
t =  int(input())
v = 0
for i in range(t):
    Hc,Dc =  map(int,input().split())
    Hm,Dm =  map(int,input().split())
    k,w,a =  map(int,input().split())
    for j in range(k+1):
        x = Hc +a*j
        y = Dc + w*(k-j)
        if mt.ceil(x/Dm) >= mt.ceil(Hm/y):
            v +=1
            break
        
  
    if v == 0 :
     print('NO')
    else :
     print('YES')
    v =0
    
          
    
