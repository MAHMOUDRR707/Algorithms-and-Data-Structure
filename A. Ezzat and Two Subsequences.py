#link  : https://codeforces.com/contest/1557/problem/A
#time : o(n)
n = int(input())
for i in range(n):
    m =  int(input())
    z = sorted(list(map(int,input().split())),reverse =  True)
    x = z[0]
    v = z[1:]
    print("{:0.9f}".format((x+(sum(v)/len(v)))))
