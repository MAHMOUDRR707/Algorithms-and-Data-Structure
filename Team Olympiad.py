#problem link: https://codeforces.com/problemset/problem/490/A
#time :  O()

n = int(input())
x = list(map(int,input().split()))
m = {1:[],2:[],3:[]}
for i  in range(n):
    if x[i] == 1 :
        m[1].append(i+1)
    if x[i] == 2 :
        m[2].append(i+1)
    elif x[i] == 3  :
        m[3].append(i+1)

z =[]
if x.count(1) == 0 or  x.count(2) == 0 or x.count(3) ==0:
    print(0)
else :
   y =  min(x.count(1), x.count(2), x.count(3))
   print(y)
   for i in range(y):
       d = []
       d.append(m[1][i])
       d.append(m[2][i])
       d.append(m[3][i])
       z.append(d)
   for i in range(y):
       print(*z[i])
       
   
               
           
       
       
