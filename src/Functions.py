# Functions are well defined set of instructions together to solve a problem.
# Python provides a keyword "def" to define functions.

# Syntax- def name_of_function (arg1, arg2, ...) :
# Adding doc string to a function


def my_addition(number1, number2):
    """
    This is the description of function, it takes two numbers and add them.
    """
    return number1 + number2

number1 = 4
number2 = 5

print "The addition of {number1} and {number2} is {sum}" \
    .format(number1=number1, number2=number2, sum=my_addition(number1, number2))

# How to see the documentation of any function in python
help(my_addition)

def say_hello (name):
    print "Hello {name}, how are you doing ?" .format(name=name)

say_hello("Sap")


def is_prime(num):
    """This a function to take any number and check if the number is prime or not. Returns true/false"""
    for n in range(2, num):
        if num % n == 0:
            return False

    else:
        return True

print is_prime(4)
print is_prime(5)
print is_prime(10)
print is_prime(13)