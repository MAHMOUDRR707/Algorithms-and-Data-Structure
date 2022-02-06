#link :  https://codeforces.com/contest/1634/problem/A
#time : O(1)
n =  int(input())
for _ in range(n):
    a,b =  map(int,input().split())
    s =  input()
    if b ==0 or s == s[::-1]:
        print(1)
    else :
        print(2)
