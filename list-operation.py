#List operations

#adding/assigning to lists

# replacing list of characters from start index to end
s1 = list('Perl')
print s1
s1[2:] = list('ar');
print s1

# replacing list from a given range
s2 = list('Enginiiring')
print s2
s2[5:7] = list('ee')
# s2[start_including:end_excluding]
print s2

#indexing
sentence = ['This','is','not','so','long','message']
print sentence.index('not')
index_i = sentence.index('not')
sentence[index_i] = 'very'
print sentence


#insert operations
numbers1 = [1,2,3,4,5,6]
print numbers1
# insert at specific location and shift right
numbers1.insert(3, 3.5)
print numbers1

# replace at specific location
numbers1[2] = 'three'
print numbers1
