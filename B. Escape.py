#problem link : https://codeforces.com/contest/148/problem/B#
#time : o(n)

p =  int(input())
d =  int(input())
t = int(input())
f =  int(input())
c = int(input())
x = 0
m1 = p*t

while  m1 < c :
    td =  m1/(d-p)
    m1 +=  p*td
    if m1>= c :
        break
    tback =  m1/d  +f 
    m1 = m1 + tback*p 
    x+=1
    
print(x)
