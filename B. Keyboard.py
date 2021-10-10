#link : https://codeforces.com/contest/88/problem/B
#time :o(n)

n,m,x =  map(int,input().split())
shift = []
pos=[(0,0)]*26
ans = 0
z = [ 0  for i in range(31)] *31
l = 0   
for i in range(n):
    y = input()
    for j in range(m):
        if y[j] != "S" :
           pos[ord(y[j]) - ord("a")] = (i,j)
           z.append(y[j])

        else :
            shift.append((i,j))
            
v = int(input())

y =  input()
for j in y :
        if j.islower():
            if not pos[ord(j)-ord("a")] or j not in z :
                       ans = -1
                       break                
                
        else :
            l+=1
            j =  j.lower()
            if shift == []  or j  not in  z :
                ans = -1
                break
            else :
                for a,b in shift :
                    c,d = pos[ord(j)-ord("a")]
                    k = (c - a)*(c - a) + (d - b)*(d - b)
                    if   not  k  > x*x :
                        ans+=1
                        break
                    
                        
                    
        
print(l-ans)      
