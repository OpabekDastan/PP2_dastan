import math
a=int(input("Input number of sides: "))
b=int(input("Input the length of a side: "))
c=(b/(4*math.tan(math.pi/a)))
d=(a * b **2)/(4*math.tan(math.pi/a))
print("The area of the polygon is: ", round(d))