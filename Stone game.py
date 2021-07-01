#time = O(n)
#link : https://codeforces.com/contest/1538/problem/A
n =  int(input())
m =[]
for i in range(n):
    x =  int(input())
    z=list(map(int,input().split()))
    y =0
    yy = 0
    mi =  min(z)
    ma =  max(z)
    mi_n = z.index(mi)
    ma_n = z.index(ma)
    if mi_n <= x//2 :
        y+= mi_n +1
        if ma_n < x//2:
            y+= abs(ma_n - mi_n)
        elif (abs(ma_n - mi_n)<x-ma_n) :
            y+= abs(ma_n - mi_n)
        else:
            y+= x-ma_n
    else :
        y+= x-mi_n
        if ma_n > x//2 :
            y+= abs(ma_n - mi_n)
        elif (abs(ma_n - mi_n)>ma_n):
            y+= ma_n+1
        else :
            y+= abs(ma_n - mi_n)

    if ma_n <= x//2 :
        yy+= ma_n +1
        if mi_n < x//2:
            yy+= abs(ma_n - mi_n)
        elif (abs(ma_n - mi_n)<x-mi_n) :
            yy+= abs(ma_n - mi_n)
        else:
            yy+= x-mi_n
    else :
        yy+= x-ma_n
        if mi_n > x//2 :
            yy+= abs(ma_n - mi_n)
        elif (abs(ma_n - mi_n)>mi_n):
            yy+= mi_n+1
        else :
            yy+= abs(ma_n - mi_n)


    m.append(min(y,yy))
for i in range(n):
    print(m[i])
