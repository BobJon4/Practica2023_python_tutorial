# Tutorial Number 30: Classes
print()
print("Tutorial 30")


class Point:

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point_1 = Point()
point_1.x = 10
point_1.y = 20
point_1.move()
print(point_1.x)

# Tutorial Number 31: Constructors
print()
print("Tutorial 31")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(4, 4)
print(point.x)


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"{self.name} is talking !")


person_1 = Person("Bob")
person_1.talk()

# Tutorial Number 32: Inheritance
print()
print("Tutorial 32")


class Mammal:

    def walk(self):
        print("walk")


class Dog(Mammal):

    def bark(self):
        print("bark")


class Cat(Mammal):

    def meow(self):
        print("meow")


dog = Dog()
dog.walk()
dog.bark()

# Tutorial Number 33: Modules
print()
print("Tutorial 33")

import converters
from converters import kg_to_lbs

print(kg_to_lbs(61))
print(converters.lbs_to_kg(134))

# Tutorial Number 34: Packages
print()
print("Tutorial 34")

import modules.shipping

modules.shipping.shipping()

from modules.shipping import shipping

shipping()

from modules import shipping

shipping.shipping()