# Temperature for today

temperature = input("ENTER TEMPERATURE: ")

if temperature > str(35): # 35 up
    print("It's Hot today")
    print("Drink water always")
elif temperature >str(20): # 21 - 34
    print("It's Getting cold today")
elif temperature >str(10): # 20 below
    print("It's colder season today")
    print("Just bring your jacker when get outside")
else:
    print("error")