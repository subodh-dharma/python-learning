#Slicing

#forward Slicing
tag1 = 'http://www.python.com'
domain = tag1[11:17]
print 'Domain1 : '+domain

#reverse Slicing
tag2 = 'http://www.python.com'
domain1 = tag2[-10:-4]
print 'Domain2 : '+domain1

#step slicing
numbers = [1,2,3,4,5,6,7,8,9,10]
# 3rd parameter defines number of positions to skip, default 1
print numbers[2:10:3]
