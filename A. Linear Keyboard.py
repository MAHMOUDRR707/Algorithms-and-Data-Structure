#link  : https://codeforces.com/contest/1607/problem/A
#time : o(n)

n = int(input())
for i in range(n):
    x=   0
    z = list(input())
    s =  input()
    for j in range(1,len(s)):
        x += abs(z.index(s[j]) - z.index(s[j-1]))
    print(x)
