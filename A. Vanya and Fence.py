n , m =  map(int,input().split())
z = list(map(int,input().split()))
x = 0
for i in z:
    if i > m  :
        x+=2
    else :
        x+=1
print(x)  
