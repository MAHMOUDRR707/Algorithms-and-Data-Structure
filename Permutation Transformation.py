#link : https://codeforces.com/problemset/problem/1490/D
#time :  O(log(n))
def Permutation_Transformation(l,r,x,z,y  ):
    if l>r :
        return 
    elif l == r  :
        z[l] =  y
    m = l
    for i in range(l+1,r+1):
        if x[m] < x[i] :
            m = i
    z[m] = y    
    Permutation_Transformation(l,m-1,x,z,y+1)
    Permutation_Transformation(m+1,r,x,z,y+1)

t =  int(input())
for i in range(t):
  n  =  int(input())
  x = list(map(int,input().split()))
  z = [0] * n
  y = 0
  Permutation_Transformation(0,n-1,x,z,y)
  print(*z)
