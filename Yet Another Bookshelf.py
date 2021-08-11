#link : https://codeforces.com/contest/1433/problem/B
#time :  O(n**2)

n =  int(input())
for i in  range(n):
    m =  int(input())
    ans = 0
    last = -1
    x =  list(map(int,input().split()))
    for j in range(m) :
        if x[j] == 1 :
            if last != -1:
              ans += j+1-1-last
            last = j+1

    print(ans)
        
