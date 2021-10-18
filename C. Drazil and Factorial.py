#problem link : https://codeforces.com/contest/515/problem/C
#time : o(n)

n = int(input())
x =  input()
z = ""
for i in x :
    y = int(i)
    if  y == 1 or y == 0:
        continue
  
    elif y == 4  :
        z+="322"

    elif y == 6:
      z+=  "53"


    elif y == 8 :
        z+="7222"
    elif y == 9 :
        z+="7332"
    else :
        z+=i
x = ""
for i  in sorted(z,reverse =  True) :
    x += i
print(x)
