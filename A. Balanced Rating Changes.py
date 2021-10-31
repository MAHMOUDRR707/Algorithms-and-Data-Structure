#problem link :  https://codeforces.com/contest/1237/problem/A
#time :o(n)
n = int(input())
z = 0
x = []
for i in range(n) :
    y = int(input())
    if y % 2 == 0:
        x.append(y//2)
    else :
       if z == 1 :
           x.append((y//2)+1)
           z = 0
       else :
           x.append((y//2))
           z = 1
for i in x :
    print(i)
