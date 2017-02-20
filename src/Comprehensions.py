# list Comprehensions: Creation if list from slightly different way.

# Simple List example
simpleList = [];

for character in "word":
    simpleList.append(character)

print simpleList

# Now using list comprehension
comprehensionList = [character for character in "word"]
print comprehensionList

# get the square of all numbers in a list from 1 to 10
squareList = [square**2 for square in range(1, 11)]
print squareList

# Check even numbers in a range
evenNumbers = [number for number in xrange(0, 20) if number%2==0]
print evenNumbers

# Convert celcius to farenhite
celcius = [0, 10, 15, 20, 25]

farenhite = [(temp * (9/5.0) + 32) for temp in celcius]
print farenhite

# Nested list comprehension
cubeNumbers = [x*x for x in [x**2 for x in range(1, 11)]]
print cubeNumbers

# Assessment 1
st = "Print only the words which starts with s in this sentence"
print [sWord for sWord in st.split(" ") if sWord.startswith("s")]

st = "Print every word in this sentence that has an even number of letters"
print [eWord for eWord in st.split(" ") if len(eWord)%2==0]

numbers=[]
fizz = "Fizz"
buzz = "Buzz"
for number in range(1, 11):
    if number%3==0 and number%5==0:
        numbers.append(fizz + buzz)
    elif number%3==0:
        numbers.append(fizz)
    elif number%5==0:
        numbers.append(buzz)
    else:
        numbers.append(number)

print numbers
