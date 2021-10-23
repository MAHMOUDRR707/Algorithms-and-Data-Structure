#problem link : https://codeforces.com/contest/415/problem/B
#time : o(n)
n,a,b =  map(int,input().split())
l =  list(map(int,input().split()))
x = 0
z = []
for i in range(n) :
        if (l[i]*a) %b == 0 :
            z.append(0)
        else :
           x = ((l[i]*a)%b)//a

           z.append(x)

        
print(*z)
