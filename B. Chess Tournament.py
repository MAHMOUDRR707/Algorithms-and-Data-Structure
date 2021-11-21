#link :  https://codeforces.com/contest/1569/problem/B
#time : o(n**2)
n =  int(input())
for i in range(n):
    m =  int(input())
    x =  input()
    if x.count("2") == 2 or  x.count("2") == 1 :
        print("NO")
    else :
     print("YES")
     y = []
     v =  [["" for _ in range(m)]for _ in range(m)]
     b = 0
     
     for j in range(m):
        v[j][j] = "X"
        if x[j] == "2" :
            b+=1
            y.append(j)

   
     for k in range(b):
         c = y[k]
         z = y[(k+1)%b]
         v[c][z] = "+"
         v[z][c] = "-"
         
     for j in range(m):
       for k in range(m) :
        if  v[j][k] == "":
           v[j][k] = "="
        
        print(v[j][k],end = "")
       print("")
            
