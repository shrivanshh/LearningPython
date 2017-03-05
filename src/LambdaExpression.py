

# Lambda Expressions are one liner anonimous functions.
# The best way to write lambda is to start from writing function and full syntax and then keep reducing them.

def my_addition(num1, num2):
    return num1+num2;


# Now transfer it to lambda function
lambda_add = lambda num1, num2: num1+ num2

print lambda_add(3, 4)

# Lambda function to find the even number


def iseven(num):
    if num % 2 == 0 :
        return True

# Now in lambda expressions

iseven = lambda num: num % 2 == 0
print iseven(4)
print iseven(5)

# Reverse a string in lambda function


reverse = lambda str: str[::-1]

print reverse("Sapion")
print reverse("Python")