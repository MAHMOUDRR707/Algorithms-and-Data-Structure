#link : https://codeforces.com/contest/1582/problem/A
#time:o(1)
n = int(input())
for i in range(n):
    a,b,c =  map(int,input().split())
    if (a%2 == 0 and c%2 == 0)  or (a%2==1 and c%2==1):
        print(0)
    else :
        print(1)
