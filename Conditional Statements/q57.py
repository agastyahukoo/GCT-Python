a = int(input("Enter 3 numbers: "))
b = int(input())
c = int(input())
if (pow(a, 2) + pow(b, 2) == pow(c, 2)) or (pow(b, 2) + pow(c, 2) == pow(a, 2)) or (pow(c, 2) + pow(a, 2) == pow(b, 2)):
    print(f"{a},{b} and {c} are Pythagorean triplets.")
else:
    print(f"{a},{b} and {c} are not Pythagorean triplets.")