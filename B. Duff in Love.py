#problem link : https://codeforces.com/contest/588/problem/B
#time : o(n**2)
n =  int(input())
for i in range(2,10**6):
    while n%(i*i) ==0 :
        n = n // i
print(n)

    
