#link  :  https://codeforces.com/contest/1566/problem/B
#time :  o(1)

n =  int(input())
for i in range(n):
    x =  input()
    if len(x) ==  x.count('1'):
        print(0)
    else :
        v = x.find('0')
        b =  x.rfind('0')
        if b-v + 1  == x.count('0') :
            print(1)
        else :
            print(2)
