#link :  https://codeforces.com/contest/363/problem/B
#time : o(n)
n,m = map(int,input().split())
l = list(map(int,input().split()))
z = [sum(l[i:i+m] )for i in range(n-m+1)]
print(z.index(min(z))+1)
