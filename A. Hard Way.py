#link:https://codeforces.com/contest/1642/problem/A
#time:o(1)
n =  int(input())
for i in range(n):
    a1,b1 = map(int,input().split())
    a2,b2 = map(int,input().split())
    a3,b3 = map(int,input().split())
    
    if b1 == b2   and b3 < b1  :
        print(abs(a1-a2))

    elif b1 == b3 and b2 < b3 :
        print(abs(a1-a3))

    elif b3 == b2  and b1 < b2 :
        print(abs(a3-a2))
        
    else :
        print(0)
    
