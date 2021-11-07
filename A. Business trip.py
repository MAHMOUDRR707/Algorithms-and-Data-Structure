#link : https://codeforces.com/contest/149/problem/A
#time : o(n)

k =  int(input())
z=  sorted(list(map(int,input().split())),reverse = True)

def bt(k,z):
 x = 0
 if k == 0 :
    return x
 else :
  for i in z  :
    k -= i
    x+=1
    if  k<=0 :
      return(x)

 return -1


print(bt(k,z))
