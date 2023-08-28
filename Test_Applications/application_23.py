# Tutorial Number 23: Function
print()
print("Tutorial 23")


def greet_user():
    print("Hi")
    print("Have a nice day")


greet_user()
# Tutorial Number 24: Parameters
print()
print("Tutorial 24")


def greet_name(name):
    print(f"Hi {name}")
    print("Have a nice day")


greet_name("Bob")
# Tutorial Number 25: Keyword Arguments
print()
print("Tutorial 25")


def greet_name(first_name,last_name):
    print(f"Hi {first_name} {last_name}")
    print("Have a nice day")


greet_name(last_name="Jonson", first_name="Bob")
# Tutorial Number 26: Return Statement
print()
print("Tutorial 26")


def power_o_four(number):
    return number*number*number*number


print(power_o_four(4))
# Tutorial Number 27: Reusable Functions
print()
print("Tutorial 27")


def maximum(numbers):
    maximum = numbers[0]
    for item in numbers:
        if item > maximum:
            maximum = item
    return maximum


numbers = [0, 1, 2, 3, 4]
print(maximum(numbers))
# Tutorial Number 28: Exceptions
print()
print("Tutorial 28")

try:
    age = int(input("Age: "))
    print(age)
except ValueError:
    print("Invalid value")

# Tutorial Number 29: Comments
print()
print("Tutorial 29")
#Comment

