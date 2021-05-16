#problem link : https://codeforces.com/contest/1520/problem/B
n =  int(input())
for i in range(n):
    z = [1,2,3,4,5,6,7,8,9]
    m =  int(input())
    if m <10 :
        print(m)
    else :
      for  j in range(10,m+1):
        y =  str(j)
        if len(y)%2 != 0:
          if y[:len(y)//2+1] == y[len(y)//2:]:
            z.append(j)
        else:
         if y[:len(y)//2] == y[len(y)//2:]:
            z.append(j)

      print(len(z))
        
