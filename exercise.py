numbers = [5, 2, 5, 2, 2]

for x in numbers:
    output = ''
    for count in range(x):
        output += 'x'
    print(output)

print()

import random

kasali = ["dave", "hello", "hi"]
leader = random.choice(kasali)
print(leader)

print()

class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second
dice = Dice()
print(dice.roll())