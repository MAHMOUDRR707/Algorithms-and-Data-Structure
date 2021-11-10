#link  : https://codeforces.com/contest/1607/problem/D
#time  :  o(n)

n = int(input())
for i in range(n) :
    m =  int(input())
    z = list(map(int,input().split()))
    b,r = [],[]
    x =  input()
    for j in range(m) :
        if x[j] == "B":
            b.append(z[j])

        else :
            r.append(z[j])
    b=  sorted(b)
    v =  True
    r = sorted(r, reverse = True)
    for k in range(len(b)):
        if b[k] < k+1:
            v =  False
    for k in range(len(r)):
        if r[k] > m-k:
            v =  False
    if    v :
        print("YES")
    else :
        print("NO")
    
    
            
            
