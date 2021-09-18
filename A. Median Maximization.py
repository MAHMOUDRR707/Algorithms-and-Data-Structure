#link : https://codeforces.com/contest/1566/problem/A
#time :  O(1)
n =  int(input())
for i in range(n):
    x,y  =  map(int,input().split())
    m = x//2 + 1
    print(y//m)
