#probblem link :https://codeforces.com/contest/431/problem/A
#time :  o(n) 

z =  list(map(int,input().split()))
x = input()
y = 0
for i in  x :
    y+=  z[int(i) -1]
print(y)
