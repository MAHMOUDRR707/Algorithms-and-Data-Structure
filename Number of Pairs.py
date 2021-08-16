#link :https://codeforces.com/contest/1538/problem/C
#time :  O(n**3)

def solve_x(n,l,r):
    z =  list(map(int,input().split()))
    y = [1 for j in range(n)
        for  k in range(j+1,n)
            if l<= z[j] + z[k] <= r ]
    if y :
      return(sum(y))
    else :
        return(0)


t =  int(input())
for i in range(t):
    n,l,r =  map(int,input().split(" "))
    print(solve_x(n,l,r))
