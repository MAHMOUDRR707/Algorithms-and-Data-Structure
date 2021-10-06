#time:o(n)
#link:https://codeforces.com/contest/451/problem/B
n = int(input())
z =  list(map(int,input().split()))
x =  sorted(z)
l,r = 0,0
for i in range(n):
    if x[i] != z[i]:
        l = i
        break
for j in range(n-1,-1,-1):
    if x[j] != z[j] :
        r = j
        break

y =  z[l:r+1]
y =z[:l]+ y[::-1] + z[r+1:]
if y == x:
    print("yes")
    print(l+1,r+1)
else :
    print("no")
