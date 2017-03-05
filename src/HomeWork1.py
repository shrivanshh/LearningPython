# TODO: couple of questions remaining, to be completed on Monday during office hours

# Write a function that computes the volume of a sphere given its radius.


def vol(rad):
    return (4.0/3) * (3.14) * (rad**3)

print vol(2)

# Write a function that checks whether a number is in a given range (Inclusive of high and low)


def ran_bool(num,low,high):
    if low < num < high:
        return True
    else:
        return False

print ran_bool(3,1,10)

# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output :
# No. of Upper case characters : 4
# No. of Lower case Characters : 33


def up_low(string_text):
    up_count = 0
    low_count = 0
    for count in range(0, len(string_text)-1):
        if 64 < ord(string_text[count]) < 91:
            up_count += 1
        elif 92 < ord(string_text[count]) < 123:
            low_count += 1
    print "No. of Upper case characters : {up_count}" .format(up_count=up_count)
    print "No. of Lower case characters : {low_count}".format(low_count=low_count)

up_low("Hello Mr. Rogers, how are you this fine Tuesday?")


# Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def unique_list(l):
    pass

unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5])


# Write a Python function to multiply all the numbers in a list.
# Sample List : [1, 2, 3, -4]
# Expected Output : -24

def multiply(numbers):
    multiplication_sum=1
    for n in numbers:
        multiplication_sum *= numbers[n]
    return multiplication_sum

print multiply([1,2,3,-4])


# Write a Python function that checks whether a passed string is palindrome or not.
# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

def palindrome(s):
    return s[::-1] == s

print palindrome('helleh')


# Write a Python function to check whether a string is pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"
# Hint: Look at the string module

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    pass

ispangram("The quick brown fox jumps over the lazy dog")
string.ascii_lowercase



