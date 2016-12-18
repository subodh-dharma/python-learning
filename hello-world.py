# simple print of string
print "Hello World! from file"
# Use of repr to convert string in python expression
print repr("Hello repr!")
print repr(100000L)
# Use of str to convert value to a string.
print str("Hello str!")
print str(10000L)

temp = 42
# error-prone stmt
# cannot use variables diectly
# print "Temperature is "+ temp
print "Temperature is "+ repr(temp)

## using user-inputs

# use of input() results in error as input is not acceptable
# use of raw_input() helps in storing the same type of input as given in console
# name = input("Enter a name")
name = raw_input("Enter a name")
print "Name Entered is "+ name
