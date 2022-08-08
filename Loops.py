# Loops Operators

print("while loops")

i = input("ENTER NUMBER: ")
x = input("ENTER NUMBER: ")
while int(i) <= int(x):
    print(i)
    i = int(i) + 1
print()


print("For Loops")

number = 1,2,3,4,5,6

for unit in number:
    print(unit)

print()

print("For Loops with range")

number = range(5,10)

for numbers in number:
    print(numbers)