#problem link : https://codeforces.com/contest/1589/problem/A
#time : o(1)
import random
n = int(input())
for i in range(n):
    solve = True
    x,y = map(int,input().split())
  
    print(-x*x,y*y)
        
