# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Simple tuple
fruit_tuple = ('Apple', 'Orange', 'Mango')
# Using constructor
# fruit_tuple = tuple(('Apple', 'Orange', 'Mango'))

print(fruit_tuple)

# Get single value
print(fruit_tuple[1])

# Can not change value
# fruit_tuple[1] = 'Grape'

# Tuples with one value should have trailing comma
fruit_tuple_2 = ('Apple',)

print(fruit_tuple_2)

# Get length of tuple
print(len(fruit_tuple))

# Delete an entire tuple
# You cannot delete a portion of a tuple
del fruit_tuple_2

# print(fruit_tuple_2)



# A Set is a collection which is unordered and unindexed. No duplicate members.

fruit_set = {'Apple', 'Orange', "Mango"}

print(fruit_set)

# Check if in set
print('Apple' in fruit_set)
print('Apples' in fruit_set)

# Add to set
fruit_set.add('Grape')

print(fruit_set)

# Remove from set
fruit_set.remove('Grape')

print(fruit_set)

# Clear set
fruit_set.clear()

print(fruit_set)

# Delete set
# del fruit_set
