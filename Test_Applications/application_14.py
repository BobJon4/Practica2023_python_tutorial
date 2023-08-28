# Tutorial Number 14: While Loops
print()
print("Tutorial 14")

i = 0

while i <= 4:
    print('*' * i)
    i += 1

# Tutorial Number 15: For Loops
print()
print("Tutorial 15")
for item in 'Python':
    print(item)

for item in ['Bob', 'John', 'Lewis']:
    print(item)

for item in range(10):
    print(item)

for item in range(4, 10):
    print(item)

for item in range(4, 10, 2):
    print(item)

print()
price = [4, 16, 64, 256]
total_price = 0
for item in price:
    total_price += item

print(total_price)

# Tutorial Number 16: Nested Roots
print()
print("Tutorial 16")

vector = [5, 2, 5, 2, 2]


for i in vector:
    segment = ''
    for j in range(i):
        segment += 'x'
    print(segment)

# Tutorial Number 17: Lists
print()
print("Tutorial 17")
names = ['Adam', 'Bob', 'Chris', 'Dan', 'Eustache']
names[0] = 'Andrew'
names[4] = 'Ellen'
print(names)

numbers = [4, 13, 26, 16, 8, 39, 52]
maximum = numbers[-1]
for index in range(len(numbers)-1):
    if numbers[index] > maximum:
        maximum = numbers[index]
print(maximum)

# Tutorial Number 18: 2D Lists
print()
print("Tutorial 18")

matrix = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print(matrix[1])
print(matrix[1][1])

# Tutorial Number 19: List Methods
print()
print("Tutorial 19")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers.insert(0, 0)
print(numbers)
numbers.remove(9)
print(numbers)
numbers.pop()
print(numbers)
print(numbers.index(4))
print(4 in numbers)
print(numbers.count(4))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers_copy = numbers.copy()
print(numbers_copy)
numbers.append(-1)
print(numbers)

print()

numbers = [4, 4, 16, 32, 4, 16, 64, 32]

for number in numbers:
    for comp_number in numbers[numbers.index(number)+1:]:
        if number == comp_number:
            numbers.remove(number)

numbers.sort()
print(numbers)

# Tutorial Number 20: Tuples
print()
print("Tutorial 20")

numbers = (1, 2, 3, 4)
print(numbers.count(4))
print(numbers.index(4))

# Tutorial Number 21: Unpacking
print()
print("Tutorial 21")

coord = (1, 4, 8)
x, y, z = coord
print(x)
print(y)
print(z)

# Tutorial Number 22: Dictionaries
print()
print("Tutorial 22")

Name = "Bob Jonson"
Email = "bobjonsonsrl@gmail.com"
Phone = "0770 278 900"

customer = {"name": Name, "e-mail": Email, "phone number": Phone}

print(customer["name"])
print(customer.get("name"))
print(customer.get("birth date", "26.10.2001"))

print()

Phone = input("Phone: ")
Translated_Phone = ''
translator = {'0': "Zero", '1': "One", '2': "Two", '3': "Three", '4': "Four", '5': "Five",
              '6': "Six", '7': "Seven", '8': "Eight", '9': "Nine", ' ': " "}

for number in Phone:
    Translated_Phone += translator.get(number) + ' '
print(Translated_Phone)

