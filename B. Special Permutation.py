#link : https://codeforces.com/contest/1612/problem/B
#time :  o(n)
n = int(input())
for i in range(n) :
    m,a,b =  map(int,input().split())
    x =  m//2
    if (a<= x and b <= x)  or (a>x and b>x) or a > (x+1)  or  b < x:
        print(-1)
    else :
        k = 1
        print(a,end =" ")
        for j in range(m,0,-1):
            if j != a  and j !=  b  and  m-1 > k :
                print(j,end = " ")
        
        print(b)
