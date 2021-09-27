#problem link :https://codeforces.com/problemset/problem/900/A
#time : O(1)
n = int(input())
pos = 0
nag = 0
for i in range(n) :
    a,b  = map(int,input().split())
    if a>0:
        pos+=1
    else :
        nag +=1
if nag -1 <=0  or pos-1 <=0 :
     print("Yes")
else :
    print("NO")
