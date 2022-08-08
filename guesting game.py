# Guesting Game

correct = 9
first_number = 0
second_nubmer = 3

while first_number < second_nubmer:
    guess = int(input('Guess the number: '))
    first_number += 1
    if guess == correct:
        print("YOU'VE WON!!")
        break
else:
    print("SORRY YOU'VE FAILED!!")