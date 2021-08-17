#link : codeforces.com/contest/1454/problem/A
#time : o(n)
import random
n = int(input())
def sure(z):
    random.shuffle(z)
    for i in range(len(z)):
        if i+1 ==  z[i]:
            sure(z)
    return z
    
for i in range(n):
    x =  int(input())
    z = [i+1 for i in range(x)]
    z = sure(z)
    print(*z)
    
    
