#link : https://codeforces.com/contest/78/problem/B
#time : o(1)
y = [ "", "G", "GB", "YGB", "YGBI", "OYGBI" , "OYGBIV"]
n = int(input())
x = "ROYGBIV"
if n <= 7   :
    print(x[:n])
else :
    x = x * int(n/7)

    m = n%7
    
    x+=y[m]
    
    print(x)
