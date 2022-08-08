
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("THE CAR IS ALREADY STARTED!!")
        else:
            started = True
            print("your car is starting")
    elif command == "stop":
        if not started:
            print("THE CAR IS ALREADY STOPPED!!")
        else:
            started = False
            print("your car is stop")
    elif command == "help":
        print("""
              start - your car is starting
              stop - your car is stop
              quit - your quitting
              """)
    elif command == "quit":
        break
    else:
        print("I am sorry I don't understand you!!")

