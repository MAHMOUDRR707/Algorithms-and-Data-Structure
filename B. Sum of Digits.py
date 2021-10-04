#problem link : https://codeforces.com/contest/102/problem/B
#time o(n**2)
n = input()
x = 0
y = n
while len(n) !=  1 :
    x+= 1
    z = 0
    for i in n :
        z+= int(i)
        
    n = str(z)  
        
print(x)
        
        
