#Task1 :Print data types

# Integer
print(123)
# Float
print(21.14)
# aomplex
print(4-1j)
#Boolean
print(True)
#String
print('How are you')

#Task2:print data types with corresponding types 

# Integer
value1=123
print(str(value1)+ "is type of"+str(type(value1))) 
# Float
value2 = 43.23
print(str(value2) + " is type of " + str(type(value2)))

# Complex
value3 = 4-1j
print(str(value3) + " is type of " + str(type(value3)))

# String
value4 = "How are you?"
print(str(value4) + " is type of " + str(type(value4)))

# Boolean
value5 = True
print(str(value5) + " is type of " + str(type(value5)))

#Task3
print(isinstance(5, int))
print(isinstance(3.14, float))
print(isinstance(True, bool))
print(isinstance(4+3j, complex))
print(isinstance("Hello World", int))
#Task4
#Check if values are instances of specific data types

print("Is 123 an instance of int?: ", isinstance(123, int))
print("Is 43.23 an instance of bool?: ", isinstance(43.23, bool))
print("Is (4-1j) an instance of complex?: ", isinstance(4-1j, complex))
print("Is True an instance of bool?: ", isinstance(True, bool))
print("Is 'How are you?' an instance of float?: ", isinstance("How are you?", float))
#Task5
# display data types
print("Is 123 an instance of int?: ", isinstance(123, int)) # Checks if 123 is an integer and displays the result
print("Is 43.23 an instance of bool?: ", isinstance(43.23, bool)) # Checks if 43.23 is a boolean and displays the result (expected result: False)
print("Is (4-1j) an instance of complex?: ", isinstance(4-1j, complex)) # Checks if 4-1j is a complex number and displays the result
print("Is True an instance of bool?: ", isinstance(True, bool)) # Checks if True is a boolean and displays the result
print("Is 'How are you?' an instance of float?: ", isinstance("How are you?", float)) # Checks if "How are you?" is a float and displays the result (expected result: False)

'''
 The first result displays True, because 123 is an integer.
 The second result displays False, because 43.23 is not a boolean.
 The third result displays True, because 4-1j is a complex number.
 The fourth result displays True, because True is a boolean.
 The fifth result displays False, because "How are you?" is not a float.
'''
