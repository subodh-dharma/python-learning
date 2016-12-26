# sorting types
# use of custom comparison func
def custcmp(arg1,arg2):
    if ( arg1 > arg2):
        return -1;
    if ( arg1 < arg2):
        return 1;
    if ( arg1 == arg2):
        return 0;


x = [4,2,8,1]
print x
x.sort(custcmp)
print x

# use of optional args

# key
x = ['abcdef', 'abcde', 'abcd', 'abc', 'ab', 'a']
print 'sorting by key=len'
# sorted based on len of the element
x.sort(key=len)
print x

# reverse
x = [4,2,8,1]
print x
print 'Sorting in reverse order'
x.sort(reverse=True)
print x
