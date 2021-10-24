#problem link :https://codeforces.com/contest/186/problem/B
#time : o(n)

n , t1 ,t2,k =  map(int,input().split())
z =[]
for i in range(n):
    a,b =  map(int, input().split())
    x =  max(a*t1 +(b-b*(k/100))*t2 ,(a-(a*k/100))*t2+b*t2)
    z.append(x)
z =  sorted(z,reverse =  True)
for i in range(n):
    print(i+1 ,"{:.2f}".format(z[i]))
    
