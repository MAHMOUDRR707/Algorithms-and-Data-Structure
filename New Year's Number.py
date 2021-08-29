#problem link : https://codeforces.com/contest/1475/problem/B
n = int(input())
for i in range(n): 
    l=  int(input())
    x =  int(l%2020)
    z =  int((l-x)/2020-x)
    print(z,x)
    if z >=0 and z*2020+x*2021 == l :
        print("yes")
    else :
        print("no")
