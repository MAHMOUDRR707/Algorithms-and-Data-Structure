#problem  link : https://codeforces.com/contest/785/problem/A
#time : o(1)
n = int(input())
x = 0
z = {"Tetrahedron": 4 , "Cube" :6,"Octahedron":8,"Dodecahedron":12,"Icosahedron":20}
for i in range(n) :
    y =  input()
    x+=z[y]
print(x)
