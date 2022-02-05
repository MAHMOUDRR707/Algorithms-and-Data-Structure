#time: o(1)
#link : https://codeforces.com/contest/1633/problem/B
n = int(input())
y = []
for i in range(n):
     x = input()
     z,o = 0 ,0
     z = x.count('0')
     o = x.count('1')
     if z == o :
        print(o-1)
     elif z > o :
        print(o)
     elif o > z :
        print(z)
