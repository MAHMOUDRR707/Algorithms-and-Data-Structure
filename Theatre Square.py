#time :  O(1)
#problem link : https://codeforces.com/problemset/problem/1/A

import math as mt
m,n,a =  map(int,input().split())
x =  mt.ceil(m/a)*mt.ceil(n/a)
print(x)
