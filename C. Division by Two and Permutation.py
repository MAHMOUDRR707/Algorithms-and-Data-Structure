#time : o(nlogn)
#link : https://codeforces.com/contest/1624/problem/C
m =  int(input())
for _ in range(m):

    n =  int(input())
    z =  sorted(list(map(int,input().split())))
    x = 0
    y = [False]*(n+1)
    k =  True
    
    for i in z :
        x = i
        while (x >n or y[x]) :
            x //=2
        if x > 0 :
            y[x] = True
        else :
            k = False

    if k  :
        print('YES')
    else:
        print('NO')
        
        
    
