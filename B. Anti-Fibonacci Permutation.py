#link:https://codeforces.com/contest/1644/problem/B
#time: o(n**2)
n = int(input())
for i in range(n):
    y =[]
    x =  int(input())
    for i in range(1,x+1):
        print(i,end=' ')
        for j in range(x,0,-1):
            if  i !=  j :
                print(j,end=' ')
        print('')
    
    
    
    
