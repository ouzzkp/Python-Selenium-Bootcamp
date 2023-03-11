# A tuple is a data type similar to a list. A tuple consists of a comma-separated set of values. 
# Unlike lists, however, they are enclosed in parentheses (( )) instead of square brackets. 
# The difference compared to lists is that it is in read-only mode. The number of items cannot be increased or updated.

tuple1 = ('abcd', 786 , 2.23, 'Bursa', 70.2)
tuple2 = (123, 'Hello')
print(tuple1)          # prints whole tuple
print(tuple1[0])       # prints first object of tuple
print(tuple1[1:3])     # prints the 2nd item and the 3rd item
print(tuple1[2:])      # prints after the 3rd item
print(tuple2 * 2)  # prints double
print(tuple1 + tuple2) # merge the two tuples

# Is it seems like lists, right? But let's try to add something in the tuple.

tuple1[0] = "dcba"
# it gives an error -> 'tuple' object does not support item assignment
