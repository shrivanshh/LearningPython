# All about lists

testList = [1, 'two', 3.0]
anotherList = ['four', 5, 'six']

print testList

print 'The length of my list is {strLen}' .format(strLen = len(testList))

print 'The first element of list if {firstElement}' .format(firstElement = testList[0])

# Similar to string manupulations, the same is also eligible in list i.e.
print 'The list of items after first is {afterFirst}' .format(afterFirst=testList[1:])
print 'The list of items everything upto index 2 is {beforeThird}' .format(beforeThird=testList[:2])
print 'The middle element of list is "{middleElement}"' .format(middleElement=testList[len(testList)/2])

print '\n---Concatination of lists ----'
print testList + [4, 'five', 6]
print testList + anotherList

thirdlist = testList + anotherList
print thirdlist

print '\n --- Double the list by * ---'
print thirdlist * 2

print '\n -- Lets check if we can reassign any variable in list, just like array ---'
thirdlist[0] = 'one'
print thirdlist

print '\n --- few methods for list ---'
intList = [1, 2, 3, 4, 5]

intList.append(6)
print 'Number 6 appended into list, and now the list is {newList}' .format(newList=intList)

print '\n --- LIFO Implementation in Python using list ---'
lifoList=[]
print lifoList
lifoList.append(1)
print lifoList
lifoList.append(2)
print lifoList
lifoList.append(3)
print lifoList
lifoList.append(4)
print lifoList
lifoList.append(5)
print lifoList

print 'The list after adding elements is {lifoList}' .format(lifoList=lifoList)
lifoList.pop()
print 'After one pop operation, the updated list is {updatedList}' .format(updatedList=lifoList)
lifoList.pop()
print 'After two pop operation, the updated list is {updatedList}' .format(updatedList=lifoList)
lifoList.pop()
print 'After three pop operation, the updated list is {updatedList}' .format(updatedList=lifoList)
lifoList.pop()
print 'After four pop operation, the updated list is {updatedList}' .format(updatedList=lifoList)


print '\n --- FIFO Implementation in Python using list ---'
lifoList=[]
print lifoList
lifoList.append(1)
print lifoList
lifoList.append(2)
print lifoList
lifoList.append(3)
print lifoList
lifoList.append(4)
print lifoList
lifoList.append(5)
print lifoList

print 'The list after adding elements is {lifoList}' .format(lifoList=lifoList)
lifoList.pop(0)
print 'After one pop operation, the updated list is {updatedList}' .format(updatedList=lifoList)
lifoList.pop(0)
print 'After two pop operation, the updated list is {updatedList}' .format(updatedList=lifoList)
lifoList.pop(0)
print 'After three pop operation, the updated list is {updatedList}' .format(updatedList=lifoList)
lifoList.pop(0)
print 'After four pop operation, the updated list is {updatedList}' .format(updatedList=lifoList)

print '\n --- List of List, i.e. Matrix example ---'
listOne = [1, 2, 3]
listTwo = [4, 5, 6]
listThree = [7, 8, 9]
print 'Matrix is {matrix}' .format(matrix=[listOne, listTwo, listThree])

matrix = [listOne, listTwo, listThree]
print 'Accessing the matrix in matrix fashion, i.e. 2, 2 as matrix[2][2] is {twotwoElement}' .format(twotwoElement = matrix[1][1])


print '\n -- Introduction of list comprehension ---'
print "Let's print column one of matrix i.e. {columnOne}" .format(columnOne = [row[0] for row in matrix])


