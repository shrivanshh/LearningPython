a = 60
b = 15
c = 20

animalFamily = ["Lion", "Tiger", "Elephant", "Monkey", "Dog"]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# If-elif-else Statement in Python
# - No Parenthesis, No Semicolon, everything is based on spaces and indentations.

if a<b :
    print "a is lesser than b"
elif a<c :
    print "a is lesser than c"
else :
    print "a is bigger than b and c"


# For Loops
# Syntax :

# for item in object:
#    do stuff

for member in animalFamily:
    print member

# Find even/odd numbers from numbers list

evenNumbers = []
oddNumbers = []

for num in numbers:
    if num % 2 == 0:
        evenNumbers.append(num)
    else:
        oddNumbers.append(num)

print "The even numbers are : {evenNumbers} and the odd numbers are : {oddNumbers}" .format(evenNumbers=evenNumbers, oddNumbers=oddNumbers)

# tuple unpacking
familyMembers = [("John", "hubby", 34), ("Marry", "wife", 32), ("luice", "daughter", 5)]

for (name, position, age) in familyMembers:
    print "Hello my name is {name}, i am {position} of our sweet family, and i am {age} years old !!!" .format(name=name, position=position, age=age)


# Example of iterators along with dictionary.
# As, dictionaries while accessing from for loop can only return keys, we needs to use iterators to use them wisely.
# i.e. .iteritems (for python 2), and .items (for python 3)

familyDictionary = {"hubby": {name: "John", age: 34}, "wife": {name: "Marry", age: 32}, "daughter": {name: "luice", age: 5}}
for position, memberDictionary in familyDictionary.iteritems():
    print "My name is {name}, with age {age}, and i am {position} of the family" .format(name=memberDictionary[name], age=memberDictionary[age], position=position)


# While Statements
# Syntax:
#   while condition:
#       do stuff
#   else: (optional)
#       final statement (optional)

# Simple Example
count = 0

while count < 5:
    print "The value of count is {count}" .format(count=count)
    count += 1
else:
    print "The count is out of range !!!"

# break, and continue statements for while loops
# find position of number 24

randomArray = [12, 23, 14, 15, 24, 56, 67, 27]
count=0

while True:
    if randomArray[count] == 24:
        print "The position of number 24 is {count}" .format(count=count)
        break
    elif count<len(randomArray):
        count += 1
        continue
    else:
        break
