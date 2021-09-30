n = int(input())
z = sorted(list(map(int,input().split())))
a,b= 0,0
for i in range(n):
    if i%2 ==0 :
        a+= z[i]
    else:
        b+= z[i]
print(max(a,b),min(a,b),end=" ")
    
