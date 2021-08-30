#problem link :https://codeforces.com/problemset/problem/1554/A
n = int(input())
for i in range(n):
    x = int(input())
    y =  list(map(int,input().split()))
    z =0
    for i in range(1,x):
        z = max(z,y[i]*y[i-1])
    print(z)
            
    
        
