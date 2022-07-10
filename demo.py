import math
x=float(input("enter the first side of the triangle"))
y=float(input("enter the second side of the triangle"))
z=float(input("enter the third sid of the triangle"))
s=(x+y+z)/2
d=math.sqrt(s*(s-x)*(s-y)*(s-z))
print("area of triangle=",d)
