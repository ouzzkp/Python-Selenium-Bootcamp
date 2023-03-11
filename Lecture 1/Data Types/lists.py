# Lists are Python's composite data type. A list contains items separated by commas and enclosed in square brackets ([]).
# In fact, lists are similar to the arrays we see in many programming languages. However, Python offers a more flexible structure. 
# That is, you can define more than one data type in a list.

list1 = [ 'abcd', 786 , 2.23, 'Bursa', 70.2 ]
list2 = [123, 'Hello']
print(list1)          # prints whole list
print(list1[0])       # prints first object of list
print(list1[1:3])     # prints the 2nd item and the 3rd item
print(list1[2:])      # prints after the 3rd item
print(list2 * 2)  # prints double
print(list1 + list2) # merge the two lists