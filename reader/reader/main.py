from reader import read

# Use Case 1: Simple Read
# reads lines into a list of strings
uc1 = read('ex1.txt')
print(uc1)

# Use Case 2: Simple Read with formatting
# reads lines into a list of integers
uc2 = read('ex1.txt', formatter='i')
print(uc2)

# Use Case 3: Separator Read with formatting
# reads lines into a list of lists of integers.
# For the inner lists, the first element is a string, the second is an integer
uc3 = read('ex2.txt', separator=' ', formatter='si')
print(uc3)

# Use Case 4: Separator Read with formatting
uc4 = read('ex3.txt', separator='', formatter='iiiii')
print(uc4)