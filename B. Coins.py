#problem link :https://codeforces.com/contest/47/problem/B
#time  :  o(1)
z ={'A':0,'B':0,'C':0}
for i in range(3):
 a =  input()
 if a[1] == '>' :
    z[a[0]] += 1 
 else:
    z[a[2]] += 1 

z= {k: v for k, v in sorted(z.items(), key=lambda z: z[1])}
y = ''
x = 0
for i,j in z.items() :
    if j  != x :
        print("Impossible")
        break
    else :
        y+=i
    x +=1
print(y)
