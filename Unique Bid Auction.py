#link  : https://codeforces.com/contest/1454/problem/B
#time o(n)
n =  int(input())
def xx(x,z):
    if x == 1 :
        return 1
    dic = {}
    for i in range(x):
        try: 
            dic[z[i]] += 1
            dic[z[i]] = -1

        except: 
            dic[z[i]] = i + 1
    for i, j in sorted(dic.items()):
        if j != -1: 
            return(j)

            return (z.index(j)+1)
    return -1
for i in range(n):
    x =  int(input())
    z =  list(map(int,input().split()))
    print(xx(x,z))
