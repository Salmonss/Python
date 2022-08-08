# Arithmetic Operation

first_number = input("ENTER FIRST NUMBER: ")
second_number = input("ENTER SECOND NUMBER: ")
choices = input("(A) , (S) , (M) , (D): ")

if choices.upper() == "A":
    converter = int(first_number) + int(second_number)
    print("The answer is: " + str(converter))
elif choices.upper() == "S":
    converter = int(first_number) - int(second_number)
    print("The answer is: " + str(converter))
elif choices.upper() == "M":
    converter = int(first_number) * int(second_number)
    print("The answer is: " + str(converter))
elif choices.upper() == "D":
    converter = float(first_number) // float(second_number)
    print("The answer is: " + str(converter))
else:
    print("ERROR")
