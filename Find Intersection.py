#time  o(2* n) = o(n)
# link : https://coderbyte.com/editor/Find%20Intersection:Python

def FindIntersection(strArr):
  x = []
  y = []
  z =[]
  for i in strArr : 
    x.append(int(i[0]))
    for j in range(len(i)-1)  :
        if i[j].isdigit() and i[j+1].isdigit():
          x.append(int(i[j]+i[j+1]))
        elif i[j].isdigit()  and not i[j-1].isdigit():
          x.append(int(i[j]))
    y.append(x)
    x = []
  z =[i for i in y[0] if i in y[1]]
  if z :
    print(z)
  else :
    print(False)
  # code goes here

# keep this function call here 
FindIntersection(raw_input())

