#problem  linkk : https://codeforces.com/contest/716/problem/B
#time :  O(n**2)

x =  list(input())
v = ""
y =  set(x)
z = list("ABCDEFGHIJKLMNOPQRZTUVWXYS")
if x.count("?") ==0  and len(y) != 26  :
    print(-1)
else :
    for i in range(len(x)) :
        if x[i] == "?" :
            for j in z :
                if j not in x :
                    x[i] =  j
    if len(x) != 26 :
        
     if len(x) > 26 and len(set(x)) == 27 :
      for i in range(len(x)) :
        if x[i] == "?" :
                x[i] =z[0]
      for i in x :
            v+= i
      print(v)
     else :
         print(-1)
        
    else :
        for i in x :
            v+= i
        print(v)
