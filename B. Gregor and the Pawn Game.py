#link : https://codeforces.com/contest/1549/problem/B
#time : o(n)
n  =  int(input())
for i in range(n):
    m =  int(input())
    x2 =  list(input())
    x1 =  list(input())
    y = 0
    for j in range(m):
        if x1[j] == "1" :
            if j == 0 :
                if x2[j] == "0" :
                    y+=1
                elif x2[j+1] == "1":
                    y+=1
                    x2[j+1] = ""
            elif j ==  m-1 :
                if x2[j] == "0":
                   y+=1
                elif x2[j-1] == "1":
                    y+=1
                    x2[j-1] = ""
            else :
                if x2[j] == "0":
                    y+=1
                elif x2[j-1] == "1" :
                    y+=1
                    x2[j-1] = ""
                elif x2[j+1] == "1" :
                    y+=1
                    x2[j+1] = ""
    print(y)
                
