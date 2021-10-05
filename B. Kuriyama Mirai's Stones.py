#time : o(n)
#link :  https://codeforces.com/problemset/problem/433/B
n = int(input())
l =  list(map(int,input().split()))
x =  sorted(l)
m =  int(input())
for i in range(m):
    a,b,c =  map(int,input().split())
    if a == 1 :
        print(sum(l[b-1:c]))
    else :
        print(sum(x[b-1:c]))
        
