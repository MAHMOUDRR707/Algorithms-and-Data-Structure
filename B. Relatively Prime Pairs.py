#link :  https://codeforces.com/contest/1051/problem/B
#time  o(n)

m,n =  map(int,input().split())
#  pervious solution
'''
z = []
for l in range(m,n+1):
    for r in range(l+1,n+1):
        if (r-l+1)/2 == 1 :
            z.append((r,l))
x =  ((n-m)+1)//2
if z :
    print("YES")
    for i,j in z[::2] :
        print(j,i)
        
else :
    print("NO")
'''
#New solution
x = ((n-m)+1) //2

print("YES")
for i in range(x) :
    print(m+i*2 , m+i*2+1)
