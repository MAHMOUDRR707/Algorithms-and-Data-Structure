a,b =  map(int,input().split())
x = 0
while 1 :
    if a >b :
        break
    x+=1
    a *= 3
    b *= 2
print(x)
