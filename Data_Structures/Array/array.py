# Explain the operations 

# The array is one of the most commonly used data structure .
# the arrays can be broadly classified into two types, fixed memory and Dynamic memory. Python only has a dynamic memory.


array =[1,2,3,4,5,6]

# Lookup 
 # To look up a value in a given index 
second_element=array[2]
print (second_element) #O(1)

# Push/pop 
# To push or pop the last element in the array 
array.append(87) # O(1) adds element to the last value in an array 
print(array)
array.extend([89,78])
print(array)


# pop
array.pop()# O(1) Pops/ removes the element at the end of the array.
print(array)


# insert 
array.insert(0,78) # inserts the element at the beginning of the array .i.e. The worst case is O(n)

print(array)


# Delete (3 differnt ways all O(n)) 
array.pop(0) # deletes the first element and shifts the rest to left
print(array)
array.remove(5)# Removes the first occurance of 17
print(array)

del array[2:4]# Removes the elements in the index 2 - 4
print(array)

