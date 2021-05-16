#problem link : https://codeforces.com/contest/1520/problem/A
def ff(x):
    z =  []
    z.append(x[0]) 
    for i in range(1,len(x)):
        if x[i] in z :
            if x[i] ==x[i-1]:
                continue
            else:
                return "No"
        else:
            z.append(x[i])
    return "YES"
n =  int(input())
for i in range(n):
    m =  int(input())
    x =  list(input())      
    print(ff(x))
