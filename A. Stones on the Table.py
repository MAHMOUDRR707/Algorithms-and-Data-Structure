n = int(input())
x = input()
z = 0
for i in range(1,n):
    if x[i] == x[i-1] :
      z+=1
print(z)
