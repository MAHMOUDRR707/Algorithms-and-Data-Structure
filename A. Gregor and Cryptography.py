#link : https://codeforces.com/contest/1549/problem/A
#time :o(n)
n =  int(input())
for i in range(n):
    m  = int(input())
    z = []
    x = []
    for j in range(1,m+1):
     y =  m%j
     if y in z:
         print(x[z.index(y)],j)
         break
     else :
        z.append(y)
        x.append(j)
        
