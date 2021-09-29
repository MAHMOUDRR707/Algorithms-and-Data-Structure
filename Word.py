x =  input()
z =0
y =0
for i in x :
    if i.isupper():
        z+=1
    else :
        y+=1
if z <= y :
    x =x.lower()
    print(x)
else :
    x =  x.upper()
    print(x)
