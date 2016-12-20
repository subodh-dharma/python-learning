# Addition

## Sequence
s1 = [1,2,3]
s2 = [4,5,6]
print s1+s2

## Strings
s3 = 'Hello '
s4 = 'World!'
print s3+s4

## IMPORTANT: DON'T MIX Sequence and Strings

# Mulitplication
# Useful for declaring sequence/arrays with any elements

# Initialize a sequence of some length with fixed value
s5 = [42]*5
print s5

# Initialize an empty sequence of some length
s6 = [None]*5
print s6
s6[3] = 44
print s6

# Length of sequence
print 'Length of Sequence: '+repr(len(s6))
