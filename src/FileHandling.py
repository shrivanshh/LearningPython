# Open a file
f = open('../resources/testFile.txt')

# Read the content of the file
print(f.read())

# As you can see that for the second call that will not print the file, because the pointer is in the end of the file.
print(f.read())

# If you want to read the file again, you need to put the cursor on begining location, i.e.
f.seek(0)
print(f.read())

# Get the content of each line as an list
f.seek(0)
print (f.readlines())

# Print the last line of the file, i.e. get the total number of lines from list, and then iterate to last one :)
f.seek(0)
print (f.readlines()[-1])

f.seek(0)
print (f.readlines()[len(f.readlines()) -1])

# For loop to print all lines of file
for line in open('../resources/testFile.txt'):
    print line

