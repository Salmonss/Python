# Convert your weight into Kilogram and Pounds

weight = input("ENTER YOUR WEIGHT: ")
unit = input("(K) Kilogram or (L) Pounds: ")

if unit.upper() == "K":
    converter = float(weight) // 0.45
    print("YOUR KILOGRAM IS " + str(converter))
elif unit.upper() == "L":
    converter = float(weight) * 0.45
    print("YOUR POUNDS IS " + str(converter))
else:
    print("ERROR")