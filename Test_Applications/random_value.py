import random


class Dice:

    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides), random.randint(1, self.sides)


dice = Dice(sides=6)
print(dice.roll())
