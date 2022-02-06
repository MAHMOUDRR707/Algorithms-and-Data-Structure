#time : https://codeforces.com/contest/1624/problem/B
#link :o(1)
n = int(input())
for i in range(n):
    z =  list(map(int,input().split()))
    a,b,c =  z[0],z[1],z[2]
    
    Na = b - (c-b)
    Nb =  int(a+ (c-a)/2)
    Nc = a + 2*(b-a)
    
    if Na != 0  and Na%a == 0 and Na >= a :
        print('YES')
        
    
    elif Nb != 0 and Nb%b == 0 and (c-a)%2== 0 and Nb >= b :
        print('YES')
        
    
    elif Nc != 0  and Nc%c == 0 and Nc >= c :
        print('YES')
    
    else :
        print('NO')
   
