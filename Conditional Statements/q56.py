a = int(input("Enter 3 numbers: "))
b = int(input())
c = int(input())
if a < b and a < c:
    print(f"{a} is the smallest number.")
elif b < a and b < c:
    print(f"{b} is the smallest number.")
else:
    print(f"{c} is the smallest number.")