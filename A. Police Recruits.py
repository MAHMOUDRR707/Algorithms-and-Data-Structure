n = int(input())
z =  list(map(int,input().split()))
total = 0
ans = 0
for i in z :
    if  i == -1 :
        if not(total) :
            ans+=1
        else :
            total -=1
    else :
        total+= i
print(ans)
