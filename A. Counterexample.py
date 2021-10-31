#problem link :https://codeforces.com/contest/483/problem/A
#time  : o(1)
l,r  = map(int,input().split())
if r-l +1 < 3 :
    print(-1)
elif  l%2 == 0 :
    print(l,l+1,l+2)
elif r-l+1 >3 :
    print(l+1,l+2,l+3)
else :
    print(-1)
    
