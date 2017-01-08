testString = "This is my first python string example"

# len function

print (len(testString))

# Slice operator :

print testString[:8]

print testString[8:]

print testString[:]

print testString[-2]

print testString[:-2]

print testString[::1]

print testString[::2]

#reverse printing
print testString[::-1]

# string with arithematic operators (string concatination is +) and
print testString * 2

print testString.upper()

print testString.lower()

print testString.split()

print testString.split('e')

# String manupulations
print "This is my test String: %s" %(testString)

floatNumber = 12345.12345
print 'This is a float number %1.2f' %(floatNumber)

firstObject = 'Hello'
secondObject = 99.21
thirdObject = 'Give me a hug !!!'
print '%s Himanshu, \n I just scored %1.2f percentages in my result and due to which my dad said \n "%s"' %(firstObject, secondObject, thirdObject)

print '\n --- .format() method ---'

print 'Hi {name}, how are you doing ??'.format(name='Himanshu')