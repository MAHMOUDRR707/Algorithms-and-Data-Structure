#problem link : https://www.google.com/url?q=http://codeforces.com/contest/680/problem/B&sa=D&source=editors&ust=1632958982695000&usg=AOvVaw0j-WFOlmUS94aFqO__VmQV
#time o(log(n))
n,m =  map(int,input().split())
z =  list(map(int,input().split()))
if z[m] == 1 :
    x = 1
else :
    x = 0
down,up =  m-1 ,  m+1
while down >= 0 or up <n :
    if x<0 :
        if z[up] == 1 :
            x+=1
    else :
        if up >= n :
            if z[down] ==  1:
                x+=1
        else :
            if z[down] ==  z[up] ==1 :
                x+=2
    up+=1
    down -=1

        
print(x)
