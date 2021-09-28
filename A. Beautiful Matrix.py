z =[]
for i in range(5) :
   z.append(list(map(int,input().split())))
x,y = 0,0
for i in range(len(z)) :
    if z[i].count(1):
        x = i+1
        y = z[i].index(1) +1
print(abs(x-3) +abs(y-3))
