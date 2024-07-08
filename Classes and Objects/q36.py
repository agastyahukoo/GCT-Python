import math
a = float(input("Enter the lengths of the 3 sides of the triangle:\n"))
b = float(input())
c = float(input())
s = (a+b+c)/2
print("Area of the triangle: ",math.sqrt(s*(s-a)*(s-b)*(s-c)))