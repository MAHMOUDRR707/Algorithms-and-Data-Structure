#link : https://codeforces.com/contest/1644/problem/A
#time: o(1)

#sol1
'''
n = int(input())

for i in range(n):
    x =  input()
    y = True
    r,g,b = 0,0,0
    for j in x :
        if j  == 'r' :
            r += 1
        elif j  == 'b' :
            b += 1
        elif j  == 'g' :
            g += 1


        if j  == 'R' and r == 0 :
            y = False

        elif j  == 'B' and b == 0 :
            y = False

        elif j  == 'G' and g == 0 :
            y =  False

    if y :
        print('YES')
    else :
        print('NO')
'''

#sol2

n  =  int(input())
for i in range(n):
    x =  list(input())
    if x.index('R') <  x.index('r') or x.index('g') >  x.index('G') or x.index('B') <  x.index('b') :
        print('NO')
    else :
        print('YES')
        
    
