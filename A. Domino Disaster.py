#link :  https://codeforces.com/contest/1567/problem/A
#time : o(n)
t  = int(input())
z = { "L":"L" , "R":"R" , "U":"D" , "D":"U" }
for i in range(t):
    n =  int(input())
    x =  input()
    v = ""
    for j in x :
        v+= z[j]
    print(v)
