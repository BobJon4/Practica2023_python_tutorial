import math

# Tutorial Number 8: Arithmetic Operations
print("Tutorial 8")
print(4/3)
print(4//3)
print(4%3)
print(4**3)

x = 10
x += 3
print(x)

# Tutorial Number 9: Operator Precedence
print("Tutorial 9")

# Tutorial Number 10: Math Functions
print("Tutorial 10")
x = 4.2
print(round(x))
print(abs(-x))
print(math.ceil(x))
print(math.floor(x))

# Tutorial Number 11: If Statements
print("Tutorial 11")
hot_day = False
cold_day = False
if hot_day:
    print("It's a hot day, drink plenty of water !")
elif cold_day:
    print("It's a cold day, wear warm clothes !")
else:
    print("It's a lovely day !")

price = 10**6
good_credit = True

if good_credit:
    print(f"Down payment of {price*0.1} $")
else:
    print(f"Down payment of {price*0.2} $")

# Tutorial Number 12: Logical Operations
print()
print("Tutorial 12")

high_income = True
good_credit = True
if high_income and good_credit:
    print("Eligible for loan")

if high_income or good_credit:
    print("Eligible for loan")

criminal_record = False
if good_credit and not criminal_record:
    print("Eligible for loan")

# Tutorial Number 13: Logical Operations
print()
print("Tutorial 13")
temperature = 36
if temperature > 30:
    print("It's a hot day, drink plenty of water !")
else:
    print("It's not a hot day")

name = 'Bob'

if len(name) < 3:
    print("Name  must be at least 3 characters long")
elif len(name) > 50:
    print("Name is too long, maximum of 50 characters")
else:
    print("name looks good")
