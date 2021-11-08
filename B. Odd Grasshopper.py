#problem link :  https://codeforces.com/contest/1607/problem/B
#time:  o(n)

'''

###########old solution #############

n=  int(input())
for i in range(n):
    a,b =  map(int,input().split())
    x = 0
    while x < b :
        x+=1
        if abs(a) %2 ==0 :
            a -= x
        else :
            a+=x
    print(a)
'''


n  =  int(input())
maps = [
    lambda x: 0,
    lambda x: x,
    lambda x: -1,
    lambda x: -x - 1
]
for i in range(n):
 a,b =  map(int,input().split())
 d  = maps[b%4](b)
 if a%2 == 0 :
     print(a-d)
 else :
    print(a+d)
 
