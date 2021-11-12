#link  :  https://codeforces.com/contest/1606/problem/B
# time : o(log(n))
n = int(input())
for i in range(n) :
    a,b = map(int,input().split())
    x = 0
    z = 1
    a-=1
    while a > 0  and z <= b:
        a-= z
        z *=2
        x+= 1
        
        if a <= 0 :
            a = 0
    
    x+=(a+b-1)//b
    print(x)
