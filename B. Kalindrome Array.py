#link : https://codeforces.com/contest/1610/problem/B
#time : o(n)
def ch(a,n,z):
    l = 1
    r = n
    while (l<=r):
        if z[l] == z[r] :
            l+=1
            r-=1
        else :
            if z[l] != a and z[r] != a :
                return False
            elif z[l] == a :
                l+=1
            elif z[r] == a :
                r-=1
    return True

t = int(input())
for i in range(t):
    n =  int(input())
    a,b = 0,0
    z = list(map(int,input().split()))
    z.insert(0,0)
    for j in range(1,n//2 +1 ):
        if z[j] !=  z[n+1-j] :
            a =  z[j]
            b = z[n+1-j]
            break
    if ch(a,n,z) or ch(b,n,z) :
        print("YES")
    else :
        print("NO")
    z =[]
