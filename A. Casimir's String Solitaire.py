#link https://codeforces.com/contest/1579/problem/A
#time :  o(n)

n = int(input())
for i in range(n):
    x =  input()
    if (x.count("A")+x.count("C")) ==  x.count("B"):
        print("YES")
    else :
        print("NO")
