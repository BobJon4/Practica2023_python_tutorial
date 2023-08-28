# Tutorial Number 5: Strings
print("Tutorial 5")
course = "Python's course for beginners "
course = 'Python for "beginners" '
course = '''
Hi Jon,

Here's our email to you.

With kind regards, Bob
'''
print(course[4])
print(course[-4])
print(course[0:4])

# Tutorial Number 6: Formatted Strings
print("Tutorial 6")
first_name = 'Bob'
last_name = 'Jonson'
full_name = first_name + ' [' + last_name + '] '
statement = full_name + 'is a coder !'
new_statement = f'{first_name} [{last_name}] is a coder !'
print(statement)
print(new_statement)

# Tutorial Number 7: String Methods
print()
print("Tutorial 7")
course = 'Python for beginners '
print(len(course))
print(course.upper())
print(course.lower())
print(course.title())
print(course.find('b'))
print(course.find('beginners'))
print(course.replace('beginners', 'absolute beginners'))
check = 'Python' in course
print(check)

