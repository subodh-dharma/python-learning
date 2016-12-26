# list as data-structure

# stack operations LIFO
stack = [1,2,3]
print 'STACK :' + repr(stack)

# Push Operation on stack
print '\nPushing 4...'
stack.append(4)
print 'STACK :' + repr(stack)

# Pop Operation on stack
print '\nPopping'
print stack.pop()
print 'STACK :' + repr(stack)

# Queue operations FIFO
queue = [1,2,3]
print 'QUEUE :' + repr(queue)

# Enqueue operations
print '\nEnqueuing 4'
queue.append(4)
print 'QUEUE :' + repr(queue)

# Dequeue
print '\nDequeueing'
print queue.pop(0)
print 'QUEUE :' + repr(queue)

# other operations

# REMOVE
# list.remove(index)

# REVERSE
# list.reverse()

# SORT
# list.sort()
