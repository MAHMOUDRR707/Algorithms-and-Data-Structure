#problem link :  https://codeforces.com/contest/371/problem/B
#time : o(log(n))

n ,m =  map(int,input().split())
x = 0
a,b,c = 0,0,0
d,e,f = 0,0,0

if n%2 == 0 or m%2 ==0 :
     
     while n%2 == 0 :
        n = int(n/2)
        a+=1
     while m%2 == 0 :
        m = int(m/2)
        d+=1

        
if n%3 == 0 or m%3 == 0:
     x+=1
     while n%3 == 0 :
                n = int(n/3)

                b+=1

     while m%3 == 0 :
                m = int(m/3)
                e+=1

        
if n%5 == 0 or m%5 == 0:
     x+=1
     while n%5 == 0 :
                n = int(n/5)

                c+=1

     while m%5 == 0 :
                m = int(m/5)

                f+=1

if  n == m:
 x =  abs(a-d) + abs(b-e) + abs(f-c)
 print(x)
else :
    print(-1)
        
