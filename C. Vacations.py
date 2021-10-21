#problem link : https://codeforces.com/contest/699/problem/C
#time : o(n**3)
n = int(input())
z=  list(map(int,input().split()))
x = 0
y = [ [-1 for i in range(3)]for i in range(105)]
def vacation(cur , prev ) :
 if cur == n  :
    return 0 
 if z[cur] == 0 :
     return 1+vacation(cur+1,0)

 if y[cur][prev] != -1 :
     return  y[cur][prev]
    
 elif z[cur] == 1 :
    if  prev  == 1 :
        y[cur][prev] =  1+vacation(cur+1,0)
        return y[cur][prev]
    else :
        y[cur][prev]=  min( vacation(cur+1,1) , 1+vacation(cur+1,0))
        return y[cur][prev]
            
 elif z[cur] == 2 :
    if  prev  == 2 :
        y[cur][prev] = 1+vacation(cur+1,0)
        return y[cur][prev]
    else :
        y[cur][prev] = min( vacation(cur+1,2) , 1+vacation(cur+1,0))
        return y[cur][prev]



                
 else :
        if prev == 1 :
                    y[cur][prev]=  min( vacation(cur+1,2) , 1+vacation(cur+1,0))
                    return y[cur][prev]

        elif prev == 2 :
                    y[cur][prev] =  min( vacation(cur+1,1) , 1+vacation(cur+1,0))
                    return y[cur][prev]
        else :
                     y[cur][prev] =  min( vacation(cur+1,1) , min(1+vacation(cur+1,0), vacation(cur+1,2) ))
                     return y[cur][prev]

print(vacation(0,0))
