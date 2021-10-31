#problem link :https://codeforces.com/contest/1009/problem/B
#time :o(n)
x = input()
O = 0
z = ""
y = []
for i in x :
    if  i == "1" :
        O +=1
    else :
        y.append(i)
n =  len(y)
i = -1
while i+1 < n  and y[i+1] == "0"  :
    i+=1
for k in range(O):
    y.insert(k+1+i,"1")

for i in y :
    z+=i
print(z)
