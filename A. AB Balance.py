#link  : https://codeforces.com/contest/1606/problem/A
#time : o(n)

n  = int(input())


for i in range(n):
    x =  list(input())
    if x[0] != x[len(x)-1] :
        if x[0] == "a":
            x[0] = "b" 
        else :
            x[0] = "a"
    s  = ""
    for i in x :
        s+=i
    print(s)
        
