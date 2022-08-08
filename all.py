# fist calculator
print("CALCULATOR")

first_number = input("ENTER FIRST NUMBER: ")
second_number = input("ENTER SECOND NUMBER: ")
choices = input("(A) , (S) , (M) , (D) : ")

if choices.upper() == "A":
    converter = int(first_number) + int(second_number)
    print("The Answer is (Addition): " + str(converter))
elif choices.upper() == "S":
    converter = int(first_number) - int(second_number)
    print("The Answer is (Subtraction): " + str(converter))
elif choices.upper() == "M":
    converter = int(first_number) * int(second_number)
    print("The Answer is (Multiplication): " + str(converter))
elif choices.upper() == "D":
    converter = float(first_number) / float(second_number)
    print("The Answer is (Division): " + str(converter))
else:
    print("ERROR")

print()

# temperature
print("TEMPERATURE")

temperature = input("ENTER TEMPERATURE: ")

if temperature > str(35): # 35 up
    print("IT'S GETTING HOT")
    print("ALWAYS DRINK WATER")
elif temperature > str(20): # 21 - 35
    print("IT'S GETTING COLD HERE")
elif temperature > str(10): # 19 down
    print("IT'S SO COLD HERE")
    print("WEAR YOUR JACKET WHEN YOU GET OUTSIDE")
else:
    print("ERROR")

print()

# converter
print("WEIGHT CONVERTER")

weight = input("ENTER YOUR WEIGHT: ")
unit = input("(K) kilogram or (L) Pounds: ")

if unit.upper() == "K":
    converter = float(weight) // 0.45
    print("YOUR KILOGRAM IS: " + str(converter))
elif unit.upper() == "L":
    converter = float(weight) * 0.45
    print("YOUR POUNDS IS: "+ str(converter))
else:
    print("ERROR")

print()

# Area of shape

# Area of Triangle
print("AREA OF TRIANGLE")

base = input("ENTER BASE: ")
height = input("ENTER HEIGHT: ")
tcalcu = int(base) * int(height) // 2
print("AREA OF TRIANGLE IS: " + str(tcalcu))
print()
#Area of Square
print("AREA OF SQUARE")

side = input("ENTER SIDE: ")
scalcu = int(side) * int(side)
print("AREA OF SQUARE IS: "+ str(scalcu))

print()

# Information about myself

print("INFORMATION")

name = input("ENTER NAME: ")
age = input("ENTER DATE YEAR: ")
year = input("ENTER YEAR: ")
course = input("ENTER COURSE: ")
id = input("ENTER ID: ")
acalcu = 2022 - int(age)

print ("MY NAME IS: " + name, "IM " + str(acalcu), "AND IM " + year, "TAKING "
            + course, "AND ALSO MY ID IS " +id)

print()
# While Loops

print(" WHILE LOOPS")

first_num = input("ENTER FIRST NUMBER: ")
second_num = input("ENTER SECOND NUMBER: ")

while int(first_num) <= int(second_num):
    print("Going Loops: " + str(first_num))
    first_num = int(first_num) + 1

print()
#For Loops

print(" FOR LOOPS ")

num = 1,2,3,4,5,6,7

for unit in num:
    print(unit)

print()

#For loops with range

print("FOR LOOPS WITH RANGE")
x = range(20)

for units in x:
    print(units)

print()

# List Statement
print("LIST STATEMENT")

names = ["Dave","Mondi","Roxy","Jude","Lara"]
names.insert("Rey")
print(names)
print(names[0])
print(names[2])
print(names[-2])
print(names[0:3])
print("Roxy" in names)