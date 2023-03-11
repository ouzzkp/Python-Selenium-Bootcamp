# Python's dictionaries are a type of hash table. They work like associative arrays or hashes of key-value pairs found 
# in many programming languages ​​(C#, Java, Perl). A dictionary key can be almost any Python type, but it's usually numbers or strings. 
# Values, on the other hand, can be any arbitrary Python object. 
# Dictionaries are surrounded by curly braces ({}), and values ​​can be assigned and accessed using square brackets ([]).

# The biggest advantage of dictionaries is that they speed up the search over the key. All elements must be checked for searching on the array. 
# This requires a loop and an if check. It covers a period of O(N) as time complexity. 
# In dictionaries, on the other hand, the key is given as input to a hash function and the value is placed in a presented memory region.
# When a data is wanted to be searched, the key is used and sent to the same hash function and the value is found in the memory.

dict1 = {} # a empty dictinary
dict1['one'] = "Key value one as string - Value part" 
dict1[2]     = "Key value as int 2 - Value part"

dict2 = {'name': 'Kaan','code':5901, 'dept': 'Computer Engineering'}
# key and value data is retrieved in the initial assignment phase.

print(dict1['one'])       # returns key one's value
print(dict1[2])           # returns key 2's value
print(dict2)          # prints whole dict
print(dict2.keys())   # prints whole keys
print(dict2.values()) # prints whole values