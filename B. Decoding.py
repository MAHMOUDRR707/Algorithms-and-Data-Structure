#time : o(1)
#link : https://codeforces.com/contest/746/problem/B
n = int(input())
x =  input()
if n <= 2 :
    print(x)
elif n%2 == 0 :
    v = x[::2]
    v = v[::-1]
    y = x[1::2]
    z =""
    z+=v
    z+=y
    print(z)
else:
 v = x[::2]
 y =  x[1::2]
 y = y[::-1]
 z= ""
 z+=y
 z+=v
 print(z)



