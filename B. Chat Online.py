#problem link :
# time : o(n**3)
p,q,l,r =  map(int,input().split())
l_p = []
l_q= []
z=[]
y =0
for i in range(p):
    a,b = map(int,input().split())
    l_p.append((a,b))
    


for i in range(q):
    c,d = map(int,input().split())
    l_q.append((c,d))

    
for i in range(p):
    for j in range(q):
        for k in range(l,r+1):
            if ((l_p[i][0] > l_q[j][1]+k)  or (l_p[i][1] < l_q[j][0]+k)) :
                continue
            else :
                z.append(k)
                
print(len(set(z)))

