# Python variables do not need explicit decleratin to allocate memory space.
# In other words, there is no need to predefine the type of variable as in C, C#, and
# Java languages. In this respect, it is similar to the definition in JavaScript and PHP 
# languages.

value = 100 # int, integer data type
distance = 10.2 # float data type
name = "Kaan" # string data type

print(value)
print(distance)
print(name)

# When we define a variable and assign a value, the memory addresses determined by the operating system 
# in the background are allocated to our application.Memory size is related to the size of 
# the defined data type.

a = b = c = 1
# This case, there will be created a integer object with value 1 and all of the variables are indicates same address
# in the memory.

print(a)
print(b)
print(c)

d , e , f = 2, 3, "Istanbul"
# Here, two integer objects with the values ​​1 and 2 are assigned to variables d and e, respectively, 
# and a string object with the value "Istanbul" is assigned to variable f.

print(d)
print(e)
print(f)

# Let's look these variables' memory address. 

print(id(a))
print(id(b))
print(id(c))

# As you can see a, b, and c have same memory address.

print(id(d))
print(id(e))
print(id(f))

# As you can see d, e, and f have different memory address.



