
#problem link : https://codeforces.com/contest/1551/problem/B1
#time :  O(n)
n =  int(input()) 
        
 
for i in range(n) :
    x = input()
    y = [0]*26
    for i in x :
        y[ord(i)-ord('a')] +=1
    c1 = 0
    c2 =0
    for j in range(len(y)):
        if y[j] == 1:
            c1+=1
        elif y[j] >0:
            c2+=1
    print((c2+c1//2))
