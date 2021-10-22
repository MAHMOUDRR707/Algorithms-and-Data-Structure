#problem link : https://codeforces.com/contest/614/problem/B
#time : o(n) 
n =  int(input())
z =  list(input().split())
def Gena_code(n,z):
 un = 1
 x = ""
 v = 0
 for i in z:
    if i == "0" :
        print(0)
        return
    elif i[0] == "1" :
        for j in i[1:] :
         if j != "0"  :
            un = i
            break
         else   :
            x+="0"
    else :
        un = i
        
    
 
    
 print(un+x)
 return
Gena_code(n,z)
