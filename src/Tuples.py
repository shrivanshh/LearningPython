myTuples = (1, 2, 'three', 4, 5, 2, 3, 4, 5, 2, 2, 2, 2)

print myTuples

# Check Length
print len(myTuples)
print myTuples[2]

# Slicing is also supported
print myTuples[-1]

# Get index of
print myTuples.index('three')

# First index of first occurence will be returned
print myTuples.index(4)

# Count the number of times the value appears
print myTuples.count(2)
