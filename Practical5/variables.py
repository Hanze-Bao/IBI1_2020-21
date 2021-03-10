a=180602
b=190784
c=100321
d=abs(a-c)
e=abs(a-b)
if d < e:
  print("e is bigger")
elif d > e:
  print("d is bigger")
X = True
Y = False
Z = (X and not Y) or (Y and not X) 
W = (X!=Y)
if W == Z:
  print("True")
exit()
