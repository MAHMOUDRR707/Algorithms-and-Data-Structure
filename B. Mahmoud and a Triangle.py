#link :  https://codeforces.com/contest/766/problem/B
#time : O(n)
n = int(input())
z = list(map(int,input().split()))
z = sorted(z)
x = "NO"
for i in range(n-1,1,-1):
    y =  z[i]
    for j in range(2):
        if y < sum(z[i-2:i]):
            x = "YES"
            break
    
        
print(x)
            
        
