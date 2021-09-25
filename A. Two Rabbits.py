#link : https://codeforces.com/problemset/problem/1304/A
#time : O(1)


n =  int(input())
for i in range(n):
 x,y,a,b =  map(int,input().split())
 if ((y-x)%(a+b)) ==0 :
    print(int((y-x)/(a+b)))
 else :
    print(-1)
