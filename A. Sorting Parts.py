#link : https://codeforces.com/contest/1637/problem/A
#time: O(log(n))
n = int(input())
for i in range(n):
    m = int(input())
    z =  list(map(int,input().split()))
    x =  sorted(z)
    if x == z :
        print('No')
    else :
        print('Yes')
