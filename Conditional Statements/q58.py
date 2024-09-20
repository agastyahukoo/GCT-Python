c1 = input("Enter the name of the city: ")
t1 = float(input("Enter the temperature of the city: "))
c2 = input("Enter the name of the city: ")
t2 = float(input("Enter the temperature of the city: "))
if t1 < t2:
    print(f"{c1} is the cooler city.")
else:
    print(f"{c2} is the cooler city.")