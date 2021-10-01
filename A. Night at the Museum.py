#problem link : https://codeforces.com/contest/731/problem/A
#time :o(n)
x =  input()
z =0
y = 'a'
m = 0
for i in x :
    m = abs(ord(i) -ord(y))
    if m > 12 :
        z+= abs(26-m)
        y = i
    else :
        z+= m
        y = i

print(z)
