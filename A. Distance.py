#link : https://codeforces.com/contest/1612/problem/A
#time: O(1)
n = int(input())
for i in range(n):
    x,y  = map(int,input().split())
    m =  min(x,y)
    v =  x+y
    if v%2 != 0 :
        print(-1,-1)
    else :
        v = v//2
        if x>y :
            print(v-m,m)
        else :
            print(m,v-m)
