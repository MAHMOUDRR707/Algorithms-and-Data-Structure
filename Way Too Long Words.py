#time : O(n)
#problem link : https://codeforces.com/problemset/problem/71/A

n =  int(input())
for i in range(n):
    x =  input()
    if len(x) < 12 :
        print(x)
    else:
        print(x[0]+str(len(x)-2)+x[len(x)-1])
