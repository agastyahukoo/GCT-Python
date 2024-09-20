s1 = int(input("Enter the sides of the triangle: "))
s2 = int(input())
s3 = int(input())
if s1 == s2 == s3:
    print("The triangle is a Equilateral Triangle")
elif (s1 == s2) or (s2 == s3) or (s3 == s1):
    print("The triangle is a Isosceles Triangle")
else:
    print("The triangle is a Scalene Triangle")